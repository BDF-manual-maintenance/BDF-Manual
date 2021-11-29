=======
Kohn-Sham方法
================================================
BDF的Kohn-Sham密度泛函计算，支持限制性（restricted）、非限制性（unrestricted）和
限制性开壳层（restricted open-shell）Kohn-Sham计算，简称为RKS、UKS和ROKS。其输入与RHF、UHF和ROHF接近，
关键是要指定交换相关泛函。BDF支持LDA，GGA，Meta-GGA，Hybrid，RS Hybrid和Hyrid Meta-GGA等多种泛函。

.. table:: BDF中支持的泛函
    :widths: 40 60

    ======================================= ====================================
     泛函类型                                       泛函
    ======================================= ====================================
     局域密度近似方法（LDA）                  LSDA, SVWN5, SAOP
     广义梯度近似方法（GGA）                  BP86, BLYP, PBE, PW91, OLYP, KT2
     含动能密度的广义梯度近似法（meta-GGA）   TPSS, M06L
     杂化泛函（Hybrid）                       B3LYP, GB3LYP, BHHLYP, PBE0, B3PW91, HFLYP, VBLYP
     范围分离泛函（RS Hybrid）                wB97, wB97X, CAM-B3LYP, LC-BLYP
     杂化含动能密度泛函（Hyrid Meta-GGA）     TPSSh, M062X
     双杂化泛函                               B2PLYP
    ======================================= ====================================

RKS/UKS和ROKS计算
-------------------------------------------------
限制性Kohn-Sham（Restricted Kohn-Sham -- RKS）方法，这里以简洁输入的模式给出一个H2O分子的DFT计算算例，使用了B3lyp泛函。

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


基于RS杂化泛函的Kohn-Sham计算
-------------------------------------------------


杂化泛函Hartree-Fock交换项的自定义
-------------------------------------------------

激发态的Kohn-Sham计算
-------------------------------------------------

色散矫正
-------------------------------------------------


提高Kohn-Sham计算的积分格点精度
-------------------------------------------------


