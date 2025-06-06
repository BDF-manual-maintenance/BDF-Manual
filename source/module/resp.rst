DFT/TDDFT梯度及响应性质 - RESP模块
================================================
resp模块用于计算DFT/TDDFT的梯度，TDDFT理论级别下的非绝热耦合矩阵元（包括基态-激发态之间的非绝热耦合矩阵元，和激发态-激发态之间的非绝热耦合矩阵元），以及激发态偶极矩等响应性质。

**基本关键词**

:guilabel:`Iprt` 参数类型：整型
------------------------------------------------
控制打印输出级别，主要用于程序调试。

:guilabel:`NOrder` 参数类型：整型
------------------------------------------------
 * 默认值：1
 * 可选值：0、1、2

几何坐标导数的阶数，可选值0、1和2。目前仅支持0和1，其中0表示计算不涉及对核坐标求导的响应性质，如激发态偶极矩；1表示计算解析梯度。尚不支持2（计算解析 Hessian）。本参数要求必须先设置Geom。

:guilabel:`Geom` 参数类型：Bool型
------------------------------------------------
本关键词无需提供参数，需要与Norder关键词联用，用于指定计算几何坐标一阶或二阶导数。

可选值：1.梯度或fo-NACMEs；2.Hessian

:guilabel:`NFiles` 参数类型：整型
------------------------------------------------
对于TD-DFT响应性质计算，指定读取哪个$tddft块的计算结果；注意当该参数等于x时，并不简单代表读取第x个$tddft块的计算结果，而是指读取istore值为x的那个$tddft块的计算结果。例如对于某闭壳层分子的以下输入（$compass、$xuanyuan、$scf略去）：

.. code-block:: bdf

     $tddft
     imethod
     1
     Nroot
     1
     istore
     1
     $end

     $tddft
     imethod
     1
     isf
     1
     Nroot
     1
     istore
     2
     $end

     $resp
     geom
     imethod
     2
     nfiles
     2            #计算最低三重激发态的梯度，而不是最低单重激发态的梯度
                  #因为nfiles=2，而只有第2个$tddft块（最低三重激发态）的istore=2
     $end

:guilabel:`Imethod` 参数类型：整型
------------------------------------------------
 * 默认值：1
 * 可选值：1、2

指定进行DFT基态计算还是TD-DFT激发态计算。1为基态，如指定2，则为激发态计算。在较老的BDF版本中该关键词写作Method，目前程序既支持Imethod也支持Method，但是未来可能会只支持前者。

.. code-block:: bdf

     #计算第一个TD-DFT激发态的TD-DFT梯度
     $tddft
     Nroot
     1
     istore
     1
     $end

     $resp
     geom
     imethod
     2
     nfiles
     1
     $end

.. code-block:: bdf

     #计算基态梯度
     $resp
     geom
     $end

:guilabel:`Ignore` 参数类型：整型
------------------------------------------------
 * 默认值：0
 * 可选值：-1、0、1

用于TDDFT梯度计算的数据一致性检查，主要用于调试程序。

-1：重新计算TDDFT的激发能，用于检查Resp和TDDFT模块对能量计算是否一致。仅供调试程序使用。

0: 检查Wmo矩阵是不是对称矩阵。理论上，Wmo矩阵应该是对称矩阵，但如果TDDFT或者Z-Vector迭代没有完全收敛，Wmo矩阵会表现出明显的不对称，此时程序报错退出，并告诉用户Wmo矩阵不对称的较可能原因是TDDFT没有完全收敛还是Z-Vector方程求解没有完全收敛。注意有时Wmo矩阵不对称也可能是用户某些关键词输入错误导致的。

1: 忽略Wmo矩阵对称性检查。仅当用户确认其设置的TDDFT和Z-vector收敛阈值足够严，不会对计算结果精度造成不可接受的影响，且输入文件各关键词输入正确，但程序仍然因对称性检查不通过而报错时，才应将ignore设置为1。

:guilabel:`IRep` & :guilabel:`IRoot` 参数类型：整型
-----------------------------------------------------
这两个关键词指定计算哪个/哪些态的TD-DFT梯度或激发态偶极矩。分4种情况：

a.	既指定IRep，又指定IRoot：如以下的输入

.. code-block:: bdf

     #计算第2个不可约表示（irrep）下的第3个根的梯度或偶极矩
     irep
     2
     iroot
     3

b.	只指定IRep：计算该不可约表示下的所有根的梯度或偶极矩。

c.	只指定IRoot：例如

.. code-block:: bdf

     #将所有不可约表示下计算的根按照能量从低到高排序，然后计算第3个根的梯度或偶极矩
     iroot
     3
     
d.	两者都不指定：计算tddft得到的所有态的梯度或偶极矩。

:guilabel:`JahnTeller` 参数类型：字符串
------------------------------------------------
对于具有一定对称性的分子，如果分子所属点群是高阶点群，则TDDFT结构优化可能会导致分子出现Jahn-Teller畸变，但畸变方向可能有多个。例如，假设一个具有Ih对称性的分子有一个三重简并的激发态T2g，则该态发生Jahn-Teller畸变后，几何结构的对称性可能会降低为D2h，D3d，D5d或这些群的子群。
因此在TDDFT结构优化中，从第二步优化开始分子结构的对称性可能会降低。
当Jahn-Teller畸变得到的点群不唯一时，可以用JahnTeller关键词指定具体的Jahn-Teller畸变方式。例如：

.. code-block:: bdf

     $resp
     ...
     JahnTeller
      D(2h)
     $End
   
上例指定当存在Jahn-Teller畸变且畸变方式不唯一时，优先选择畸变后结构属于D2h群的畸变方式。如果由群论可以推出该分子在当前电子态下不会发生Jahn-Teller畸变，或虽然会发生Jahn-Teller畸变但不会得到属于D2h群的结构，则程序会打印警告信息，并忽略用户输入。
如果当前分子会发生Jahn-Teller畸变，但用户没有指定JahnTeller关键词，则程序会在Jahn-Teller畸变时尽量保持分子的高阶对称轴。仍以上述Ih群的T2g态为例，若不指定JahnTeller关键词，则分子会畸变为D5d结构，因为只有这样才能保持Ih群的五重对称轴。

:guilabel:`Line` 参数类型：Bool型
------------------------------------------------
执行resp进行线性响应计算。

:guilabel:`Quad` 参数类型：Bool型
------------------------------------------------
指定resp进行二次响应计算。

:guilabel:`Fnac` 参数类型：Bool型
------------------------------------------------
指定resp计算一阶非绝热耦合（first-oder noadibatic couplings）向量，需要与Single或者Double参数联用，分别指定计算基态-激发态、激发态-激发态非绝热耦合向量。

:guilabel:`Single` 参数类型：Bool型
------------------------------------------------
指定计算基态-激发态非绝热耦合向量。

:guilabel:`States` 参数类型：整型数组
------------------------------------------------
指定计算哪些态与基态的非绝热耦合向量。本参数是多行参数：

第一行：输入整数n, 指定要计算基态与n个激发态之间的非绝热耦合向量。

第二行至第n+1行，指定电子态，格式为 m i l 三个整数，m为先前的TDDFT计算istore指定存储的文件编号，i为第i个不可约表示，l是该不可约表示的第l个根。

:guilabel:`Double` 参数类型：Bool型
------------------------------------------------
指定计算激发态-激发态非绝热耦合向量。

:guilabel:`Pairs` 参数类型：整型数组
------------------------------------------------
指定计算哪两组激发态之间的非绝热耦合向量。本参数是多行参数：

第一行：输入整数n, 指定要计算n对激发态之间的非绝热耦合向量。

第二行至第n+1行，指定电子态，格式为 m1 i1 l1 m2 i2 l2 六个整数，每三个整数指定一个激发态。m1为先前的TDDFT计算istore指定存储的文件编号，i1为第i1个不可约表示，l1是该不可约表示的第l1个根。另三个整数同理。

:guilabel:`Noresp` 参数类型：Bool型
------------------------------------------------
指定在Double和FNAC计算中忽略跃迁密度矩阵的响应项。推荐使用该关键词。

:guilabel:`Grid` 参数类型：字符串
------------------------------------------------
 * 默认值：Medium
 * 可选值：Ultra Coarse、Coarse、Medium、Fine、Ultra Fine

指定DFT计算的格点类型。

:guilabel:`Gridtol` 参数类型：浮点型
------------------------------------------------
 * 默认值：1.0E-6（对于meta-GGA为1.0E-8）
 
 指定产生DFT自适应格点的截断阈值。该值越低，格点数越多，因此数值积分精度越高，但计算量也越大。

:guilabel:`MPEC+COSX` 参数类型：Bool型
------------------------------------------------
指定利用多级展开库伦势（Multipole expansion of Coulomb potential, MPEC）方法计算J矩阵， COSX（Chain-of-sphere exchange）方法计算K矩阵。
在 ``resp`` 模块中保留该关键词只是为了向下兼容，建议在 ``Compass`` 模块中设定该关键词。

:guilabel:`Solneqlr` 参数类型：Bool型
------------------------------------------------
指定进行线性响应非平衡溶剂化效应计算。

:guilabel:`Soleqlr` 参数类型：Bool型
------------------------------------------------
指定进行线性响应平衡溶剂化效应计算。

:guilabel:`Solneqss` 参数类型：Bool型
------------------------------------------------
指定进行态特定非平衡溶剂化效应计算。

:guilabel:`Soleqss` 参数类型：Bool型
------------------------------------------------
指定进行态特定平衡溶剂化效应计算。



