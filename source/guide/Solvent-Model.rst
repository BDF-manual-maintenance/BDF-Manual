溶剂化模型
================================================

溶剂化模型用于计算溶质和溶剂之间的相互作用，一般分为隐式溶剂模型（连续介质模型）和显式模型两种。 在BDF中，对于连续溶剂模型，我们采用
ddCOSMO(domain-decomposition COSMO solvation model)，对于显示溶剂模型我们采用QM/MM方法，结合pDymamo2.0程序包进行计算。

溶剂化效应计算
------------------------------------------------
BDF目前支持基态溶剂化效应计算，包括HF和DFT方法。以下是甲醛分子溶剂化效应计算的输入文件：

.. code-block:: C

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
    schwarz
  $END
  $SCF
    rks
    dft
    b3lyp
   solvent
    water
    grid
       medium
  $END

其中，在 ``SCF`` 中加 ``solvent`` 关键字，表示要进行溶剂化效应计算，紧跟一行可以输入溶剂类型，这里是 ``water`` 。BDF中
支持的溶剂类型列表如下：

.. table:: BDF中支持的溶剂模型
    :widths: auto
 
    ================ ================
     序号               溶剂
    ================ ================
     1                 Water
     2                 Acetonitrile
     3                 Methanol
     4               Ethanol
     5               IsoQuinoline
     6               Quinoline
     7               Chloroform
     8               DiethylEther
     9               Dichloromethane
     10               DiChloroEthane
     11               CarbonTetraChloride
     12               Benzene
     13               Toluene
     14               ChloroBenzene
     15               NitroMethane
     16               Heptane
     17               CycloHexane
     18               Aniline
     19               Acetone
     20               TetraHydroFuran
     21               DiMethylSulfoxide
     22               Argon
     23               Krypton
     24               Xenon
     25               n-Octanol
     26               1,1,1-TriChloroEthane
     27               1,1,2-TriChloroEthane
     28               1,2,4-TriMethylBenzene
     29               1,2-DiBromoEthane
     30               1,2-EthaneDiol
     31               1,4-Dioxane
     32               1-Bromo-2-MethylPropane
     33               1-BromoOctane
     34               1-BromoPentane
     35               1-BromoPropane
     36               1-Butanol
     37               1-ChloroHexane
     38               1-ChloroPentane
     39               1-ChloroPropane
     40               1-Decanol
     41               1-FluoroOctane
     42               1-Heptanol
     43               1-Hexanol
     44               1-Hexene
     45               1-Hexyne
     46               1-IodoButane
     47               1-IodoHexaDecane
     48               1-IodoPentane
     49               1-IodoPropane
     50               1-NitroPropane
     51               1-Nonanol
     52               1-Pentanol
     53               1-Pentene
     54               1-Propanol
     55               2,2,2-TriFluoroEthanol
     56               2,2,4-TriMethylPentane
     57               2,4-DiMethylPentane
     58               2,4-DiMethylPyridine
     59               2,6-DiMethylPyridine
     60               2-BromoPropane
     61               2-Butanol
     62               2-ChloroButane
     63               2-Heptanone
     64               2-Hexanone
     65               2-MethoxyEthanol
     66               2-Methyl-1-Propanol
     67               2-Methyl-2-Propanol
     68               2-MethylPentane
     69               2-MethylPyridine
     70               2-NitroPropane
     71               2-Octanone
     72               2-Pentanone
     73               2-Propanol
     74               2-Propen-1-ol
     75               3-MethylPyridine
     76               3-Pentanone
     77               4-Heptanone
     78               4-Methyl-2-Pentanone
     79               4-MethylPyridine
     80               5-Nonanone
     81               AceticAcid
     82               AcetoPhenone
     83               a-ChloroToluene
     84               Anisole
     85               Benzaldehyde
     86               BenzoNitrile
     87               BenzylAlcohol
     88               BromoBenzene
     89               BromoEthane
     90               Bromoform
     91               Butanal
     92               ButanoicAcid
     93               Butanone
     94               ButanoNitrile
     95               ButylAmine
     96               ButylEthanoate
     97               CarbonDiSulfide
     98               Cis-1,2-DiMethylCycloHexane
     99               Cis-Decalin
     100               CycloHexanone
     101               CycloPentane
     102               CycloPentanol
     103               CycloPentanone
     104               Decalin-mixture
     105               DiBromomEthane
     106               DiButylEther
     107               DiEthylAmine
     108               DiEthylSulfide
     109               DiIodoMethane
     110               DiIsoPropylEther
     111               DiMethylDiSulfide
     112               DiPhenylEther
     113               DiPropylAmine
     114               e-1,2-DiChloroEthene
     115               e-2-Pentene
     116               EthaneThiol
     117               EthylBenzene
     118               EthylEthanoate
     119               EthylMethanoate
     120               EthylPhenylEther
     121               FluoroBenzene
     122               Formamide
     123               FormicAcid
     124               HexanoicAcid
     125               IodoBenzene
     126               IodoEthane
     127               IodoMethane
     128               IsoPropylBenzene
     129               m-Cresol
     130               Mesitylene
     131               MethylBenzoate
     132               MethylButanoate
     133               MethylCycloHexane
     134               MethylEthanoate
     135               MethylMethanoate
     136               MethylPropanoate
     137               m-Xylene
     138               n-ButylBenzene
     139               n-Decane
     140               n-Dodecane
     141               n-Hexadecane
     142               n-Hexane
     143               NitroBenzene
     144               NitroEthane
     145               n-MethylAniline
     146               n-MethylFormamide-mixture
     147               n,n-DiMethylAcetamide
     148               n,n-DiMethylFormamide
     149               n-Nonane
     150               n-Octane
     151               n-Pentadecane
     152               n-Pentane
     153               n-Undecane
     154               o-ChloroToluene
     155               o-Cresol
     156               o-DiChloroBenzene
     157               o-NitroToluene
     158               o-Xylene
     159               Pentanal
     160               PentanoicAcid
     161               PentylAmine
     162               PentylEthanoate
     163               PerFluoroBenzene
     164               p-IsoPropylToluene
     165               Propanal
     166               PropanoicAcid
     167               PropanoNitrile
     168               PropylAmine
     169               PropylEthanoate
     170               p-Xylene
     171               Pyridine
     172               sec-ButylBenzene
     173               tert-ButylBenzene
     174               TetraChloroEthene
     175               TetraHydroThiophene-s,s-dioxide
     176               Tetralin
     177               Thiophene
     178               Thiophenol
     179               trans-Decalin  
     180               TriButylPhosphate
     181               TriChloroEthene
     182               TriEthylAmine
     183               Xylene-mixture
     184               z-1,2-DiChloroEthene
    ================ ================

输入介电常数
--------------------------------------------------------

对于表中没有的溶剂，可以输入介电常数。格式如下：

.. code-block:: python 

  solvent
    user
  dielectric
    78.3553


.. note::

  溶剂化效应目前只支持能量计算，梯度计算会在近期完成。



