FLMO及其相关计算方法
========================================

FLMO指分片分子轨道 (Fragment local molecular orbital) , 起初是基于用 **分子片合成分子** 的思想，用于获得大分子定域轨道的方法。后来FLMO用于 FLMO-SCF、iOI、FLMO-MP2、O(1)-NMR等方法，还可以计算开壳层的单重态，用于研究单分子磁体等问题。

计算分片定域分子轨道FLMO
--------------------------------------------

为了使用户对FLMO有个直观的了解，我们给出一个FLMO的计算示例。这里，我们要通过FLMO方法计算 :math:`C_4H_{10}` 分子的定域化轨道。
我们先进行计算4个分子片，每个分子片是由中心原子、缓冲区原子和链接H原子组成。分子片SCF计算收敛后，通过Boys定域化方法得到分子片定域轨道。所有分子片计算完成后，再用四个分子片的定域轨道合成整体分子的pFLMO (primitive Fragment Local Molecule Orbital)。利用pFLMO做初始猜测，计算整个C4H8分子，并得到定域化的FLMO。输入示例如下：

.. code-block:: bdf

  ###### Fragment 1
  %echo "-------CHECKDATA: Calculate the 1st fragment -------------"
  #%export BDFTASK=c8h10frag1
  $COMPASS 
  Title
   CH2 Molecule test run, cc-pvqz 
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
  Check
  Skeleton
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
  #%export BDFTASK=c8h10frag2
  $COMPASS 
  Title
   CH2 Molecule test run, cc-pvqz 
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
  Check
  Skeleton
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
  #%export BDFTASK=c8h10frag3
  
  $COMPASS 
  Title
   CH2 Molecule test run, cc-pvqz 
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
  Check
  Skeleton
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
  #%export BDFTASK=c8h10frag4
  
  $COMPASS 
  Title
   CH2 Molecule test run, cc-pvqz 
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
  Check
  Skeleton
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
   CH2 Molecule test run, cc-pvqz 
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
  Check
  Skeleton
  Group
   C(1)
  $END
  
  $XUANYUAN
  Direct
  $END
  
  $SCF
  RHF
  FLMO
  iprtmo
   2
  sylv
  threshconverg
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

在输入中，我们给出了注释。每个分子片的计算由 ``compass``、 ``xuanyuan`` 、 ``scf`` 及 ``localmo`` 四个模块构成。分别做预处理、积分计算、SCF计算和分子轨道定域化四个步骤，最后，通过插入Shell命令 ``cp $BDF_WORKDIR/$BDFTASK.flmo $BDF_TMPDIR/fragment*`` 将存储定域轨道的文件 **$BDFTASK.flmo** 拷贝到 **$BDF_TMPDIR** 所在的目录备用。最后是整体分子计算，输入从 **# Whole Molecule calculation** 开始。在 ``compass`` 中，有关键词 ``Nfragment 4`` ，提示要读入4个分子片，分子片信息在 ``&DATABSE`` 域中定义。

整体分子的SCF计算，首先会读入4个分子片的定域轨道，构建pFLMO，并给出轨道伸展系数 Mos (molecular orbital spread)，如下：

.. code-block:: bdf

   Reading fragment information and mapping orbitals ... 

   Survived FLMO dims of frag( 11):       8      17       0      46       9
   Survived FLMO dims of frag( 15):       8      16       0      66      12
   Survived FLMO dims of frag( 15):       8      16       0      66      12
   Survived FLMO dims of frag( 11):       8      17       0      46       9
   Input Nr. of FLMOs (total, occ., soc., vir.) :       98       32        0       66
    nmo != nbas 
                     98                   92
    Local Occupied Orbitals Mos and Moc 
   Max_Mos:    1.89136758 Min_Mos:    0.31699600 Aver_Mos:    1.32004368
    Local Virtual Orbitals Mos and Moc 
   Max_Mos:    2.46745638 Min_Mos:    1.46248295 Aver_Mos:    2.14404812
   The prepared  Nr. of pFLMOs (total, occ., vir.) :       98       32        0       66
  
   Input Nr. of FLMOs (total, double-occ., single-occ, vir.) :       98       32        0       66
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
    Finally                    29  orbitals left. Number of cutted MO                    0
   Max_Mos:    1.89136758 Min_Mos:    0.31699600 Aver_Mos:    1.29690971
   Perform Lowdin orthonormalization to occ pFLMOs
   Project pFLMO occupied components out of virtual FLMOs
   Max_Mos:    2.46467150 Min_Mos:    1.46222542 Aver_Mos:    2.14111949
        3 linear dependent orbitals removed by preliminary scan
   Initial NO, NV, AO dimension are :     29     63     92
    Finally                    92  orbitals left. Number of cutted MO                    0
   Max_Mos:    2.46467150 Min_Mos:    1.46222542 Aver_Mos:    2.15946681
   Perform Lowdin orthonormalization to virtual pFLMOs                   63
    Local Occupied Orbitals Mos and Moc 
   Max_Mos:    1.88724854 Min_Mos:    0.31689707 Aver_Mos:    1.29604628
    Local Virtual Orbitals Mos and Moc 
   Max_Mos:    2.53231018 Min_Mos:    1.46240853 Aver_Mos:    2.16493518
   Prepare FLMO time :       0.03 S      0.02 S       0.05 S
   Finish FLMO-SCF initial ...

可以看出，整体分子的pFLMO最大 Mos都小于2.6，不论占据或是虚轨道，pFLMO都是定域的。利用pFLMO做整体分子的初始猜测，进入SCF迭代，利用分块对角化方法保持对轨道的最小扰动，输出如下：

.. code-block:: bdf

   Iter.   idiis  vshift       SCF Energy            DeltaE          RMSDeltaD          MaxDeltaD      Damping    Times(S) 
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
  
     1      0    0.000    -308.5629490672     397.3667689027       0.0021008410       0.0272282919    0.0000      0.53
    DNR !! 
   Final iter :   57 Norm of Febru  0.48415E-06
   X --> U time:       0.000      0.000      0.017
   block diag       0.000      0.000      0.017
    block norm :    1.3067586006786384E-004

     2      1    0.000    -308.5710099304      -0.0080608632       0.0002638070       0.0032306300    0.0000      0.52
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

可以看出，最终的FLMO的Mos与pFLMO相比变化不大，保持了很好的定域性。


利用FLMO计算开壳层单重态
--------------------------------------------

研究单分子磁体，常遇到所谓反铁磁耦合的态，又称开壳层的单重态。开壳层的单重态，两个自旋相反的电子以开壳层的形式占据在不同的原子中心。BDF可以结合FLMO方法计算开壳层的单重态，算例如下：

.. code-block::

  $autofrag
  method
   flmo
  nprocs
   4  # ask for 4 processes to perform FLMO calculation
  spin
  # Set +1 spin population on atom 9 (O), set -1 spin population on atom 16 (Cu)
   9 +1 16 -1
  # Add no buffer atoms, except for those necessary for saturating dangling bonds.
  # Minimizing the buffer radius helps keeping the spin centers in different fragments
  radbuff
   0
  # Use the PHO method to treat the subsystem boundaries. This is more stable than
  # hydrogen link atoms for systems with small or no buffer
  PHO
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
  Skeleton
  Check
  $end
  
  $xuanyuan
  Direct
  Schwarz
  $end
  
  $scf
  uks
  dft
   PBE1PBE
  spinmulti
   1
  D3
  # The Semiempirical Model Hamiltonian SCF converger. Generally recommended
  # for open-shell metal complexes, although not mandatory for FLMO
  SMH
  molden
  $end
  
  $localmo
  FLMO
  Pipek
  $end

FLMO计算目前不支持简洁输入。这个算例， ``autofrag`` 模块用于对分子自动分片，并产生FLMO计算的基本输入。BDF先根据 ``compass`` 模块中的分子结构与 ``autofrag`` 的参数定义信息产生分子片段，分子片段定域化轨道计算的输入。然后用分子片段的定域轨道组装整体分子的pFLMO (primitive Fragment Local Molecular Orbital) 做为SCF计算的初始猜测轨道，再通过SCF计算在保持每一迭代步轨道都保持定域的下，得到整体分子的开壳层单重态。在计算中，为了输出简洁，分子片段计算输出保存为 ``${BDFTASK}.framgmentN.out`` , **N** 为片段编号，标准输出只打印整体分子计算的输出。

输出会给出分子分片的信息，

.. code-block::

   ----------- Buffered molecular fragments ----------
   BMolefrag    1:   [[1, 3, 19, 2, 4, 20, 5, 6, 7, 8, 9, 10, 11, 12, 13, 21], [], [14], [14, 15], 0.0, 1.4700001016690913]
   BMolefrag    2:   [[14, 15, 16, 17, 18], [2, 4, 20], [21], [21], 0.0, 1.4700001016690913]
   -----------------------------------------
   Automatically assigned charges and spins:
   Fragment  Natom  Charge  Spin
          1     17       0     2
          2      9       0    -2
   -----------------------------------------
   
    Generate BDF input file ....

这里可以看出，我们产生了两个分子片段，指定了分子片 **1** 的编号为17号原子 (17是原子在整体分子中的编号) 自旋多重度指认为2 (Alpha占据)，分子片 **2** 编号为17号原子的自旋多重度设置为-2 （Beta占据）。随后会分别计算2个分子片，提示信息如下：

.. code-block:: bdf

  Starting subsystem calculations ...
  Number of parallel processes:  4
  Number of OpenMP threads per process:  1
  Please refer to test117.fragment*.out for detailed output
  
  Total number of not yet converged subsystems:  2
  List of not yet converged subsystems:  [1, 2]
  Finished calculating subsystem   2 (  1 of   2)
  Finished calculating subsystem   1 (  2 of   2)
  
  Starting global calculation ...

这要注意计算资源的设置。总的计算资源是 **processes*threads** ，即进程数与线程数的乘积。整体计算输出类似普通的SCF计算，但采用了分块对角化Fock矩阵的方法以保持轨道的定域性。

.. code-block:: bdf

  Iter.   idiis  vshift       SCF Energy            DeltaE          RMSDeltaD          MaxDeltaD      Damping    Times(S) 
   Check initial pFLMO orbital MOS
    Openshell  alpha :
    Local Occupied Orbitals Mos and Moc 
   Max_Mos:    1.92219706 Min_Mos:    0.22131628 Aver_Mos:    1.15571382
    Local Virtual Orbitals Mos and Moc 
   Max_Mos:    8.05179109 Min_Mos:    1.51039059 Aver_Mos:    3.02849285
    Openshell  beta  :
    Local Occupied Orbitals Mos and Moc 
   Max_Mos:    2.74831230 Min_Mos:    0.22684452 Aver_Mos:    1.26845818
    Local Virtual Orbitals Mos and Moc 
   Max_Mos:    8.04796147 Min_Mos:    1.63421761 Aver_Mos:    3.01821062
    DNR !! 
   SDNR: warning: rotation angle too large, aborting
   Final iter :    7 Norm of Febru  0.44086E+00
   X --> U time:       0.017      0.000      0.017
   block diag       0.033      0.000      0.017
    block norm :   0.59854165697594264     
  
    DNR !! 
   SDNR: warning: rotation angle too large, aborting
   Final iter :    2 Norm of Febru  0.75922E+00
   X --> U time:       0.017      0.000      0.017
   block diag       0.017      0.000      0.017
    block norm :   0.63338645710957497     
  
     1      0    0.000    -848.6372669802    1169.2042363645       0.0924364022       8.3724618763    0.0000      7.52
    DNR !! 
   Final iter :  375 Norm of Febru  0.75524E-06
   X --> U time:       0.000      0.000      0.017
   block diag       0.083      0.017      0.050
    block norm :    7.9508890032621102E-003
  
    DNR !! 
   Final iter :  372 Norm of Febru  0.72183E-06
   X --> U time:       0.017      0.000      0.017
   block diag       0.100      0.033      0.067
    block norm :    9.5284464944807995E-003

迭代开始会给出轨道伸展 (**Mos**) 的信息， 数字越小，轨道定域性越好。SCF收敛后会再次打印 **Mos** 。 从布居分析的结果，

.. code-block:: bdf

 [Mulliken Population Analysis]
  Atomic charges and Spin densities : 
     1C      -0.2485    0.0010
     2C      -0.1507   -0.0027
     3H       0.2514   -0.0002
     4H       0.2648    0.0006
     5C      -0.3616   -0.0079
     6H       0.2513    0.0239
     7H       0.2437   -0.0013
     8N       0.0127    0.3100
     9O      -0.2745    0.6563
    10C      -0.5937   -0.0091
    11H       0.2697    0.0040
    12H       0.2415    0.0242
    13H       0.2302   -0.0016
    14N       0.1416    0.0259
    15C      -0.2249   -0.0859
    16Cu      0.8229   -0.5878
    17F      -0.5270   -0.1742
    18F      -0.5250   -0.1766
    19H       0.2210    0.0008
    20H       0.2676    0.0006
    21O      -0.3125    0.0002
     Sum:     0.0000   -0.0000

可看出，Cu原子的自旋密度为 **-0.5878**， O原子的自旋密度为 **0.6564** ，接近理论的自旋密度为 -0.5和0.5, 计算结果为开壳层单重态。 

iOI-SCF方法
----------------------------------------------------------

iOI方法，基于用 **分子片合成分子** 的思想，先计算分子片段，再迭代扩大分子片以逼近整体分子。iOI能降低大分子的计算标度，加速SCF收敛。示例如下：

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
  Skeleton
  $end
  
  $xuanyuan
  Direct
  Schwarz
  rs # the range separation parameter omega (or mu) of wB97X
   0.3
  $end
  
  $scf
  rks
  dft
   wB97X
  iprt
   2
  charge
   2
  coulpot+cosx
  $end
  
  $localmo
  FLMO
  $end


