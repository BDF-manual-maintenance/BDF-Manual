组合QM/MM方法
================================================
组合QM/MM方法一般把系统分为两个区域，QM区和MM区。将体系总能量写为：

.. math::
    E_{QM/MM}(\mathbb{S}) = E_{MM}(\mathbb{O})+E_{QM}(\mathbb{I+L})+E_{QM/MM}(\mathbb{I,O}) 

其中
:math:`E_{MM}(\mathbb{O})`
采用分子力学力场计算，
:math:`E_{QM/MM}(\mathbb{I,O})`
包括两项：

.. math::
    E_{QM/MM}(\mathbb{I,O})=E_{nuc-MM}+V_{elec-MM}

:math:`E_{nuc-MM}+V_{elec-MM}` 在BDF中通过在QM区加入外部点电荷来实现。

所以整个体系的总能量包括两个部分，:math:`E_{MM}` 采用分子力学方法计算，:math:`E_{QM}` 和 :math:`E_{QM/MM}`
采用量子化学方法计算。同时，QM区和MM区的相互作用还包括VDW相互作用等，这里不在赘述。对于QM区和MM区的断键，一般采用链接原子模型。

BDF程序主要完成量子化学计算部分，其余部分由课题组修改的pdynamo2.0程序包完成。具体见相关算例。

.. note::
  
  pdynamo 程序的安装见程序包中相关说明。有关程序包的详细功能见程序包中的帮助文件。pdynamo 程序包同时也支持使用ORCA进行QM/MM计算。
 本手册只提供BDF相关计算说明和算例。

点电荷模型
------------------------------------------------
BDF支持将MM区原子电荷作为点电荷输入进行计算。点电荷以与计算任务同名的:math:`$BDFTASK.extcharge` 文件作为输入，具体格式如下：

.. code-block:: C
    
    $COMPASS
    Title
    water molecule in backgroud of exteral charges
    Basis
      6-31g
    Geometry
    O   0.000000   0.000000   0.106830
    H   0.000000   0.785178  -0.427319
    H   0.000000  -0.785178  -0.427319
    End Geometry
    Extcharge  \# *表示需要输入点电荷*
    point      \# *表示输入电荷类型为点电荷*                                                                                                                                        
    Check
    Skeleton
    $END

   $XUANYUAN
     direct
     schwarz
    $END

   $SCF
   RHF
   $END

点电荷输入文件如下：

.. code-block:: C

    **h2o.extcharge**
   External charge, Point charge   \# *第一行为标题和说明行*
   6  \# *要输入的点电荷数* number of point charges. Next six lines are label, charge, x,y,z coordinates. Unit: angstrom(default)
   C1     -0.732879     0.000000     5.000000     0.114039 
   C2      0.366440     0.000000     5.780843    -0.456155 
   C3      0.366440     0.000000     4.219157    -0.456155
   C4     -0.732879     0.000000     10.00000     0.114039 
   C5      0.366440     0.000000     10.78084    -0.456155 
   C6      0.366440     0.000000     9.219157    -0.456155

.. note::
 *点电荷的默认输入格式为: * 标签  电荷  坐标 *x y z*

-------------------------------------------------
point charge
