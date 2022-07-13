
.. _QMMM:

BDF-QM/MM案例教程
=====================================================

本专题将介绍一种量子化学与分子力学结合的方法（QM/MM方法），该方法既包括量子化学的精确性，又利用分子力学的高效性，其基本思想是用量子力学处理感兴趣的中心，其余部分用经典分子力学来处理。

本章节以一个典型的没食子酸分子（Gallic Acid，GA）为例，介绍输入文件准备，QM/MM 单点计算，QM/MM结构优化，QM/MM激发态计算。其中，BDF程序主要完成量子化学计算部分，其余部分由BDF开发成员修改的pDynamo2.0程序包完成。同时介绍如何读取数据用于结果分析，帮助用户深入了解BDF软件的使用。

输入文件准备
-------------------------------------------------

一般来说，QM/MM计算之前，需要对目标体系进行分子动力学模拟，得到适合的初始构象。当采用PDB、MOL2或xyz文件作为输入时，pDynamo2.0程序包仅支持OPLS力场，对于小分子和非标准氨基酸力场参数不全，不推荐使用。建议优先采用Amber程序，通过拓扑文件输入力场参数。以Amber为例，从动力学模拟轨迹提取感兴趣的结构存储于.crd文件中，与对应的参数/拓扑文件.prmtop一起可以作为QM/MM计算的起始点。Python脚本如下：

.. code-block:: python

  from pBabel import AmberCrdFile_ToCoordinates3, AmberTopologyFile_ToSystem
  # 读取输入信息
  molecule  = AmberTopologyFile_ToSystem(Topfile)
  molecule.coordinates3 = AmberCrdFile_ToCoordinates3(CRDfile)

其中，需要提前安装好AmberTools，python2.0版本，并正确设置好 **AMBERHOME** 和 **PDYNAMO** 环境变量，关于如何将GallicAcid.pdb初始结构文件(图1，晶胞为2*1*1)生成使用AmberTools21程序相对应的坐标文件GallicAcid.crd和参数/拓扑文件GallicAcid.prmop的方法如下：

.. figure:: /TADF-example/GA.png
     :width: 800
     :align: center

运行antechamber程序将Pdb文件转化为mol2文件：
######################################################
antechamber -i GallicAcid.pdb -fi pdb -o GallicAcid.mol2 -fo mol2 -j 5 -at amber -dr no

- -i 指定输入文件
- -fi 指定输入文件类型
- -o 指定输出文件
- -fo 指定输出文件类型
- -j 匹配原子类型和键类型
- -at 定义原子类型


运行parmchk2程序生成对应体系的力场参数文件
######################################################
parmchk2 -i GallicAcid.mol2 -f mol2 -o GallicAcid.frcmod

运行tleap程序构建系统拓扑并为分子定义力场参数步骤如下:
######################################################
1. 使用 **tleap** 命令启动tleap程序

.. code-block:: bdf

   -I: Adding /es01/jinan/hzw001/home/hzw1011/anaconda3/envs/AmberTools21/dat/leap/prep to search path.
   -I: Adding /es01/jinan/hzw001/home/hzw1011/anaconda3/envs/AmberTools21/dat/leap/lib to search path.
   -I: Adding /es01/jinan/hzw001/home/hzw1011/anaconda3/envs/AmberTools21/dat/leap/parm to search path.
   -I: Adding /es01/jinan/hzw001/home/hzw1011/anaconda3/envs/AmberTools21/dat/leap/cmd to search path.
   
   Welcome to LEaP!
   (no leaprc in search path)
   >

2. 确定并加载体系力场：source leaprc.gaff(此为GAFF力场) 

.. code-block:: bdf
   
   > source leaprc.gaff
   ----- Source: /es01/jinan/hzw001/home/hzw1011/anaconda3/envs/AmberTools21/dat/leap/cmd/leaprc.gaff
   ----- Source of /es01/jinan/hzw001/home/hzw1011/anaconda3/envs/AmberTools21/dat/leap/cmd/leaprc.gaff done
   Log file: ./leap.log
   Loading parameters: /es01/jinan/hzw001/home/hzw1011/anaconda3/envs/AmberTools21/dat/leap/parm/gaff.dat
   Reading title:
   AMBER General Force Field for organic molecules (Version 1.81, May 2017)
   >

3. 调入配体mol2文件：GA = loadmol2 GallicAcid.mol2

.. code-block:: bdf
   
   > GA = loadmol2 GallicAcid.mol2
   Loading Mol2 file: ./GallicAcid.mol2
   Reading MOLECULE named WAT
   >
   
4. 检查导入的结构是否准确或缺失参数：check GA
5. 调入体系分子的模板，并补全库文件中缺失的参数:loadamberparams GallicAcid.frcmod
6. 准备生成的Sustiva库文件：saveoff GA GallicAcid.lib
7. 修改生成的Sustiva库文件并调入该文件：loadoff GallicAcid.lib

.. code-block:: bdf

   > loadoff GallicAcid.lib
   Loading library: ./GallicAcid.lib


8. 保存.crd和.prmop文件：saveamberparm GA GallicAcid.prmtop GallicAcid.crd

.. code-block:: bdf

   > saveamberparm GA GallicAcid.prmtop GallicAcid.crd
   Checking Unit.
   Building topology.
   Building atom parameters.
   Building bond parameters.
   Building angle parameters.
   Building proper torsion parameters.
   Building improper torsion parameters.
    total 112 improper torsions applied
   Building H-Bond parameters.
   Incorporating Non-Bonded adjustments.
   Not Marking per-residue atom chain types.
   Marking per-residue atom chain types.
     (Residues lacking connect0/connect1 -
      these don't have chain types marked:
   
           res     total affected
   
           WAT     1
     )
    (no restraints)
   >

9. 退出tleap程序：quit

分子动力学模拟
-------------------------------------------------

1.	此处采用amber软件进行分子动力学模拟，首先对体系进行能量最小化模拟，输入文件min.in如下：

.. code-block:: bdf

    Initial minimisation of GallicAcid complex
     &cntrl
      imin=1, maxcyc=200, ncyc=50,
      cut=16, ntb=0, igb=1,
    &end


- imin=1：运行能量最小化
- maxcyc=200：能量最小化的最大循环数
- ncyc=50：最初的0到ncyc循环使用最速下降算法, 此后的ncyc到maxcyc循环切换到共轭梯度算法
- cut=16：以埃为单位的非键截断距离
- ntb=0：关闭周期性边界条件
- igb=1：Born模型

使用如下命令运行能量最小化:

 **sander -O -i min.in -o GallicAcid_min.out -p GallicAcid.prmtop -c GallicAcid.crd -r GallicAcid_min.rst  &** 

其中GallicAcid_min.rst为输出包含坐标和速度的重启文件

2.	接下来利用最小化模拟得到的重启文件升温系统，从而完成分子动力学模拟，输入文件md.in如下：

.. code-block:: bdf

   Initial MD equilibration
    &cntrl
     imin=0, irest=0,
     nstlim=1000,dt=0.001, ntc=1,
     ntpr=20, ntwx=20,
     cut=16, ntb=0, igb=1,
     ntt=3, gamma_ln=1.0,
     tempi=0.0, temp0=300.0,
   &end

- imin=0：进行分子动力学(MD)
- irest=0：读取先前保存的重新启动文件读取坐标和速度
- nstlim=1000：运行的MD步数
- dt=0.001：时间步长（单位：ps）
- ntc=1：不启用SHAKE约束
- ntpr=20：每ntpr步输出能量信息mdout一次
- ntwx=20：每ntwx步输出Amber轨迹文件mdcrd一次
- ntt=3：Langevin恒温器控制温度
- gamma_ln=1.0：Langevin恒温器的碰撞频率
- tempi=0.0：模拟的初始温度
- temp0=300.0：模拟的最终温度

使用如下命令运行分子动力学模拟:

 **sander -O -i md.in -o md.out -p GallicAcid.prmtop -c GallicAcid_min.rst -r GallicAcid_md.rst -x GallicAcid_md.mdcrd -inf GallicAcid_md.mdinfo** 

其中GallicAcid_md.mdcrd文件即为MD模拟的轨迹文件，可借助VMD软件进行可视化显示分子结构，并从动力学模拟轨迹提取感兴趣的结构存储于.crd文件中。


QM/MM 总能量计算
-------------------------------------------------

分子动力学模拟后提取文件为GallicAcid.prmtop， GallicAcid.crd，可对体系进行全量子化学总能量计算，python代码如下：

.. code-block:: bdf
  
   import glob, math, os
   from pBabel import AmberCrdFile_ToCoordinates3, AmberTopologyFile_ToSystem
   from pCore import logFile
   from pMolecule import QCModelBDF,  System
   #  读取水盒子坐标和拓扑信息
   molecule = AmberTopologyFile_ToSystem ("GallicAcid.prmtop")
   molecule.coordinates3 = AmberCrdFile_ToCoordinates3("GallicAcid.crd")
   # 定义能量计算模式，此处为全体系密度泛函计算，可以定义方法和基组，分别为GB3LYP和6-31g，
   model = QCModelBDF("GB3LYP:6-31g")
   molecule.DefineQCModel(model)
   molecule.Summary()  #输出体系计算设置信息
   # 计算总能量
   energy  = molecule.Energy()


除了可以用全量子化学QM计算体系总能量，也可对感兴趣的分子进行QM/MM计算（本例为指定第五个分子用QM方法计算），QM/MM组合能量计算python脚本如下：

.. code-block:: bdf

   import glob, math, os
   from pBabel import AmberCrdFile_ToCoordinates3, AmberTopologyFile_ToSystem
   from pCore import logFile, Selection
   from pMolecule import NBModelORCA, QCModelBDF,  System
    # 定义能量计算模式
   nbModel = NBModelORCA()  #处理QM和MM区相互作用
   qcModel = QCModelBDF("GB3LYP:6-31g")
   # 读取体系坐标和拓扑信息
   molecule = AmberTopologyFile_ToSystem("GallicAcid.prmtop")
   molecule.coordinates3 = AmberCrdFile_ToCoordinates3("GallicAcid.crd")
   # 关闭体系对称性
   molecule.DefineSymmetry(crystalClass = None)  # QM/MM方法不支持使用周期性边界条件，故关闭周期性边界条件
   # 指定QM区
   qm_area = Selection.FromIterable(range (72, 90))  # 指定第五个分子用QM方法计算，其中(72, 90)指明原子列表索引值为72，73，74…..87,88,89，该值=原子序数-1
   # 定义能量计算模式
   molecule.DefineQCModel (qcModel, qcSelection = qm_area)
   molecule.DefineNBModel (nbModel)
   molecule.Summary()
   # 计算总能量
   energy  = molecule.Energy()

QM/MM模拟的输出总结了MM部分，QM部分，QM区和MM区相互作用部分的计算细节如下：

.. code-block:: bdf
  
   ----------------------------------- Summary for MM Model "AMBER" -----------------------------------
   LJ 1-4 Scaling                   =          0.500  El. 1-4 Scaling                  =          0.833
   Number of MM Atoms               =            288  Number of MM Atom Types          =              6
   Number of Inactive MM Atoms      =             18  Total MM Charge                  =           0.00
   Harmonic Bond Terms              =            288  Harmonic Bond Parameters         =              7
   Harmonic Bond Inactive           =             18  Harmonic Angle Terms             =            400
   Harmonic Angle Parameters        =              9  Harmonic Angle Inactive          =             25
   Fourier Dihedral Terms           =            592  Fourier Dihedral Parameters      =              5
   Fourier Dihedral Inactive        =             37  Fourier Improper Terms           =            112
   Fourier Improper Parameters      =              1  Fourier Improper Inactive        =              7
   Exclusions                       =           1216  1-4 Interactions                 =            528
   LJ Parameters Form               =          AMBER  LJ Parameters Types              =              5
   1-4 Lennard-Jones Form           =          AMBER  1-4 Lennard-Jones Types          =              5
   ----------------------------------------------------------------------------------------------------
   
   ------------------- Summary for QC Model "BDF:GB3LYP:STO-3g" -------------------
   Number of QC Atoms     =             18  Boundary Atoms         =              0
   Nuclear Charge         =             88  Orbital Functions      =              0
   Fitting Functions      =              0  Energy Base Line       =        0.00000
   --------------------------------------------------------------------------------
   
   ----------------------------- ORCA NB Model Summary ----------------------------
   El. 1-4 Scaling        =       0.833333  QC/MM Coupling         =    RC Coupling
   --------------------------------------------------------------------------------
   
   ------------------------------- Sequence Summary -------------------------------
   Number of Atoms            =        288  Number of Components       =         16
   Number of Entities         =          1  Number of Linear Polymers  =          0
   Number of Links            =          0  Number of Variants         =          0
   --------------------------------------------------------------------------------

输出体系总能量信息以及各部分能量贡献如下：

.. code-block:: bdf
  
  --------------------------------- Summary of Energy Terms --------------------------------
  Potential Energy          =    -1671893.4718  RMS Gradient              =             None
  Harmonic Bond             =        1743.3211  Harmonic Angle            =         124.9878
  Fourier Dihedral          =         269.8417  Fourier Improper          =           0.1346
  MM/MM LJ                  =        -138.0022  MM/MM 1-4 LJ              =         474.4044
  QC/MM LJ                  =         -42.2271  BDF QC                    =    -1674325.9320
  ------------------------------------------------------------------------------------------


QM/MM 结构优化
-------------------------------------------------
QM/MM几何构型优化计算的python脚本如下：

.. code-block:: bdf

  import glob, math, os.path

  from pBabel import  AmberCrdFile_ToCoordinates3, \
                      AmberTopologyFile_ToSystem , \
                      SystemGeometryTrajectory   , \
                      AmberCrdFile_FromSystem    , \
                      PDBFile_FromSystem         , \
                      XYZFile_FromSystem
  
  from pCore import Clone, logFile, Selection
  
  from pMolecule import NBModelORCA, QCModelBDF, System
  
  from pMoleculeScripts import ConjugateGradientMinimize_SystemGeometry, \
                               FIREMinimize_SystemGeometry             , \
                               LBFGSMinimize_SystemGeometry            , \
                               SteepestDescentMinimize_SystemGeometry
  # 定义结构优化接口
  def opt_ConjugateGradientMinimize(molecule, selection):
      molecule.DefineFixedAtoms(selection)       #固定原子
      #定义优化方法
      ConjugateGradientMinimize_SystemGeometry(
          molecule,
          maximumIterations    =  40,   # 最大优化步数
          rmsGradientTolerance =  0.1, #优化收敛控制
          trajectories   = [(trajectory, 1)]
      )   # 定义轨迹保存频率
  #  定义能量计算模式
  nbModel = NBModelORCA()
  qcModel = QCModelBDF("GB3LYP:6-31g")
  # 读取体系坐标和拓扑信息
  molecule = AmberTopologyFile_ToSystem ("GallicAcid.prmtop")
  molecule.coordinates3 = AmberCrdFile_ToCoordinates3("GallicAcid.crd")
  # 关闭体系对称性
  molecule.DefineSymmetry(crystalClass = None)  # QM/MM方法不支持使用周期性边界条件
  #. Define Atoms List
  natoms = len(molecule.atoms)                      # 系统中总原子数
  qm_list = range(72, 90)                            # QM 区原子
  activate_list = range(126, 144) + range (144, 162)   # MM区活性原子（优化中可以移动）
  #定义MM区原子
  mm_list = range (natoms)
  for i in qm_list:
      mm_list.remove(i)                              # MM 删除QM原子
  mm_inactivate_list = mm_list[:]
  for i in activate_list :
      mm_inactivate_list.remove(i)
  # 输入QM原子
  qmmmtest_qc = Selection.FromIterable(qm_list)     
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
  #定义输出文件目录名
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
  #保存优化坐标，可以为xyz/crd/pdb等。
  XYZFile_FromSystem(outlabel +  ".xyz", molecule)
  AmberCrdFile_FromSystem(outlabel +  ".crd" , molecule)
  PDBFile_FromSystem(outlabel +  ".pdb" , molecule)

输出体系收敛信息如下（此处仅展示前20步优化收敛结果）：

.. code-block:: bdf

    ----------------------------------------------------------------------------------------------------------------
    Iteration       Function             RMS Gradient        Max. |Grad.|          RMS Disp.         Max. |Disp.|
    ----------------------------------------------------------------------------------------------------------------
     0     I   -1696839.69778731          2.46510318          9.94250232          0.00785674          0.03168860
     2   L1s   -1696839.82030342          1.38615730          5.83254788          0.00043873          0.00126431
     4   L1s   -1696839.90971371          1.41241184          5.29242524          0.00067556          0.00172485
     6   L0s   -1696840.01109863          1.41344485          4.70119338          0.00090773          0.00265969
     8   L1s   -1696840.09635696          1.44964059          5.72496661          0.00108731          0.00328490
     10  L1s   -1696840.17289698          1.28607709          4.73666387          0.00108469          0.00354577
     12  L1s   -1696840.23841524          1.03217304          3.00441004          0.00081945          0.00267931
     14  L1s   -1696840.30741088          1.40349698          5.22220965          0.00162080          0.00519590
     16  L1s   -1696840.43546466          1.32604042          4.51175225          0.00158796          0.00455431
     18  L0s   -1696840.52547251          1.27123125          4.20616166          0.00158796          0.00428040
     20  L0s   -1696840.60265453          1.08553355          3.12355616          0.00158796          0.00470223
    ----------------------------------------------------------------------------------------------------------------

输出体系总能量信息如下：

.. code-block:: bdf
 
  --------------------------------- Summary of Energy Terms --------------------------------
  Potential Energy          =    -1696841.6016  RMS Gradient              =             None
  Harmonic Bond             =           3.0295  Harmonic Angle            =           3.6222
  Fourier Dihedral          =          32.0917  Fourier Improper          =           0.0040
  MM/MM LJ                  =         -69.3255  MM/MM 1-4 LJ              =          43.9528
  QC/MM LJ                  =         -47.2706  BDF QC                    =    -1696807.7057
------------------------------------------------------------------------------------------

.. note::

   QM/MM几何构型优化一般不容易收敛，在实际操作中需要的技巧较多。常见的有，固定MM区，优化QM区；然后固定QM区优化MM区。如此往复循环几次后，再同时优化QM区和MM区。优化是否收敛，和QM区的选择及QM/MM边界是否有带电较多的原子等关系很大。为了加速优化，可以在计算时固定MM区，仅选择离QM区较近的合适区域，作为活性区域，在优化中坐标可以变化。



QM/MM 激发态计算
-------------------------------------------------

基于上一步的QM/MM几何构型优化，继而即可将MM区活性原子添加到QM区进行QM/MM-TDDFT计算，完整的代码如下:

.. code-block:: bdf
  
  import glob, math, os.path

  from pBabel import  AmberCrdFile_ToCoordinates3, \
                      AmberTopologyFile_ToSystem , \
                      SystemGeometryTrajectory   , \
                      AmberCrdFile_FromSystem    , \
                      PDBFile_FromSystem         , \
                      XYZFile_FromSystem
  
  from pCore import Clone, logFile, Selection
  
  from pMolecule import NBModelORCA, QCModelBDF, System
  
  from pMoleculeScripts import ConjugateGradientMinimize_SystemGeometry, \
                               FIREMinimize_SystemGeometry             , \
                               LBFGSMinimize_SystemGeometry            , \
                               SteepestDescentMinimize_SystemGeometry
  # 定义结构优化接口
  def opt_ConjugateGradientMinimize(molecule, selection):
      molecule.DefineFixedAtoms(selection)       #固定原子
      #定义优化方法
      ConjugateGradientMinimize_SystemGeometry(
          molecule,
          maximumIterations    =  40,   # 最大优化步数
          rmsGradientTolerance =  0.1, #优化收敛控制
          trajectories   = [(trajectory, 1)]
      )   # 定义轨迹保存频率
  #  定义能量计算模式
  nbModel = NBModelORCA()
  qcModel = QCModelBDF("GB3LYP:6-31g")
  # 读取体系坐标和拓扑信息
  molecule = AmberTopologyFile_ToSystem ("GallicAcid.prmtop")
  molecule.coordinates3 = AmberCrdFile_ToCoordinates3("GallicAcid.crd")
  # 关闭体系对称性
  molecule.DefineSymmetry(crystalClass = None)  # QM/MM方法不支持使用周期性边界条件
  #. Define Atoms List
  natoms = len(molecule.atoms)                      # 系统中总原子数
  qm_list = range(72, 90)                            # QM 区原子
  activate_list = range(126, 144) + range (144, 162)   # MM区活性原子（优化中可以移动）
  #定义MM区原子
  mm_list = range (natoms)
  for i in qm_list:
      mm_list.remove(i)                              # MM 删除QM原子
  mm_inactivate_list = mm_list[:]
  for i in activate_list :
      mm_inactivate_list.remove(i)
  # 输入QM原子
  qmmmtest_qc = Selection.FromIterable(qm_list)     
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
  #定义输出文件目录名
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
  #保存优化坐标，可以为xyz/crd/pdb等。
  XYZFile_FromSystem(outlabel +  ".xyz", molecule)
  AmberCrdFile_FromSystem(outlabel +  ".crd" , molecule)
  PDBFile_FromSystem(outlabel +  ".pdb" , molecule)
  
  #  TDDFT计算
  qcModel = QCModelBDF_template ( )
  qcModel.UseTemplate (template = 'head_bdf_nosymm.inp' )
  
  tdtest = Selection.FromIterable ( qm_list + activate_list )
  # . Define the energy model.
  molecule.DefineQCModel ( qcModel, qcSelection = tdtest )
  molecule.DefineNBModel ( nbModel )
  molecule.Summary ( )
  
  # . Calculate
  energy  = molecule.Energy ( )

输出体系总能量信息如下：

.. code-block:: bdf

  --------------------------------- Summary of Energy Terms --------------------------------
  Potential Energy          =    -5088333.3818  RMS Gradient              =             None
  Harmonic Bond             =           0.0000  Harmonic Angle            =           0.0000
  Fourier Dihedral          =           0.0000  Fourier Improper          =           0.0000
  QC/MM LJ                  =        -112.3207  BDF QC                    =    -5088221.0611
  ------------------------------------------------------------------------------------------

同时生成.log结果文件，和普通的激发态计算一样，可以看到振子强度，激发能，激发态的总能量等信息:

.. code-block:: bdf

    No.     1    w=      4.7116 eV    -1937.8276358207 a.u.  f=    0.0217   D<Pab>= 0.0000   Ova= 0.6704
      CV(0):    A( 129 )->   A( 135 )  c_i:  0.7254  Per: 52.6%  IPA:     7.721 eV  Oai: 0.6606
      CV(0):    A( 129 )->   A( 138 )  c_i:  0.2292  Per:  5.3%  IPA:     9.104 eV  Oai: 0.8139
      CV(0):    A( 132 )->   A( 135 )  c_i:  0.4722  Per: 22.3%  IPA:     7.562 eV  Oai: 0.6924
      CV(0):    A( 132 )->   A( 138 )  c_i: -0.4062  Per: 16.5%  IPA:     8.946 eV  Oai: 0.6542

随后还打印了跃迁偶极矩:

.. code-block:: bdf

   *** Ground to excited state Transition electric dipole moments (Au) ***
    State          X           Y           Z          Osc.
       1       0.0959       0.1531       0.3937       0.0217       0.0217
       2       0.0632      -0.1286       0.3984       0.0207       0.0207
       3      -0.0797      -0.2409       0.4272       0.0287       0.0287
       4       0.0384      -0.0172      -0.0189       0.0003       0.0003
       5       1.1981       0.8618      -0.1305       0.2751       0.2751
