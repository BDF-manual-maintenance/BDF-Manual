安装和运行
************************************

.. attention::

   普通用户不需要阅读安装和编译有关的内容，可以直接跳到 :ref:`BDF程序运行<run-bdfpro>` 和 :ref:`BDF图形界面<run-bdfgui>` 。


安装说明
================================================

硬件环境
-------------------------------------------------
原则上说，BDF可以在任何Unix和类Unix操作系统上进行编译安装。我们已经在一些常见的软硬件环境下进行了编译测试，
对于其他硬件平台，由于操作系统和编译器版本的限制和缺陷，用户可能会遇到一些问题。
绝大多数况下，用户根据自己的硬件环境，设置正确的编译器标志和系统软件路径等，最终可以成功编译安装BDF软件。

要编译BDF软件，至少需要 2 GB 的可用磁盘空间，具体取决于您的安装方式（例如，CMake 保留目标文件），
编译后的实际大小约为 1.3 GB。要运行BDF的测试算例，应该提供至少 1 GB 的磁盘空间用于缓存计算的中间数据，
具体需要的缓存空间取决于计算体系大小和使用的积分方式（采用积分直接算法需要的磁盘空间远小于传统的存储双电子积分的模式）。通常来说，对于采用积分直接算法的计算，应当提供4 GB以上的磁盘空间用于数据缓存。

软件环境配置
------------------------------------------------------------------------

从BDF的源代码直接编译安装，对于编译器和数学库的最低要求是：

 * Fortran编译器（支持Fortran 95及以上版本的语法）
 * C++ 编译器（支持C++03及以上版本的语法）
 * C 编译器
 * BLAS/LAPACK 数学库，接口需为64位整数
 * CMake 3.15版本及以上（使用cmake进行编译）
 * Python 2.7及以上版本。Python 2与Python 3不兼容，Python 3目前还未完全适配
 
通常使用GCC 4.6及以上的版本即可正常编译。

可选配置：
 * Intel Parallel Studio XE Cluster版C/C++、Fortran编译器
 * 优化的BLAS/LAPACK 库（如Intel的MKL，AMD的ACML，OpenBLAS等）
 * 编译并行版本的BDF，需要Openmpi 1.4.1或以上版本
 * 编译GPU版的BDF，需要OpenCL 1.5或以上版本，以及AMD的Rocm或Nvidia的Cuda

cmake编译BDF
==========================================================================

1. Intel Fortran编译器、GNU gcc/g++编译器混合使用，链接MKL数学库，支持OpenMP并行
--------------------------------------------------------------------------------

.. code-block:: shell

    # 设置编译器
    $ export FC=ifort
    $ export CC=gcc
    $ export CXX=g++
    # cmake由setup命令自动执行
    $ ./setup --fc=${FC} --cc=${CC} --cxx=${CXX} --bdfpro --omp --int64 --mkl sequential $1
    # 在build目录下构建BDF
    $ cd build
    # 使用make命令编译BDF，利用-j4参数指定使用4个CPU并行编译 
    $ make -j4
    # 安装BDF
    $ make install
    # 将build下bdf-pkg-pro复制至任意路径后，在bdfrc中写入正确路径，如：
    $ BDFHOME=/home/user/bdf-pkg-pro
    # 运行命令
    $ $BDFHOME/sbin/bdfdrv.py -r **.inp

2. GNU编译器gfortran/gcc/g++，链接MKL数学库，支持OpenMP并行
-------------------------------------------------------------------

.. code-block:: shell

    # 设置编译器
    $ export FC=gfortran
    $ export CC=gcc
    $ export CXX=g++
    # cmake由setup命令自动执行
    $ ./setup --fc=${FC} --cc=${CC} --cxx=${CXX} --bdfpro --omp --int64 --mkl sequential $1
    # 在build目录下构建BDF
    $ cd build
    # 使用make命令编译BDF，利用-j4参数指定使用4个CPU并行编译 
    $ make -j4
    # 安装BDF
    $ make install
    # 将build下bdf-pkg-pro复制至任意路径后，在bdfrc中写入正确路径，如：
    $ BDFHOME=/home/user/bdf-pkg-pro
    # 运行命令
    $ $BDFHOME/sbin/bdfdrv.py -r **.inp

3. Intel编译器ifort/icc/icpc，链接MKL数学库，支持OpenMP并行
-------------------------------------------------------------------

.. code-block:: shell

    # 设置编译器
    $ export FC=ifort
    $ export CC=icc
    $ export CXX=icpc
    # cmake由setup命令自动执行
    $ ./setup --fc=${FC} --cc=${CC} --cxx=${CXX} --bdfpro --omp --int64 --mkl sequential $1
    # 在build目录下构建BDF
    $ cd build
    # 使用make命令编译BDF，利用-j4参数指定使用4个CPU并行编译 
    $ make -j4
    # 安装BDF
    $ make install
    # 将build下bdf-pkg-pro复制至任意路径后，在bdfrc中写入正确路径，如：
    $ BDFHOME=/home/user/bdf-pkg-pro
    # 运行命令
    $ $BDFHOME/sbin/bdfdrv.py -r **.inp

.. Warning::
   1. gcc编译器9.0及以上版本，与Intel Fortran编译器混合使用，链接程序出错，原因是Intel Fortran编译器的OpenMP版本落后于GNU编译器。因而，GNU 9.0及以上版本编译器目前不支持GNU与Intel编译器混合编译。
   2. Intel Fortran 2018版编译器Bug较多，应避免使用。

4  编译BDFpro，并要求生成鸿之微License文件
-------------------------------------------------------------------

主要步骤同前面3种情况，在运行setup命令时，需要加入参数 ``--hzwlic``，如：

.. code-block:: bdf

    #cmake由setup命令自动执行
    $./setup --fc=${FC} --cc=${CC} --cxx=${CXX} --bdfpro --hzwlic --omp --int64 --mkl sequential $1

在运行完安装命令 ``make install`` 后，最后会给出如下的输出：

.. code-block:: bdf

    Please run command '/home/bsuo/bdf-pkg-pro/bdf-pkg-pro/bin/hzwlic.x /home/bsuo/bdf-pkg-pro/build/bdf-pkg-pro' to generate Hongzhiwei license!

这里， ``/home/bsuo/bdf-pkg-pro`` 是BDFpro源文件目录， ``/home/bsuo/bdf-pkg-pro/build/bdf-pkg-pro`` 是BDFpro的二进制代码安装目录。运行命令：

.. code-block:: bdf

    /home/bsuo/bdf-pkg-pro/bdf-pkg-pro/bin/hzwlic.x /home/bsuo/bdf-pkg-pro/build/bdf-pkg-pro

后，目录 ``/home/bsuo/bdf-pkg-pro/build/bdf-pkg-pro/license`` 中，生成文件 **LicenseNumber.txt** 。


.. _run-bdfpro:

程序运行
==========================================================================

BDF需在Linux终端下运行。运行BDF，需要先准备输入文件，输入文件的具体格式在手册后几节详述。
在BDF安装目录的tests/input下包含了一些BDF输入算例。这里我们利用BDF自带的测试算例作为例子，先简述如何运行BDF。

运行BDF会使用一些环境变量：

+---------------------+---------------------------------------------------+----------------------+
|环境变量             | 说明                                              |  是否必须设置        |
+---------------------+---------------------------------------------------+----------------------+
|BDFHOME              | 指定BDF的安装目录                                 | 是                   |
+---------------------+---------------------------------------------------+----------------------+
|BDF_WORKDIR          | BDF的工作目录，即当前任务的执行目录               | 否，自动设置         |
+---------------------+---------------------------------------------------+----------------------+
|BDF_TMPDIR           | 指定BDF的缓存文件存储目录                         | 是                   |
+---------------------+---------------------------------------------------+----------------------+
|BDFTASK              | BDF的计算任务名，如果输入为h2o.inp, 任务名为 h2o  | 否，自动设置         |
+---------------------+---------------------------------------------------+----------------------+

单机运行BDF，用Shell脚本执行作业
---------------------------------------------
假设用户目录为 /home/user，BDF被安装在 /home/user/bdf-pkg-pro中。准备好输入文件 ``ch2-hf.inp`` 之后，需要再准备一个shell脚本，输入如下内容

.. code-block:: shell

    #!/bin/bash

    export BDFHOME=/home/user/bdf-pkg-pro
    export BDF_WORKDIR=./
    export BDF_TMPDIR=/tmp/$RANDOM

    ulimit -s unlimited
    ulimit -t unlimited

    export OMP_NUM_THREADS=4
    export OMP_STACKSIZE=512M 

    $BDFHOME/sbin/bdfdrv.py -r $1

并命名为run.sh，利用 "chmod +x run.sh" 赋予脚本执行权限，然后按照如下方法执行。 

.. code-block:: shell

    # 在/home/user中新建一个文件夹test
    $ mkdir test
    $ cd test
    # 拷贝/home/user/bdf-pkg-pro/tests/easyinput/ch2-hf.inp到test文件夹
    $ cp /home/user/bdf-pkg-pro/tests/easyinput/ch2-hf.inp
    # 在test目录中运行提交命令
    $ ./run.sh ch2-hf.inp &> ch2-hf.out&

.. hint::
    BDF将输出打印至标准输出，需要用重定向命令 ``>`` 定向到文件ch2-hf.out中。

利用PBS作业管理系统提交BDF作业
------------------------------------------------

PBS提交BDF作业的脚本示例如下：

.. code-block:: shell

    #!/bin/bash
    #PBS -N jobname
    #PBS -l nodes=1:ppn=4
    #PBS -l walltime=1200:00:00
    #PBS -q batch
    #PBS -S /bin/bash
    
    #### Set the environment variables #######
    #module load tools/openmpi-3.0.1-intel-socket

    #module load compiler/intel-compiler-2020
    
    #### Set the PATH to find your applications #####
    export BDFHOME=/home/bbs/bdf-pkg-pro
    
    # 指定BDF运行的临时文件存储目录
    export BDF_TMPDIR=/tmp/$RANDOM
    
    # 指定OpenMP的Stack内存大小
    export OMP_STACKSIZE=2G
    
    # 指定OpenMP可用线程数，应该等于ppn定义的数目
    export OMP_NUM_THREADS=4
    
    #### Do not modify this section ! #####
    cd $PBS_O_WORKDIR
    
    $BDFHOME/sbin/bdfdrv.py -r jobname.inp


利用Slurm作业管理系统提交BDF作业
------------------------------------------------

Slurm提交BDF作业的脚本示例如下：

.. code-block:: shell

    #!/bin/bash
    #SBATCH --partition=v6_384
    #SBATCH -J bdf.slurm
    #SBATCH -N 1
    #SBATCH --ntasks-per-node=48

    
    #### Set the environment variables #######
    #module load tools/openmpi-3.0.1-intel-socket
    #module load compiler/intel-compiler-2020
    
    #### Set the PATH to find your applications #####
    export BDFHOME=/home/bbs/bdf-pkg-pro
    
    # 指定BDF运行的临时文件存储目录
    export BDF_WORKDIR=./
    export BDF_TMPDIR=/tmp/$RANDOM
    
    # 指定OpenMP的Stack内存大小
    export OMP_STACKSIZE=2G
    
    # 指定OpenMP可用线程数，应该等于ppn定义的数目
    export OMP_NUM_THREADS=4
    
    #### Do not modify this section ! #####
    $BDFHOME/sbin/bdfdrv.py -r jobname.inp



.. important::
    1. stacksize的问题。Intel Fortran编译器对程序运行的堆区（stack）内存要求较大，Linux系统默认的stacksize的大小通常太小，需要通过ulimit -s unlimited指定堆区内存大小。
    2. OpenMP并行的线程数。OMP_NUM_THREADS用于设定OpenMP的并行线程数。BDF依赖于OpenMP并行提高计算效率。如果用户使用了Bash Shell，可以用命令 ``export OMP_NUM_THREADS=N`` 指定使用N个OpenMP线程加速计算。
    3. OpenMP可用堆区内存，用户可以用 ``export OMP_STACKSIZE=1024M`` 指定OpenMP每个线程可用的堆区内存大小，总的堆区内存大小为 ``OMP_STACKSIZE*OMP_NUM_THREADS`` .



QM/MM计算环境配置
-------------------------------------------------
.. _qmmmsetup:

推荐使用Anaconda管理和配置QM/MM计算环境（ `详见官网 <https://www.anaconda.com>`_ ）。

*  在anaconda中配置运行环境

.. code-block:: shell

  conda create –name yourEnvname python=2.7
  conda activate yourEnvname
  #配置Cython和PyYAML
  conda install pyyaml #或者 pip install pyyaml
  conda install cython 

*  pDynamo-2的安装与配置

BDF中pDynamo-2已经内置于安装目录的sbin目录下，在sbin目录下依次运行如下命令进行安装和配置：

.. code-block:: shell

  cd pDynamo_2.0.0
  cd installation
  python ./install.py

安装脚本运行后，会生成 environment_bash.com，environment_cshell.com两个环境配置文件。用户可以在自己的 ``.bashrc`` 通过source加载这个
环境文件，设置运行环境。

.. note::

  编译过程会自动选择C编译器，对于MAC系统，建议使用 ``homebrew`` 安装GCC编译器，并添加 CC=gcc-8。其它版本的gcc编译器分别对应 gcc-6 或者 gcc-7等。
  高于gcc-8版本目前没有测试。 

pDynamo-2运行时，默认调用sbin目录下的 ``qmmmrun.sh`` 文件进行QM计算。环境配置时，需要确保sbin目录在系统PATH中。
可以用如下命令添加。

.. code-block:: shell

  export PATH=/BDFPATH/sbin:$PATH

*  最后一步，指定BDF程序临时文件存储文件夹，可以运行如下命令指定，也可以将该变量设置在环境变量中。

.. code-block:: shell
  
  export PDYNAMO_BDFTMP=YourBDF_tmpPATH

若要检测pDynamo是否正确安装，可以运行软件自带的算例进行检测，算例文件位于 **pDynamo_2.0.0/book/examples** 目录中，
可以运行以下命令测试：

.. code-block:: shell

  python RunExamples.py
