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

之后程序对每个不可约表示进行逐一求解，例如Ag表示：

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

to be done...
