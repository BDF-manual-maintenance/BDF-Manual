scf模块
================================================
SCF模块是BDF的核心计算模块之一，进行Hartree-Fock和DFT计算。

**计算方法关键词**

:guilabel:`RHF/UHF/ROHF` 参数类型：Βοοl型
------------------------------------------------
如果做Hartree-Fock计算，这三个参数必须3选1，用于控制Hartree-Fock计算的类型。
``RHF`` 为Restricted Hartree-Fock；
``UHF`` 为Unrestricted Hartree-Fock；
``ROHF`` 为Restricted Open-shell Hartree-Fock

:guilabel:`RKS/UKS/ROKS` 参数类型：Βοοl型
---------------------------------------------------
如果做DFT计算，这三个参数必须3选1，用于控制DFT计算的类型。
``RKS`` 为Restricted Kohn-Sham；
``UKS`` 为Unrestricted Kohn-Sham；
``ROKS`` 为Restricted Open-shell Kohn-Sham

**波函数与占据数关键词**

:guilabel:`Charge` 参数类型：整数
------------------------------------------------
默认值：0

指定计算的分子体系的电荷数。

:guilabel:`Spin` 参数类型：整数
---------------------------------------------------
指定计算的分子体系的自旋，这里输入的是自旋多重度2S+1。

:guilabel:`Occupy` 参数类型：整数数组
------------------------------------------------
指定每个不可约表示分子轨道中双电子占据的轨道数目，用于RHF/RKS计算。

:guilabel:`Alpha & Beta` 参数类型：整数数组
---------------------------------------------------
Alpha & Beta必须联用，用于UHF/UKS计算，分别指定alpha或beta轨道每种不可约表示占据轨道数目。

**DFT交换相关泛函关键词**

:guilabel:`DFT` 参数类型：字符串
---------------------------------------------------
指定DFT计算的交换相关泛函。参见BDF支持的交换相关泛函列表。

:guilabel:`D3` 参数类型：Bool型
------------------------------------------------
指定对DFT计算加入Grimme的D3色散矫正。

:guilabel:`RS` 参数类型：浮点型
---------------------------------------------------
指定Range-Speration泛函如CAM-B3LYP等的系数。建议值：0.33。

**DFT数值积分格点控制参数关键词**

:guilabel:`NPTRAD` 参数类型：整型
---------------------------------------------------
指定数值积分径向格点数。一般本参数用于调试程序。

:guilabel:`NPTANG` 参数类型：整型
------------------------------------------------
指定数值积分角向格点数。一般本参数用于调试程序。

:guilabel:`COSXNGRID` 参数类型：字符串+整型+整型
---------------------------------------------------
指定在Coulpot+Cosx计算每种原子类型的径向与角向格点数。

.. code-block:: python
     #CH2分子，Coulpot+Cosx计算
     $scf
     RKS
     Coulpot+Cosx
     CosxNGrid
     C 20 194
     H 20 194
     ...
     $end

:guilabel:`Grid` 参数类型：字符串
------------------------------------------------
默认值：Medium

可选值：Ultra Coarse、Coarse、Medium、Fine、Ultra Fine、SG1

指定DFT计算格点类型。
