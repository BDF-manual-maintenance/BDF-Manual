QM/MM组合方法
================================================
QM/MM组合方法一般把系统分为两个区域，QM区和MM区。将体系总能量写为：

.. math::

    E_{QM/MM}(\mathbb{S}) = E_{MM}(\mathbb{O})+E_{QM}(\mathbb{I+L})+E_{QM/MM}(\mathbb{I,O}) 

其中, S 表示系统， I 表示QM层， O表示MM层，L表示链接原子。
:math:`E_{MM}(\mathbb{O})`
采用分子力学力场计算，
:math:`E_{QM/MM}(\mathbb{I,O})`
包括两项：

.. math::

    E_{QM/MM}(\mathbb{I,O})=E_{nuc-MM}+V_{elec-MM}

:math:`E_{nuc-MM}+V_{elec-MM}` 在BDF中通过在QM区加入外部点电荷来实现。

所以整个体系的总能量包括两个部分，:math:`E_{MM}` 采用分子力学方法计算，:math:`E_{QM}` 和 :math:`E_{QM/MM}`
采用量子化学方法计算。同时，QM区和MM区的相互作用还包括VDW相互作用等，这里不再赘述。对于QM区和MM区的断键，一般采用链接原子模型来描述。

BDF程序主要完成量子化学计算部分，其余部分由课题组修改的pdynamo2.0程序包完成。具体见相关算例。

.. note::
  
  pdynamo 程序的安装见程序包中相关说明。有关程序包的详细功能见程序包中的帮助文件。
  本手册只提供使用BDF进行QM/MM计算的相关说明和算例。

  QM/MM计算环境安装和配置参考：:ref:`QM/MM计算环境配置<qmmmsetup>`


输入文件准备
-------------------------------------------------
一般来说，QM/MM计算之前，需要对目标体系进行分子动力学模拟，得到适合的初始构象。不同的分子动力学软件，输出文件不尽相同，
pDynamo-2目前支持 ``Amber、CHARMM、Gromacs`` 等力场，同时支持 ``PDB、MOL2、xyz`` 等格式读入分子坐标。

.. note::

  当采用PDB、MOL2或xyz文件作为输入时，pDynamo 程序仅支持OPLS力场，对于小分子和非标准氨基酸力场参数不全，不推荐使用。建议优先采用Amber程序，
  通过拓扑文件输入力场参数。如果只做QM计算，各种输入方法都可以。

以Amber为例，从动力学模拟轨迹提取感兴趣的结构存储于 ``crd`` 文件中，与对应的拓扑文件 ``.prmtop`` 一起可以作为QM/MM计算的
起始点。Python 脚本如下：

.. code-block:: python

  from pBabel import AmberCrdFile_ToCoordinates3, AmberTopologyFile_ToSystem
  # 读取输入信息
  molecule  = AmberTopologyFile_ToSystem(Topfile)
  molecule.coordinates3 = AmberCrdFile_ToCoordinates3(CRDfile)


此时，分子信息存储于 ``molecule`` 结构中。具体QM/MM计算中，需要对体系进行能量计算、几何构型优化等操作。同时，可以在MM区定义活性区域，加速计算。

总能量计算
-------------------------------------------------

以10埃的水盒子为例，分子动力学模拟后提取文件为 ``wat.prmtop, wat.crd`` ，可对体系进行全量子化学计算，代码如下：

.. code-block:: python

  import glob, math, os
  from pBabel import AmberCrdFile_ToCoordinates3, AmberTopologyFile_ToSystem
  from pCore import logFile
  from pMolecule mport QCModelBDF,  System
  #  读取水盒子坐标和拓扑信息
  molecule = AmberTopologyFile_ToSystem ("wat.prmtop")
  molecule.coordinates3 = AmberCrdFile_ToCoordinates3("wat.crd") 
  # 定义能量计算模式，此处为全体系密度泛函计算，GB3LYP:6-31g
  model = QCModelBDF("GB3LYP:6-31g")
  molecule.DefineQCModel(model)
  molecule.Summary()  #输出体系计算设置信息
  # 计算总能量
  energy  = molecule.Energy()

在 ``QCModelBDF`` 类中可以定义方法和基组 ``GB3LYP:6-31g``, 方法和基组间采用 ``:`` 分割。上例中也可以选择感兴趣的分子（比如，第五个水分子）
进行QM/MM计算，第五个水分子用QM方法来算，其余用MM（本例中为amber力场）来计算。由于在MD计算时采用周期性边界条件，而QM/MM方法不支持使用周期性边界
条件，所以在脚本中加入选项，关闭周期性边界条件。

.. code-block:: python

 molecule.DefineSymmetry( crystalClass = None )

在pDynamo 定义了类 ``Selection`` 可以用于选择特定的QM原子，具体见使用说明。选择QM原子的脚本如下：

.. code-block:: python

 qm_area = Selection.FromIterable(range(12, 15))
 #12、13、14为原子列表索引值（该值 = 原子序号 - 1），等于选择 15号水分子
 molecule.DefineQCModel(qcModel, qcSelection = qm_area)

总体，QM/MM组合能量计算的脚本如下：

.. code-block:: python

  import glob, math, os
  from pBabel import AmberCrdFile_ToCoordinates3, AmberTopologyFile_ToSystem
  from pCore import logFile, Selection
  from pMolecule import NBModelORCA, QCModelBDF,  System
   # . Define the energy models.
  nbModel = NBModelORCA()
  qcModel = QCModelBDF("GB3LYP:6-31g")
  # . Read the data.
  molecule = AmberTopologyFile_ToSystem("wat.prmtop")
  molecule.coordinates3 = AmberCrdFile_ToCoordinates3("wat.crd")
  # .Close symmetry to a system
  molecule.DefineSymmetry(crystalClass = None)   # QM/MM need Close the symmetry.
  # .Selection qm area 
  qm_area = Selection.FromIterable(range (12, 15))  # Select WAT 5 as the QM area.
  # . Define the energy model.
  molecule.DefineQCModel (qcModel, qcSelection = qm_area)
  molecule.DefineNBModel (nbModel)
  molecule.Summary()
  # . Calculate
  energy  = molecule.Energy()

.. note::
  * QM/MM计算支持两种输入模式，对于简单的算例，可以在 ``QCModelBDF`` 类中作为参数输入。 

  * 相对复杂的算例可以采用 ``计算模版`` 方式输入。

几何构型优化
-------------------------------------------------
QM/MM几何构型优化一般不容易收敛，在实际操作中需要的技巧较多。常见的有，固定MM区，优化QM区；然后固定QM区优化MM区。如此往复循环几次后，再同时优化QM区和MM区。
优化是否收敛，和QM区的选择及QM/MM边界是否有带电较多的原子等关系很大。为了加速优化，可以在计算时固定MM区，仅选择离QM区较近的合适区域，作为活性区域，在优化中
坐标可以变化。以下为几何构型优化的算例：

.. code-block:: python

  import glob, math, os.path

  from pBabel import  AmberCrdFile_ToCoordinates3, \
                      AmberTopologyFile_ToSystem , \
                      SystemGeometryTrajectory   , \
                      AmberCrdFile_FromSystem    , \
                      PDBFile_FromSystem         , \
                      XYZFile_FromSystem

  from pCore import Clone, logFile, Selection

  from pMolecule import NBModelORCA, QCModelBDF, System

  from pMoleculeScripts import ConjugateGradientMinimize_SystemGeometry
                             
  # 定义 Opt interface
  def opt_ConjugateGradientMinimize(molecule, selection):
      molecule.DefineFixedAtoms(selection)       # Define 固定原子
      #定义优化方法
      ConjugateGradientMinimize_SystemGeometry(
          molecule,
          maximumIterations    =  4,   # 最大优化步数
          rmsGradientTolerance =  0.1, #优化收敛控制
          trajectories   = [(trajectory, 1)]
      )   # 定义轨迹保存频率
  # . Define the energy models.
  nbModel = NBModelORCA()
  qcModel = QCModelBDF("GB3LYP:6-31g")
  # . Read the data.
  molecule = AmberTopologyFile_ToSystem ("wat.prmtop")
  molecule.coordinates3 = AmberCrdFile_ToCoordinates3("wat.crd")
  # . Close symmetry to a system
  molecule.DefineSymmetry(crystalClass = None)  # QM/MM need Close the symmetry.
  #. Define Atoms List 
  natoms = len(molecule.atoms)                      # 系统中总原子数
  qm_list = range(12, 15)                            # QM 区原子
  activate_list = range(6, 12) + range (24, 27)   # MM区活性原子（优化中可以移动）
  #定义MM区原子
  mm_list = range (natoms)
  for i in qm_list:
      mm_list.remove(i)                              # MM 删除QM原子
  mm_inactivate_list = mm_list[:]
  for i in activate_list :
      mm_inactivate_list.remove(i)                   
  # 输入QM原子
  qmmmtest_qc = Selection.FromIterable(qm_list)     # Select WAT 5 as the QM area.
  #  定义各选择区
  selection_qm_mm_inactivate = Selection.FromIterable(qm_list + mm_inactivate_list)
  selection_mm = Selection.FromIterable(mm_list)
  selection_mm_inactivate = Selection.FromIterable(mm_inactivate_list)
  # . Define the energy model.
  molecule.DefineQCModel(qcModel, qcSelection = qmmmtest_qc)
  molecule.DefineNBModel(nbModel)
  molecule.Summary()
  #计算优化开始时总能量
  eStart = molecule.Energy()
  #定义输出文件
  outlabel = 'opt_watbox_bdf'
  if os.path.exists(outlabel):
      pass
  else:
      os.mkdir (outlabel)
  outlabel = outlabel + '/' + outlabel
  # 定义输出轨迹
  trajectory = SystemGeometryTrajectory (outlabel + ".trj" , molecule, mode = "w")
  # 开始第一阶段优化
  # 定义优化两步
  iterations = 2
  #  顺次固定QM区和MM区进行优化
  for i in range(iterations):
      opt_ConjugateGradientMinimize(molecule, selection_qm_mm_inactivate) #固定QM区优化
      opt_ConjugateGradientMinimize(molecule, selection_mm)                #固定MM区优化
  # 开始第二阶段优化
  # QM区和MM区同时优化
  opt_ConjugateGradientMinimize(molecule, selection_mm_inactivate)
  #输出优化后总能量
  eStop = molecule.Energy()
  #保存优化坐标， 可以为xyz/crd/pdb等。
  XYZFile_FromSystem(outlabel +  ".xyz", molecule)
  AmberCrdFile_FromSystem(outlabel +  ".crd" , molecule)
  PDBFile_FromSystem(outlabel +  ".pdb" , molecule)


QM/MM-TDDFT算例
-------------------------------------------------
在几何构型优化结束后，可基于QM/MM计算得到的基态进行TDDFT计算。BDF程序接口设计了 ``计算模版`` 功能，可基于用户给定的 ``.inp`` 文件，更新系统坐标
进行计算。同时，在几何构型优化和激发态计算过程中，可根据需要选择不同的QM区域。比如，为了考虑溶剂化效应，可以把感兴趣的分子的第一水合层添加到QM区进行
QM/MM-TDDFT计算。以前一节中完成的算例为例，可以继续添加如下代码进行计算。

.. code-block:: python

  #接前一节几何构型优化代码。
  #开始TDDFT计算。使用模版文件作为输入。
  qcModel = QCModelBDF_template(template = 'head_bdf_nosymm.inp') 
  # 调整QM区原子
  tdtest = Selection.FromIterable(qm_list + activate_list)        # Redefine the QM region.
  molecule.DefineQCModel(qcModel, qcSelection = tdtest)
  molecule.DefineNBModel(nbModel)
  molecule.Summary()
  #采用模版中的方法进行能量计算，（可以是TDDFT）
  energy  = molecule.Energy()

上面代码中，选用的模版为BDF的输入文件，文件内容如下：

.. code-block:: bdf

 $COMPASS
 Title
  cla_head_bdf
 Basis
  6-31g
 Geometry
  H 100.723 207.273 61.172
  MG   92.917  204.348   68.063
  C   95.652  206.390   67.185
 END geometry
 Extcharge
  point
 nosymm
 $END

 $XUANYUAN
 RSOMEGA
   0.33
 $END
 
 $SCF
 RKS
 DFT
   cam-B3LYP
 $END

 $tddft   #TDDFT计算控制
 iprt
  3
 iroot
  5
 $end





