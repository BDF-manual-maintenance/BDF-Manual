常见问题
************************************

**重启中断的计算任务？**
  BDF支持一部分常见任务的断点续算，包括：
   1. SCF单点能：利用 ``guess`` 关键词读取中断的任务的最后一步SCF迭代的分子轨道作为初猜即可。具体而言，只需在$scf模块中加入

.. code-block:: bdf

  guess
   readmo

并且重新运行该输入文件即可。

   2. TDDFT单点能：原则上，当TDDFT任务中断，且idiag不等于2时，可以读取该任务最后一步TDDFT迭代（当idiag=1时为Davidson迭代，当idiag=3时为iVI迭代）的TDDFT激发矢量作为初猜。不过需要注意的是：（1）这样节省的TDDFT迭代次数比同等条件下SCF断点续算节省的迭代次数要少，因此除非之前已经中断的那个任务的TDDFT迭代已经接近收敛，否则断点续算可能并不比从头计算节省迭代次数；（2）TDDFT默认不将迭代当中的TDDFT激发矢量保存到硬盘，必须指定iguess为1、11或21才能将迭代当中的TDDFT激发矢量保存到硬盘。如果此前中断的计算没有包含该关键词，则无法进行断点续算。

TDDFT任务断点续算的方式是：在$scf模块里用 ``guess`` 关键词读取被中断的任务的收敛的SCF波函数，并在$tddft模块里用 ``iguess`` 指定读取被中断的任务的TDDFT激发矢量。To be done

   3. 结构优化：在$compass模块中加入 ``restart`` 关键词即可，具体参见 :doc:`compass` 小节。
   4. 数值频率计算：To be done

**BDF如何引用？**
  | 使用BDF首先要引用BDF程序的原文 :cite:`doi:10.1007/s002140050207,doi:10.1063/1.5143173,doi:10.1142/S0219633603000471,doi:10.1142/9789812794901_0009` 。除此以外，使用BDF的不同功能还应当同时引用对应方法的文章，参见 :doc:`Cite` 小节。

**TDDFT计算的虚频问题(imaginary frequencies)?**
  xxxxxxxxxx

**TDDFT的J、K算符可用内存与计算效率**
   memjkop

**内存**
  xxxxxxxxxx

**2018编译器**
  xxxxxxxxxx

**Openmp并行**
  xxxxxxxxxx

**SCF不收敛**
  参见 :doc:`SCFTech` 章节。
