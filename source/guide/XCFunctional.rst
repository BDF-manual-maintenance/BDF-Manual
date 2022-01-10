BDF支持的交换相关泛函
===============================================
BDF的密度泛函理论（DFT）支持限制性（restricted）、非限制性（unrestricted）和
限制性开壳层（restricted open-shell）Kohn-Sham计算，分别简称为RKS，UKS和ROKS。其输入与RHF、UHF和ROHF接近，
关键是要指定交换相关泛函。BDF支持LDA，GGA，Meta-GGA，Hybrid，RS Hybrid和Hyrid Meta-GGA等多种泛函。

.. table:: BDF中支持的泛函
    :widths: 40 60

    ========================================  ====================================================
     泛函类型                                  泛函
    ========================================  ====================================================
     局域密度近似（LDA）                       LSDA, SVWN5, SAOP
     广义梯度近似（GGA）                       BP86, BLYP, PBE, PW91, OLYP, KT2
     含动能密度的广义梯度近似（meta-GGA）      TPSS, M06L, M11L, MN12L, MN15L, SCAN, r2SCAN
     杂化GGA泛函（Hybrid GGA）                 B3LYP, GB3LYP, BHHLYP, PBE0, B3PW91, HFLYP, VBLYP
     范围分离GGA泛函（RS Hybrid GGA）          wB97, wB97X, CAM-B3LYP, LC-BLYP
     杂化含动能密度泛函（Hybrid Meta-GGA）     TPSSh, M062X, PW6B95
     双杂化泛函（Double Hybrid）               B2PLYP
    ========================================  ====================================================

.. attention::
    1. B3LYP的LDA相关项采用VWN5, 而GB3LYP对应Gaussian程序中的B3LYP，LDA相关项采用VWN3。
    2. 对于范围分离泛函计算，必须手动在 ``Xuanyuan`` 模块里设定 ``rs`` 值（参见 :ref:`xuanyuan模块的关键词列表<xuanyuan>` ）。wB97, wB97X, CAM-B3LYP, LC-BLYP的rs值分别为0.40, 0.30, 0.33和0.33。
    3. 对于双杂化泛函计算，必须在 ``SCF`` 模块后面添加一个 ``MP2`` 模块（参见 :doc:`算例说明<Example>` 里的算例test116），并从 ``MP2`` 模块的输出读取最终结果。
    4. 可以在 ``SCF`` 模块里用 ``facex`` 和 ``facco`` 关键字调整泛函的HF交换项比例和MP2相关项比例，从而实现用户自定义泛函（参见 :doc:`SCF模块的关键词列表<scf>` ）。
    5. BDF使用了libxc，原则上支持libxc所包含的所有泛函，但需要时间来完善与补充。用户可以向我们反馈需要的泛函，以便我们按照需求来补充。
    
需要注意的是，虽然所有泛函都支持（不带色散校正的）基态单点能计算，但是有的功能只被部分泛函支持。以下是各种计算任务支持的泛函列表：


.. table:: BDF不同计算任务类型支持的泛函
    :widths: 30 70

    ======================== ===================================================================================================
     计算任务类型             泛函
    ======================== ===================================================================================================
     TDDFT单点能、SOC计算     除双杂化泛函外的所有泛函
     TDDFT激发态偶极矩        LSDA, SVWN5, BP86, BLYP, PBE, OLYP, B3LYP, GB3LYP, BHHLYP, PBE0, HFLYP, CAM-B3LYP, LC-BLYP
     基态梯度                 除SAOP、PW91、KT2、B3PW91、VBLYP、SF5050外的所有LDA、GGA、杂化GGA泛函、meta-GGA和杂化meta-GGA泛函
     激发态梯度、NAC          除SAOP、PW91、KT2、B3PW91、VBLYP、SF5050外的所有LDA、GGA和杂化GGA泛函
     能量转移/电子转移积分    所有泛函均支持，但其中B2PLYP的结果不包含MP2相关项的贡献，因而是近似的
     NMR                      所有的LDA、GGA和杂化GGA泛函
     色散校正                 BP86, BLYP, PBE, B3LYP, GB3LYP, BHHLYP, B3PW91, PBE0, CAM-B3LYP, B2PLYP
    ======================== ===================================================================================================
    

    
