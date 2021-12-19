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
     双杂化泛函 (Double Hybrid)              B2PLYP
    ====================================== ====================================

.. note::
    1. 这里的B3LYP的LDA相关项用的是VWN5, 而GB3LYP对应的是高斯程序中的B3LYP，LDA相关项用的是VWN3;
    2. 对于范围分离泛函计算，必须手动在$xuanyuan模块里设定rs值（参见 :ref:`xuanyuan模块的关键词列表<xuanyuan>` ）。wB97, wB97X, CAM-B3LYP, LC-BLYP的rs值分别为0.40, 0.30, 0.33和0.33；
    3. 对于双杂化泛函计算，必须在$scf模块后面添加一个$mp2模块（参见 :ref:`算例说明<Example>` 里的算例test116），并从$mp2模块的输出读取最终结果。
    4. BDF使用了libxc，原则上支持libxc所支持的所有泛函，但需要时间来完善与补充。用户可以向我们反馈需要的泛函，以便我们按照需求来补充。
    
