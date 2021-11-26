安装和运行
************************************

安装说明
================================================

硬件环境
-------------------------------------------------
一般来说，BDF可以在任何unix操作系统上进行编译安装，我们也已经在一些常见的软硬件环境下进行了编译测试。对于其他硬件平台，由于操作系统和编译器版本的问题，用户可能会遇到一些问题。绝大多数况下，根据自己的硬件环境，设置正确的编译器标志和系统软件路径等，最终可以成功编译安装BDF软件。

要编译BDF软件，至少需要 2 GB 的可用磁盘空间，具体取决于您的安装方式（例如，CMake 保留目标文件），编译后的实际大小约为 1.3 GB。要运行BDF的测试例，应该提供至少 1 GB 的磁盘空间用于缓存计算的中间数据，具体需要的缓存空间取决于计算体系大小和使用的积分方式（采用积分直接算法需要的磁盘空间远小于传统的存储双电子积分的模式）。通常来说，对于采用积分直接算法的计算，应当提供4 GB以上的磁盘空间用于数据缓存。

软件环境配置
------------------------------------------------------------------------

从BDF的源代码直接编译安装，对于编译器和数学库的最低要求是：

 * Fortran编译器（支持fortran95及更新版本的语法）
 * C++ 编译器（支持C++03及更新版本的语法）
 * C 编译器
 * BLAS/LAPACK 数学库
  
通常使用GCC 4.6及以上的版本即可正常编译。

可选配置：
 * Intel Parallel Studio XE Cluster版C/C++ Fortran编译器
 * CMake 2.8.11版本及以上（使用cmake进行编译）
 * 优化的BLAS/LAPACK 库（如Intel的MKL，AMD的ACML，OpenBLAS等）
 * openmpi 1.4.1版本及以上（编译并行版本的BDF）


.. _1.1 配置编译BDF:

配置编译BDF
==========================================================================

------------------------------------------------------------------------------------------------------------------------------------------------------------------

以Linux下Bash Shell为例，所有操作均在BDF的主目录:


.. _1.1.1 Intel Fortran、C/C++编译器及MKL数学库:

Intel Fortran、C/C++编译器及MKL数学库
------------------------------------------------------

------------------------------------------------------------------------------------------------------------------------------------------------------------------



.. code-block:: shell

    #设置编译器
    $export FC=ifort
    $export CC=icc
    $export CXX=icpc
    #设置数学库
    $export MATHLIB=”-lmkl_intel_ilp64 -lmkl_sequential -lmkl_core”
    $export MATHINCLUDE=”-I/opt/intel/mkl/include”
    #配置BDF，产生Makefile
    $./configure --enable-mkl=yes --enable-openmp=yes --enable-i8=yes
    #编译BDF
    $make 

.. _ 1.1.2 Intel Fortran编译器，gcc/g++编译器，MKL数学库:

Intel Fortran编译器，gcc/g++编译器，MKL数学库
------------------------------------------------------

------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. code-block:: shell

    #设置编译器
    $export FC=ifort
    $export CC=icc
    $export CXX=g++
    #设置数学库
    $export MATHLIB=”-lmkl_intel_ilp64 -lmkl_sequential -lmkl_core”
    $export MATHINCLUDE=”-I/opt/intel/mkl/include”
    #配置BDF，产生Makefile
    $./configure --enable-mkl=yes --enable-openmp=yes --enable-i8=yes
    #编译BDF
    $make 

.. _ 1.1.3 GNU的Fortran编译器gfortran，gcc/g++编译器，Netlib的Blas和Lapack数学库:

GNU的Fortran编译器gfortran，gcc/g++编译器，Netlib的Blas和Lapack数学库
------------------------------------------------------

------------------------------------------------------------------------------------------------------------

.. code-block:: shell

    #设置编译器
    $export FC=gfortran
    $export CC=icc
    $export CXX=g++
    #设置数学库
    $export MATHLIB=”-L/home/bsuo/lapack-3.8.0 -llapack -lblas -lcblas -llapacke”
    $export MATHINCLUDE=”-I/home/bsuo/lapack-3.8.0/LAPACKE/include -I/home/bsuo/lapack-3.8.0/CBLAS/include”
    #配置BDF，产生Makefile
    $./configure --enable-mkl=no --enable-openmp=yes --enable-i8=yes
    #编译BDF
    $make 

.. _ 1.2 cmake编译BDF-GTO:


cmake编译BDF-GTO
==========================================================================

------------------------------------------------------------------------------------------------------------



.. _ 1.2.1 Intel Fortran编译器，gcc/g++编译器，MKL数学库:

Intel Fortran编译器，gcc/g++编译器，MKL数学库
------------------------------------------------------

------------------------------------------------------------------------------------------------------------

.. code-block:: shell

    #设置编译器
    $export FC=ifort
    $export CC=icc
    $export CXX=g++
    #cmake由setup命令自动执行
    $./setup --fc=${FC} --cc=${CC} --cxx=${CXX} --bdfpro --int64 --mkl sequential $1
    #在build目录下构建BDF
    $cd build 
    $make
    #安装BDF
    $make install
    #将build下bdf-pkg-pro复制至任意路径后，在bdfrc中写入正确路径，如：
    $BDFHOME=/home/user/bdf-pkg-pro
    #运行命令
    $$BDFHOME/sbin/bdfdrv.py -r **.inp

.. _ 1.3 程序运行:


程序运行
==========================================================================

------------------------------------------------------------------------------------------------------------

BDF需要在Linux终端下运行。运行BDF，需要先准备输入文件。输入文件的具体格式在手册后几节详述。这里我们利用BDF自带的测试算例作为例子，先简述如何运行BDF。
假设用户目录为 /home/user, BDF被安装在 /home/user/bdf-pkg-pro中。准备好输入文件 ``ch2-hf.inp`` 之后，按照如下方法执行。 

.. code-block:: shell

    #在/home/user中新建一个文件夹test
    $mkdir test
    $cd test
    #拷贝/home/user/bdf-pkg-pro/tests/easyinput/ch2-hf.inp到test文件夹
    $cp /home/user/bdf-pkg-pro/tests/easyinput/ch2-hf.inp
    #在test目录中运行提交命令
    $$BDFHOME/sbin/bdfdrv.py -r **.inp



