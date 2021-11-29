xuanyuan模块
================================================
Xuanyuan模块主要计算单、双电子积分和其他必要的积分并存储到文件中。

:guilabel:`Direct` 参数类型：Bool型
--------------------------------------
指定使用积分直接的SCF（Direct）计算。

积分直接的SCF不存储双电子积分，按照Schwartz不等式，结合积分对Fock矩阵的贡献，对积分计算进行预筛选，对基函数数目大于约300的计算，可以有效的利用双电子积分重复计算来避免IO操作，且支持OpenMP的多核并行计算。BDF中大多数需要计算Fock-Like矩阵（J与K矩阵）的模块，如SCF，TDDFT等都已经实现了积分直接计算。

.. note::

    积分直接的SCF计算，需要在compass模块中加上 :ref:`Skeleton<compass.skeleton>` 关键词。

.. code-block:: python

     $xuanyuan
     Direct
     $end

:guilabel:`Maxmem` 参数类型：Bool型
--------------------------------------
指定非积分直接的SCF双电子积分计算缓存大小。大的缓存可以减少积分排序的次数。输入格式为数字+MW或数字+GW，1 Word=2 Byte， 因此512MW就等于1024MB。

.. code-block:: python
    
     $xuanyuan
     Maxmem
       512MW
     $end

:guilabel:`RS` 参数类型：浮点型
--------------------------------------
指定Range-Speration泛函如CAM-B3LYP等的系数。建议值：0.33，如果DFT使用了Range-Speration泛函，必须加入此参数。

.. code-block:: python
    
     $xuanyuan
     RS
       0.33
     $end
     $scf
       dft
         cam-b3lyp
     $end

:guilabel:`Scalar` 参数类型：Bool型
--------------------------------------------
指定利用无自旋（Spin-free）的哈密顿考虑相对论效应，该参数须与Heff联用。

:guilabel:`Heff` 参数类型:整型
-------------------------------------------------
 * 默认值：2
 * 可选值：1、2、3/4、5、21、22、23

指定相对论哈密顿，如果只输入了Scalar，未加Heff，则默认是sf-X2C哈密顿。

.. code-block:: python
    
     $xuanyuan
     Scaler
     Heff
       3
     $end

:guilabel:`Soint` 参数类型：Bool型
---------------------------------------------------
指定计算自旋轨道（SOC）耦合积分，需与Hsoc联用。

:guilabel:`Hsoc` 参数类型:整型
----------------------------------------------------
 * 可选值：0、1、2、3、4、5

指定SOC积分类型。

.. code-block:: python
    
     $xuanyuan
     Soint
     Hsoc
       1
     $end

:guilabel:`Nuclear&Inuc` 参数类型：Bool型&整数
---------------------------------------------------
 * 默认值：0
 * 可选值：0、1

指定原子核电荷分布模型。0为点电荷模型；1为高斯电荷模型。

:guilabel:`Cholesky` 参数类型:字符串+浮点数
----------------------------------------------------
 * 可选值：S-CD、1c-CD

指定对双电子积分做Cholesky分解，设置Cholesky分解的方法及阈值。

.. code-block:: python
    
     $xuanyuan
     Cholesky
       S-CD 1.D-5
     $end
