TDDFT
================================================

BDF支持多种激发态计算方法，其中以基于Kohn-Sham参考态的线性响应含时密度泛函 （TDDFT）方法为主。与其他量化软件相比，BDF的TDDFT模块独具特色，主要体现在：

1. 支持各种自旋翻转（spin-flip）方法；
2. 支持自旋匹配TDDFT方法X-TDDFT，可以有效解决参考态为开壳层时激发态存在自旋污染的问题，适用于自由基、过渡金属等体系的激发态计算；
3. 支持核激发态（core excited state）相关的计算，如计算X射线吸收谱（XAS）。一般的TDDFT算法为了计算一个激发态，常需要同时把比该激发态的激发能更低的所有态均计算出来，而核激发态的能量通常非常高，这样做是不现实的。而BDF所使用的iVI方法则可以在不计算更低的激发态的情况下，直接计算某个较高的能量区间内的所有激发态，从而大大节省计算资源。

除此之外，BDF还支持在pp-TDA水平下计算激发态，以及利用MOM方法在SCF水平下计算激发态等。


闭壳层体系计算：R-TDDFT
----------------------------------------------------------

R-TDDFT用于计算闭壳层体系。如果基态计算从RHF出发，TDDFT模块执行的是TDHF计算。
利用TDDFT计算H2O分子激发能，简洁输入如下：

.. code-block:: python

  #!bdf.sh
  TDDFT/B3lyp/cc-pvdz     
  
  geometry
  O
  H  1  R1
  H  1  R1  2 109.
  
  R1=1.0       # OH bond length in angstrom
  end geometry

这里，关键词

* ``TDDFT/B3lyp/cc-pvdz`` 指定执行TDDFT计算，所用泛函为 ``B3lyp`` ,基组为 ``cc-pVDZ``. 

与之对应的高级输入为：

.. code-block:: python

  $compass
  geometry
    O
    H 1 1.0
    H 1 1.0 2 109.
  end geometry
  skeleton
  basis
    cc-pvdz
  $end
   
  $xuanyuan
  direct
  maxmem
    512MW
  $end
   
  $scf
  rks      # Restricted Kohn-sham
  dft      # DFT exchange-correlation functional B3lyp
    b3lyp
  charge   # charge = 0
    0
  spin     # 2S+1=1， singlet
    1
  $end
  
  # input for tddft
  $tddft
  imethod   # imethod=1, starts from rhf/rks
    1
  isf       # isf=0, no spin-flip
    0
  itda     # itda=0, TDDFT
    0
  idiag    # Davidson diagonalization for solving Casida equation
    1
  iroot    # Each irreps, calculate 1 root. on default, 10 roots are calculated for each irreps
    1
  memjkop  #maxium memeory for Coulomb and Exchange operator. 512MW(Mega Words).
    512
  $end

完成计算将顺序调用 ``compass`` , ``xuanyuan`` , ``scf`` 及 ``tddft`` 四个模块。其中 ``scf`` 模块执行 ``RKS`` 计算。
基于RKS的计算结果，进行后续的 ``TDDFT`` 计算，注意 ``TDDFT`` 中的 ``imethod`` 关键词值设定为 ``1`` 。Kohn-Sham计算的输出前面已经
介绍过，这里我们只关注 ``TDDFT`` 计算的结果。程序输出会先给出TDDFT计算的设置信息方便用户检查是否计算的设置，如下：

.. code-block:: python

      --------------------------------------------------   
      --- PRINT: Information about TDDFT calculation ---   
      --------------------------------------------------   
   ERI Maxblk=     8M
   [print level]
    iprt= 0
   [method]
    R-TD-DFT 
    isf= 0
    SC Excitations 
    RPA: (A-B)(A+B)Z=w2*Z 
   [special choice for method]
    ialda= 0
   [active space]
    Full active space 
   [algorithm]
    Target Excited State in each rep / Diag method :
    1   A1       1   1
    2   A2       1   1
    3   B1       1   1
    4   B2       1   1
   [dvdson_parameters]
    iupdate =   3
    Nfac =  50
    Nmaxcycle=  50
    nblock   =  50
    crit_e   = 0.10E-06
    crit_vec = 0.10E-04
    crit_demo= 0.10E-07
    crit_indp= 0.10E-09
    guess    =  20
    dump     =   0
   [output eigenvector control]
    cthrd= 0.100
      -------------------------------------------------   
      --- END : Information about TDDFT calculation ---   
      -------------------------------------------------   

这里，

* ``R-TD-DFT`` 表示正在进行的是基于限制性基态波函数计算的TDDFT；
* ``isf= 0`` 表示计算不翻转自旋；
* ``ialda= 0`` 表示使用 ``Full none-collinear Kernel``，这是非自旋翻转TDDFT的默认Kernel。

下面的输出给出了每个不可约表示计算的根的数目。

.. code-block:: python

    Target Excited State in each rep / Diag method :
    1   A1       1   1
    2   A2       1   1
    3   B1       1   1
    4   B2       1   1

TDDFT模块还会打印占据轨道，虚轨道等TDDFT计算的活性轨道信息

.. code-block:: python

             Print [Active] Orbital List         
              ---[Alpha set]---
   idx irep (rep,ibas,type)       F_av(eV)     iact 
 ---------------------------------------------------
    1    1   A1     1   2          -520.34813    0.05
    2    1   A1     2   2           -26.42196    1.84
    3    3   B1     1   2           -13.66589    2.96
    4    1   A1     3   2            -9.50404    2.49
    5    4   B2     1   2            -7.62124    2.12
    6    1   A1     4   0             1.23186    9.86
    7    3   B1     2   0             3.27539   11.48
    8    3   B1     3   0            15.02893    7.40
    9    1   A1     5   0            15.44682    6.60
   10    1   A1     6   0            24.53525    4.35
   11    4   B2     2   0            25.07569    3.88
   12    3   B1     4   0            27.07545    6.17
   13    2   A2     1   0            33.09515    3.99
   14    1   A1     7   0            34.03695    5.08
   15    4   B2     3   0            39.36812    4.67
   16    3   B1     5   0            43.83066    4.86
   17    1   A1     8   0            43.91179    4.34
   18    3   B1     6   0            55.56126    4.35
   19    1   A1     9   0            56.13188    4.04
   20    4   B2     4   0            78.06511    2.06
   21    2   A2     2   0            80.16952    2.10
   22    1   A1    10   0            83.17934    2.38
   23    1   A1    11   0            94.37171    2.81
   24    3   B1     7   0            99.90789    2.86

这里，轨道1-5是占据轨道，6-24是虚轨道，其中，第5个和第6个轨道分别是HOMO和LUMO轨道, 分别属于不可约表示B2和不可约表示A1，
轨道能分别是-7.62124 eV和1.23186 eV。由于H2O分子有4个不可约表示，TDDFT会对每个不可约表示逐一求解。
在进入Davidson迭代求解Casida方程之前，系统会估计内存使用情况，

.. code-block:: python

 ==============================================
  Jrep: 1  ExctSym:  A1  (convert to td-psym)
  Irep: 1  PairSym:  A1  GsSym:  A1
  Nexit:       1     Nsos:      33
 ==============================================
 Estimated memory for JK operator:          0.053 M
 Maxium memory to calculate JK operator:         512.000 M
 Allow to calculate    1 roots at one pass for RPA ...
 Allow to calculate    2 roots at one pass for TDA ...

  Nlarge=               33 Nlimdim=               33 Nfac=               50
  Estimated mem for dvdson storage (RPA) =           0.042 M          0.000 G
  Estimated mem for dvdson storage (TDA) =           0.017 M          0.000 G

这里，系统统计存储JK算符需要的内存约 0.053MB, 输入设置的内存是512MB (见 ``memjkop`` 关键词 )。
系统提示RPA计算，及完全的TDDFT计算每次(one pass)可以算1个根，TDA计算每次可以算2个根。由于分子体系小，内存足够。
分子体系较大时，如果这里输出的允许的每次可算根的数目小于系统这是数目，TDDFT模块将根据最大允许可算根的数目，通过
多次积分计算构造JK算符，计算效率会降低，用户需要用 MEMJKOP关键词增加内存。Davidson迭代开始计算输出信息如下，

.. code-block:: python

      Iteration started !
  
   Niter=     1   Nlarge =      33   Nmv =       2
   Ndim =     2   Nlimdim=      33   Nres=      31
   Approximated Eigenvalue (i,w,diff/eV,diff/a.u.):
      1        9.5246226546        9.5246226546           0.350E+00
   No. of converged eigval:     0
   Norm of Residuals:
      1        0.0120867135        0.0549049429           0.121E-01           0.549E-01
   No. of converged eigvec:     0
   Max norm of residues   :  0.549E-01
   *** New Directions : sTDDFT-Davidson step ***
   Left  Nindp=    1
   Right Nindp=    1
   Total Nindp=    2
   [tddft_dvdson_ZYNI]
   Timing For TDDFT_AVmat, Total:         0.08s         0.02s         0.02s
                         MTrans1:         0.00s         0.02s         0.00s
                         COULPOT:         0.00s         0.00s         0.00s
                         AVint  :         0.08s         0.00s         0.02s
                         MTrans2:         0.00s         0.00s         0.00s
  
   TDDFT ZYNI-AV time-TOTAL         0.08 S         0.02 S         0.02 S 
   TDDFT ZYNI-AV time-Coulp         0.08 S         0.02 S         0.02 S 
   TDDFT ZYNI-AV time-JKcon         0.00 S         0.00 S         0.00 S 
  
       tddft JK operator time:         0.00 S         0.00 S         0.00 S 
  
  
   Niter=     2   Nlarge =      33   Nmv =       4
   Ndim =     4   Nlimdim=      33   Nres=      29
   Approximated Eigenvalue (i,w,diff/eV,diff/a.u.):
      1        9.3817966321        0.1428260225           0.525E-02
   No. of converged eigval:     0
   Norm of Residuals:
      1        0.0029082582        0.0074085379           0.291E-02           0.741E-02
   No. of converged eigvec:     0

收敛信息如下：

.. code-block:: python

       Niter=     5   Nlarge =      33   Nmv =      10
   Ndim =    10   Nlimdim=      33   Nres=      23
   Approximated Eigenvalue (i,w,diff/eV,diff/a.u.):
      1        9.3784431931        0.0000001957           0.719E-08
   No. of converged eigval:     1
   ### Cong: Eigenvalues have Converged ! ###
   Norm of Residuals:
      1        0.0000009432        0.0000023006           0.943E-06           0.230E-05
   No. of converged eigvec:     1
   Max norm of residues   :  0.230E-05
   ### Cong.  Residuals Converged ! ###
  
   ------------------------------------------------------------------
    Orthogonality check2 for iblock/dim =      0       1
    Averaged nHxProd =     10.000
    Ndim =        1  Maximum nonzero deviation from Iden = 0.333E-15
   ------------------------------------------------------------------
  
   ------------------------------------------------------------------
    Statistics for [dvdson_rpa_block]:
     No.  of blocks =        1
     Size of blocks =       50
     No.  of eigens =        1
     No.  of HxProd =       10      Averaged =    10.000
     Eigenvalues (a.u.) = 
          0.3446513056
   ------------------------------------------------------------------
  
这里，5次迭代计算收敛，上面输出的最后4行，随后打印了收敛后电子态的信息，

.. code-block:: python

   No.     1    w=      9.3784 eV      -76.0358398606 a.u.  f= 0.0767   D<Pab>= 0.0000   Ova= 0.5201
        CV(0):   A1(   3 )->  A1(   4 )  c_i:  0.9883  Per: 97.7%  IPA:    10.736 eV  Oai: 0.5163
        CV(0):   B1(   1 )->  B1(   2 )  c_i: -0.1265  Per:  1.6%  IPA:    16.941 eV  Oai: 0.6563
   Estimate memory in tddft_init mem:           0.001 M

其中第1行的信息，

* ``No.     1    w=      9.3784 eV`` 表示第一激发态激发能为 ``9.3784 eV``;
* ``-76.0358398606 a.u.`` 给出第一激发态的总能量;
* ``f= 0.0767`` 给出第一激发态的振子强度;
* ``D<Pab>= 0.0000`` 为激发态的<S^2>值与基态的<S^2>值之差（对于自旋守恒跃迁，该值反映了激发态的自旋污染程度；对于自旋翻转跃迁，该值与理论值``S(S+1)(激发态)-S(S+1)(基态)`` 之差反映了激发态的自旋污染程度）；
* ``Ova= 0.5201`` 为绝对重叠积分（absolute overlap integral，取值范围为[0,1]，该值越接近0，说明相应的激发态的电荷转移特征越明显，否则说明局域激发特征越明显）。

第2行和第3行给出激发主组态信息

* ``CV(0):`` 中CV(0)表示该激发是Core到Virtual轨道激发，0表示是Singlet激发;
* ``A1(   3 )->  A1(   4 )`` 表示是从A1表示的第3个轨道即发到A1表示的第4个轨道，结合上面输出轨道信息，这是HOMO-2到LUMO的激发；
* ``c_i: 0.9883`` 代表该跃迁在整个激发态里的线性组合系数为0.9883;
* ``Per: 97.7%`` 表示该激发组态占97.7%；
* ``IPA:    14.207 eV`` 代表该跃迁所涉及的两个轨道的能量差为10.736 eV；
* ``Oai: 0.5001`` 表示假如该激发态只有这一个跃迁的贡献，那么该激发态的绝对重叠积分为0.5163，由这一信息可以方便地得知哪些跃迁是局域激发，哪些跃迁是电荷转移激发。


所有不可约表示求解完后，所有的激发态会按照能量高低排列总结输出，

.. code-block:: python

  No. Pair   ExSym   ExEnergies  Wavelengths      f     D<S^2>          Dominant Excitations             IPA   Ova     En-E1

    1  B2    1  B2    7.1935 eV    172.36 nm   0.0188   0.0000  99.8%  CV(0):  B2(   1 )->  A1(   4 )   8.853 0.426    0.0000
    2  A2    1  A2    9.0191 eV    137.47 nm   0.0000   0.0000  99.8%  CV(0):  B2(   1 )->  B1(   2 )  10.897 0.356    1.8256
    3  A1    2  A1    9.3784 eV    132.20 nm   0.0767   0.0000  97.7%  CV(0):  A1(   3 )->  A1(   4 )  10.736 0.520    2.1850
    4  B1    1  B1   11.2755 eV    109.96 nm   0.0631   0.0000  98.0%  CV(0):  A1(   3 )->  B1(   2 )  12.779 0.473    4.0820


开壳层体系计算：U-TDDFT
----------------------------------------------------------
开壳层体系可以用U-TDDFT计算，例如对于H2O+离子，先进行UKS计算，然后利用U-TDDFT计算激发态，一个典型的输入为，

.. code-block:: python

    #!bdf.sh
    TDDFT/B3lyp/cc-pvdz iroot=4 group=C(1) charge=1    
    
    geometry
    O
    H  1  R1
    H  1  R1  2 109.
    
    R1=1.0     # OH bond length in angstrom 
    end geometry

这里，关键词，
* ``iroot=4`` 指定TDDFT计算每个不可约表示计算4个根；
* ``charge=1`` 指定体系的电荷为+1；
* ``group=C(1)`` 指定强制使用C1点群计算。

与之对应的高级输入为，

.. code-block:: python

  $compass
  #Notice: length unit for geometry is angstrom
  geometry
   O
   H 1 1.0
   H 1 1.0 2 109.
  end geometry
   skeleton
  basis
   cc-pvdz
  group
   C(1)  # Force to use C1 symmetry
  $end
   
  $xuanyuan
  direct
  maxmem
   512MW
  $end
   
  $scf
  uks
  dft
   b3lyp
  charge
   1
  spin
   2
  $end
   
  $tddft
  imethod  # ask for U-TDDFT. This keyword can be neglected. It can be determined from SCF
   2
  iroot
   4
  $end

这个输入要注意的几个细节是：

* 1. ``compass`` 模块中利用关键词 ``group`` 强制计算使用点群 ``C(1)`` ;
* 2. ``scf`` 模块设置 ``UKS`` 计算， ``charge`` 为 ``1`` ， ``spin`` (自旋多重度,2S+1)=2;   
* 3. ``tddft`` 模块设置 ``imethod`` 为 ``2`` ，``iroot`` 设定每个不可约表示算4个根，由于用了C1对称性，计算给出水的阳离子的前四个激发态。

从输出

.. code-block:: python

        --------------------------------------------------   
    --- PRINT: Information about TDDFT calculation ---   
    --------------------------------------------------   
 ERI Maxblk=     8M
 [print level]
  iprt= 0
 [method]
  U-TD-DFT 
  isf= 0
  SC Excitations 
  RPA: (A-B)(A+B)Z=w2*Z 

可以看出执行的是U-TDDFT计算。计算总结输出的4个激发态为，

.. code-block:: python

      No. Pair   ExSym   ExEnergies  Wavelengths      f     D<S^2>          Dominant Excitations             IPA   Ova     En-E1

    1   A    2   A    2.1958 eV    564.65 nm   0.0009   0.0023  99.4% CO(bb):   A(   4 )->   A(   5 )   5.954 0.626    0.0000
    2   A    3   A    6.3479 eV    195.32 nm   0.0000   0.0030  99.3% CO(bb):   A(   3 )->   A(   5 )   9.983 0.578    4.1521
    3   A    4   A   12.0990 eV    102.47 nm   0.0028   1.9312  65.8% CV(bb):   A(   4 )->   A(   6 )  14.636 0.493    9.9033
    4   A    5   A   13.3619 eV     92.79 nm   0.0174   0.0004  97.6% CV(aa):   A(   4 )->   A(   6 )  15.624 0.419   11.1661



开壳层体系：自旋匹配(Spin-adapted)的TDDFT
----------------------------------------------------------


计算自旋翻转(spin-flip)的开壳层激发态:SF-TDDFT
----------------------------------------------------------

基于TDDFT的自旋轨道耦合计算: TDDFT-SOC
----------------------------------------------------------


TDDFT计算示例1：UV-Vis吸收光谱的计算（垂直激发）
----------------------------------------------------------
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

 * ``-77.9524434004 a.u.`` 为激发态的电子能（等于基态电子能加激发能）；
 * ``f= 0.0000`` 为振子强度；
 * ``D<Pab>= 0.0000`` 为激发态的<S^2>值与基态的<S^2>值之差（对于自旋守恒跃迁，该值反映了激发态的自旋污染程度；对于自旋翻转跃迁，该值与理论值``S(S+1)(激发态)-S(S+1)(基态)`` 之差反映了激发态的自旋污染程度）；
 * ``Ova= 0.5044`` 为绝对重叠积分（absolute overlap integral，取值范围为[0,1]，该值越接近0，说明相应的激发态的电荷转移特征越明显，否则说明局域激发特征越明显）。

这一行下面列举了该激发态主要由哪些跃迁组成，以**CV(0):   Ag(   3 )->  Ag(   4 )  c_i: -0.9836  Per: 96.7%  IPA:    14.207 eV  Oai: 0.5001**为例：

 * ``CV`` 代表从闭壳层轨道（Closed shell orbital，也即双占轨道）到开壳层轨道（Vacant shell orbital，也即空轨道）的跃迁；
 * ``(0)`` 代表该CV跃迁产生的两个单电子彼此耦合成单重态（S=0），如耦合成三重态，此处会输出``(1)``；
 * ``Ag(   3 )->  Ag(   4 )`` 代表从Ag不可约表示的第3个轨道到Ag不可约表示的第4个轨道的跃迁；
 * ``c_i: -0.9836`` 代表该跃迁在整个激发态里的线性组合系数为-0.9836，注意一般所谓的某跃迁占激发态的比例并不是这个数，而是这个数的平方，即后面输出的``Per: 96.7%``；
 * ``IPA:    14.207 eV`` 代表该跃迁所涉及的两个轨道的能量差为14.207 eV；
 * ``Oai: 0.5001`` 表示假如该激发态只有这一个跃迁的贡献，那么该激发态的绝对重叠积分为0.5001，由这一信息可以方便地得知哪些跃迁是局域激发，哪些跃迁是电荷转移激发。

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
-------------------------------------------------------
