简洁输入关键词
===============================

:guilabel: `方法/泛函/基组` 或 `泛函/基组` 参数类型: Bool，必选参数
----------------------------------------------------
设定计算方法、DFT/TDDFT计算的泛函和基组

计算方法列表

+---------------------+-----------------------------------------------------------------+
| 方法                | 功能             |
+---------------------+-----------------------------------------------------------------+
| HF                 | Hatree-Fock      |
| RHF                | restricted Hatree-Fock |
| UHF                | Unrestricted Hartree-Fock |
| ROHF               | Restricted open-shell Hatree-Fock |
| KS                 | Kohn-Sham |
| RKS                | Restricted Kohn-Sham |
| UKS                | Unrestricted Kohn-Sham |
| TDDFT              | Time dependent density functional theory |
| TDA                | Tamm-Dancoff Approximation |
| X-TDDFT            | Extended spin-adapted TDDFT |
| X-TDA              | Extended spin-adapted TDA   |
| TDDFT-SOC          | TDDFT with spin-orbit coupling |
| TDA-SOC            | TDA with spin-orbit coupling    |
| X-TDDFT-SOC        | Extended spin-adapted TDDFT with spin-orbit coupling |
| X-TDA-SOC          | Extended TDA with SOC |
| TDDFT-NAC          | TDDFT with non-adabatic coupling |
| TDA-NAC            | TDA with non-adabatic coupling |
| X-TDDFT-NAC        | X-TDDFT with non-adabatic coupling |
| X-TDA-NAC          | X-TDA with non-adabatic coupling |
| MP2                | Mollor-Plesset second order perturbation theory |
| RI-MP2             | MP2 using Resolution of Identity |
+--------------------+------------------------------------------------------------------+


**哈密顿和自旋轨道耦合**

:guilabel:`hamilton` 参数类型: 字符串，可选参数
----------------------------------------------------
设定计算的相对论哈密顿

默认值: nonrel， 相对论基组时 sf-X2C

可选值: sf-X2C, sf-X2C-AXR, sf-X2C-AU


:guilabel:`SOC` 参数类型: Bool，可选参数
------------------------------------------------
要求进行自旋轨道耦合(SOC)计算，并设置相应的SOC算符。如果计算方法是TDDFT，进行基于TDDFT的SOC计算；方法是TDA，则进行基于TDA的SOC计算。

默认值: DKH1e+mf1c

可选值: DKH1e+mf1c, DKH1e, BP; 全电子用DKH1e+mf1c，相对论有效势用BP算符。

.. note::

  * 默认原则: 如果指定哈密顿，BDF将根据基函数选择合适的哈密顿。对于考虑了相对论优化的全电子基组或非相对论全电子基组，对spin-free项采用 **sf-X2C** 哈密顿，自旋轨道耦合算符采用 **DHK1e+mf1c** ，用户可以强行设置为 **DHK1e**, 对于轻元素会有较大的误差。对于相对论有效势及基组，有效势已经考虑了相对论效应，无需设置哈密顿，SOC算符默认为BP。
  * 如果用户的输入为 `TDDFT/泛函/基组 SOC`， 使用了SOC关键词，等价于在方法中设置 `X-TDDFT/泛函/基组` , 哈密顿和SOC算符将按照默认原则设置。
..

**坐标单位，电荷和自旋多重度**

:guilabel:`unit` 参数类型: 字符串，可选参数
------------------------------------------------
原子坐标单位

默认值: angstrom

可选值: angstrom, Bohr

:guilabel:`spinmult` 参数类型: 整数，可选参数
------------------------------------------------
自旋多重度， `2S+1`

默认值: 偶数电子体系，1； 奇数电子体系，2


:guilabel:`charge` 参数类型: 整数，可选参数
------------------------------------------------
电荷数

默认值: 0

**自旋匹配的TDDFT和TDA**

:guilabel:`SpinAdapt`
------------------------------------------------
设置对进行自旋匹配的TDDFT或TDA， `TDDFT/泛函/基组 SpinAdapt` 等价于 `X-TDDFT/泛函/基组` 或X-TDA。 只对开壳层体系有意义，

**非绝热耦合**

:guilabel:`NAC` 参数类型: Bool，可选参数
------------------------------------------------
基于含时密度泛函(TDDFT)的非绝热耦合计算(NAC)

默认值: False


**势能面与结构优化**

:guilabel:`opt` 参数类型: Bool，可选参数
------------------------------------------------
稳定点分子几何结构优化。

默认值: False

:guilabel:`opt+freq` 参数类型: Bool，可选参数
------------------------------------------------
稳定点分子几何结构优化，随后进行频率计算。

默认值: False


:guilabel:`ts+freq` 参数类型: Bool，可选参数
------------------------------------------------
过度态优化，随后进行频率计算。

默认值: False


:guilabel:`freq` 参数类型: Bool，可选参数
------------------------------------------------
频率计算。

默认值: False

:guilabel:`scan` 参数类型: Bool，可选参数
------------------------------------------------
分子势能面扫描，需配合内坐标输入使用。

默认值: False

:guilabel:`scan+opt` 参数类型: Bool，可选参数
------------------------------------------------
分子势能面柔性扫描，即固定某些内坐标参量，优化其他坐标参量，需配合内坐标输入使用。

默认值: False


**加速算法**

:guilabel:`MPEC+COSX`, 参数类型: Bool，可选参数 
------------------------------------------------
利用 `Multipole expansion of Coulomb potential - MPEC` 及 `Chain-Of-Sphere Exchange - cosx` 加速 `SCF`、 `TDDFT` 能量及梯度计算。

默认值: False


:guilabel:`RI`, 参数类型: Bool，可选参数 
------------------------------------------------
利用RI加速 `SCF`、 `TDDFT`或 `MP2` 计算，需要配合RI基组使用。

默认值: False

.. Tips::
  * RI在BDF中主要用于加速MP2计算，SCF和TDDFT均可用 MPEC+COSX方法，该方法是BDF特有的加速算法，即不需要冗余基组，和RI算法的精度类似。

