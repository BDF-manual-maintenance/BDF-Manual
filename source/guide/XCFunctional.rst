BDF支持的交换相关泛函
===============================================
BDF的Kohn-Sham密度泛函计算方法，支持限制性(restricted)、非限制性(unrestricted)和
限制性开壳层(restricted open-shell)Kohn-Sham计算，简称为RKS、UKS和ROKS。其输入与RHF、UHF和ROHF接近，
关键是要指定交换相关泛函。BDF支持LDA，GGA，Meta-GGA，Hybrid，RS Hybrid和Hyrid Meta-GGA等多种泛函。

.. table:: BDF中支持的泛函
    :widths: 40 60

    ====================================== ====================================
     泛函类型                                       泛函
    ====================================== ====================================
     局域密度近似方法 (LDA)                   LSDA, SVWN5, SAOP
     广义梯度近似方法 (GGA)                   BP86, BLYP, PBE, PW91, OLYP, KT2
     含动能密度的广义梯度近似法 (meta-GGA)     TPSS, M06L
     杂化泛函 (Hybrid)                       B3LYP, GB3LYP, BHHLYP, PBE0, B3PW91, HFLYP, VBLYP
     范围分离泛函 (RS Hybrid)                 wB97, wB97X, CAM-B3LYP, LC-BLYP
     杂化含动能密度泛函 (Hyrid Meta-GGA)      TPSSh, M062X
     双杂化泛函 ()                           B2PLYP
    ====================================== ====================================

.. note::
    这里的B3LYP用的是VWN5, 而GB3LYP对应的是高斯程序中的B3LYP