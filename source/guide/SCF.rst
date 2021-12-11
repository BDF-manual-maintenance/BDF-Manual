自洽场方法：Hartree-Fock和Kohn-Sham
===========================================

BDF的自洽场包括Hartree-Fock和Kohn-Sham方法。

限制性Hartree-Fock方法
-----------------------------------------------------------------

对于所有电子均成对的偶数电子体系，应使用 ``RHF`` 方法进行Hartree-Fock计算，相关内容已在 :ref:`第一个算例章节<FirstExample>` 提及，这里不再赘述。

非限制性Hartree-Fock方法
-----------------------------------------------------------------

对于有不成对电子的体系，需要用 ``UHF`` 或者限制性开壳层Hartree-Fock （restricted open-shell Hartree-Fock）方法。
对于奇数电子体系，BDF默认自旋多重度为2，且利用UHF计算。例如计算 :math:`C_3H_5` 分子，

.. code-block:: bdf

    #!bdf.sh
    UHF/3-21G 

    geometry
    C                  0.00000000    0.00000000    0.00000000
    C                  0.00000000    0.00000000    1.45400000
    C                  1.43191047    0.00000000    1.20151555
    H                  0.73667537   -0.61814403   -0.54629970
    H                 -0.90366611    0.32890757   -0.54629970
    H                  2.02151364    0.91459433    1.39930664
    H                  2.02151364   -0.91459433    1.39930664
    H                 -0.79835551    0.09653770    2.15071009
    end geometry

UHF计算输出和RHF类似，从 ``scf`` 模块输出可以检查电荷和自旋多重度是否正确，

.. code-block:: 

    Wave function information ...
    Total Nuclear charge    :      23
    Total electrons         :      23
    Ecp-core electrons      :       0
    Spin multiplicity(2S+1) :       2
    Num. of alpha electrons :      12
    Num. of beta  electrons :      11

轨道占据情况按 ``Alpha`` 和 ``Beta`` 轨道分别给出，

.. code-block:: 

    [Final occupation pattern: ]
    
     Irreps:        A   
    
     detailed occupation for iden/irep:      1   1
        1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00
        1.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
        0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
        0.00 0.00 0.00 0.00 0.00 0.00 0.00
     Alpha      12.00
    
     detailed occupation for iden/irep:      2   1
        1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00
        1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
        0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
        0.00 0.00 0.00 0.00 0.00 0.00 0.00
     Beta       11.00
    
轨道能， ``HOMO-LUMO gap`` 也按照 ``Alpha`` 和 ``Beta`` 轨道分开打印

.. code-block:: 

    [Orbital energies:]
   
    Energy of occ-orbsA:    A            12
                -11.18817955     -11.18789391     -11.17752809      -1.11801069      -0.85914580
                 -0.78861789      -0.65514687      -0.61300160      -0.55514631      -0.49906127
                 -0.37655522      -0.30477047
    Energy of vir-orbsA:    A            25
                  0.18221017       0.28830234       0.31069644       0.32818004       0.35397043
                  0.38822931       0.42917813       0.49394022       0.93909970       0.94842069
                  0.96877856       0.97277131       1.02563249       1.05399606       1.11320732
                  1.17687697       1.26547430       1.31245896       1.32719078       1.34493766
                  1.37905664       1.45903968       1.80285556       1.93877012       2.01720415
   
   
    Energy of occ-orbsB:    A            11
                -11.19670896     -11.16769083     -11.16660825      -1.07470168      -0.84162305
                 -0.74622771      -0.63695581      -0.58068095      -0.53876236      -0.46400924
                 -0.37745766
    Energy of vir-orbsB:    A            26
                  0.15755278       0.18938428       0.30608423       0.33204779       0.33996597
                  0.38195612       0.39002159       0.43644421       0.52237314       0.94876233
                  0.96144960       0.97568581       1.01804430       1.05467405       1.09547593
                  1.13390456       1.19865205       1.28139866       1.32654541       1.33938005
                  1.34914150       1.38200544       1.47565481       1.79509704       1.96917149
                  2.03513467
   
    Alpha   HOMO energy:      -0.30477047 au      -8.29322996 eV  Irrep: A       
    Alpha   LUMO energy:       0.18221017 au       4.95819299 eV  Irrep: A       
    Beta    HOMO energy:      -0.37745766 au     -10.27114977 eV  Irrep: A       
    Beta    LUMO energy:       0.15755278 au       4.28723115 eV  Irrep: A       
    HOMO-LUMO gap:       0.46232325 au      12.58046111 eV

其他输出信息可参见RHF计算的例子，这里不再冗述。

限制性开壳层Hartree-Fock方法
------------------------------------------------------------------------------------------

限制性开壳层Hartree-Fock (Restricted open-shell Hartree-Fock - ROHF)可以计算开壳层分子体系。这里给出一个 :math:`CH_2` 三重态的ROHF算例，

.. code-block:: bdf

    #!bdf.sh
    rohf/cc-pvdz spinmulti=3
    
    geometry   # 输入坐标单位 Angstrom
     C     0.000000        0.00000        0.31399
     H     0.000000       -1.65723       -0.94197
     H     0.000000        1.65723       -0.94197
    end geometry

这里，在第二行指定使用 ``ROHF`` 方法，且利用关键词 ``spinmulti=3`` 设定计算三重态。ROHF的输出和UHF类似，
但其 ``Alpha`` 轨道和 ``Beta`` 是一样的，所以相对应的 ``Alpha`` 和 ``Beta`` 轨道能量相等，如下所示：

.. code-block:: 

    [Orbital energies:]
   
    Energy of occ-orbsA:    A1            3
                -11.42199273      -0.75328533      -0.22649749
    Energy of vir-orbsA:    A1            8
                  0.05571960       0.61748052       0.70770696       0.83653819       1.29429307
                  1.34522491       1.56472153       1.87720054
    Energy of vir-orbsA:    A2            2
                  1.34320056       1.53663810
   
    Energy of occ-orbsA:    B1            1
                 -0.37032603
    Energy of vir-orbsA:    B1            6
                  0.06082087       0.66761691       0.77091474       1.23122892       1.51131609
                  1.91351353
   
    Energy of occ-orbsA:    B2            1
                 -0.16343739
    Energy of vir-orbsA:    B2            3
                  0.65138659       1.35768658       1.54657952
   
   
    Energy of occ-orbsB:    A1            2
                -11.42199273      -0.75328533
    Energy of vir-orbsB:    A1            9
                 -0.22649749       0.05571960       0.61748052       0.70770696       0.83653819
                  1.29429307       1.34522491       1.56472153       1.87720054
    Energy of vir-orbsB:    A2            2
                  1.34320056       1.53663810
   
    Energy of occ-orbsB:    B1            1
                 -0.37032603
    Energy of vir-orbsB:    B1            6
                  0.06082087       0.66761691       0.77091474       1.23122892       1.51131609
                  1.91351353
    Energy of vir-orbsB:    B2            4
                 -0.16343739       0.65138659       1.35768658       1.54657952
                 
由于 ``Alpha`` 与 ``Beta`` 轨道的占据数不同， ``Alpha`` 的HOMO、LUMO轨道、轨道能与 ``Beta`` 的不同，如下：

.. code-block:: 

    Alpha   HOMO energy:      -0.16343739 au      -4.44735961 eV  Irrep: B2      
    Alpha   LUMO energy:       0.05571960 au       1.51620803 eV  Irrep: A1      
    Beta    HOMO energy:      -0.37032603 au     -10.07708826 eV  Irrep: B1      
    Beta    LUMO energy:      -0.22649749 au      -6.16331290 eV  Irrep: A1      
    HOMO-LUMO gap:      -0.06306010 au      -1.71595329 eV


RKS/UKS和ROKS计算
-------------------------------------------------
限制性Kohn-Sham (Restricted Kohn-Sham -- RKS)方法，这里以简洁输入的模式给出一个 :math:`H_{2}O`  分子的DFT计算算例，使用了B3lyp泛函。

.. code-block:: bdf

  #!bdf.sh
  B3lyp/3-21G    

  geometry
  O
  H  1  R1 
  H  1  R1  2 109.

  R1=1.0     # OH bond length, unit is Angstrom
  end geometry

这个输入对应的高级模式的输入为

.. code-block:: bdf

    $compass
    geometry # On default: bond length unit in angstrom
    o
    h 1 1.0
    h 1 1.0 2 109.
    end geometry
    skeleton # 计算骨架Fock矩阵
    basis
      3-21g
    $end

    $xuanyuan
    direct # ask for direct SCF
    maxmem
      512mw
    $end

    $scf
    rks # Restricted Kohn-Sham calculation
    dft # ask for B3lyp functional, it is different with B3lyp implemented in Gaussian. 
      b3lyp
    $end

这里，输入要求使用 ``B3lyp`` 泛函。相比于Hartree-Fock，输出多了Exc项的贡献，如下所示：

.. code-block:: 

   Final scf result
     E_tot =               -75.93603354
     E_ele =               -84.72787022
     E_nn  =                 8.79183668
     E_1e  =              -122.04354727
     E_ne  =              -197.45852687
     E_kin =                75.41497960
     E_ee  =                44.81744844
     E_xc  =                -7.50177140
    Virial Theorem      2.006909

:math:`H_{2}O^{+}` 离子的ROKS计算，简洁输入如下，

.. code-block:: bdf

    #!bdf.sh
    ROKS/B3lyp/cc-pvdz charge=1    
    
    geometry
    O
    H  1  R1
    H  1  R1  2 109.
    
    R1=1.0     # OH bond length in angstrom 
    end geometry

.. hint::
    相比于Hartree-Fock，Kohn-Sham需要在高级输入使用dft关键词执行交换相关泛函。如果是简洁输入，只需指定交换相关泛函和基组。系统会根据自旋态选择使用RKS或UKS，如果要使用ROKS，必须明确输入。


基于RS杂化泛函的Kohn-Sham计算
-------------------------------------------------

CAM-B3LYP等RS杂化泛函，将库伦相互作用分为长短程，

.. math::

    \frac{1}{r_{12}} = \frac{1-[\alpha + \beta \cdot erf(\mu r_{12})]}{r_{12}}+\frac{\alpha + \beta \cdot erf(\mu r_{12})}{r_{12}}

采用BDF高级输入时，可以通过xuanyuan模块中的关键字RS，调整 :math:`\mu` 参数。CAM-B3lyp默认的 :math:`\mu` 参数为0.33。例如 1,3-Butadiene
分子，利用CAM-B3lyp的RKS计算高级模式输入为，

.. code-block:: bdf

   $compass
   basis
    cc-pVDZ
   geometry
   C -2.18046929 0.68443844 -0.00725330
   H -1.64640852 -0.24200621 -0.04439369
   H -3.24917614 0.68416040 0.04533562
   C -1.50331750 1.85817167 -0.02681816
   H -0.43461068 1.85844971 -0.07940766
   C -2.27196552 3.19155924 0.02664018
   H -3.34067218 3.19128116 0.07923299
   C -1.59481380 4.36529249 0.00707382
   H -2.12887455 5.29173712 0.04421474
   H -0.52610710 4.36557056 -0.04551805
   end geometry
   skeleton
   $end
   
   $xuanyuan
   direct
   rs
    0.33   # define mu=0.33 in CAM-B3lyp functional
   $end
   
   $scf
   rks # restricted Kohn-Sham
   dft
    cam-b3lyp
   $end


杂化泛函Hartree-Fock交换项成分的自定义
-------------------------------------------------

【注：该方法目前git上的BDF版本还不支持，过几天我再push上来】

对于某些计算，可能需要用户手动调节泛函的Hartree-Fock交换项成分，才能获得满意的精度。此时可在 ``$scf`` 模块里加入 ``facex`` 关键字，例如若要将B3LYP泛函的Hartree-Fock交换项成分由默认的20%改为15%，可以写

.. code-block:: bdf

   $scf
   uks # unrestricted Kohn-Sham. Of course, the facex keyword can also be applied to RKS and ROKS
   dft
    b3lyp
   facex
    0.15
   $end

对弱相互作用的色散矫正
-------------------------------------------------
常见的交换相关泛函如B3lyp对弱相互作用不能很好的描述，这时，在计算能量或者做分子结构优化时，需要加入色散矫正。BDF采用了Stefan Grimme开发的
D3色散矫正方法，需要在SCF模块的输入中指定D3关键词，输入如下，

.. code-block:: bdf

    #!bdf.sh
    B3lyp/cc-pvdz     
    
    geometry
    O
    H  1  R1
    H  1  R1  2 109.
    
    R1=1.0     # OH bond length in angstrom 
    end geometry
    
    $scf
    D3   # Gremme's dispersion correction
    $end

在Kohn-Sham计算结束后加入色散矫正，计算输出如下，

.. code-block:: 

    diis/vshift is closed at iter =   8
      9      0    0.000     -76.3804911662      -0.0000000001       0.0000000170       0.0000001684    0.0000      0.02
   
     Label              CPU Time        SYS Time        Wall Time
    SCF iteration time:         0.467 S        0.033 S        0.233 S
   
    Final DeltaE =  -7.5459638537722640E-011
    Final DeltaD =   1.6950036756030376E-008   5.0000000000000002E-005
   
    Final scf result
      E_tot =               -76.38106481
      E_ele =               -85.17290149
      E_disp=                -0.00057364
      E_nn  =                 8.79183668
      E_1e  =              -122.51287853
      E_ne  =              -198.42779201
      E_kin =                75.91491348
      E_ee  =                44.84995532
      E_xc  =                -7.50940464
     Virial Theorem      2.006140

这里的总能量 ``E_tot`` 包含了色散矫正能， ``E_disp = -0.00057364`` 。


提高Kohn-Sham计算的积分格点精度
-------------------------------------------------

虽然BDF默认对不同的泛函，按照精度要求自定义了积分格点，例如Meta-GGA类泛函对积分格点要求很高，BDF默认对Meta-GGA使用Fine类型的格点，
用户可能还希望能对积分格点进行调节。Kohn-Sham泛函的积分格点可以在SCF模块的输入中通过Grid等关键词定义，Grid的有效值为 ``Ultra coarse`` ,
``Coarse`` , ``medium`` , ``fine``, ``Ultra fine``, ``sg1`` 等6个，从 ``Ultra coarse`` 到 ``Ultra fine`` 积分格点依次增加，数值积分精度依次提高。

例如， :math:`H_{2}O` 分子计算采用了M062X泛函，属于Hybrid Meta-GGA泛函，要求密集的积分格点，需要采用BDF的高级输入和简洁输入混合模式，如下所示：

.. code-block:: bdf

    #!bdf.sh
    M062X/cc-pvdz     
    
    geometry
    O
    H  1  R1
    H  1  R1  2 109.
    
    R1=1.0     # OH bond length in angstrom 
    end geometry
    
    $scf
    grid # set numerical integration grid as ultra fine
     ultra fine
    $end

BDF在Kohn-Sham计算的开始几步采用 ``Ultra coarse`` 积分格点，如下所示，

.. code-block:: 

    Switch to Ultra Coarse grid ...
    [ATOM SCF control]
     heff=                     0
    After initial atom grid ...
    After initial atom grid ...
   
     Generating Numerical Integration Grid.
   
      1  O     Second Kind Chebyshev ( 21)  Lebedev ( -194)         
         Atoms:      1
      2  H     Second Kind Chebyshev ( 21)  Lebedev ( -194)         
         Atoms:      2     3
    Partition Function:  SSF   Partitioning with Scalar=  0.64.
    Gtol, Npblock, Icoulpot, Iop_adaptive :  0.10E-04    128      0          0
    Number of symmetry operation =   4
   
    Basis Informations for Self-adaptive Grid Generation, Cutoff=  0.10E-04
       1O     GTO( 14) Ntot=  26 MaxL= 2 MaxNL= 0 MaxRad= 0.530E+01
     basis details in form ( N L Zeta Cutradius): 
     ( 1  0   0.117E+05   0.02)  ( 1  0   0.176E+04   0.06)  ( 1  0   0.401E+03   0.13)  ( 1  0   0.114E+03   0.24)
     ( 1  0   0.370E+02   0.42)  ( 1  0   0.133E+02   0.70)  ( 1  0   0.503E+01   1.14)  ( 1  0   0.101E+01   2.53)
     ( 1  0   0.302E+00   4.64)  ( 2  1   0.177E+02   0.66)  ( 2  1   0.385E+01   1.42)  ( 2  1   0.105E+01   2.72)
     ( 2  1   0.275E+00   5.30)  ( 3  2   0.119E+01   2.73)
       2H     GTO(  5) Ntot=   7 MaxL= 1 MaxNL= 0 MaxRad= 0.730E+01
     basis details in form ( N L Zeta Cutradius): 
     ( 1  0   0.130E+02   0.71)  ( 1  0   0.196E+01   1.82)  ( 1  0   0.445E+00   3.82)  ( 1  0   0.122E+00   7.30)
     ( 2  1   0.727E+00   3.26)
     Numerical Grid Generated SUCCESSFULLY! 
    Total and symmetry independent Grid Number:      4352      1181

当能量收敛到0.01 Hartree之内时，会切换积分格点到 ``Ultra fine`` ，输出如下所示：

.. code-block:: 

     3      2    0.000     -76.3545948190      -0.0080960042       0.0057803268       0.0577528497    0.0000      0.02
     Switch to Ultra Fine grid ...
     [ATOM SCF control]
      heff=                     0
     After initial atom grid ...
     After initial atom grid ...
    
      Generating Numerical Integration Grid.
    
       1  O     Second Kind Chebyshev (100)  Lebedev (-1202)         
          Atoms:      1
       2  H     Second Kind Chebyshev (100)  Lebedev (-1202)         
          Atoms:      2     3
     Partition Function:  SSF   Partitioning with Scalar=  0.64.
     Gtol, Npblock, Icoulpot, Iop_adaptive :  0.10E-04    128      0          0
     Number of symmetry operation =   4
    
     Basis Informations for Self-adaptive Grid Generation, Cutoff=  0.10E-04
        1O     GTO( 14) Ntot=  26 MaxL= 2 MaxNL= 0 MaxRad= 0.530E+01
      basis details in form ( N L Zeta Cutradius): 
      ( 1  0   0.117E+05   0.02)  ( 1  0   0.176E+04   0.06)  ( 1  0   0.401E+03   0.13)  ( 1  0   0.114E+03   0.24)
      ( 1  0   0.370E+02   0.42)  ( 1  0   0.133E+02   0.70)  ( 1  0   0.503E+01   1.14)  ( 1  0   0.101E+01   2.53)
      ( 1  0   0.302E+00   4.64)  ( 2  1   0.177E+02   0.66)  ( 2  1   0.385E+01   1.42)  ( 2  1   0.105E+01   2.72)
      ( 2  1   0.275E+00   5.30)  ( 3  2   0.119E+01   2.73)
        2H     GTO(  5) Ntot=   7 MaxL= 1 MaxNL= 0 MaxRad= 0.730E+01
      basis details in form ( N L Zeta Cutradius): 
      ( 1  0   0.130E+02   0.71)  ( 1  0   0.196E+01   1.82)  ( 1  0   0.445E+00   3.82)  ( 1  0   0.122E+00   7.30)
      ( 2  1   0.727E+00   3.26)
      Numerical Grid Generated SUCCESSFULLY! 
     Total and symmetry independent Grid Number:     94208     24827

这里，H和O原子的积分格点都为100*1202, 其中，100是径向格点的数目，1202是角向格点的数目。

大体系的SCF计算：片段局域分子轨道（FLMO）方法和迭代轨道相互作用（iOI）方法
-----------------------------------------------------------------

对于大体系（例如原子数大于300的体系），以上介绍的传统SCF计算方法常常不再适用，原因除了每步Fock矩阵构建时间变长以外，还包括以下因素：

 * Fock矩阵对角化时间占计算总时间的比例增加。当体系足够大时，每步Fock矩阵的构建时间与体系大小的平方成正比，但Fock矩阵对角化时间和体系大小的三次方成正比，因此对于特别大（如上千个原子）的体系，Fock矩阵对角化占总计算时间的比例将相当可观。
 * 大体系的局部稳定波函数更多，导致大体系SCF计算收敛到用户期望的态的概率降低。换言之，SCF可能收敛到很多个不同的解，其中只有一个是用户想要的，因此增加了用户判断SCF解是否是自己期望的解，以及（如果收敛到非期望的解时）重新提交计算等时间开销。
 * 大体系的SCF收敛比小体系更加困难，需要更多的迭代步数，甚至完全不能收敛。这除了是因为上述的局部稳定解变多以外，也有一部分原因是因为一般的基于原子密度的SCF初猜的质量随着体系增大而变差。
 
针对以上问题，一种解决方案是将体系分为若干片段（该过程称为分片；这些片段彼此之间可以重叠），对每个片段分别做SCF，再把所有片段的收敛的波函数汇总，作为总体系SCF计算的初猜。BDF的FLMO方法即属于一种基于分片的方法，其中每个片段的SCF收敛后，程序对每个片段的波函数进行局域化，再用所得的局域轨道产生总体系计算的初猜。相比不依赖局域轨道的分片方法，这样做会带来一些额外的好处：

 * SCF迭代可以在局域轨道基上进行，在局域轨道基下Fock矩阵无需进行全对角化，而只需进行块对角化，即转动轨道使得占据-空块为零即可，该步骤的计算量较全对角化小。
 * 局域轨道基下的Fock矩阵的占据-空块非常稀疏，可以利用这种稀疏性进一步减小块对角化的计算量。
 * 用户可以在进行全局SCF计算之前就指定某个局域轨道的占据数，从而选择性地得到该局域轨道占据或未占据的电子态，例如计算由一个Fe(II)和一个Fe(III)组成的金属团簇，可以通过指定Fe 3d轨道的占据数来控制哪个Fe收敛到二价组态，哪个Fe收敛到三价组态。在当前的BDF版本里实际还支持另外一种做法，即直接指定原子的形式氧化态和自旋态（见下）。出于便捷性考虑，一般建议用户直接通过原子的形式氧化态和自旋态来指定收敛到哪个电子态。
 * SCF计算直接得到收敛的局域轨道，而不是像一般的SCF计算那样只得到正则轨道。如果用户需要得到收敛的局域轨道来进行波函数分析等，那么FLMO方法相比传统的先得到正则轨道再进行局域化的做法而言，可以节省很多计算时间，也可以规避大体系局域化迭代次数多、容易不收敛的问题。

例如，下述算例采用FLMO方法计算一个含有Cu(II)和氮氧稳定自由基的体系的自旋破缺基态：

.. code-block:: bdf

    $autofrag
    method
     flmo
    nprocs # parallelize the subsystem calculations across 4 processes
     4
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
    spin
     1
    D3
    # The Semiempirical Model Hamiltonian SCF converger. Generally recommended
    # for open-shell metal complexes, although not mandatory for FLMO
    SMH
    $end

    $localmo
    FLMO
    Pipek # Selects Pipek-Mezey localization (recommended when the molecule contains pi systems) instead of the default Boys localization (recommended otherwise)
    $end

To be done
