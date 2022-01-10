大体系的iOI-SCF计算及FLMO方法
========================================

对于大体系（例如原子数大于300的体系），传统SCF计算方法常常不再适用，原因除了每步Fock矩阵构建时间变长以外，还包括以下因素：

 * Fock矩阵对角化时间占计算总时间的比例增加。当体系足够大时，每步Fock矩阵的构建时间与体系大小的平方成正比，但Fock矩阵对角化时间和体系大小的三次方成正比，因此对于特别大（如上千个原子）的体系，Fock矩阵对角化占总计算时间的比例将相当可观。
 * 大体系的局部稳定波函数更多，导致大体系SCF计算收敛到用户期望的态的概率降低。换言之，SCF可能收敛到很多个不同的解，其中只有一个是用户想要的，因此增加了用户判断SCF解是否是自己期望的解，以及（如果收敛到非期望的解时）重新提交计算等时间开销。
 * 大体系的SCF收敛比小体系更加困难，需要更多的迭代步数，甚至完全不能收敛。这除了是因为上述的局部稳定解变多以外，也有一部分原因是因为一般的基于原子密度的SCF初猜的质量随着体系增大而变差。
 
针对以上问题，一种解决方案是将体系分为若干片段（该过程称为分片；这些片段彼此之间可以重叠），对每个片段分别做SCF，再把所有片段的收敛的波函数汇总，作为总体系SCF计算的初猜。BDF的FLMO方法 (Fragment localized molecular orbital) 即属于一种基于分片的方法，其中每个片段的SCF收敛后，程序对每个片段的波函数进行局域化，再用所得的局域轨道产生总体系计算的初猜。相比不依赖局域轨道的分片方法，这样做会带来一些额外的好处：

 * SCF迭代可以在局域轨道基上进行，在局域轨道基下Fock矩阵无需进行全对角化，而只需进行块对角化，即转动轨道使得占据-空块为零即可，该步骤的计算量较全对角化小。
 * 局域轨道基下的Fock矩阵的占据-空块非常稀疏，可以利用这种稀疏性进一步减小块对角化的计算量。
 * 用户可以在进行全局SCF计算之前就指定某个局域轨道的占据数，从而选择性地得到该局域轨道占据或未占据的电子态，例如计算由一个Fe(II)和一个Fe(III)组成的金属团簇，可以通过指定Fe 3d轨道的占据数来控制哪个Fe收敛到二价组态，哪个Fe收敛到三价组态。在当前的BDF版本里实际还支持另外一种做法，即直接指定原子的形式氧化态和自旋态（见下）。出于便捷性考虑，一般建议用户直接通过原子的形式氧化态和自旋态来指定收敛到哪个电子态。
 * SCF计算直接得到收敛的局域轨道，而不是像一般的SCF计算那样只得到正则轨道。如果用户需要得到收敛的局域轨道来进行波函数分析等，那么FLMO方法相比传统的先得到正则轨道再进行局域化的做法而言，可以节省很多计算时间，也可以规避大体系局域化迭代次数多、容易不收敛的问题。

FLMO已被用于获得分子的定域化轨道、iOI-SCF、FLMO-MP2、O(1)-NMR等方法，还可以计算开壳层的单重态，用于研究单分子磁体等问题。

计算分片定域分子轨道FLMO（手动分片）
--------------------------------------------

为了使用户对FLMO有个直观的了解，我们给出一个FLMO的计算示例。这里，我们要通过FLMO方法计算1,3,5,7-辛四烯 :math:`\ce{C8H10}` 分子的定域化轨道。
我们先计算4个分子片，每个分子片是由中心原子、缓冲区原子和链接H原子组成。因分子结构较简单，这里的分子片是通过手动分片得到的，即每个分子片的中心原子为一个C=C双键及与其相连的所有氢原子，缓冲区原子为和该C=C双键直接相连的C=C双键及其所带的氢原子，也即分子片1和分子片4为1,3-丁二烯，分子片2和分子片3为1,3,5-己三烯。分子片SCF计算收敛后，通过Boys定域化方法得到分子片定域轨道。所有分子片计算完成后，再用四个分子片的定域轨道合成整体分子的pFLMO (primitive Fragment Localized Molecular Orbital)。利用pFLMO做初始猜测，计算整个 :math:`\ce{C8H10}` 分子，并得到定域化的FLMO。输入示例如下：

.. code-block:: bdf

  ###### Fragment 1
  %echo "-------CHECKDATA: Calculate the 1st fragment -------------"
  $COMPASS 
  Title
   Fragment 1
  Basis
   6-31G
  Geometry
   c   0.5833330000  0.0   0.0000000000   
   c   1.9203330000  0.0   0.0000000000   
   h   0.0250410000  0.0  -0.9477920000   
   h   0.0250620000  0.0   0.9477570000   
   h   2.4703130000  0.0  -0.9525920000   
   c   2.6718330000  0.0   1.3016360000    B
   c   4.0088330000  0.0   1.3016360000    B
   h   4.7603330000  0.0   2.6032720000    L
   h   2.1218540000  0.0   2.2542280000    B 
   h   4.5588130000  0.0   0.3490440000    B
  End geometry
  $END
  
  $XUANYUAN
  $END
  
  $SCF
  RHF
  iprtmo
   2
  $END
  
  $localmo
  FLMO
  $end
  
  # copy pFLMO punch file
  %cp $BDF_WORKDIR/$BDFTASK.flmo $BDF_TMPDIR/fragment1
  %cp $BDF_WORKDIR/$BDFTASK.flmo $BDF_WORKDIR/fragment1
  
  ##### Fragment 2
  %echo "-------CHECKDATA: Calculate the 2nd fragment -------------"
  $COMPASS 
  Title
   Fragment 2
  Basis
   6-31G
  Geometry
   c   0.5833330000  0.0   0.0000000000    B
   c   1.9203330000  0.0   0.0000000000    B
   h   0.0250410000  0.0  -0.9477920000    L
   h   0.0250620000  0.0   0.9477570000    B
   h   2.4703130000  0.0  -0.9525920000    B
   c   2.6718330000  0.0   1.3016360000     
   c   4.0088330000  0.0   1.3016360000
   h   2.1218540000  0.0   2.2542280000
   h   4.5588130000  0.0   0.3490440000
   c   4.7603330000  0.0   2.6032720000    B
   c   6.0973330000  0.0   2.6032720000    B
   h   4.2103540000  0.0   3.5558650000    B
   h   6.6473130000  0.0   1.6506800000    B
   h   6.8488330000  0.0   3.9049090000    L
  End geometry
  $END
  
  $XUANYUAN
  $END
  
  $SCF
  RHF
  iprtmo
   2
  $END
  
  $localmo
  FLMO
  $end
  
  # copy pFLMO punch file
  %cp $BDF_WORKDIR/$BDFTASK.flmo $BDF_TMPDIR/fragment2
  %cp $BDF_WORKDIR/$BDFTASK.flmo $BDF_WORKDIR/fragment2
  %ls -l  $BDF_TMPDIR
  %rm -rf $BDF_TMPDIR/$BDFTASK.*
  
  # Fragment 3
  %echo "-------CHECKDATA: Calculate the 3rd fragment -------------"
  $COMPASS 
  Title
   Fragment 3
  Basis
   6-31G
  Geometry
    c   2.6718330000  0.0   1.3016360000  B
    c   4.0088330000  0.0   1.3016360000  B
    h   1.9203330000  0.0   0.0000000000  L
    h   2.1218540000  0.0   2.2542280000  B
    h   4.5588130000  0.0   0.3490440000  B
    c   4.7603330000  0.0   2.6032720000  
    c   6.0973330000  0.0   2.6032720000
    h   4.2103540000  0.0   3.5558650000
    h   6.6473130000  0.0   1.6506800000
    c   6.8488330000  0.0   3.9049090000  B
    c   8.1858330000  0.0   3.9049090000  B
    h   6.2988540000  0.0   4.8575010000  B
    h   8.7441260000  0.0   4.8527010000  L
    h   8.7441050000  0.0   2.9571520000  B
  End geometry
  $END
  
  $XUANYUAN
  $END
  
  $SCF
  RHF
  iprtmo
   2
  $END
  
  # flmo_coef_gen=1, iprt=2, ipro=(6,7,8,9), icut=(3,13),
  $localmo
  FLMO
  $end
  
  # copy pFLMO punch file
  %cp $BDF_WORKDIR/$BDFTASK.flmo $BDF_TMPDIR/fragment3
  %cp $BDF_WORKDIR/$BDFTASK.flmo $BDF_WORKDIR/fragment3
  %ls -l  $BDF_TMPDIR
  %rm -rf $BDF_TMPDIR/$BDFTASK.*
  
  # Fragment 4
  %echo "-------CHECKDATA: Calculate the 4th fragment -------------"
  $COMPASS 
  Title
   Fragment 4
  Basis
   6-31G
  Geometry
    h   4.0088330000  0.0   1.3016360000  L
    c   4.7603330000  0.0   2.6032720000  B
    c   6.0973330000  0.0   2.6032720000  B
    h   4.2103540000  0.0   3.5558650000  B
    h   6.6473130000  0.0   1.6506800000  B
    c   6.8488330000  0.0   3.9049090000  
    c   8.1858330000  0.0   3.9049090000
    h   6.2988540000  0.0   4.8575010000
    h   8.7441260000  0.0   4.8527010000
    h   8.7441050000  0.0   2.9571520000
  End geometry
  $END
  
  $XUANYUAN
  $END
  
  $SCF
  RHF
  iprtmo
   2
  $END
  
  # flmo_coef_gen=1, iprt=1, ipro=(6,7,8,9,10), icut=(1) 
  $localmo
  FLMO
  $end
  
  # copy pFLMO punch file
  %cp $BDF_WORKDIR/$BDFTASK.flmo $BDF_TMPDIR/fragment4
  %cp $BDF_WORKDIR/$BDFTASK.flmo $BDF_WORKDIR/fragment4
  %ls -l  $BDF_TMPDIR
  %rm -rf $BDF_TMPDIR/$BDFTASK.*
  
  # Whole Molecule calculation
  %echo "--------CHECKDATA: From fragment to molecular SCF calculation---------------"
  $COMPASS 
  Title
   Whole Molecule calculation
  Basis
   6-31G
  Geometry
    c   0.5833330000  0.0   0.0000000000
    c   1.9203330000  0.0   0.0000000000
    h   0.0250410000  0.0  -0.9477920000
    h   0.0250620000  0.0   0.9477570000
    h   2.4703130000  0.0  -0.9525920000
    c   2.6718330000  0.0   1.3016360000
    c   4.0088330000  0.0   1.3016360000
    h   2.1218540000  0.0   2.2542280000
    h   4.5588130000  0.0   0.3490440000
    c   4.7603330000  0.0   2.6032720000
    c   6.0973330000  0.0   2.6032720000
    h   4.2103540000  0.0   3.5558650000
    h   6.6473130000  0.0   1.6506800000
    c   6.8488330000  0.0   3.9049090000
    c   8.1858330000  0.0   3.9049090000
    h   6.2988540000  0.0   4.8575010000
    h   8.7441260000  0.0   4.8527010000
    h   8.7441050000  0.0   2.9571520000
  End geometry
  Nfragment
   4
  Group
   C(1)
  $END
  
  $XUANYUAN
  $END
  
  $SCF
  RHF
  FLMO
  iprtmo
   2
  sylv
  threshconv
   1.d-8 1.d-6
  $END
  
  &DATABASE
  fragment 1  9        # Fragment 1 with 9 atoms
   1 2 3 4 5 6 7 8 9   # atom number in the whole molecule
  fragment 2 12
   1 2 4 5 6 7 8 9 10 11 12 13
  fragment 3 12
   6 7 8 9 10 11 12 13 14 15 16 18 
  fragment 4 9
   10 11 12 13 14 15 16 17 18 
  &END

在输入中，我们给出了注释。每个分子片的计算由 ``compass``、 ``xuanyuan`` 、 ``scf`` 及 ``localmo`` 四个模块构成。分别做预处理、积分计算、SCF计算和分子轨道定域化四个步骤，并通过在localmo模块后插入Shell命令
``cp $BDF_WORKDIR/$BDFTASK.flmo $BDF_TMPDIR/fragment*``
将存储定域轨道的文件 **$BDFTASK.flmo** 拷贝到 **$BDF_TMPDIR** 所在的目录备用。4个分子片段算完后是整体分子的计算，输入从
``# Whole Molecule calculation``
开始。在 ``compass`` 中，有关键词 ``Nfragment 4`` ，提示要读入4个分子片，分子片信息在 ``&DATABASE`` 域中定义。

整体分子的SCF计算，首先会读入4个分子片的定域轨道，构建pFLMO，并给出轨道伸展系数 Mos (molecular orbital spread，某个定域轨道的Mos越大代表该定域轨道越离域，反之则代表该定域轨道越局域)，如下：

.. code-block:: bdf

   Reading fragment information and mapping orbitals ... 

   Survived FLMO dims of frag( 11):       8      17       0      46       9
   Survived FLMO dims of frag( 15):       8      16       0      66      12
   Survived FLMO dims of frag( 15):       8      16       0      66      12
   Survived FLMO dims of frag( 11):       8      17       0      46       9
   Input Nr. of FLMOs (total, occ., soc., vir.) :   98   32   0   66
    nmo != nbas 
                     98                   92
    Local Occupied Orbitals Mos and Moc 
   Max_Mos:    1.89136758 Min_Mos:    0.31699600 Aver_Mos:    1.32004368
    Local Virtual Orbitals Mos and Moc 
   Max_Mos:    2.46745638 Min_Mos:    1.46248295 Aver_Mos:    2.14404812
   The prepared  Nr. of pFLMOs (total, occ., vir.) :   98   32   0   66
  
   Input Nr. of FLMOs (total, double-occ., single-occ, vir.) :   98   32   0   66
   No. double-occ orbitals:        29
   No. single-occ orbitals:         0
   No. virtual    orbitals:        63
  
  iden=     1    29    63    32    66
   Transfer dipole integral into Ao basis ...
  
   Transfer quadrupole integral into Ao basis ...
  
    Eliminate the occupied linear-dependent orbitals !
   Max_Mos:    1.89136758 Min_Mos:    0.31699600 Aver_Mos:    1.32004368
        3 linear dependent orbitals removed by preliminary scan
   Initial MO/AO dimension are :      29     92
    Finally                    29  orbitals left. Number of cutted MO    0
   Max_Mos:    1.89136758 Min_Mos:    0.31699600 Aver_Mos:    1.29690971
   Perform Lowdin orthonormalization to occ pFLMOs
   Project pFLMO occupied components out of virtual FLMOs
   Max_Mos:    2.46467150 Min_Mos:    1.46222542 Aver_Mos:    2.14111949
        3 linear dependent orbitals removed by preliminary scan
   Initial NO, NV, AO dimension are :     29     63     92
    Finally                    92  orbitals left. Number of cutted MO    0
   Max_Mos:    2.46467150 Min_Mos:    1.46222542 Aver_Mos:    2.15946681
   Perform Lowdin orthonormalization to virtual pFLMOs                  63
    Local Occupied Orbitals Mos and Moc 
   Max_Mos:    1.88724854 Min_Mos:    0.31689707 Aver_Mos:    1.29604628
    Local Virtual Orbitals Mos and Moc 
   Max_Mos:    2.53231018 Min_Mos:    1.46240853 Aver_Mos:    2.16493518
   Prepare FLMO time :       0.03 S      0.02 S       0.05 S
   Finish FLMO-SCF initial ...

可以看出，整体分子的pFLMO最大 Mos都小于2.6，不论占据或是虚轨道，pFLMO都是定域的。利用pFLMO做整体分子的初始猜测，进入SCF迭代，利用分块对角化方法保持对轨道的最小扰动，输出如下：

.. code-block:: bdf

   Check initial pFLMO orbital MOS
    Local Occupied Orbitals Mos and Moc 
   Max_Mos:    1.88724854 Min_Mos:    0.31689707 Aver_Mos:    1.29604628
    Local Virtual Orbitals Mos and Moc 
   Max_Mos:    2.53231018 Min_Mos:    1.46240853 Aver_Mos:    2.16493518
    DNR !! 
   Final iter :   79 Norm of Febru  0.86590E-06
   X --> U time:       0.000      0.000      0.000
   block diag       0.017      0.000      0.017
    block norm :    2.3273112079137773E-004

    1    0   0.000 -308.562949067 397.366768902  0.002100841  0.027228292  0.0000   0.53
    DNR !! 
   Final iter :   57 Norm of Febru  0.48415E-06
   X --> U time:       0.000      0.000      0.017
   block diag       0.000      0.000      0.017
    block norm :    1.3067586006786384E-004

    2    1   0.000 -308.571009930  -0.008060863  0.000263807  0.003230630  0.0000   0.52
    DNR !! 
   Final iter :   43 Norm of Febru  0.64098E-06
   X --> U time:       0.000      0.000      0.000
   block diag       0.017      0.000      0.017
    block norm :    3.6831175797520882E-005

SCF收敛后，系统会再一次打印分子轨道的Mos信息，

.. code-block:: bdf

   Print pFLMO occupation for checking ...
   Occupied alpha obitals ...
    Local Occupied Orbitals Mos and Moc 
   Max_Mos:    1.91280597 Min_Mos:    0.31692300 Aver_Mos:    1.30442588
    Local Virtual Orbitals Mos and Moc 
   Max_Mos:    2.53288468 Min_Mos:    1.46274299 Aver_Mos:    2.16864691
    Write FLMO coef into scratch file ...               214296
    Reorder orbital via orbital energy ...                    1                    1

可以看出，最终FLMO的Mos与pFLMO相比变化不大，保持了很好的定域性。

以上的手动分片方法对于结构较复杂的分子来说比较繁琐，因为不仅需要手动给出每个分子片的定义，还需要在 ``&DATABASE`` 域中给出每个分子片和总体系的原子序号的对应关系。相比之下，更加方便的方法是使用以下的自动分片方法。

利用FLMO计算开壳层单重态（自动分片）
--------------------------------------------

研究单分子磁体以及某些催化体系等，常遇到所谓反铁磁耦合的态，一般由两个自旋相反的电子以开壳层的形式占据在不同的原子中心（开壳层单重态），但也可能涉及多个单电子。BDF可以结合FLMO方法计算开壳层单重态。例如，下述算例采用FLMO方法计算一个含有Cu(II)和氮氧稳定自由基的体系的自旋破缺基态：

.. code-block::

  $autofrag
  method
   flmo
  nprocs
   2  # ask for 2 parallel processes to perform FLMO calculation
  spinocc
  # Set +1 spin population on atom 9 (O), set -1 spin population on atom 16 (Cu)
   9 +1 16 -1
  # Add no buffer atoms, except for those necessary for saturating dangling bonds.
  # Minimizing the buffer radius helps keeping the spin centers localized in
  # different fragments
  radbuff
   0
  $end
  
  $compass
  Title
   antiferromagnetically coupled nitroxide-Cu complex
  Basis
   LANL2DZ
  Geometry
   C                 -0.16158257   -0.34669203    1.16605797
   C                  0.02573099   -0.67120566   -1.13886544
   H                  0.90280854   -0.26733412    1.24138440
   H                 -0.26508467   -1.69387001   -1.01851639
   C                 -0.81912799    0.50687422    2.26635740
   H                 -0.52831123    1.52953831    2.14600864
   H                 -1.88351904    0.42751668    2.19103081
   N                 -0.38402395    0.02569744    3.58546820
   O                  0.96884699    0.12656182    3.68120994
   C                 -1.01167974    0.84046608    4.63575398
   H                 -0.69497152    0.49022160    5.59592309
   H                 -0.72086191    1.86312982    4.51540490
   H                 -2.07607087    0.76110974    4.56042769
   N                 -0.40937388   -0.19002965   -2.45797639
   C                 -0.74875417    0.18529223   -3.48688305
   Cu                -1.32292113    0.82043400   -5.22772307
   F                 -1.43762557   -0.29443417   -6.57175160
   F                 -1.72615042    2.50823941   -5.45404079
   H                 -0.45239892   -1.36935628    1.28640692
   H                  1.09012199   -0.59184704   -1.06353906
   O                 -0.58484750    0.12139125   -0.11715881
  End geometry
  $end
  
  $xuanyuan
  $end
  
  $scf
  uks
  dft
   PBE0
  spinmulti
   1
  D3
  molden
  $end
  
  $localmo
  FLMO
  Pipek # Pipek-Mezey localization, recommended when pure sigma/pure pi LMOs are needed.
        # Otherwise Boys is better
  $end

FLMO计算目前不支持简洁输入。这个算例， ``autofrag`` 模块用于对分子自动分片，并产生FLMO计算的基本输入。BDF先根据 ``compass`` 模块中的分子结构与 ``autofrag`` 的参数定义信息产生分子片段，以及分子片段定域化轨道计算的输入文件。然后用分子片段的定域轨道组装整体分子的pFLMO (primitive Fragment Local Molecular Orbital) 作为全局SCF计算的初始猜测轨道，再通过全局SCF计算，在保持每一步迭代轨道都保持定域的前提下，得到整体分子的开壳层单重态。在计算中，为了输出简洁，分子片段计算输出保存为 ``${BDFTASK}.framgmentN.out`` , **N** 为片段编号，标准输出只打印整体分子计算的输出。

输出会给出分子分片的信息，

.. code-block::

 ----------- Buffered molecular fragments ----------
  BMolefrag    1:   [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 19, 20, 21], [], [14], [14, 15], 0.0, 1.4700001016690913]
  BMolefrag    2:   [[14, 15, 16, 17, 18], [2, 4, 20], [21], [21], 0.0, 1.4700001016690913]
 --------------------------------------------------------------------
 Automatically assigned charges and spin multiplicities of fragments:
 --------------------------------------------------------------------
    Fragment  Total No. of atoms  Charge  SpinMult  SpinAlignment
           1                  17       0         2          Alpha
           2                   9       0         2           Beta
 --------------------------------------------------------------------
   
    Generate BDF input file ....

这里可以看出，我们产生了两个分子片段，指定了分子片 **1** 由17个原子组成，自旋多重度指认为2，分子片 **2** 由9个原子组成，自旋多重度也指认为2，但自旋方向和分子片 **1** 相反，也即beta电子比alpha电子多一个，而不是alpha电子比beta电子多一个。随后会分别计算2个分子片，提示信息如下（假设环境变量 ``OMP_NUM_THREADS`` 设为4）：

.. code-block:: bdf

  Starting subsystem calculations ...
  Number of parallel processes:  2
  Number of OpenMP threads per process:  2
  Please refer to test117.fragment*.out for detailed output
  
  Total number of not yet converged subsystems:  2
  List of not yet converged subsystems:  [1, 2]
  Finished calculating subsystem   2 (  1 of   2)
  Finished calculating subsystem   1 (  2 of   2)
  
  Starting global calculation ...

这要注意计算资源的设置。总的计算资源是进程数（Number of parallel processes）与每个进程的线程数（Number of OpenMP threads per process）的乘积，其中进程数是通过 ``autofrag`` 模块的 ``nprocs`` 关键词设定的，而总的计算资源是通过环境变量 ``OMP_NUM_THREADS`` 设定的，每个进程的线程数由程序自动通过总的计算资源除以进程数来得到。

整体分子的计算输出类似普通的SCF计算，但采用了分块对角化Fock矩阵的方法以保持轨道的定域性。

.. code-block:: bdf

  Check initial pFLMO orbital MOS
   Openshell  alpha :
   Local Occupied Orbitals Mos and Moc
  Max_Mos:    1.89684048 Min_Mos:    0.25791767 Aver_Mos:    1.15865182
   Local Virtual Orbitals Mos and Moc
  Max_Mos:    8.01038107 Min_Mos:    1.56092594 Aver_Mos:    3.04393282
   Openshell  beta  :
   Local Occupied Orbitals Mos and Moc
  Max_Mos:    3.00463332 Min_Mos:    0.21757580 Aver_Mos:    1.24636228
   Local Virtual Orbitals Mos and Moc
  Max_Mos:    8.00411948 Min_Mos:    1.78248588 Aver_Mos:    3.04672070

 ...

    1    0   0.000 -849.642342776 1158.171170064 0.046853948  4.840619682  0.5000   3.54
   DNR !!
  SDNR: warning: rotation angle too large, aborting
  Final iter :    5 Norm of Febru  0.20133E+00
  X --> U time:       0.000      0.000      0.000
  block diag       0.000      0.000      0.000
   block norm :   0.290774097871744

   DNR !!
  Final iter :  359 Norm of Febru  0.82790E-06
  X --> U time:       0.000      0.000      0.000
  block diag       0.020      0.000      0.010
   block norm :   8.589840290871769E-003


迭代开始会给出轨道伸展 (**Mos**) 的信息， 数字越小，轨道定域性越好。SCF收敛后会再次打印 **Mos** 。 从布居分析的结果，

.. code-block:: bdf

 [Mulliken Population Analysis]
   Atomic charges and Spin densities :
      1C      -0.2481    0.0010
      2C      -0.1514    0.0013
      3H       0.2511   -0.0002
      4H       0.2638   -0.0006
      5C      -0.3618   -0.0079
      6H       0.2511    0.0240
      7H       0.2436   -0.0013
      8N       0.0128    0.3100
      9O      -0.2747    0.6562
     10C      -0.5938   -0.0092
     11H       0.2696    0.0040
     12H       0.2414    0.0242
     13H       0.2302   -0.0016
     14N       0.1529   -0.0202
     15C      -0.2730    0.0162
     16Cu      0.8131   -0.5701
     17F      -0.5019   -0.2113
     18F      -0.4992   -0.2143
     19H       0.2207    0.0008
     20H       0.2666   -0.0000
     21O      -0.3128   -0.0008
      Sum:    -0.0000    0.0000

可看出，Cu原子的自旋密度为 **-0.5701**， 9O原子的自旋密度为 **0.6562** ，其符号与预先指定的自旋相符，表明计算确实收敛到了所需要的开壳层单重态。注意此处自旋密度的绝对值小于1，说明Cu和9O上的自旋密度并不是严格定域在这两个原子上的，而是有一部分离域到了旁边的原子上。

在以上算例中， ``autofrag`` 模块输入的写法看似复杂，但是其中的 ``spinocc`` 和 ``radbuff`` 关键词对于FLMO方法而言不是必需的，也即以下写法的输入文件仍能成功运行，只不过不能确保Cu和O的自旋取向是用户指定的取向：

.. code-block::

  $autofrag
  method
   flmo
  nprocs
   2
  $end

而 ``nprocs`` 表示对各个子体系的SCF计算进行并行化，以上述算例为例，即允许同时计算多个子体系，且任何时刻同时计算的子体系不超过2个。如果省略 ``nprocs`` 关键词，等价于将 ``nprocs`` 设为1，程序会依次计算所有子体系，每个子体系占用8个OpenMP线程，且每次待一个子体系计算结束后再计算下一个子体系。计算结果相比使用 ``nprocs`` 不会有任何区别，只是计算效率可能会有所降低。因此 ``nprocs`` 只影响FLMO计算的效率，而不影响其计算结果，也即以下写法同样可以成功运行，但计算时间可能比写 ``nprocs`` 略长：

.. code-block::

  $autofrag
  method
   flmo
  $end

需要注意的是 ``nprocs`` 设置过大或过小，均可能导致计算时间增加。为讨论方便起见，假设在某较大分子的FLMO计算中，环境变量 ``OMP_NUM_THREADS`` 设定为8。则

.. code-block::

  nprocs
   4

表示：

 1. 程序开始进行子体系计算时，会同时调用4个并发的BDF进程，每个进程计算一个子体系。如果子体系总数N小于4个，则只调用N个并发的BDF进程。
 2. 每个BDF进程使用2个OpenMP线程。当子体系总数小于4个时，有的子体系计算可能使用3个或4个OpenMP线程，但整个计算任务同时并发的OpenMP线程数始终不超过8个。
 3. 在计算刚开始时，整个计算恰好使用8个OpenMP线程，但随着计算接近结束，当只剩余不到4个子体系尚未计算完成时，整个计算所用的OpenMP线程数可能小于8个。

决定 ``nprocs`` 的最优值的因素主要有两个：

 1. 因OpenMP的并行效率一般低于100%，所以如果同时运行4个用时相同的任务，每个任务使用2个OpenMP线程，所用时间一般小于每个任务依次运行，且每个任务使用8个OpenMP线程所用的时间。
 2. 各个子体系的计算时间并不完全相同，甚至可能存在数倍的差别。仍以同时运行4个任务为例，如某些任务所用时间明显较其他任务长，则同时计算这4个子体系、每个子体系使用2个线程，可能反倒比依次计算、每个子体系使用8个线程更慢，因为当同时计算这4个子体系时，在计算后期一部分计算资源会闲置。这也就是所谓的负载均衡问题。

因此， ``nprocs`` 太小或太大，均有可能导致计算效率降低。一般 ``nprocs`` 设为子体系总数的1/5~1/3左右比较适宜，如在计算前对于系统产生的子体系数目没有一个适当的估计值，也可将 ``nprocs`` 简单地设为1、2等较小的正整数。例外情况是如果已知该计算的各个子体系计算量相仿的话， ``nprocs`` 可以设得大一些，例如在本小节开头的算例中，虽然只有两个子体系，但是其中较小的子体系含有过渡金属原子Cu，而较大的子体系是纯有机体系，因此两个子体系的计算时间相仿，可以同时计算。

.. _iOI-Example:

iOI-SCF方法
----------------------------------------------------------

iOI方法可以看作是FLMO方法的一种改进。在FLMO方法中，即便采用自动分片，用户仍然需要用 ``radcent`` 、 ``radbuff`` 等关键词指定分子片的大小，尽管这两个关键词都有默认值（分别是3.0和2.0），但无论是默认值还是用户指定的值，都不能保证对于当前体系是最优的。如果分子片太小，得到的定域轨道质量太差；如果分子片太大，又会导致计算量太大，以及定域化迭代不收敛。而iOI方法则是从比较小的分子片出发，不断增大、融合分子片，直至分子片刚好达到所需的大小为止，然后进行全局计算。其中每次增大、融合分子片称为一次宏迭代（Macro-iteration）。
示例如下：

.. code-block:: bdf

  $autofrag
  method
   ioi # To request a conventional FLMO calculation, change ioi to flmo
  nprocs
   2 # Use at most 2 parallel processes in calculating the subsystems
  $end
  
  $compass
  Title
   hydroxychloroquine (diprotonated)
  Basis
   6-31G(d)
  Geometry # snapshot of GFN2-xTB molecular dynamics at 298 K
  C    -4.2028   -1.1506    2.9497
  C    -4.1974   -0.4473    4.1642
  C    -3.7828    0.9065    4.1812
  C    -3.4934    1.5454    2.9369
  C    -3.4838    0.8240    1.7363
  C    -3.7584   -0.5191    1.7505
  H    -4.6123   -0.8793    5.0715
  C    -3.3035    3.0061    2.9269
  H    -3.1684    1.2214    0.8030
  H    -3.7159   -1.1988    0.9297
  C    -3.1506    3.6292    4.2183
  C    -3.3495    2.9087    5.3473
  H    -2.8779    4.6687    4.2878
  H    -3.2554    3.3937    6.3124
  N    -3.5923    1.5989    5.4076
  Cl   -4.6402   -2.7763    3.0362
  H    -3.8651    1.0100    6.1859
  N    -3.3636    3.6632    1.7847
  H    -3.4286    2.9775    1.0366
  C    -3.5305    5.2960   -0.0482
  H    -2.4848    5.4392   -0.0261
  H    -3.5772    4.3876   -0.6303
  C    -4.1485    6.5393   -0.7839
  H    -3.8803    6.3760   -1.8559
  H    -5.2124    6.5750   -0.7031
  C    -3.4606    7.7754   -0.2653
  H    -2.3720    7.6699   -0.3034
  H    -3.7308    7.9469    0.7870
  N    -3.8415    8.9938   -1.0424
  H    -3.8246    8.8244   -2.0837
  C    -2.7415    9.9365   -0.7484
  H    -1.7736    9.4887   -0.8943
  H    -2.8723   10.2143    0.3196
  C    -2.7911   11.2324   -1.6563
  H    -1.7773   11.3908   -2.1393
  H    -3.5107   10.9108   -2.4646
  H    -3.0564   12.0823   -1.1142
  C    -5.1510    9.6033   -0.7836
  H    -5.5290    9.1358    0.1412
  H    -5.0054   10.6820   -0.6847
  C    -6.2224    9.3823   -1.8639
  H    -6.9636   10.1502   -1.7739
  H    -5.8611    9.4210   -2.8855
  O    -6.7773    8.0861   -1.6209
  H    -7.5145    7.9086   -2.2227
  C    -4.0308    4.9184    1.3736
  H    -3.7858    5.6522    2.1906
  C    -5.5414    4.6280    1.3533
  H    -5.8612    3.8081    0.7198
  H    -5.9086    4.3451    2.3469
  H    -6.1262    5.5024    1.0605
  End geometry
  MPEC+cosx   # Accelerate the SCF iterations using MPEC+COSX. Not mandatory
  $end
  
  $xuanyuan
  rs # the range separation parameter omega (or mu) of wB97X
   0.3
  $end
  
  $scf
  rks
  dft
   wB97X
  iprt # Increase print level for more verbose output. Not mandatory
   2
  charge
   2
  $end
  
  $localmo
  FLMO
  $end

注意在iOI计算中， ``nprocs`` 关键词的含义和FLMO计算相同，也需要根据分子的大小来选择合适的值，且 ``nprocs`` 的不同取值仍然只是影响计算速度而不影响计算结果。和FLMO计算的区别在于，iOI计算涉及多步宏迭代（见下），每步宏迭代的子体系数目是逐步减小的，因此 ``nprocs`` 的最优取值应当保守一些，例如取为第0步宏迭代子体系数目的1/10~1/5。

程序一开始将该分子分为5个分子片：

.. code-block:: bdf

 ----------- Buffered molecular fragments ----------
  BMolefrag    1:   [[4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 18, 19], [1, 16, 2, 3, 7, 15, 17, 46, 47, 48, 49, 50, 51], [20], [20, 21, 22, 23], 2.0, 2.193]
  BMolefrag    2:   [[20, 21, 22, 23, 24, 25, 26, 27, 28, 46, 47, 48, 49, 50, 51], [18, 19, 29, 30], [8, 31, 38], [8, 4, 11, 31, 32, 33, 34, 38, 39, 40, 41], 2.0, 2.037]
  BMolefrag    3:   [[2, 3, 7, 15, 17], [1, 16, 4, 8, 5, 6, 9, 10, 11, 12, 13, 14], [18], [18, 19, 46], 2.0, 3.5]
  BMolefrag    4:   [[29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45], [23, 24, 25, 26, 27, 28, 20, 21, 22], [46], [46, 18, 47, 48], 2.0, 3.386]
  BMolefrag    5:   [[1, 16], [2, 3, 7, 5, 6, 9, 10, 4, 8], [15, 11, 18], [15, 12, 17, 11, 13, 18, 19, 46], 2.0, 2.12]
 --------------------------------------------------------------------
 Automatically assigned charges and spin multiplicities of fragments:
 --------------------------------------------------------------------
    Fragment  Total No. of atoms  Charge  SpinMult  SpinAlignment
           1                  26       1         1           N.A.
           2                  22       1         1           N.A.
           3                  18       1         1           N.A.
           4                  27       1         1           N.A.
           5                  14       1         1           N.A.
 --------------------------------------------------------------------

这里SpinAlignment显示为N.A.，是因为所有分子片都是闭壳层的，因此不存在自旋取向的问题。

之后开始进行子体系计算，

.. code-block:: bdf

 Starting subsystem calculations ...
 Number of parallel processes:  2
 Number of OpenMP threads per process:  2
 Please refer to test106.fragment*.out for detailed output

 Macro-iter 0:
 Total number of not yet converged subsystems:  5
 List of not yet converged subsystems:  [4, 1, 2, 3, 5]
 Finished calculating subsystem   4 (  1 of   5)
 Finished calculating subsystem   2 (  2 of   5)
 Finished calculating subsystem   1 (  3 of   5)
 Finished calculating subsystem   5 (  4 of   5)
 Finished calculating subsystem   3 (  5 of   5)
 Maximum population of LMO tail: 110.00000
 ======================================
 Elapsed time of post-processing: 0.10 s
 Total elapsed time of this iteration: 34.28 s

此后程序将这5个分子片进行两两融合，并扩大缓冲区，得到3个较大的子体系。这3个较大的子体系的定义在 ``${BDFTASK}.ioienlarge.out`` 里给出：

.. code-block:: bdf

 Finding the optimum iOI merge plan...
 Initial guess merge plan...
 Iter 0 Number of permutations done: 1
 New center fragments (in terms of old center fragments):
 Fragment 1: 5 3
 NBas: 164 184
 Fragment 2: 2 4
 NBas: 164 174
 Fragment 3: 1
 NBas: 236
 Center fragment construction done, total elapsed time 0.01 s
 Subsystem construction done, total elapsed time 0.01 s

也即新的子体系1是由旧的子体系5、3融合（并扩大缓冲区）得到的，新的子体系2是由旧的子体系2、4融合（并扩大缓冲区）得到的，而新的子体系3则直接由旧的子体系1扩大缓冲区而得到。然后以原来5个较小子体系的收敛的定域轨道作为初猜，进行这些较大子体系的SCF计算：

.. code-block:: bdf

 Macro-iter 1:
 Total number of not yet converged subsystems:  3
 List of not yet converged subsystems:  [2, 3, 1]
 Finished calculating subsystem   3 (  1 of   3)
 Finished calculating subsystem   1 (  2 of   3)
 Finished calculating subsystem   2 (  3 of   3)
 Fragment 1 has converged
 Fragment 2 has converged
 Fragment 3 has converged
 Maximum population of LMO tail: 0.04804
 ======================================

 *** iOI macro-iteration converged! ***

 Elapsed time of post-processing: 0.04 s
 Total elapsed time of this iteration: 33.71 s

此时程序自动判断这些子体系的大小已经足以将体系的LMO收敛到所需精度，因而iOI宏迭代收敛，进行iOI全局计算。iOI全局计算的输出与FLMO全局计算类似，但为了进一步加快Fock矩阵的块对角化，在iOI全局计算里，某些已经收敛的LMO会被冻结，从而降低需要块对角化的Fock矩阵的维度，但也引入了少许误差（一般在 :math:`10^{-6} \sim 10^{-5}` Hartree数量级）。以最后一步SCF迭代为例：

.. code-block:: bdf

   DNR !!
      47 of     90 occupied and    201 of    292 virtual orbitals frozen
  SDNR. Preparation:         0.01      0.00      0.00
   norm and abs(maximum value) of Febru  0.35816E-03 0.11420E-03 gap =    1.14531
  Survived/total Fia =        472      3913
   norm and abs(maximum value) of Febru  0.36495E-03 0.11420E-03 gap =    1.14531
  Survived/total Fia =        443      3913
   norm and abs(maximum value) of Febru  0.16908E-03 0.92361E-04 gap =    1.14531
  Survived/total Fia =        615      3913
   norm and abs(maximum value) of Febru  0.11957E-03 0.21708E-04 gap =    1.14531
  Survived/total Fia =        824      3913
   norm and abs(maximum value) of Febru  0.68940E-04 0.15155E-04 gap =    1.14531
  Survived/total Fia =        965      3913
   norm and abs(maximum value) of Febru  0.56539E-04 0.15506E-04 gap =    1.14531
  Survived/total Fia =        737      3913
   norm and abs(maximum value) of Febru  0.30450E-04 0.62094E-05 gap =    1.14531
  Survived/total Fia =       1050      3913
   norm and abs(maximum value) of Febru  0.36500E-04 0.82498E-05 gap =    1.14531
  Survived/total Fia =        499      3913
   norm and abs(maximum value) of Febru  0.14018E-04 0.38171E-05 gap =    1.14531
  Survived/total Fia =       1324      3913
   norm and abs(maximum value) of Febru  0.43467E-04 0.15621E-04 gap =    1.14531
  Survived/total Fia =        303      3913
   norm and abs(maximum value) of Febru  0.12151E-04 0.26221E-05 gap =    1.14531
  Survived/total Fia =        837      3913
   norm and abs(maximum value) of Febru  0.15880E-04 0.82575E-05 gap =    1.14531
  Survived/total Fia =        185      3913
   norm and abs(maximum value) of Febru  0.52265E-05 0.71076E-06 gap =    1.14531
  Survived/total Fia =       1407      3913
   norm and abs(maximum value) of Febru  0.31827E-04 0.12985E-04 gap =    1.14531
  Survived/total Fia =        253      3913
   norm and abs(maximum value) of Febru  0.77674E-05 0.24860E-05 gap =    1.14531
  Survived/total Fia =        650      3913
   norm and abs(maximum value) of Febru  0.56782E-05 0.38053E-05 gap =    1.14531
  Survived/total Fia =        264      3913
  SDNR. Iter:         0.01      0.00      0.00
  Final iter :   16 Norm of Febru  0.25948E-05
  X --> U time:       0.000      0.000      0.000
  SDNR. XcontrU:       0.00      0.00      0.00
  block diag       0.020      0.000      0.000
   block norm :   2.321380955939448E-004

  Predicted total energy change:      -0.0000000659
    9      0    0.000   -1401.6261867529      -0.0011407955       0.0000016329       0.0000904023    0.0000     16.97

即冻结了47个占据轨道和201个虚轨道。

iOI全局计算SCF收敛后，可以仿照一般SCF计算的输出文件读取能量、布居分析等信息，此处不再赘述。
