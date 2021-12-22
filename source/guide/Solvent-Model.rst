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

.. table:: BDF中支持的溶剂模型
    :widths: auto
 
    ================           ================              ================ 
          溶剂                       溶剂                          溶剂          
    ================           ================              ================ 
     Water                      2-Heptanone                  |  IodoBenzene
     Acetonitrile               2-Hexanone                   |  IodoEthane
     Methanol                   2-MethoxyEthanol             |  IodoMethane
     Ethanol                    2-Methyl-1-Propanol          |  IsoPropylBenzene
     IsoQuinoline               2-Methyl-2-Propanol          |  m-Cresol
     Quinoline                  2-MethylPentane              |  Mesitylene
     Chloroform                 2-MethylPyridine             |  MethylBenzoate
     DiethylEther               2-NitroPropane               |  MethylButanoate
     Dichloromethane            2-Octanone                   |  MethylCycloHexane
     DiChloroEthane             2-Pentanone                  |  MethylEthanoate
     CarbonTetraChloride        2-Propanol                   |  MethylMethanoate
     Benzene                    2-Propen-1-ol                |  MethylPropanoate
     Toluene                    3-MethylPyridine             |  m-Xylene
     ChloroBenzene              3-Pentanone                  |  n-ButylBenzene
     NitroMethane               4-Heptanone                  |  n-Decane
     Heptane                    4-Methyl-2-Pentanone         |  n-Dodecane       
     CycloHexane                4-MethylPyridine             |  n-Hexadecane    
     Aniline                    5-Nonanone                   |  n-Hexane  
     Acetone                    AceticAcid                   |  NitroBenzene        
     TetraHydroFuran            AcetoPhenone                 |  NitroEthane       
     DiMethylSulfoxide          a-ChloroToluene              |  n-MethylAniline        
     Argon                      Anisole                      |  n-MethylFormamide-mixture
     Krypton                    Benzaldehyde                 |  n,n-DiMethylAcetamide    
     Xenon                      BenzoNitrile                 |  n,n-DiMethylFormamide    
     n-Octanol                  BenzylAlcohol                |  n-Nonane     
     1,1,1-TriChloroEthane      BromoBenzene                 |  n-Octane        
     1,1,2-TriChloroEthane      BromoEthane                  |  n-Pentadecane        
     1,2,4-TriMethylBenzene     Bromoform                    |  n-Pentane        
     1,2-DiBromoEthane          Butanal                      |  n-Undecane    
     1,2-EthaneDiol             ButanoicAcid                 |  o-ChloroToluene      
     1,4-Dioxane                Butanone                     |  o-Cresol  
     1-Bromo-2-MethylPropane    ButanoNitrile                |  o-DiChloroBenzene          
     1-BromoOctane              ButylAmine                   |  o-NitroToluene
     1-BromoPentane             ButylEthanoate               |  o-Xylene 
     1-BromoPropane             CarbonDiSulfide              |  Pentanal 
     1-Butanol                  Cis-1,2-DiMethylCycloHexane  |  PentanoicAcid
     1-ChloroHexane             Cis-Decalin                  |  PentylAmine      
     1-ChloroPentane            CycloHexanone                |  PentylEthanoate    
     1-ChloroPropane            CycloPentane                 |  PerFluoroBenzene    
     1-Decanol                  CycloPentanol                |  p-IsoPropylToluene    
     1-FluoroOctane             CycloPentanone               |  Propanal    
     1-Heptanol                 Decalin-mixture              |  PropanoicAcid    
     1-Hexanol                  DiBromomEthane               |  PropanoNitrile    
     1-Hexene                   DiButylEther                 |  PropylAmine 
     1-Hexyne                   DiEthylAmine                 |  PropylEthanoate 
     1-IodoButane               DiEthylSulfide               |  p-Xylene    
     1-IodoHexaDecane           DiIodoMethane                |  Pyridine    
     1-IodoPentane              DiIsoPropylEther             |  sec-ButylBenzene     
     1-IodoPropane              DiMethylDiSulfide            |  tert-ButylBenzene      
     1-NitroPropane             DiPhenylEther                |  TetraChloroEthene    
     1-Nonanol                  DiPropylAmine                |  TetraHydroThiophene-s,s-dioxide      
     1-Pentanol                 e-1,2-DiChloroEthene         |  Tetralin            
     1-Pentene                  e-2-Pentene                  |  Thiophene  
     1-Propanol                 EthaneThiol                  |  Thiophenol  
     2,2,2-TriFluoroEthanol     EthylBenzene                 |  trans-Decalin              
     2,2,4-TriMethylPentane     EthylEthanoate               |  TriButylPhosphate             
     2,4-DiMethylPentane        EthylMethanoate              |  TriChloroEthene            
     2,4-DiMethylPyridine       EthylPhenylEther             |  TriEthylAmine             
     2,6-DiMethylPyridine       FluoroBenzene                |  Xylene-mixture            
     2-BromoPropane             Formamide                    |  z-1,2-DiChloroEthene
     2-Butanol                  FormicAcid                   |   
     2-ChloroButane             HexanoicAcid                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    ================           ================              ================

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





