mrci模块
================================================
MRCI模块与DRT模块联用，执行非收缩的MRCI计算。

:guilabel:`Nrroots` 参数类型：整型
------------------------------------------------
指定MRCI计算的根的数目。

:guilabel:`PrintThresh` 参数类型：整型
------------------------------------------------
默认值：0.05

指定打印输出的CSF的阈值。

:guilabel:`Convergence` 参数类型：浮点型数组
------------------------------------------------
默认值：1.D-8、1.D-6、1.D-8

指定MRCI计算的收敛阈值。输入三个浮点数，分别控制MRCI的迭代大的能量、波函数和残余向量收敛阈值。

:guilabel:`Maxiter` 参数类型：整型
------------------------------------------------
指定MRCI计算最大迭代次数。

:guilabel:`Cipro` 参数类型：整型
------------------------------------------------
指定计算单电子约化密度矩阵即相关的性质，如偶极矩等。

