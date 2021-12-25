
核磁共振屏蔽常数
================================================

BDF支持限制性Hartree-Fock（RHF）和限制性Kohn-Sham（RKS）方法的核磁共振屏蔽常数（NMR）计算，
其中外矢势规范原点的问题可以使用Common gauge方法和GIAO（gauge-including atomic orbitals）处理。

.. warning::

    由于NMR计算需要libcint库，需要在计算脚本中增加一行：
    export USE_LIBCINT=yes



NMR算例
----------------------------------------------------------
以下为甲烷分子核磁共振屏蔽常数计算的输入文件：


.. code-block:: bdf

  $COMPASS  # 分子坐标输入及对称性判断等
  Title
  CH4 Molecule NR-DFT-NMR       # job title
  Basis
  CC-PVQZ                       # basis set
  Geometry
  C  0.000   00000    0.000     # molecule geometry
  H  1.196   1.196    1.196
  H -1.196  -1.196    1.196
  H -1.196   1.196   -1.196
  H  1.196  -1.196   -1.196
  END geometry
  nosymm                        # NMR模块暂不支持对称性
  UNIT
    BOHR                        # input molecule geometry in bohr
  $END

  $xuanyuan # 单双电子积分相关设定和计算
  $end

  $SCF      # 自洽场计算模块
  RKS       # Restrict Kohn-Sham
  DFT
    b3lyp
  $END

  $NMR      # 核磁共振屏蔽常数计算模块
  icg
   1        # 可输入0或1，0为不进行COMMON GAUGE计算，1为进行COMMON GAUGE计算，默认为0
  igiao
   1        # 可输入0或1，0为不进行GIAO计算，1为进行GIAO计算，默认为0
  $END

完成计算将顺序调用 ``compass`` , ``xuanyuan`` , ``scf`` 及 ``nmr`` 四个模块。其中 ``scf`` 模块执行 ``RKS`` 计算。
基于RKS的计算结果，进行后续的 ``NMR`` 计算，其中 ``NMR`` 计算将顺序进行COMMON GAUGE计算和GIAO计算，计算将给出所有原子的
各向同性以及各向异性核磁共振屏蔽常数。

COMMON GAUGE
----------------------------------------------------------
可以通过关键词icg控制进行COMMON GAUGE的NMR计算：

.. code-block:: bdf 

  $NMR
  icg
    1
  $END

可以输入0或者1，默认值为0，即不进行COMMON GAUGE计算，输入为1时，则为进行COMMON GAUGE计算。

在COMMON GAUGE计算中，规范原点默认位于坐标原点，即（0，0，0）处，可以通过关键词igatom将规范原点指定在某个原子上，
也可以通过cgcoord将规范原点设置为空间某个指定的位置，具体输入方式如下：

.. code-block:: bdf 

  $NMR
  icg
    1
  igatom
    3             # 将规范原点指定在3号原子上，输入为整型数，范围为0到分子原子数，
                  # 如输入值0，则将规范原点指定在坐标原点上
  cgcoord
    1.0 0.0 0.0   # 输入为3个实型数，将规范原点至于空间坐标为（1.0，0.0，0.0）的点上
  cgunit
    angstrom      # cgcoord坐标的单位，默认值为原子单位，当输入为angstrom，输入的规范原点坐标
                  # 单位为埃；其他输入（如bohr，AU），坐标单位为原子单位，输入不区分大小写
  $END

当输入中同时存在igatom和cgcoord时，以后输入的为准。例如上面的例子，最终规范原点设定在空间坐标为（1.0，0.0，0.0）（单位埃）的位置上。
如两个参数igatom和cgcoord都未输入，计算COMMON GAUGE的NMR值时，规范原点设在坐标原点上，即设在（0.0，0.0，0.0）的位置上。

输出文件中Common gauge计算从 ``[nmr_nr_cg]`` 开始，如下：

.. code-block:: bdf 

  [nmr_nr_cg]
    Doing nonrelativistic-CG-DFT nmr...

  [nmr_set_common_gauge]
    set the common gauge origin as the coordinate origin(default)
        0.000000000000      0.000000000000      0.000000000000

略过中间部分输出，最终结果输出如下：

.. code-block:: bdf 

  Isotropic/anisotropic constant by atom type:
    atom-C
      186.194036      0.000003
    atom-H
       31.028177      9.317141
       31.028176      9.317141
       31.028177      9.317141
       31.028177      9.317141

分别为C原子和H原子的核磁共振屏蔽常数，单位为ppm，第一列为各向同性屏蔽常数，第二列为各向异性屏蔽常数。


GIAO
----------------------------------------------------------
可以通过关键词igiao控制进行GIAO的NMR计算：

.. code-block:: bdf 

  $NMR
  igiao
    1
  $END

可以输入0或者1，默认值为0，即不进行GIAO计算，输入为1时，进行GIAO计算。

.. warning::
  NMR模块中，icg和igiao可以仅输入其中之一为1，即设定进行其中一种计算，也可以两者都输入设为1（即两种计算都进行），但是不能都不输入或者都设为0，
  不然NMR模块不会得出任何核磁共振屏蔽常数值。

输出文件中GIAO计算从 ``[nmr_nr_giao]`` 开始，如下：

.. code-block:: bdf

 [nmr_nr_giao]
  Doing nonrelativistic-GIAO-DFT nmr

 [set_para_for_giao_eri]

 [nmr_int]
   Doing nmr integral of operators resulting from the response of B10...

   No. of pGTOs and cGTOs:     196     196

   giao integrals...

略过中间部分输出，最终结果输出如下：

.. code-block:: bdf 

    Isotropic/anisotropic constant by atom type:
      atom-C
        186.461988      0.000019
      atom-H
        31.204947      9.070916
        31.204944      9.070916
        31.204947      9.070921
        31.204946      9.070920

同COMMON GAUGE的情况，上面结果分别为C原子和H原子的GIAO核磁共振屏蔽常数，单位为ppm，
第一列为各向同性屏蔽常数，第二列为各向异性屏蔽常数。

.. warning::
  输出中的关键词 ``Isotropic/anisotropic constant by atom type`` 对于
  GIAO与COMMON GAUGE完全相同，在读取结果时应注意是在 ``[nmr_nr_cg]`` 后的，
  还是 ``[nmr_nr_giao]`` 后的，来区分COMMON GAUGE的结果还是GIAO的结果
