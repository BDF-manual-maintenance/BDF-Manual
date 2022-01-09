自洽场方法：Hartree-Fock和Kohn-Sham
===========================================

BDF的自洽场包括Hartree-Fock和Kohn-Sham方法。

限制性Hartree-Fock方法
-----------------------------------------------------------------

限制性Hatree-Fock方法(RHF)的示例已在 :ref:`第一个算例一节<FirstExample>` 提及，这里不再赘述。

非限制性Hartree-Fock方法
-----------------------------------------------------------------

对于有不成对电子的体系，需要用 ``UHF`` 方法，此外也可以用限制性开壳层Hartree-Fock （restricted open-shell Hartree-Fock）方法，见后。
对于奇数电子体系，BDF默认自旋多重度为2，且利用UHF计算。例如计算 :math:`\ce{C3H5}` 分子，

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
     -11.18817955    -11.18789391    -11.17752809     -1.11801069     -0.85914580
      -0.78861789     -0.65514687     -0.61300160     -0.55514631     -0.49906127
      -0.37655522     -0.30477047
    Energy of vir-orbsA:    A            25
       0.18221017      0.28830234      0.31069644      0.32818004      0.35397043
       0.38822931      0.42917813      0.49394022      0.93909970      0.94842069
       0.96877856      0.97277131      1.02563249      1.05399606      1.11320732
       1.17687697      1.26547430      1.31245896      1.32719078      1.34493766
       1.37905664      1.45903968      1.80285556      1.93877012      2.01720415
   
   
    Energy of occ-orbsB:    A            11
      -11.19670896   -11.16769083    -11.16660825     -1.07470168     -0.84162305
      -0.74622771     -0.63695581     -0.58068095     -0.53876236     -0.46400924
      -0.37745766
    Energy of vir-orbsB:    A            26
       0.15755278      0.18938428      0.30608423      0.33204779      0.33996597
       0.38195612      0.39002159      0.43644421      0.52237314      0.94876233
       0.96144960      0.97568581      1.01804430      1.05467405      1.09547593
       1.13390456      1.19865205      1.28139866      1.32654541      1.33938005
       1.34914150      1.38200544      1.47565481      1.79509704      1.96917149
       2.03513467
   
    Alpha   HOMO energy:      -0.30477047 au      -8.29322996 eV  Irrep: A       
    Alpha   LUMO energy:       0.18221017 au       4.95819299 eV  Irrep: A       
    Beta    HOMO energy:      -0.37745766 au     -10.27114977 eV  Irrep: A       
    Beta    LUMO energy:       0.15755278 au       4.28723115 eV  Irrep: A       
    HOMO-LUMO gap:       0.46232325 au      12.58046111 eV

其他输出信息可参见RHF计算的例子，这里不再冗述。

限制性开壳层Hartree-Fock方法
------------------------------------------------------------------------------------------

限制性开壳层Hartree-Fock（Restricted open-shell Hartree-Fock - ROHF）也可以计算开壳层分子体系。这里给出一个 :math:`\ce{CH2}` 三重态的ROHF算例，

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
      -11.42199273    -0.75328533     -0.22649749
    Energy of vir-orbsA:    A1            8
      0.05571960       0.61748052      0.70770696      0.83653819      1.29429307
      1.34522491       1.56472153      1.87720054
    Energy of vir-orbsA:    A2            2
      1.34320056       1.53663810
   
    Energy of occ-orbsA:    B1            1
     -0.37032603
    Energy of vir-orbsA:    B1            6
      0.06082087       0.66761691      0.77091474      1.23122892      1.51131609
      1.91351353
   
    Energy of occ-orbsA:    B2            1
     -0.16343739
    Energy of vir-orbsA:    B2            3
      0.65138659       1.35768658      1.54657952
   
   
    Energy of occ-orbsB:    A1            2
      -11.42199273    -0.75328533
    Energy of vir-orbsB:    A1            9
       -0.22649749     0.05571960      0.61748052      0.70770696      0.83653819
        1.29429307     1.34522491      1.56472153      1.87720054
    Energy of vir-orbsB:    A2            2
        1.34320056     1.53663810
   
    Energy of occ-orbsB:    B1            1
       -0.37032603
    Energy of vir-orbsB:    B1            6
        0.06082087     0.66761691      0.77091474      1.23122892      1.51131609
        1.91351353
    Energy of vir-orbsB:    B2            4
       -0.16343739     0.65138659      1.35768658      1.54657952
                 
由于 ``Alpha`` 与 ``Beta`` 轨道的占据数不同， ``Alpha`` 的HOMO、LUMO轨道、轨道能与 ``Beta`` 的不同，如下：

.. code-block:: 

    Alpha   HOMO energy:      -0.16343739 au      -4.44735961 eV  Irrep: B2      
    Alpha   LUMO energy:       0.05571960 au       1.51620803 eV  Irrep: A1      
    Beta    HOMO energy:      -0.37032603 au     -10.07708826 eV  Irrep: B1      
    Beta    LUMO energy:      -0.22649749 au      -6.16331290 eV  Irrep: A1      
    HOMO-LUMO gap:      -0.06306010 au      -1.71595329 eV


RKS，UKS，和ROKS计算
-------------------------------------------------
对于限制性Kohn-Sham（Restricted Kohn-Sham, RKS）方法，这里以简洁输入的模式给出一个 :math:`\ce{H2O}`  分子的RKS计算算例，使用了B3lyp泛函。

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
    basis
      3-21g
    $end

    $xuanyuan
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

:math:`\ce{H2O+}` 离子的ROKS计算，简洁输入如下，

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
    相比于Hartree-Fock，Kohn-Sham需要在高级输入使用dft关键词指定交换相关泛函。如果是简洁输入，只需指定交换相关泛函和基组。系统会根据自旋态选择使用RKS或UKS，如果要使用ROKS，必须明确输入。


基于RS杂化泛函的Kohn-Sham计算
-------------------------------------------------

CAM-B3LYP等RS杂化泛函，将库伦相互作用分为长短程，

.. math::

    \frac{1}{r_{12}} = \frac{1-[\alpha + \beta \cdot erf(\mu r_{12})]}{r_{12}}+\frac{\alpha + \beta \cdot erf(\mu r_{12})}{r_{12}}

采用BDF高级输入时，可以通过xuanyuan模块中的关键词RS，调整 :math:`\mu` 参数。CAM-B3lyp默认的 :math:`\mu` 参数为0.33，
其它范围分离泛函中的 :math:`\mu` 值见 :ref:`RSOMEGA<xuanyuan_rsomega>` 关键词。
例如 1,3-Butadiene 分子，利用CAM-B3lyp的RKS高级模式输入为，

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
   $end
   
   $xuanyuan
   rs
    0.33   # define mu=0.33 in CAM-B3lyp functional
   $end
   
   $scf
   rks # restricted Kohn-Sham
   dft
    cam-b3lyp
   $end


自定义杂化泛函、双杂化泛函的精确交换项和相关项成分
-----------------------------------------------------------

对于某些计算，可能需要用户手动调节泛函的精确交换项成分，才能获得满意的精度。此时可在 ``$scf`` 模块里加入 ``facex`` 关键词，例如若要将B3LYP泛函的精确交换项成分由默认的20%改为15%，可以写

.. code-block:: bdf

   $scf
   ...
   dft
    b3lyp
   facex
    0.15
   $end

类似地，可以用 ``facco`` 关键词自定义双杂化泛函的MP2相关项成分。注意并不是所有泛函都支持自定义facex和facco（参见 :ref:`SCF模块的关键词列表<scf>` ）。

对弱相互作用的色散矫正
-------------------------------------------------
常见的交换相关泛函如B3lyp不能很好地描述弱相互作用，需要在计算能量或者做分子结构优化时，加入色散矫正。BDF采用了Stefan Grimme开发的
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
    D3   # Grimme's dispersion correction
    $end

.. tip::

    * 这里使用了BDF混合模式的输入方式，在简洁输入基础上，通过添加SCF模块关键词精确控制SCF计算。


在Kohn-Sham计算结束后加入色散矫正，计算输出如下，

.. code-block:: 

    diis/vshift is closed at iter =   8
    9    0   0.000  -76.380491166  -0.000000000  0.000000017  0.000000168  0.0000   0.02
   
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

虽然BDF对不同的泛函按照精度要求定义了默认积分格点（例如Meta-GGA类泛函对积分格点要求很高，BDF默认使用Fine格点），
用户可能还希望对积分格点进行调节。Kohn-Sham泛函的积分格点可以在SCF模块的输入中通过Grid关键词定义，Grid的有效值为 ``Ultra coarse`` ，
``Coarse`` ， ``medium`` ， ``fine`` ， ``Ultra fine`` ， ``sg1`` 等6个，从 ``Ultra coarse`` 到 ``sg1`` 积分格点依次增加，数值积分精度依次提高。

示例： :math:`\ce{H2O}` 分子的M062X计算。该泛函属于杂化Meta-GGA类型泛函，要求密集的积分格点，因此输入用到了高级输入和简洁输入混合模式，如下所示：

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
     ( 1  0   0.117E+05   0.02)  ( 1  0   0.176E+04   0.06)  ( 1  0   0.401E+03   0.13)
     ( 1  0   0.114E+03   0.24)  ( 1  0   0.370E+02   0.42)  ( 1  0   0.133E+02   0.70)
     ( 1  0   0.503E+01   1.14)  ( 1  0   0.101E+01   2.53)  ( 1  0   0.302E+00   4.64)
     ( 2  1   0.177E+02   0.66)  ( 2  1   0.385E+01   1.42)  ( 2  1   0.105E+01   2.72)
     ( 2  1   0.275E+00   5.30)  ( 3  2   0.119E+01   2.73)
       2H     GTO(  5) Ntot=   7 MaxL= 1 MaxNL= 0 MaxRad= 0.730E+01
     basis details in form ( N L Zeta Cutradius): 
     ( 1  0   0.130E+02   0.71)  ( 1  0   0.196E+01   1.82)  ( 1  0   0.445E+00   3.82)
     ( 1  0   0.122E+00   7.30)  ( 2  1   0.727E+00   3.26)
     Numerical Grid Generated SUCCESSFULLY! 
    Total and symmetry independent Grid Number:      4352      1181

当能量收敛到0.01 Hartree之内时，会切换到 ``Ultra fine`` 积分格点，输出如下所示：

.. code-block:: 

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
      ( 1  0   0.117E+05   0.02)  ( 1  0   0.176E+04   0.06)  ( 1  0   0.401E+03   0.13)
      ( 1  0   0.114E+03   0.24)  ( 1  0   0.370E+02   0.42)  ( 1  0   0.133E+02   0.70)
      ( 1  0   0.503E+01   1.14)  ( 1  0   0.101E+01   2.53)  ( 1  0   0.302E+00   4.64)
      ( 2  1   0.177E+02   0.66)  ( 2  1   0.385E+01   1.42)  ( 2  1   0.105E+01   2.72)
      ( 2  1   0.275E+00   5.30)  ( 3  2   0.119E+01   2.73)
        2H     GTO(  5) Ntot=   7 MaxL= 1 MaxNL= 0 MaxRad= 0.730E+01
      basis details in form ( N L Zeta Cutradius): 
      ( 1  0   0.130E+02   0.71)  ( 1  0   0.196E+01   1.82)  ( 1  0   0.445E+00   3.82)
      ( 1  0   0.122E+00   7.30)  ( 2  1   0.727E+00   3.26)
      Numerical Grid Generated SUCCESSFULLY! 
     Total and symmetry independent Grid Number:     94208     24827

这里，H和O原子的积分格点都为100*1202，其中，100是径向格点的数目，1202是角向格点的数目。

