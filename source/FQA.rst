常见问题
************************************

**重启中断的计算任务？**
=================================

BDF支持一部分常见任务的断点续算，包括：
  
1. SCF单点能：用 ``guess`` 关键词读取中断任务的最后一步SCF迭代的分子轨道作为初猜。具体而言，只需在$scf模块中指定初猜为 ``readmo`` ，并且重新运行该输入文件即可。

  .. code-block:: bdf

    $scf
    ...
    guess
     readmo
    $end


2. TDDFT单点能：当TDDFT任务中断，且idiag不等于2时，可以读取该任务最后一步TDDFT迭代（当idiag=1时为Davidson迭代，当idiag=3时为iVI迭代）的TDDFT激发矢量作为初猜。其中当idiag=3时，只有采用C(1)对称性的计算允许断点续算。

   TDDFT任务断点续算的方式是：在$scf模块里用 ``guess`` 关键词读取被中断的任务的收敛的SCF波函数，并在$tddft模块里用 ``iguess`` 指定读取被中断的任务的TDDFT激发矢量。假设输入文件为

   .. code-block:: bdf
   
     $scf
     ...
     $end
     
     $tddft
     ...
     iguess
      21
     $end

   其中iguess=21的十位数2表示选择tight-binding初始猜测（但这对于这个例子而言不是必要的，也就是说以下的讨论对iguess=1或iguess=11也是适用的），而个位数1表示将每步的TDDFT激发矢量写到文件（当idiag=1时，激发矢量保存在后缀为.dvdsonvec*的文件中；当idiag=3时，激发矢量保存在后缀为.tdx的文件中）。如该任务中断，断点续算的方法为将该输入文件改成：

   .. code-block:: bdf
   
     $scf
     ...
     guess
      readmo
     $end
     
     $tddft
     ...
     iguess
      11 # or 10, if the user is sure that the job will not be interrupted again
     $end

   其中 ``guess readmo`` 是为了读取之前SCF迭代的轨道，从而避免浪费时间重新进行SCF迭代；而iguess=11的十位数1表示从.dvdsonvec*或.tdx文件内读取TDDFT激发矢量作为初猜。关于iguess各种取值的意义，详见 :doc:`tddft` 小节。

   需要注意的是：（1）由于Davidson和iVI方法的特点，以上方法节省的TDDFT迭代次数比同等条件下SCF断点续算节省的迭代次数要少，因此除非之前已经中断的那个任务的TDDFT迭代已经接近收敛，否则断点续算可能并不比从头计算节省迭代次数；（2）TDDFT默认不将迭代当中的TDDFT激发矢量保存到硬盘，必须指定iguess为1、11或21才能将迭代当中的TDDFT激发矢量保存到硬盘。如果此前中断的计算没有包含该关键词，则无法进行断点续算。之所以程序没有默认保存每步的激发矢量，主要是因为这样导致的硬盘读写时间可能不可忽略，因此用户在执行计算时需要权衡是否需要指定保存激发矢量。

3. 结构优化：在$compass模块中加入 ``restart`` 关键词即可，具体参见 :doc:`compass` 小节。
4. 数值频率计算：在$bdfopt模块中加入 ``restarthess`` 关键词即可，具体参见 :doc:`bdfopt` 小节。

**BDF如何引用？**
=================================

使用BDF首先要引用BDF程序的原文 :cite:`doi:10.1007/s002140050207,doi:10.1063/1.5143173,doi:10.1142/S0219633603000471,doi:10.1142/9789812794901_0009` 。除此以外，使用BDF的不同功能还应当同时引用对应方法的文章，参见 :doc:`Cite` 小节。

**TDDFT计算的虚激发能/复激发能问题**
=================================================================

如果基态波函数不稳定或者SCF收敛得到的态并非真正的基态，TDDFT计算会提示出现虚激发能, 极少情况下甚至出现复激发能。虚激发能和复激发能无物理意义。当使用Davidson方法时，程序会给出警告**Warning: Imaginary Excitation Energy!**，并在迭代收敛后给出所有虚/复激发能的模；当使用iVI方法时，程序会给出警告**Error in ETDVSI: ABBA mat is not positive! Suggest to use nH-iVI.**，且后续计算不会尝试继续求解虚/复激发能，而是只求解实激发能（因此当使用iVI方法时，不能仅根据最终收敛的激发能全部是实数就断定体系不存在虚/复激发能的激发态）。这时，应重新优化基态波函数，寻找稳定的解，或采用TDA计算激发能。

**TDDFT的J、K算符可用内存与计算效率**
=================================================================

如果TDDFT计算要求解的根的数目较多，程序默认的内存不够，造成TDDFT计算效率降低。TDDFT模块的关键词 **MEMJKOP** 可用来设置TDDFT计算J、K算符时最大可用内存。例如要求计算 **4** 个根，TDDFT给出了如下输出：

.. code-block:: bdf

     Maximum memory to calculate JK operator:        1024.000 M
     Allow to calculate    2 roots at one pass for RPA ...
     Allow to calculate    4 roots at one pass for TDA ...

提示计算JK算符最大可用内存为 **1024M** ，这里的单位是兆字节（MB），如果是RPA（即TDDFT）计算，每次积分计算允许算2个根，TDA计算允许算4个根。如果用户要求的是TDA计算，一次积分计算将得到所有根的JK算符，RPA计算需要将积分计算两次，计算效率降低。可以设置 ``MEMJKOP`` 为2048MB，增加内存使得每步迭代只需计算一次积分。注意，实际用到的物理内存大约是 **2048MB*OMP_NUM_THREADS** ，即需要乘以OpenMP线程的数目。

**计算出现segmentation fault与可用stack区内存**
=================================================================

BDF计算如果出现 **segmentation fault** ，大多数情况下都是用户可用的stack区内存不够造成的，Linux系统下，可通过命令 **ulimit** 设置可用stack区内存大小。

首先输入命令：

.. code-block:: bdf 

  $ulimit -a

输出提示如下：

.. code-block:: bdf

    core file size          (blocks, -c) 0
    data seg size           (kbytes, -d) unlimited
    scheduling priority             (-e) 0
    file size               (blocks, -f) unlimited
    pending signals                 (-i) 256378
    max locked memory       (kbytes, -l) 64
    max memory size         (kbytes, -m) unlimited
    open files                      (-n) 4096
    pipe size            (512 bytes, -p) 8
    POSIX message queues     (bytes, -q) 819200
    real-time priority              (-r) 0
    stack size              (kbytes, -s) 4096 
    cpu time               (seconds, -t) unlimited
    max user processes              (-u) 256378
    virtual memory          (kbytes, -v) unlimited
    file locks                      (-x) unlimited

这里的 ``stack size              (kbytes, -s) 4096`` 表示用户可用的stack区内存大小为4096KB，只有4兆，可通过命令

.. code-block:: bdf

    ulimit -s unlimited

设置用户可用stack区内存大小不受限。很多Linux发行版都对stack区内存有限制。严格的说，stack区内存限制大小分为 **硬上限** 和 **软限制** ，普通用户仅有权限设置小于 **硬上限** 的stack区内存。如果 ``ulimit -s unlimited`` 提示错误，

.. code-block:: bdf

    $ulimit -S
    -bash: ulimit: stack size: cannot modify limit: Operation not permitted

需要用root账户更改可用stack区的内存 **硬上限** 或者联系您的系统管理员解决问题。

**OpenMP并行计算**
=================================================================

BDF支持OpenMP并行计算，需要在运行脚本中设置可用的OpenMP线程数目，如下：

.. code-block:: bdf

    export OMP_NUM_THREADS=8

这里设置最大可用8个OpenMP线程并行计算。

**OpenMP的stack区内存大小**
=================================================================

Intel编译器可用stack区内存，特别是使用OpenMP并行计算时，intel编译器将并行区的动态内存放入stack区以获得较高的计算效率。因而，用户需要在BDF的运行脚本中设置OpenMP可用stack区内存大小，如下：

.. code-block:: bdf

    export OMP_STACKSIZE=2048M

这里设置了OpenMP每个线程可用堆区(Stack)内存大小为2048MB. 注意： 如果使用OpenMP做多线程并行，系统使用的总堆区内存为 **OMP_STACKSIZE*OMP_NUM_THREADS** 。

.. important::
  环境变量OMP_STACKSIZE是通用环境变量，与其它OpenMP运行库的特殊环境变量之间存在覆盖关系：

  KMP_STACKSIZE（Intel OpenMP） > GOMP_STACKSiZE（GNU OpenMP） > OMP_STACKSIZE

  因此如果在脚本中设置了优先级更高的环境变量，会覆盖OMP_STACKSIZE的值。

**Intel 2018版Fortran编译器**
=================================================================

Intel 2018版的Fortran编译器Bug较多，编译BDF应避免使用该版本的编译器。


**SCF不收敛**
=================================================================

参见 :doc:`SCFTech` 章节的 :ref:`处理自洽场计算的不收敛问题<SCFConvProblems>` 小节。

**SCF能量远低于预期值（较预期值低1 Hartree以上），或SCF能量显示为一串星号**
=============================================================================

一般是基组线性相关问题导致的。参见 :doc:`SCFTech` 章节的 :ref:`处理自洽场计算的不收敛问题<SCFConvProblems>` 小节关于基组线性相关问题的讨论。注意虽然该章节主要讨论的是基组线性相关问题导致SCF不收敛的问题的解决方法，但是这些方法对于基组线性相关问题仅导致SCF能量错误、而并未导致不收敛的情形也是适用的。

**如何使用自定义基组**
=================================================================

参见 :doc:`Gaussian-Basis-Set` 里的 :ref:`自定义基组文件<SelfdefinedBasis>` 小节。
