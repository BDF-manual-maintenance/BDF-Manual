.. _FirstExample:

第一个算例 :math:`\ce{H2O}` 分子的RHF计算
================================================
Hartree-Fock是量子化学最基本算法。本小节，我们将通过一个水分子的Hartree-Fock计算例子，引导用户完成一个BDF计算并分析输入与输出信息。这里，我们先给出BDF的简洁输入，为了使用户理解BDF的简洁输入与高级输入模式的区别，我们也会给出每个简洁输入对应的高级输入文件。


准备输入
-------------------------------------------------------
首先准备水分子单点能量Hartree-Fock计算的输入文件，命名为 ``h2o.inp``, 输入内容如下：

.. code-block:: bdf 

    #!bdf.sh
    HF/3-21G    
  
    Geometry
    O
    H  1  R1 
    H  1  R1  2 109.
  
    R1=1.0     # input bond length with the default unit angstrom
    End geometry

输入解读如下：
 - 第一行必须以 ``#!`` 开始，跟着一个名为 ``bdf.sh`` 字符串，这个可以是任意的字母和数组字成字符串，不能包含除 ``.`` 外的特殊字符。第一行是系统保留行，用户可以利用这个字符串来标记计算任务。
 - 第二行 ``HF/3-21G`` 是BDF的计算参数控制行， ``HF`` 是Hartree-Fock的缩写， ``3-21G`` 指定计算使用 ``3-21G`` 基组。关键参数控制行可以是连续的多行。
 - 第三行为空行，可忽略。这里输入是为了区分不同的输入内容，增强输入的可读性，建议用户保留。
 - 第四行与第十行分别为 ``Geometry`` 和 ``End geometry`` ，标记分子几何结构输入的起始与中止，坐标的默认单位是埃 (Angstrom)。
 - 第五行到第九行用内坐标的模式输入了水分子的结构。(详见 :ref:`分子结构的内坐标格式输入<Internal-Coord>`)

这个简单的输入对应的BDF高级输入为：

.. code-block:: bdf 

  $compass
  Geometry
    O
    H 1 1.0
    H 1 1.0 2 109.
  End geometry
  Basis
    3-21g  # set basis set as 3-21g
  $end
  
  $xuanyuan
  $end
  
  $scf
  RHF       # 限制性Hartree-Fock方法
  Charge    # 分子的电荷设置为0，默认计算中性分子，电荷为零
    0    
  Spinmulti # 自旋多重度 2S+1，偶数电子体系默认计算单重态
    1    
  $end

从高级输入可以看出，BDF将按顺序执行模块 **COMPASS** ， **XUANYUAN** 和 **SCF** 完成水分子的单点能量计算。
**COMPASS** 用于读入分子结构，基函数等基本信息，判断分子的对称性，将分子转动到标准取向(Standard orientation，详见 :ref:`BDF对群论的使用小节<Point-Group>`)，产生对称匹配轨道等，
并将这些信息存入BDF的执行目录下的文件 ``h2o.chkfil`` 。 **COMPASS** 中的关键词

 * ``Geometry`` 到 ``End geometry`` 之间定义的分子结构;
 * ``Basis`` 定义基组为 ``3-21G``;

执行完 **COMPASS** 模块后，BDF利用 **XUANYUAN** 模块计算单、双电子积分。由于BDF默认采用的是 **重复计算双电子积分的SCF** 方法，即 **Integral Direct SCF** 。

最后，BDF执行 **SCF** 模块，完成基于Hartree-Fock的自洽场计算。

 * ``RHF`` 指定使用限制性Hartree-Fock方法;
 * ``Charge`` 指定体系的电荷为0;
 * ``Spinmulti`` 指定体系的自旋多重度为1。

这里 ``RHF`` 是必须输入的关键词， ``Charge`` 和 ``Spinmulti`` 对于限制性方法可以忽略。

执行计算
-------------------------------------------------------
执行计算，需要准备一个Shell脚本，命名为 ``run.sh`` ,放入 输入文件 ``h2o.inp`` 所在的目录。内容如下：

.. code-block:: shell

    #!/bin/bash

    # 设置BDF的安装目录
    export BDFHOME=/home/bsuo/bdf-pkg-pro
    # 设置BDF的临时文件存放目录
    export BDF_TMPDIR=/tmp/$RANDOM

    # 设置可用堆区内存不受限，如果在超算环境计算，可能会受系统管理的限制
    ulimit -s unlimitted
    # 设定可用计算时间不受限，如果在超算环境计算，可能会受系统管理的限制
    ulimit -t unlimitted

    # 设置OpenMP并行线程数
    export OMP_NUM_THREADS=4
    # 设置OpenMP可用堆区内存大小
    export OMP_STACKSIZE=1024M

    # 执行BDF计算，注意，默认输出会打印至标准输出
    $BDFHOME/sbin/bdfdrv.py -r h2o.inp 

以上是 ``Bash Shell`` 脚本，定义了一些基本的环境变量，并利用 ``$BDFHOME/sbin/bdfdrv.py`` 执行计算。脚本中定义的环境变量有：

 * ``BDFHOME`` 变量指定BDF的安装目录；
 * ``BDF_TMPDIR`` 变量指定BDF运行时临时文件存放目录；
 * ``ulimit -s unlimitted`` 设定程序可用的Stack区内存不受限；
 * ``ulimit -t unlimitted`` 设定程序执行时间不受限；
 * ``export OMP_NUM_THREADS=4`` 设定可用4个OpenMP线程执行并行计算；
 * ``export OMP_STACKSIZE=1024M`` 设定OpenMP可用的Stack区内存为1024兆字节。

执行计算的命令为

.. code-block:: shell

    $ ./run.sh h2o.inp &>h2o.out&

由于BDF将默认输出打印到标准输出，这里我们用了Linux的重定向命令，将标准输出定向到文件 ``h2o.out`` 。

计算结果分析
-------------------------------------------------------
计算结束后，将得到 ``h2o.out`` , ``h2o.chkfil`` , ``h2o.scforb`` 等文件。
 
 * ``h2o.out`` 是文本文件，用户可读，存储BDF输出打印信息；
 * ``h2o.chkfil`` 是二进制文件，用户不可读，用于在BDF不同模块间传递数据；
 * ``h2o.scforb`` 是文本文件，用户可读，存储了 ``scf`` 自洽迭代的分子轨道因子、轨道能等信息，主要用于重启动或作为其他scf计算的初始猜测轨道。

如果输入文件采用的是BDF简洁输入模式， ``h2o.out`` 中首先会给出一些基本的用户设置信息,

.. code-block:: bdf 

  |================== BDF Control parameters ==================|
 
    1: Input BDF Keywords
      soc=None    scf=rhf    skeleton=True    xcfuntype=None    
      xcfun=None    direct=True    charge=0    hamilton=None    
      spinmulti=1    
   
    2: Basis sets
       ['3-21g']
   
    3: Wavefunction, Charges and spin multiplicity
      charge=0    nuclearcharge=10    spinmulti=1    
   
    5: Energy method
       scf
   
    7: Acceleration method
       ERI
   
    8: Potential energy surface method
       energy

  |============================================================|

这里，

 * ``Input BDF Keywords`` 给出了一些基本控制参数； 
 * ``Basis set`` 给出计算所用基组；
 * ``Wavefunction, Charges and spinmulti`` 给出了体系电荷、总的核电荷数和自旋多重度(2S+1)；
 * ``Energy method`` 给出能量计算方法；
 * ``Accleration method`` 给出双电子积分计算加速方法；
 * ``Potential energy surface method`` 给出势能面计算方法，这里是单点能量计算。

随后，系统执行 **COMPASS** 模块，会给出如下提示：

.. code-block:: 
  
    |************************************************************|
    
        Start running module compass
        Current time   2021-11-18  11:26:28

    |************************************************************|


然后打印输入的分子结构的笛卡尔坐标，单位为 **Bohr** ，以及每种类型原子的基函数详细信息

.. code-block:: 

    |---------------------------------------------------------------------------------|
    
     Atom   Cartcoord(Bohr)               Charge Basis Auxbas Uatom Nstab Alink  Mass
      O     0.000000  0.000000  0.000000  8.00    1     0     0     0   E     15.9949
      H     1.889726  0.000000  0.000000  1.00    2     0     0     0   E      1.0073
      H    -0.615235  1.786771  0.000000  1.00    2     0     0     0   E      1.0073
    
    |----------------------------------------------------------------------------------|
    
      End of reading atomic basis sets ..
     Printing basis sets for checking ....
    
     Atomic label:  O   8
     Maximum L  1 6s3p ----> 3s2p NBF =   9
     #--->s function
          Exp Coef          Norm Coef       Con Coef
               322.037000   0.192063E+03    0.059239    0.000000    0.000000
                48.430800   0.463827E+02    0.351500    0.000000    0.000000
                10.420600   0.146533E+02    0.707658    0.000000    0.000000
                 7.402940   0.113388E+02    0.000000   -0.404454    0.000000
                 1.576200   0.355405E+01    0.000000    1.221562    0.000000
                 0.373684   0.120752E+01    0.000000    0.000000    1.000000
     #--->p function
          Exp Coef          Norm Coef       Con Coef
                 7.402940   0.356238E+02    0.244586    0.000000
                 1.576200   0.515227E+01    0.853955    0.000000
                 0.373684   0.852344E+00    0.000000    1.000000
    
    
     Atomic label:  H   1
     Maximum L  0 3s ----> 2s NBF =   2
     #--->s function
          Exp Coef          Norm Coef       Con Coef
                 5.447178   0.900832E+01    0.156285    0.000000
                 0.824547   0.218613E+01    0.904691    0.000000
                 0.183192   0.707447E+00    0.000000    1.000000

随后，自动判断分子对称性，并根据用户设置决定是否转动为标准取向模式，

.. code-block:: 

    Auto decide molecular point group! Rotate coordinates into standard orientation!
    Threshold= 0.10000E-08 0.10000E-11 0.10000E-03
    geomsort being called!
    gsym: C02V, noper=    4
    Exiting zgeomsort....
    Representation generated
    Binary group is observed ...
    Point group name C(2V)                       4
    User set point group as C(2V)   
     Largest Abelian Subgroup C(2V)                       4
     Representation generated
     C|2|V|                    2

    Symmetry check OK
    Molecule has been symmetrized
    Number of symmery unique centers:                     2
    |---------------------------------------------------------------------------------|
    
     Atom   Cartcoord(Bohr)               Charge Basis Auxbas Uatom Nstab Alink  Mass
      O     0.000000  0.000000  0.000000  8.00    1     0     0     0   E     15.9949
      H     1.889726  0.000000  0.000000  1.00    2     0     0     0   E      1.0073
      H    -0.615235  1.786771  0.000000  1.00    2     0     0     0   E      1.0073
    
    |----------------------------------------------------------------------------------|
    
     Atom   Cartcoord(Bohr)               Charge Basis Auxbas Uatom Nstab Alink  Mass
      O     0.000000 -0.000000  0.219474  8.00    1     0     0     0   E     15.9949
      H    -1.538455  0.000000 -0.877896  1.00    2     0     0     0   E      1.0073
      H     1.538455 -0.000000 -0.877896  1.00    2     0     0     0   E      1.0073
    
    |----------------------------------------------------------------------------------|

细心的用户可能已经注意到，这里的水分子的坐标与输入的不一样。最后， **COMPASS** 会产生对称匹配轨道（Symmetry adapted orbital），并给出偶极矩和四极矩所属
的不可约表示，打印 ``C(2v)`` 点群的乘法表，给出总的基函数数目和每个不可约表示对称匹配轨道数目。

.. code-block:: 

    Number of irreps:    4
    IRREP:   3   4   1
    DIMEN:   1   1   1
    
     Irreps of multipole moment operators ...
     Operator  Component    Irrep       Row
      Dipole       x           B1          1
      Dipole       y           B2          1
      Dipole       z           A1          1
      Quadpole     xx          A1          1
      Quadpole     xy          A2          1
      Quadpole     yy          A1          1
      Quadpole     xz          B1          1
      Quadpole     yz          B2          1
      Quadpole     zz          A1          1
    
     Generate symmetry adapted orbital ...
     Print Multab
      1  2  3  4
      2  1  4  3
      3  4  1  2
      4  3  2  1
    
    |--------------------------------------------------|
              Symmetry adapted orbital                   
    
      Total number of basis functions:      13      13
    
      Number of irreps:   4
      Irrep :   A1        A2        B1        B2      
      Norb  :      7         0         4         2
    |--------------------------------------------------|

这里， ``C(2v)`` 点群有4个一维不可约表示，标记为 ``A1, A2, B1, B2`` , 分别有 ``7, 0, 4, 2`` 个对称匹配的轨道。

.. attention::

    不同的量子化学软件，可能会采用不同的分子标准取向，导致某些分子轨道在不同程序中标记为不同的不可约表示。

最后， ``COMPASS`` 计算正常结束，会给出如下输出：

.. code-block:: 

    |******************************************************************************|

        Total cpu     time:          0.00  S
        Total system  time:          0.00  S
        Total wall    time:          0.02  S
    
        Current time   2021-11-18  11:26:28
        End running module compass
    |******************************************************************************|


.. note::

    BDF的每个模块执行，都会有开始执行和执行结束后打印时间信息，方便用户具体定位哪个计算模块出错。


本算例计算执行的第二个模块是 **XUANYUAN** ， 该模块主要用于计算单、双电子积分。如果不特别指定，BDF默认采用直接计算双电子积分构造Fock矩阵的算法。这里， **XUANYUAN** 模块只计算和保存单电子积分及需要做积分预筛选的特殊双电子积分。如果用户在 ``compass`` 模块指定了 :ref:`Saorb<compass.saorb>` 关键词，双电子积分将被计算并保存到硬盘。 **XUANYUAN** 模块的输出比较简单，一般不需要特别关注。这里，我们给出最关键的输出：

.. code-block:: 

    [aoint_1e]
      Calculating one electron integrals ...
      S T and V integrals ....
      Dipole and Quadupole integrals ....
      Finish calculating one electron integrals ...
    
     ---------------------------------------------------------------
      Timing to calculate 1-electronic integrals                                      
    
      CPU TIME(S)      SYSTEM TIME(S)     WALL TIME(S)
              0.017            0.000               0.000
     ---------------------------------------------------------------
    
     Finish calculating 1e integral ...
     Direct SCF required. Skip 2e integral!
     Set significant shell pairs!
    
     Number of significant pairs:        7
     Timing caluclate K2 integrals.
     CPU:       0.00 SYS:       0.00 WALL:       0.00
    
从输出我们看到单电子重叠、动能与核吸引积分被计算，还计算了偶极矩和四极矩积分。由于输入要求默认的积分直接SCF计算（Direct SCF），双电子积分计算被忽略。

最后，BDF调用 **SCF** 模块执行 **RHF** 自洽场计算。需要关注的信息有：

.. code-block:: 

     Wave function information ...
     Total Nuclear charge    :      10
     Total electrons         :      10
     ECP-core electrons      :       0
     Spin multiplicity(2S+1) :       1
     Num. of alpha electrons :       5
     Num. of beta  electrons :       5

这里给出了核电荷数、总电子数、赝势计算的芯电子数、自旋多重度、alpha及beta电子数等信息，用户应当检查电子态是否正确。
然后， ``scf`` 模块先计算原子，并产生分子计算的初始猜测密度矩阵，

.. code-block:: 

     [ATOM SCF control]
      heff=                     0
     After initial atom grid ...
     Finish atom    1  O             -73.8654283850
     After initial atom grid ...
     Finish atom    2  H              -0.4961986360
    
     Superposition of atomic densities as initial guess.

检查处理基函数可能的线性相关问题，

.. code-block:: 

     Check basis set linear dependence! Tolerance =   0.100000E-04

随后进入SCF迭代，8次迭代收敛后关闭 **DIIS** 和 **Level shift** 等加速收敛方法并重新计算能量，

.. code-block:: 

    Iter. idiis vshift  SCF Energy    DeltaE     RMSDeltaD    MaxDeltaD   Damping Times(S) 
    1    0   0.000  -75.465225043  -0.607399386  0.039410497  0.238219747  0.0000   0.00
    2    1   0.000  -75.535887715  -0.070662672  0.013896819  0.080831047  0.0000   0.00
    3    2   0.000  -75.574187153  -0.038299437  0.004423591  0.029016074  0.0000   0.00
    4    3   0.000  -75.583580885  -0.009393732  0.000961664  0.003782740  0.0000   0.00
    5    4   0.000  -75.583826898  -0.000246012  0.000146525  0.000871203  0.0000   0.00
    6    5   0.000  -75.583831666  -0.000004768  0.000012300  0.000073584  0.0000   0.00
    7    6   0.000  -75.583831694  -0.000000027  0.000001242  0.000007487  0.0000   0.00
    8    7   0.000  -75.583831694  -0.000000000  0.000000465  0.000002549  0.0000   0.00
    diis/vshift is closed at iter =   8
    9    0   0.000  -75.583831694  -0.000000000  0.000000046  0.000000221  0.0000   0.00
    
      Label              CPU Time        SYS Time        Wall Time
     SCF iteration time:         0.017 S        0.017 S        0.000 S

最后打印不同项的能量贡献和维里比。

.. code-block:: 

     Final scf result
       E_tot =               -75.58383169
       E_ele =               -84.37566837
       E_nn  =                 8.79183668
       E_1e  =              -121.94337426
       E_ne  =              -197.24569473
       E_kin =                75.30232047
       E_ee  =                37.56770589
       E_xc  =                 0.00000000
      Virial Theorem      2.003738

根据维里定律(Virial Theorem)，对于非相对论系统，系统的总势能的绝对值是电子的动能的2倍，这里的维里比是 ``2.003738`` 。 系统的能量为：

 * ``E_tot`` 是系统总能量，即 ``E_ele`` + ``E_nn`` ;
 * ``E_ele`` 是电子能量，即 ``E_1e`` + ``E_ee`` + ``E_xc`` ;
 * ``E_nn``  是原子核排斥能;
 * ``E_1e``  是单电子能量，即 ``E_ne`` + ``E_kin`` ;
 * ``E_ne``  是原子核对电子的吸引能;
 * ``E_kin`` 是电子动能;
 * ``E_ee`` 是双电子能，包括库伦排斥和交换能；
 * ``E_xc`` 是交换相关能，DFT计算时不为0.

能量打印后输出的是轨道的占据情况、轨道能、HUMO-LOMO能量和能隙等信息，如下所示：

.. code-block:: 

     [Final occupation pattern: ]
    
     Irreps:        A1      A2      B1      B2  
    
     detailed occupation for iden/irep:      1   1
        1.00 1.00 1.00 0.00 0.00 0.00 0.00
     detailed occupation for iden/irep:      1   3
        1.00 0.00 0.00 0.00
     detailed occupation for iden/irep:      1   4
        1.00 0.00
     Alpha       3.00    0.00    1.00    1.00
    
    
     [Orbital energies:]
    
     Energy of occ-orbs:    A1            3
        -20.43281195      -1.30394125      -0.52260024
     Energy of vir-orbs:    A1            4
          0.24980046       1.23122290       1.86913815       3.08082943
    
     Energy of occ-orbs:    B1            1
         -0.66958992
     Energy of vir-orbs:    B1            3
          0.34934415       1.19716413       2.03295437
    
     Energy of occ-orbs:    B2            1
          -0.47503768
     Energy of vir-orbs:    B2            1
           1.78424252
    
     Alpha   HOMO energy:      -0.47503768 au     -12.92643838 eV  Irrep: B2      
     Alpha   LUMO energy:       0.24980046 au       6.79741929 eV  Irrep: A1      
     HOMO-LUMO gap:       0.72483814 au      19.72385767 eV

这里

 * ``[Final occupation pattern: ]`` 给出的是轨道占据情况。由于我们进行的是限制性Hartree-Fock计算，占据情况只给出了Alpha轨道的信息，按照不可约表示分别给出。从这个例子可以看出，A1轨道的前3个、B1和B2轨道的第1个分别有1个电子占据。由于本算例是RHF，alpha与beta轨道是一样的，所以A1表示有3个双占据轨道，B1和B2表示分别有1个双占据轨道。
 * ``[Orbital energies:]`` 按照不可约表示分别给出轨道能；
 * ``Alpha   HOMO energy:`` 按照单位 au 和 eV 给出了HOMO轨道能；该轨道所属的不可约表示，这里是B2；
 * ``Alpha   LUMO energy:`` 按照单位 au 和 eV 给出了LUMO轨道能；该轨道所属的不可约表示，这里是A1；
 * ``HOMO-LUMO gap:`` 给出HOMO和LUMO轨道的能差。

为了减少输出行数，BDF默认不打印轨道成分及分子轨道系数，只按照不可约表示分类给出部分轨道占据数和轨道能信息，如下：

.. code-block:: 

      Symmetry   1 A1
    
        Orbital          1          2          3          4          5          6
        Energy     -20.43281   -1.30394   -0.52260    0.24980    1.23122    1.86914
        Occ No.      2.00000    2.00000    2.00000    0.00000    0.00000    0.00000
    
    
      Symmetry   2 A2
    
    
      Symmetry   3 B1
    
        Orbital          8          9         10         11
        Energy      -0.66959    0.34934    1.19716    2.03295
        Occ No.      2.00000    0.00000    0.00000    0.00000
    
    
      Symmetry   4 B2
    
        Orbital         12         13
        Energy      -0.47504    1.78424
        Occ No.      2.00000    0.00000
             
**SCF** 模块最后打印的是Mulliken和Lowdin布居分析的结果，分子的偶极矩信息。

.. code-block:: 

     [Mulliken Population Analysis]
      Atomic charges: 
         1O      -0.7232
         2H       0.3616
         3H       0.3616
         Sum:    -0.0000
    
     [Lowdin Population Analysis]
      Atomic charges: 
         1O      -0.4756
         2H       0.2378
         3H       0.2378
         Sum:    -0.0000
    
    
     [Dipole moment: Debye]
               X          Y          Z     
       Elec:-.1081E-64 0.4718E-32 -.2368E+01
       Nucl:0.0000E+00 0.0000E+00 0.5644E-15
       Totl:   -0.0000     0.0000    -2.3684

.. hint:: 
    1. 在 **SCF** 模块输入中加入 ``iprtmo`` 关键词，值设置为 ``2`` ，可以输出分子轨道的详细信息；
    2. 在 **SCF** 模块输入中加入 ``molden`` 关键词，可以将分子轨道和占据输出为molden格式的文件，
    可用第三方程序做可视化（如 `GabEdit <http://gabedit.sourceforge.net/>`_， `JMol <http://jmol.sourceforge.net>`_，
    `Molden <https://www.theochem.ru.nl/molden/>`_，`Multiwfn <http://sobereva.com/multiwfn/>`_），
    进行 :ref:`波函数分析<1e-prop>` ，或计算 :ref:`单电子性质<1e-prop>` 。

