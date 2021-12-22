溶剂化模型
================================================

溶剂化模型用于计算溶质和溶剂之间的相互作用，一般分为隐式溶剂模型（连续介质模型）和显式模型两种。 在BDF中，对于连续溶剂模型，我们采用
ddCOSMO(domain-decomposition COSMO solvation model)，对于显示溶剂模型我们采用QM/MM方法，结合pDymamo2.0程序包进行计算。

溶剂化效应计算
------------------------------------------------
BDF目前支持基态溶剂化效应计算，包括HF和DFT方法。以下是甲醛分子溶剂化效应计算的输入文件：

.. code-block:: bdf

  $COMPASS
  Title
    ch2o Molecule test run
  Basis
    6-31g
  Geometry
    C    0.00000000    0.00000000   -0.54200000
    O    0.00000000    0.00000000    0.67700000
    H    0.00000000    0.93500000   -1.08200000
    H    0.00000000    -0.9350000  -1.08200000
  END geometry
  skeleton
  Check
  nosym
  unit
   ang
  $END

  $xuanyuan
  direct
  $END

  $SCF
  rks
  dft
    b3lyp
  solvent   #溶剂化计算开关
    water    #指定溶剂
  grid
    medium
  $END

其中，在 ``SCF`` 中加 ``solvent`` 关键字，表示要进行溶剂化效应计算，紧跟一行可以输入溶剂类型，这里是 ``water`` 。BDF中
支持的溶剂类型列表如下：

.. table::

   ======================================================= ====================================================== =============================================================
    Water :math:`{\epsilon}`=78.3553                        2-Heptanone :math:`{\epsilon}`=11.658                  IodoBenzene :math:`{\epsilon}`=4.5470              
    Acetonitrile :math:`{\epsilon}`=35.688                  2-Hexanone :math:`{\epsilon}`=14.136                   IodoEthane :math:`{\epsilon}`=7.6177
    Methanol :math:`{\epsilon}`=32.613                      2-MethoxyEthanol :math:`{\epsilon}`=17.2               IodoMethane :math:`{\epsilon}`=6.8650
    Ethanol :math:`{\epsilon}`=24.852                       2-Methyl-1-Propanol :math:`{\epsilon}`=16.777          IsoPropylBenzene :math:`{\epsilon}`=2.3712
    IsoQuinoline :math:`{\epsilon}`=11.00                   2-Methyl-2-Propanol :math:`{\epsilon}`=12.47           m-Cresol :math:`{\epsilon}`=12.44
    Quinoline :math:`{\epsilon}`=9.16                       2-MethylPentane :math:`{\epsilon}`=1.89                Mesitylene :math:`{\epsilon}`=2.2650
    Chloroform :math:`{\epsilon}`=4.7113                    2-MethylPyridine :math:`{\epsilon}`=9.9533             MethylBenzoate :math:`{\epsilon}`=6.7367
    DiethylEther :math:`{\epsilon}`=4.24                    2-NitroPropane :math:`{\epsilon}`=25.654               MethylButanoate :math:`{\epsilon}`=5.5607
    Dichloromethane :math:`{\epsilon}`=8.93                 2-Octanone :math:`{\epsilon}`=9.4678                   MethylCycloHexane :math:`{\epsilon}`=2.024
    DiChloroEthane :math:`{\epsilon}`=10.125                2-Pentanone :math:`{\epsilon}`=15.2                    MethylEthanoate :math:`{\epsilon}`=6.8615
    CarbonTetraChloride :math:`{\epsilon}`=2.2280           2-Propanol :math:`{\epsilon}`=19.264                   MethylMethanoate :math:`{\epsilon}`=8.8377
    Benzene :math:`{\epsilon}`=2.2706                       2-Propen-1-ol :math:`{\epsilon}`=19.011                MethylPropanoate :math:`{\epsilon}`=6.0777
    Toluene :math:`{\epsilon}`=2.3741                       3-MethylPyridine :math:`{\epsilon}`=11.645             m-Xylene :math:`{\epsilon}`=2.3478
    ChloroBenzene :math:`{\epsilon}`=5.6968                 3-Pentanone :math:`{\epsilon}`=16.78                   n-ButylBenzene :math:`{\epsilon}`=2.36
    NitroMethane :math:`{\epsilon}`=36.562                  4-Heptanone :math:`{\epsilon}`=12.257                  n-Decane :math:`{\epsilon}`=1.9846
    Heptane :math:`{\epsilon}`=1.9113                       4-Methyl-2-Pentanone :math:`{\epsilon}`=12.887         n-Dodecane :math:`{\epsilon}`=2.0060      
    CycloHexane :math:`{\epsilon}`=2.0165                   4-MethylPyridine :math:`{\epsilon}`=11.957             n-Hexadecane :math:`{\epsilon}`=2.0402   
    Aniline :math:`{\epsilon}`=6.8882                       5-Nonanone :math:`{\epsilon}`=10.6                     n-Hexane :math:`{\epsilon}`=1.8819 
    Acetone :math:`{\epsilon}`=20.493                       AceticAcid :math:`{\epsilon}`=6.2528                   NitroBenzene :math:`{\epsilon}`=34.809       
    TetraHydroFuran :math:`{\epsilon}`=7.4257               AcetoPhenone :math:`{\epsilon}`=17.44                  NitroEthane :math:`{\epsilon}`=28.29      
    DiMethylSulfoxide :math:`{\epsilon}`=46.826             a-ChloroToluene :math:`{\epsilon}`=6.7175              n-MethylAniline :math:`{\epsilon}`=5.96       
    Argon :math:`{\epsilon}`=1.430                          Anisole :math:`{\epsilon}`=4.2247                      n-MethylFormamide-mixture :math:`{\epsilon}`=181.56
    Krypton :math:`{\epsilon}`=1.519                        Benzaldehyde :math:`{\epsilon}`=18.220                 n,n-DiMethylAcetamide :math:`{\epsilon}`=37.781   
    Xenon :math:`{\epsilon}`=1.706                          BenzoNitrile :math:`{\epsilon}`=25.592                 n,n-DiMethylFormamide :math:`{\epsilon}`=37.219   
    n-Octanol :math:`{\epsilon}`=9.8629                     BenzylAlcohol :math:`{\epsilon}`=12.457                n-Nonane :math:`{\epsilon}`=1.9605    
    1,1,1-TriChloroEthane :math:`{\epsilon}`=7.0826         BromoBenzene :math:`{\epsilon}`=5.3954                 n-Octane :math:`{\epsilon}`=1.9406       
    1,1,2-TriChloroEthane :math:`{\epsilon}`=7.1937         BromoEthane :math:`{\epsilon}`=9.01                    n-Pentadecane :math:`{\epsilon}`=2.0333       
    1,2,4-TriMethylBenzene :math:`{\epsilon}`=2.3653        Bromoform :math:`{\epsilon}`=4.2488                    n-Pentane :math:`{\epsilon}`=1.8371       
    1,2-DiBromoEthane :math:`{\epsilon}`=4.9313             Butanal :math:`{\epsilon}`=13.45                       n-Undecane :math:`{\epsilon}`=1.9910   
    1,2-EthaneDiol :math:`{\epsilon}`=40.245                ButanoicAcid :math:`{\epsilon}`=2.9931                 o-ChloroToluene :math:`{\epsilon}`=4.6331     
    1,4-Dioxane :math:`{\epsilon}`=2.2099                   Butanone :math:`{\epsilon}`=18.246                     o-Cresol :math:`{\epsilon}`=6.76 
    1-Bromo-2-MethylPropane :math:`{\epsilon}`=7.7792       ButanoNitrile :math:`{\epsilon}`=24.291                o-DiChloroBenzene :math:`{\epsilon}`=9.9949         
    1-BromoOctane :math:`{\epsilon}`=5.0244                 ButylAmine :math:`{\epsilon}`=4.6178                   o-NitroToluene :math:`{\epsilon}`=25.669
    1-BromoPentane :math:`{\epsilon}`=6.269                 ButylEthanoate :math:`{\epsilon}`=4.9941               o-Xylene :math:`{\epsilon}`=2.5454
    1-BromoPropane :math:`{\epsilon}`=8.0496                CarbonDiSulfide :math:`{\epsilon}`=2.6105              Pentanal :math:`{\epsilon}`=10.0
    1-Butanol :math:`{\epsilon}`=17.332                     Cis-1,2-DiMethylCycloHexane :math:`{\epsilon}`=2.06    PentanoicAcid :math:`{\epsilon}`=2.6924
    1-ChloroHexane :math:`{\epsilon}`=5.9491                Cis-Decalin :math:`{\epsilon}`=2.2139                  PentylAmine :math:`{\epsilon}`=4.2010     
    1-ChloroPentane :math:`{\epsilon}`=6.5022               CycloHexanone :math:`{\epsilon}`=15.619                PentylEthanoate :math:`{\epsilon}`=4.7297   
    1-ChloroPropane :math:`{\epsilon}`=8.3548               CycloPentane :math:`{\epsilon}`=1.9608                 PerFluoroBenzene :math:`{\epsilon}`=2.029   
    1-Decanol :math:`{\epsilon}`=7.5305                     CycloPentanol :math:`{\epsilon}`=16.989                p-IsoPropylToluene :math:`{\epsilon}`=2.2322   
    1-FluoroOctane :math:`{\epsilon}`=3.89                  CycloPentanone :math:`{\epsilon}`=13.58                Propanal :math:`{\epsilon}`=18.5   
    1-Heptanol :math:`{\epsilon}`=11.321                    Decalin-mixture :math:`{\epsilon}`=2.196               PropanoicAcid :math:`{\epsilon}`=3.44   
    1-Hexanol :math:`{\epsilon}`=12.51                      DiBromomEthane :math:`{\epsilon}`=7.2273               PropanoNitrile :math:`{\epsilon}`=29.324   
    1-Hexene :math:`{\epsilon}`=2.0717                      DiButylEther :math:`{\epsilon}`=3.0473                 PropylAmine :math:`{\epsilon}`=4.9912
    1-Hexyne :math:`{\epsilon}`=2.615                       DiEthylAmine :math:`{\epsilon}`=3.5766                 PropylEthanoate :math:`{\epsilon}`=5.5205
    1-IodoButane :math:`{\epsilon}`=6.173                   DiEthylSulfide :math:`{\epsilon}`=5.723                p-Xylene :math:`{\epsilon}`=2.2705   
    1-IodoHexaDecane :math:`{\epsilon}`=3.5338              DiIodoMethane :math:`{\epsilon}`=5.32                  Pyridine :math:`{\epsilon}`=12.978   
    1-IodoPentane :math:`{\epsilon}`=5.6973                 DiIsoPropylEther :math:`{\epsilon}`=3.38               sec-ButylBenzene :math:`{\epsilon}`=2.3446    
    1-IodoPropane :math:`{\epsilon}`=6.9626                 DiMethylDiSulfide :math:`{\epsilon}`=9.6               tert-ButylBenzene :math:`{\epsilon}`=2.3447     
    1-NitroPropane :math:`{\epsilon}`=23.73                 DiPhenylEther :math:`{\epsilon}`=3.73                  TetraChloroEthene :math:`{\epsilon}`=2.268   
    1-Nonanol :math:`{\epsilon}`=8.5991                     DiPropylAmine :math:`{\epsilon}`=2.9112                TetraHydroThiophene-s,s-dioxide :math:`{\epsilon}`=43.962     
    1-Pentanol :math:`{\epsilon}`=15.13                     e-1,2-DiChloroEthene :math:`{\epsilon}`=2.14           Tetralin :math:`{\epsilon}`=2.771           
    1-Pentene :math:`{\epsilon}`=1.9905                     e-2-Pentene :math:`{\epsilon}`=2.051                   Thiophene :math:`{\epsilon}`=2.7270 
    1-Propanol :math:`{\epsilon}`=20.524                    EthaneThiol :math:`{\epsilon}`=6.667                   Thiophenol :math:`{\epsilon}`=4.2728 
    2,2,2-TriFluoroEthanol :math:`{\epsilon}`=26.726        EthylBenzene :math:`{\epsilon}`=2.4339                 trans-Decalin :math:`{\epsilon}`=2.1781             
    2,2,4-TriMethylPentane :math:`{\epsilon}`=1.9358        EthylEthanoate :math:`{\epsilon}`=5.9867               TriButylPhosphate :math:`{\epsilon}`=8.1781            
    2,4-DiMethylPentane :math:`{\epsilon}`=1.8939           EthylMethanoate :math:`{\epsilon}`=8.3310              TriChloroEthene :math:`{\epsilon}`=3.422           
    2,4-DiMethylPyridine :math:`{\epsilon}`=9.4176          EthylPhenylEther :math:`{\epsilon}`=4.1797             TriEthylAmine :math:`{\epsilon}`=2.3832            
    2,6-DiMethylPyridine :math:`{\epsilon}`=7.1735          FluoroBenzene :math:`{\epsilon}`=5.42                  Xylene-mixture :math:`{\epsilon}`=2.3879           
    2-BromoPropane :math:`{\epsilon}`=9.3610                Formamide :math:`{\epsilon}`=108.94                    z-1,2-DiChloroEthene :math:`{\epsilon}`=9.2
    2-Butanol :math:`{\epsilon}`=15.944                     FormicAcid :math:`{\epsilon}`=51.1                    
    2-ChloroButane :math:`{\epsilon}`=8.3930                HexanoicAcid :math:`{\epsilon}`=2.6                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
   ======================================================= ====================================================== =============================================================

输入介电常数
--------------------------------------------------------

对于表中没有的溶剂，可以输入介电常数。格式如下：

.. code-block:: bdf 

  solvent
    user   #用户指定
  dielectric
    78.3553   #输入介电常数


.. note::

   溶剂化效应目前只支持能量计算，梯度计算会在近期完成。 


激发态溶剂化效应
----------------------------------------------------------

激发态溶剂化效应可以采用显式溶剂和隐式溶剂相结合的方法计算。以水溶液为例，由于溶质分子的HOMO和LUMO轨道有可能弥散到
第一水合层，所以在进行激发态计算时可以将第一水合层的水分子包括在TDDFT计算区域，而其余部分用隐式溶剂处理。

以芥子酸（sinapic acid）为例。为了确定溶质分子的第一水合层，可以采用Amber程序将芥子酸分子置于小的水盒子中进行分子动力学模拟。
待体系平衡后，可分析溶质分子周围水分子分布情况，从而确定第一水合层。当然，也可以选取多帧结构进行计算，然后取平均。

水合层分子选取可以采用VMD程序完成。假设输入为PDF文件，在命令行中可以选择第一水合层分子，并保存为PDF文件。命令如下：

.. code-block:: bdf 

  atomselect top  "same resid as (within 3.5  of not water)"   # 选择第一水合层
  atomselect0 writepdb sa.pdb                                  #溶质分子和第一水合层保存于pdb文件

上例中选取了距离溶质分子距离3.5埃范围内的所有水分子，并且水分子的三个原子中只要有一个在截断范围内，就选择整个分子。选取结果如图所示：

.. figure:: /images/SAtddft.jpg

依据sa.pdb文件中的坐标信息，可以进行TDDFT计算，输入文件如下：

.. code-block:: bdf

  $COMPASS 
  Title
   SA Molecule test run
  Basis
   6-31g
  Geometry
  C          14.983  14.539   6.274
  C          14.515  14.183   7.629
  C          13.251  14.233   8.118
  C          12.774  13.868   9.480
  C          11.429  14.087   9.838
  C          10.961  13.725  11.118
  O           9.666  13.973  11.525
  C           8.553  14.050  10.621
  C          11.836  13.125  12.041
  O          11.364  12.722  13.262
  C          13.184  12.919  11.700
  O          14.021  12.342  12.636
  C          15.284  11.744  12.293
  C          13.648  13.297  10.427
  O          14.270  14.853   5.341
  O          16.307  14.468   6.130
  H          15.310  13.847   8.286
  H          12.474  14.613   7.454
  H          10.754  14.550   9.127
  H           7.627  14.202  11.188
  H           8.673  14.888   9.924
  H           8.457  13.118  10.054
  H          10.366  12.712  13.206
  H          15.725  11.272  13.177
  H          15.144  10.973  11.525
  H          15.985  12.500  11.922
  H          14.687  13.129  10.174
  H          16.438  14.756   5.181
  O          18.736   9.803  12.472
  H          18.779  10.597  11.888
  H          19.417  10.074  13.139
  O          18.022  14.021   8.274
  H          17.547  14.250   7.452
  H          18.614  13.310   7.941
  O           8.888  16.439   7.042
  H           9.682  16.973   6.797
  H           8.217  17.162   7.048
  O           4.019  14.176  11.140
  H           4.032  13.572  10.360
  H           4.752  14.783  10.885
  O          16.970   8.986  14.331
  H          17.578   9.273  13.606
  H          17.497   8.225  14.676
  O           8.133  17.541  10.454
  H           8.419  17.716  11.386
  H           8.936  17.880   9.990
  O           8.639  12.198  13.660
  H           7.777  11.857  13.323
  H           8.413  13.155  13.731
  O          13.766  11.972   4.742
  H          13.858  12.934   4.618
  H          13.712  11.679   3.799
  O          10.264  16.103  14.305
  H           9.444  15.605  14.054
  H          10.527  15.554  15.084
  O          13.269  16.802   3.701
  H          13.513  16.077   4.325
  H          14.141  17.264   3.657
  O          13.286  14.138  14.908
  H          13.185  14.974  14.393
  H          13.003  13.492  14.228
  O          16.694  11.449  15.608
  H          15.780  11.262  15.969
  H          16.838  10.579  15.161
  O           7.858  14.828  14.050
  H           7.208  15.473  13.691
  H           7.322  14.462  14.795
  O          15.961  17.544   3.706
  H          16.342  16.631   3.627
  H          16.502  17.866   4.462
  O          10.940  14.245  16.302
  H          10.828  13.277  16.477
  H          11.870  14.226  15.967
  O          12.686  10.250  14.079
  H          11.731  10.151  14.318
  H          12.629  11.070  13.541
  O           9.429  11.239   8.483
  H           8.927  10.817   7.750
  H           9.237  12.182   8.295
  O          17.151  15.141   3.699
  H          17.124  14.305   3.168
  H          18.133  15.245   3.766
  O          17.065  10.633   9.634
  H          16.918  10.557   8.674
  H          17.024   9.698   9.909
  O          17.536  14.457  10.874
  H          18.014  13.627  11.089
  H          17.683  14.460   9.890
  O           5.836  16.609  13.299
  H           4.877  16.500  13.549
  H           5.760  16.376  12.342
  O          19.014  12.008  10.822
  H          18.249  11.634  10.308
  H          19.749  11.655  10.256
  O          15.861  14.137  15.750
  H          14.900  13.990  15.574
  H          16.185  13.214  15.645
  O          11.084   9.639  10.009
  H          11.641   9.480   9.213
  H          10.452  10.296   9.627
  O          14.234  10.787  16.235
  H          13.668  10.623  15.444
  H          13.663  10.376  16.925
  O          14.488   8.506  13.105
  H          13.870   9.136  13.550
  H          15.301   8.683  13.628
  O          14.899  17.658   9.746
  H          15.674  18.005   9.236
  H          15.210  16.754   9.926
  O           8.725  13.791   7.422
  H           9.237  13.488   6.631
  H           8.845  14.770   7.309
  O          10.084  10.156  14.803
  H           9.498  10.821  14.366
  H          10.215  10.613  15.669
  O           5.806  16.161  10.582
  H           5.389  16.831   9.993
  H           6.747  16.470  10.509
  O           6.028  13.931   7.206
  H           5.971  14.900   7.257
  H           6.999  13.804   7.336
  O          17.072  12.787   2.438
  H          16.281  12.594   1.885
  H          17.062  11.978   3.013
  END geometry
  skeleton
  Check
  nosym
  unit
  ang
  $END
  
  $xuanyuan
  direct
  $end
  
  $SCF
  rks
  dft
   b3lyp   
  solvent
   water 
  grid
   medium
  $END
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
  memjkop  #maxium memeory for Coulomb and Exchange operator. 1024MW(Mega Words).
    1024 
  $end





