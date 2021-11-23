激发态计算
================================================

BDFpro支持多种激发态计算方法，其中以基于Kohn-Sham参考态的线性响应TDDFT方法为主。与其他量化软件相比，BDFpro的TDDFT模块独具特色，主要体现在：

1. 支持各种自旋翻转（spin-flip）方法；
2. 支持自旋匹配TDDFT方法X-TDDFT，可以有效解决参考态为开壳层时激发态存在自旋污染的问题，适用于自由基、过渡金属等体系的激发态计算；
3. 支持核激发态（core excited state）相关的计算，如计算X射线吸收谱（XAS）。一般的TDDFT算法为了计算一个激发态，常需要同时把比该激发态的激发能更低的所有态均计算出来，而核激发态的能量通常非常高，这样做是不现实的。而BDFpro所使用的iVI方法则可以在不计算更低的激发态的情况下，直接计算某个较高的能量区间内的所有激发态，从而大大节省计算资源。

除此之外，BDFpro还支持在pp-TDA水平下计算激发态，以及利用MOM方法在SCF水平下计算激发态等。

TDDFT计算示例1：UV-Vis吸收光谱的计算（垂直激发）
-------------------------------------------
垂直激发能以及振子强度是TDDFT最基本的应用场景之一。以下以乙烯在PBE0/def2-SVP级别下的垂直激发为例，介绍TDDFT垂直激发计算的输入文件写法以及输出文件的分析。

.. code-block:: python
  
  $COMPASS
  Title
   TDDFT test
  Basis
   def2-SVP
  geometry
   C                  0.00000000   -0.67760000    0.00000000
   H                  0.92664718   -1.21260000    0.00000000
   H                 -0.92664718   -1.21260000    0.00000000
   C                 -0.00000000    0.67760000    0.00000000
   H                 -0.92664718    1.21260000    0.00000000
   H                  0.92664718    1.21260000   -0.00000000
  End geometry
  Skeleton
  $END

  $XUANYUAN
  Direct
  $END

  $SCF
  RKS
  dft
   PBE0
  $END

  $TDDFT
  iroot
   2
  $END

可以看到，输入文件的大部分内容和SCF单点能计算的输入文件一致，仅在最后添加了TDDFT模块，以iroot（也可写iexit，作用相同）关键词指定需要计算的激发态数目即可。注意因为乙烯分子属于D2h点群，共有8个不可约表示，而不同不可约表示的激发态是分别求解的，因此视用户需求而定，有以下若干种指定激发态数目的方法，例如：

（1）每个不可约表示均计算2个激发态：

.. code-block:: python
  
  $TDDFT
  iroot
   2
  $END

（2）只计算一个B1u激发态和一个B1g激发态，不计算其他不可约表示下的激发态：

.. code-block:: python
  
  $TDDFT
  nroot
   0 1 0 0 0 1 0 0
  $END

其中nroot关键字（也可写nexit）表明用户分别对每个不可约表示指定激发态的数目。因程序内部将D2h点群的不可约表示以Ag、B1g、B3g、B2g、Au、B1u、B3u、B2u的顺序排列，因此以上输入表明只计算B1g、B1u激发态各一个。如用户确需要对每个不可约表示单独指定激发态数目，建议先运行一个只有COMPASS模块的输入文件，由COMPASS模块的输出（详见本说明书的Hartree-Fock章节）即可知晓当前分子所属点群各个不可约表示的顺序。

（3）计算最低的8个激发态，而不限定这些激发态的不可约表示

.. code-block:: python
  
  $TDDFT
  iroot
   -8
  $END

此时程序通过初始猜测的激发能来判断各个不可约表示应当求解多少个激发态，但因为初始猜测的激发能排列顺序可能和完全收敛的激发能有一定差异，程序不能严格保证求得的8个激发态一定是能量最低的8个激发态。如用户要求严格保证得到的8个激发态为最低的8个激发态，用户应当令程序计算多于8个激发态，如12个激发态，然后取能量最低的8个。

输出文件中，COMPASS、XUANYUAN和SCF模块的输出与SCF单点能算例类似，在此不再赘述。TDDFT模块输出一些基本信息以后，进入实际的TDDFT计算，首先输出每个不可约表示的总激发态数，以及程序将求解的激发态数目（以每个不可约表示均计算2个激发态的输入文件为例）：

.. code-block:: python
  
 [tddft_select]
 [ Targeted Excited States / Diag method ]
  TD-Nsym:    8
  1   Ag       2 from       57   1
  2  B1g       2 from       23   1
  3  B3g       2 from       31   1
  4  B2g       2 from       49   1
  5   Au       2 from       23   1
  6  B1u       2 from       59   1
  7  B3u       2 from       49   1
  8  B2u       2 from       29   1
  Total No. of excited states:      16
 Estimate memory in tddft_init mem:           0.003 M

之后程序对每个不可约表示进行逐一求解，例如Ag表示（需要注意的是，此处ExctSym是激发态的不可约表示，而PairSym是激发态所涉及的占据轨道和虚轨道的不可约表示的直积；ExctSym等于PairSym和基态的不可约表示的直积。对于该示例，因基态属于全同表示，ExctSym和PairSym相同，但是对于开壳层分子，基态不一定属于全同表示，因此ExctSym和PairSym可能会不同）：

.. code-block:: python
  
 ==============================================
  Jrep: 1  ExctSym:  Ag  (convert to td-psym)
  Irep: 1  PairSym:  Ag  GsSym:  Ag
  Nexit:       2     Nsos:      57
 ==============================================
 Estimated memory for JK operator:          0.422 M
 Maximum memory to calculate JK operator:         512.000 M
 Allow to calculate    2 roots at one pass for RPA ...
 Allow to calculate    4 roots at one pass for TDA ...

  Nlarge=               57 Nlimdim=               57 Nfac=               50
  Estimated mem for dvdson storage (RPA) =           0.127 M          0.000 G
  Estimated mem for dvdson storage (TDA) =           0.051 M          0.000 G
  
 ...
  
 Iteration started !

 Niter=     1   Nlarge =      57   Nmv =       3
 Ndim =     3   Nlimdim=      57   Nres=      54
 Approximated Eigenvalue (i,w,diff/eV,diff/a.u.):
    1       12.9280903589       12.9280903589           0.475E+00
    2       14.7433759852       14.7433759852           0.542E+00
 No. of converged eigval:     0
 Norm of Residuals:
    1        0.0115391158        0.0530850207           0.115E-01           0.531E-01
    2        0.0091215630        0.0512021244           0.912E-02           0.512E-01
 No. of converged eigvec:     0
 Max norm of residues   :  0.531E-01
 
 ...
 
 Niter=     5   Nlarge =      57   Nmv =      19
 Ndim =    19   Nlimdim=      57   Nres=      38
 Approximated Eigenvalue (i,w,diff/eV,diff/a.u.):
    1       12.8023123809        0.0000000222           0.816E-09
    2       14.5634695655        0.0000000761           0.280E-08
 No. of converged eigval:     2
 ### Cong: Eigenvalues have Converged ! ###
 Norm of Residuals:
    1        0.0000002743        0.0000003243           0.274E-06           0.324E-06
    2        0.0000007972        0.0000009911           0.797E-06           0.991E-06
 No. of converged eigvec:     2
 Max norm of residues   :  0.991E-06
 ### Cong.  Residuals Converged ! ###

经5次Davidson迭代后，程序求得了最低的两个Ag激发态，其激发能分别为12.80 eV和14.56 eV，并给出两个态的主要成分：

.. code-block:: python
 No.     1    w=     12.8023 eV      -77.9524434004 a.u.  f= 0.0000   D<Pab>= 0.0000   Ova= 0.5044
      CV(0):   Ag(   3 )->  Ag(   4 )  c_i: -0.9836  Per: 96.7%  IPA:    14.207 eV  Oai: 0.5001
      CV(0):  B2g(   1 )-> B2g(   2 )  c_i:  0.1389  Per:  1.9%  IPA:    15.662 eV  Oai: 0.5951

 No.     2    w=     14.5635 eV      -77.8877220911 a.u.  f= 0.0000   D<Pab>= 0.0000   Ova= 0.6002
      CV(0):  B2g(   1 )-> B2g(   2 )  c_i:  0.9599  Per: 92.1%  IPA:    15.662 eV  Oai: 0.5951
      CV(0):  B3u(   1 )-> B3u(   2 )  c_i: -0.2091  Per:  4.4%  IPA:    16.607 eV  Oai: 0.6484
      CV(0):  B2u(   1 )-> B2u(   2 )  c_i: -0.1209  Per:  1.5%  IPA:    21.635 eV  Oai: 0.8303

其中：
 * ``-77.9524434004 a.u.``为激发态的电子能（等于基态电子能加激发能）；
 * ``f= 0.0000``为振子强度；
 * ``D<Pab>= 0.0000``为激发态的<S^2>值与基态的<S^2>值之差（对于自旋守恒跃迁，该值反映了激发态的自旋污染程度；对于自旋翻转跃迁，该值与理论值``S(S+1)(激发态)-S(S+1)(基态)``之差反映了激发态的自旋污染程度）；
 * ``Ova= 0.5044``为绝对重叠积分（absolute overlap integral，取值范围为[0,1]，该值越接近0，说明相应的激发态的电荷转移特征越明显，否则说明局域激发特征越明显）。

这一行下面列举了该激发态主要由哪些跃迁组成，以**CV(0):   Ag(   3 )->  Ag(   4 )  c_i: -0.9836  Per: 96.7%  IPA:    14.207 eV  Oai: 0.5001**为例：
 * ``CV``代表从闭壳层轨道（Closed shell orbital，也即双占轨道）到开壳层轨道（Vacant shell orbital，也即空轨道）的跃迁；
 * ``(0)``代表该CV跃迁产生的两个单电子彼此耦合成单重态（S=0），如耦合成三重态，此处会输出``(1)``；
 * ``Ag(   3 )->  Ag(   4 )``代表从Ag不可约表示的第3个轨道到Ag不可约表示的第4个轨道的跃迁；
 * ``c_i: -0.9836``代表该跃迁在整个激发态里的线性组合系数为-0.9836，注意一般所谓的某跃迁占激发态的比例并不是这个数，而是这个数的平方，即后面输出的``Per: 96.7%``；
 * ``IPA:    14.207 eV``代表该跃迁所涉及的两个轨道的能量差为14.207 eV；
 * ``Oai: 0.5001``表示假如该激发态只有这一个跃迁的贡献，那么该激发态的绝对重叠积分为0.5001，由这一信息可以方便地得知哪些跃迁是局域激发，哪些跃迁是电荷转移激发。

待所有不可约表示均计算完毕后，程序会把所有不可约表示的计算结果汇总，并按激发能从低到高排序：

.. code-block:: python
 *** List of excitations ***

  Ground-state spatial symmetry:  Ag
  Ground-state spin: Si=  0.0000

  Spin change: isf=  0
  D<S^2>_pure=  2.0000 for excited state (Sf=Si+1)
  D<S^2>_pure=  0.0000 for excited state (Sf=Si)

  Imaginary/complex excitation energies :   0 states
  Reversed sign excitation energies :   0 states

  No. Pair   ExSym   ExEnergies  Wavelengths      f     D<S^2>          Dominant Excitations             IPA   Ova     En-E1

    1 B1u    1 B1u    8.0033 eV    154.92 nm   0.3736   0.0000  89.7%  CV(0): B2u(   1 )-> B3g(   1 )   7.923 0.885    0.0000
    2 B1g    1 B1g    8.3656 eV    148.21 nm   0.0000   0.0000  98.0%  CV(0): B2g(   1 )-> B3g(   1 )  10.429 0.550    0.3623
    3 B2u    1 B2u    8.7304 eV    142.01 nm   0.0057   0.0000  99.5%  CV(0): B2u(   1 )->  Ag(   4 )  10.340 0.393    0.7271
    4 B1g    2 B1g    9.2857 eV    133.52 nm   0.0000   0.0000  98.3%  CV(0): B2u(   1 )-> B3u(   2 )  11.013 0.390    1.2824
    5 B3g    1 B3g    9.3762 eV    132.23 nm   0.0000   0.0000  94.7%  CV(0):  Ag(   3 )-> B3g(   1 )  11.790 0.573    1.3729
    6 B3g    2 B3g    9.9293 eV    124.87 nm   0.0000   0.0000  95.1%  CV(0): B2u(   1 )-> B1u(   3 )  11.372 0.419    1.9260
    7 B2g    1 B2g   11.2908 eV    109.81 nm   0.0000   0.0000  99.5%  CV(0): B2g(   1 )->  Ag(   4 )  12.846 0.565    3.2875
    8  Au    1  Au   11.3006 eV    109.71 nm   0.0000   0.0000  87.2%  CV(0): B3u(   1 )-> B3g(   1 )  13.517 0.535    3.2973
    9  Au    2  Au   11.5993 eV    106.89 nm   0.0000   0.0000  87.2%  CV(0): B2u(   1 )-> B2g(   2 )  13.156 0.353    3.5960
   10 B1u    2 B1u   12.1876 eV    101.73 nm   0.3045   0.0000  98.4%  CV(0): B2g(   1 )-> B3u(   2 )  13.519 0.635    4.1843
   11 B3u    1 B3u   12.5222 eV     99.01 nm   0.3468   0.0000  98.6%  CV(0): B2g(   1 )-> B1u(   3 )  13.878 0.589    4.5189
   12  Ag    2  Ag   12.8023 eV     96.85 nm   0.0000   0.0000  96.7%  CV(0):  Ag(   3 )->  Ag(   4 )  14.207 0.504    4.7990
   13 B3u    2 B3u   13.3154 eV     93.11 nm   0.1864   0.0000  95.5%  CV(0):  Ag(   3 )-> B3u(   2 )  14.880 0.526    5.3121
   14  Ag    3  Ag   14.5635 eV     85.13 nm   0.0000   0.0000  92.1%  CV(0): B2g(   1 )-> B2g(   2 )  15.662 0.600    6.5602
   15 B2u    2 B2u   15.0558 eV     82.35 nm   0.0828   0.0000  90.9%  CV(0): B1u(   2 )-> B3g(   1 )  16.377 0.713    7.0525
   16 B2g    2 B2g   15.3421 eV     80.81 nm   0.0000   0.0000  94.3%  CV(0):  Ag(   3 )-> B2g(   2 )  17.023 0.438    7.3388
 
 
TDDFT计算示例2：荧光光谱的计算（激发态结构优化）
-------------------------------------------
