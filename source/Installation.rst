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

 * Fortran 编译器
    * gfortran 7.5 及以上, ifort 17 及以上, ifx 2024 及以上
 * C 编译器 (原则上完全支持 `C11 <http://www.open-std.org/jtc1/sc22/wg14/www/docs/n1548.pdf>`_ 并能够向后兼容至 `C17 <https://files.lhmouse.com/standards/ISO%20C%20N2176.pdf>`_)
    * gcc 4.8.5 及以上, icc 17 及以上, clang 5.0.0 及以上, icx 的任意版本, AppleClang 的任意版本
 * C++ 编译器 (原则上完全支持 `C++17 <https://wg21.link/std17>`_ 及以上)
    * g++ 8.1 及以上, clang++ 5.0.0 及以上, icpc 19.0.1 及以上, icpx 的任意版本, AppleClang 的任意版本
 * C++ 标准库/标准模板库 STL (原则上完全支持 `C++17 <https://wg21.link/std17>`_ 及以上. 原则上可以使用 GCC, LLVM, 及 Microsoft 对 STL 的实现)
    * GCC STL (也作 libstdc++ 或 glibcxx) 需要发行系列 8 及以上, LLVM STL (也作 libc++ 或 libcpp) 需要发行系列 16 及以上, MSVC STL 要求在 19.14 及以上
 * BLAS 及 LAPACK 数学库，需提供 64 位整数接口
    * 推荐使用由 Intel MKL, AMD ACML, OpenBLAS 等提供的 BLAS 及 LAPACK 实现
 * CMake 3.15 及以上
 * Python 3

可选配置：
 * 编译并行版本的 BDF, 需要 Openmpi 1.4.1 或以上版本
 * 编译 GPU 版的 BDF, 需要 OpenCL 1.5 或以上版本，以及 AMD 的 ROCm 或 Nvidia 的 CUDA

.. attention::

    Intel 并没有实现 STL. 根据平台, Intel 编译器将使用 GCC 或 Microsoft 的 STL 实现.

    Intel 编译器需要使用 GCC 或 MSVC 提供的基础设施. Intel 编译器不会为您检查并自动选择其所兼容的 GCC 和/或 MSVC 版本.
    您的 Intel 编译器所兼容的 GCC 和/或 MSVC 版本会在其 Release Note 中列出.

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

4. 编译BDFpro，并要求生成鸿之微License文件
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

.. note::

  若安装目录没有自动生成license文件夹，需手动创建。

.. _run-bdfpro:

5. Intel 编译器, 启用 C++14 功能, 链接 MKL 数学库, 支持 OpenMP 并行
---------------------------------------------------------------------

主要步骤同前面几种示例. 您需要使用最低支持 C++14 的编译器及 STL, 并在运行 setup 脚本时传入选项 ``ALLOW_CXX14``，如:

.. code-block:: shell

    $ ./setup --fc=ifort --cc=icc --cxx=icpc --cmake-options="-DALLOW_CXX14=YES" \
              --bdfpro --omp --int64 --mkl sequential build
    $ cd build
    $ make && make install

.. Note::
   1. 如需启用 C++17 或 C++20 标准请使用 ALLOW_CXX17 或 ALLOW_CXX20 选项
   2. 若您不传入这些允许启用高版本 C++ 标准的 CMake 选项, BDF 将在 C++11 标准下进行编译
   3. 传入选项如 ``ALLOW_CXX14=YES`` 仅仅 "允许" 更高 (高于 C++11) 的 C++ 标准被启用, 实际所用之标准取决于您的编译器. 因此, 即使在您的编译器及 STL 不支持 C++14 时使用 ``ALLOW_CXX14=YES`` 在原则上也不会引起编译错误
   4. BDF 中的部分功能要求使用 C++14 或更高标准进行编译. 若您不允许或您的编译器及/或 STL 不支持这些功能所要求的标准它们将被自动禁用
   5. Intel 编译器会使用由 GNU 编译器所提供的基础设施, 其中包含 STL. 但 Intel 编译器并非与所有版本的 GNU 编译器所提供的基础设施皆兼容, 详情参见您所用 Intel 编译器的发行说明
.. Hint::
   SecScf 模块 (提供二阶 SCF 功能) 要求使用最低 C++14, 建议使用 C++17, 标准进行编译. 您若希望使用该模块提供的功能请在运行 setup 脚本时传入 ``ALLOW_CXX17=YES``, CMake 将自动进行对您的编译器及 STL 进行功能测试, 若测试通过则 SecScf 将被自动启用

6. 在Mac OS平台编译BDF
---------------------------------------------------------------------

Intel MKL已经不支持，Mac平台，可以使用netlib的blas和lapack库替代MKL数学库。代码可以从https://www.netlib.org/lapack/index.html下载。需要注意的是，BDF的Fortran代码默认的整数长度为64位，netlib的数学库在编译时应默认开启64位整数支持。此外，BDF的部分代码基于C++开发，需要netlib的lapackc扩展库支持。

首先，编译netlib的lapack数学库。在lapack-3.10.0目录下，有一个示例文件make.inc.example，将其复制为make.inc，修改C及Fortran编译器和它们的编译参数，如下:

.. code-block::

    CC = gcc   
    CFLAGS = -O3 -m64 -DHAVE_LAPACK_CONFIG_H -DLAPACK_COMPLEX_STRUCTURE -DLAPACK_ILP64

    FC = gfortran
    FFLAGS = -O2 -frecursive -fdefault-integer-8
    FFLAGS_DRV = $(FFLAGS)
    FFLAGS_NOOPT = -O0 -frecursive -fdefault-integer-8

这里，CC和CFLAGS分别定义C编译器和C编译参数，FC和FFLAGS分别定义Fortran编译器及Fortran编译参数。在然后在lapack-3.12.1的主目录下执行make命令，编译陈成功后生成liblapack.a,librefblas.a和libtmglib.a三个文件，分别对应lapack库，blas库和tgmglib库。Netlib的lapack默认不编译BLAS和lapack的C接口，所以要分别进入CBLAS和LPACKE目录执行make命令，生成libcblas.a和liblapacke.a两个文件。

准备好blas和lapack库后，使用如下命令配置BDF，生成make文件

.. code-block:: shell

    # C, Fortran and C++ compiler
    $ export FC=gfortran
    $ export CC=gcc
    $ export CXX=g++

    # lib and include path for math libraries
    $ export LIBMATH="-L/Users/bsuo/Library/mathlib/lapack-3.12.1 -llapack -lrefblas -lcblas -llapacke"
    $ export INCMATH="-I/Users/bsuo/Library/mathlib/lapack-3.12.1/LAPACKE/include -I/Users/bsuo/Library/mathlib/lapack-3.12.1/CBLAS/include"

    # Generate make files
    $ ./setup --fc=${FC} --cc=${CC} --cxx=${CXX} --debug \
        --int64 --mathinclude-flags="${INCMATH}" \
        --mathlib-flags="${LIBMATH}" \
        --blasdir="/Users/bsuo/Library/mathlib/lapack-3.12.1" \
        --lapackdir="/Users/bsuo/Library/mathlib/lapack-3.12.1" \
        $1
    $ cd build
    $ make -j8 &>log&
    $ make -j8 install

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
    $ cp /home/user/bdf-pkg-pro/tests/easyinput/ch2-hf.inp test/
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
    
    #### Set the PATH to find your applications #####
    export BDFHOME=/home/bbs/bdf-pkg-pro
    
    # 指定BDF运行的临时文件存储目录
    export BDF_TMPDIR=/tmp/$RANDOM
    
    # 指定OpenMP的Stack内存大小
    export OMP_STACKSIZE=2G
    
    # 指定OpenMP可用线程数，应该等于ppn定义的数目
    export OMP_NUM_THREADS=4
    
    #### Do not modify this section ! #####
    $BDFHOME/sbin/bdfdrv.py -r jobname.inp



.. important::
    1. stacksize的问题。Intel Fortran编译器对程序运行的栈区（stack）内存要求较大，Linux系统默认的stacksize的大小通常太小，需要通过ulimit -s unlimited指定栈区内存大小。
    2. OpenMP并行的线程数。OMP_NUM_THREADS用于设定OpenMP的并行线程数。BDF依赖于OpenMP并行提高计算效率。如果用户使用了Bash Shell，可以用命令 ``export OMP_NUM_THREADS=N`` 指定使用N个OpenMP线程加速计算。其中N一般需要小于等于节点的物理核数。若用户没有使用作业管理系统，且同一个节点上已经跑了占用M个核的计算，则N一般需要小于物理核数减M。
    3. OpenMP可用栈区内存，用户可以用 ``export OMP_STACKSIZE=1024M`` 指定OpenMP每个线程可用的栈区内存大小，总的栈区内存大小为 ``OMP_STACKSIZE*OMP_NUM_THREADS`` 。
    4. 对于BDF商业版支持的大部分计算任务而言，当使用很多核并行计算时，程序使用的栈内存远多于堆内存，因此一般可只指定 ``OMP_STACKSIZE`` 而无需指定堆内存。但对于解析Hessian计算而言，堆内存往往占据程序消耗内存的大部分。2025年7月及之后的BDF版本允许用户调节堆内存，即在 ``resp`` 模块中用 ``maxmem`` 关键词指定（单位为GB，默认值32）。堆内存与栈内存之和必须小于节点总物理内存，考虑到内存估计的误差及同一个节点上的其他进程消耗的内存，建议小于节点总物理内存的80%。也即： ``OMP_STACKSIZE*OMP_NUM_THREADS + maxmem <= 物理内存*80%`` 。对于解析Hessian计算，建议 ``OMP_STACKSIZE*OMP_NUM_THREADS`` 为 ``maxmem`` 的1/3~1/10左右，但若这使得 ``OMP_STACKSIZE`` 小于1G，则设置 ``OMP_STACKSIZE=1G`` 。



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


安装和运行 (WSL)
************************************

总结
========================================================================================================================
通过适用于 Linux 的 Windows 子系统 (WSL), BDF (北京密度泛函程序) 可被安装至运行 Windows 操作系统的计算机上. 本文档记录了可分发的 BDF 镜像的构造及部署步骤. 构造可分发的 BDF 镜像是程序发布者的工作, 普通用户无需阅读关于镜像的构造部分的内容.

前提条件
========================================================================================================================
本文档假设您的计算机已

- 启用 WSL, 并已
- 更新 WSL 至一支持 WSL 2 的版本 (可选, 但强烈建议.)

.. note::

   -  WSL 的安装步骤可参见 `Install WSL \| Microsoft Learn <https://learn.microsoft.com/en-us/windows/wsl/install>`_.
   -  若要安装 WSL, 虚拟化技术必须被 (从 BIOS 或 UEFI 里) 启用. 要检查您的计算机是否已经启用虚拟化技术可查看 Windows 任务管理器 > 性能 > CPU > 虚拟化.
   -  我们推荐使用 WSL 2. 如果您想使用 WSL 1, 则需要执行一些未包含在当前版本的文档中的额外步骤. 您可以在 `ArchWSL Documentation <https://wsldl-pg.github.io/ArchW-docs/Known-issues/>`_ 中找到更多信息. WSL 1 同 WSL 2 的比较见 `Comparing WSL Versions \| Microsoft Learn <https://learn.microsoft.com/en-us/windows/wsl/compare-versions>`_.

创建 BDF 可分发镜像的步骤
========================================================================================================================

1. 将 BDF Distributable Blank 注册为一新的 WSL distro
------------------------------------------------------------------------------------------------------------------------

在 Windows PowerShell 中执行下面的命令

.. code:: powershell

    wsl --import BdfServer <InstallLocation> BdfDistributableBlank.vhdx --version 2 --vhd

或

.. code:: powershell

    wsl --import BdfServer <InstallLocation> BdfDistributableBlank.tar.gz --version 2

要确认新的 distro 以被成功注册可以运行下面的命令 ``wsl -l -v``.
您应期待类似下面的内容被打印至屏幕 (注意最后一行)

.. code:: console

    PS C:\Users\UserName> wsl -l -v
      NAME                   STATE           VERSION
    * Arch                   Running         2
      CentOS8                Stopped         2
      openSUSE               Stopped         2
      BdfServer              Stopped         2

.. note::
   -  BdfDistributableBlank 可从\ `此处 <https://github.com/AndBrn743/BdfDistributableBlank/releases>`__\ 获取.
   -  请将 ``<InstallLocation>`` 替换为真正的安装路径.
   -  您不一定需要将其命名为 ``BdfServer``.

2. 下载, 编译, 并安装 BDF
------------------------------------------------------------------------------------------------------------------------

2.1. 进入 BdfServer distro
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

在 Windows PowerShell 运行下面的命令

.. code:: powershell

   wsl -d BdfServer

现在您应进入 BdfServer distro 的一个Bash shell 实例

2.2. 进行系统更新 (可选)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

在 Linux Bash shell 中执行

.. code:: bash

   pacman -Syyu

并按照屏幕上的指示操作

.. note::
   -  您可在 `ArchLinux wiki <https://wiki.archlinux.org/title/Pacman>`_ 上阅读关于 ``pacman`` 的更多信息

2.3. 下载或复制 BDF 源文件至 BdfServer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

在 Linux 的Bash shell 运行下面的命令

.. code:: bash

   git clone user_name@server:/path/to/bdf-pkg

如,

.. code:: bash

   git clone user_name@182.92.69.169:/opt/gitroot/bdf-pkg

或

.. code:: bash

   cp /mnt/windows/path/to/bdf-pkg.tar.gz .

如,

.. code:: bash

   cp /mnt/d/data/bdf-pkg.tar.gz .

如果 ``bdf-pkg.tar.gz`` 可以在 Windows 下的路径 ``D:\data\bdf-pkg.tar.gz`` 中被找到

2.4. 编译并安装 BDF
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

BDF Distributable Blank (BDF) 自带一 ``compile_and_install_bdf`` 脚本. 在 Linux Bash shell 中运行 ``compile_and_install_bdf`` 便可自动使用 BDB 捆绑的线性代数库编译 BDF 并将 BDF 安装至一合适的路径下. 若 BDF 的源代码所在文件夹为 ``bdf-pkg`` 且位于当前工作目录或当前用户的 home 路径下, 则您仅需运行下面的命令:

.. code:: bash

   compile_and_install_bdf

您也可以将 BDF 源代码所在的自定义路径作为 ``compile_and_install_bdf`` 的第一个命令行参数传给它, 如

.. code:: bash

   compile_and_install_bdf /custom/path/to/bdf/source/files

额外的 build flags 也可被直接传给 ``compile_and_install_bdf``, 如

.. code:: bash

   compile_and_install_bdf -DENABLE_LICENSE=YES -DONLY_BDFPRO=YES

.. note::

   -  请用管理员权限运行 ``compile_and_install_bdf`` 脚本
   -  ``compile_and_install_bdf`` 脚本不支持自定义安装路径. 将 BDF 安装至非默认路径将导致捆绑的 BDF 运行脚本 ``bdf`` 不可用
   -  在编译和安装完成后 ``compile_and_install_bdf`` 将询问您是否希望删除编译路径, 源代码所在文件夹, 及 pacman 缓存. 除非您有特殊原因, 否则请全部选择 ``Y``

2.5. 清理
^^^^^^^^^^^^^^^^^^

-  删除 BDF 编译文件夹, 若尚未删除
-  删除 BDF 源代码文件夹, 若尚未删除
-  删除 pacman 的全部缓存文件, 若尚未删除 (执行 ``pacman -Scc`` 并对所有选择都选择 ``Y``)
-  删除 IDE 及代码编辑器 (如, Visual Studio, Visual Studio Code, CLion, Rider, 及 PyCharm) 的缓存文件及文件夹, 若您曾将它们连接至 ``BdfServer``
-  删除其它临时文件及文件夹

3. 产生可分发镜像
------------------------------------------------------------------------------------------------------------------------

3.1. 关闭所有连接至 ``BdfServer`` 了的所有 Windows 程序, 其中包括但不限于 ``conhost.exe``, Windows Terminal, Windows File Explorer, Visual Studio, 及 Visual Studio Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3.2. 将 WSL 置于关机状态
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

在 Windows PowerShell 运行下面的命令

.. code:: powershell

   wsl --shutdown

.. attention::
   -  仅运行 ``wsl -t BdfServer`` 据我们的经验无法达到相同的效果, 您的结果可能与我们不同
   -  ``BdfServer`` 可以被连接至其的 Windows 程序重新启动, 若如此将影响下一步

3.3. 导出 BDF 可发布镜像
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3.3.1. 导出 tar 格式的可分发镜像
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

请在 Windows PowerShell 中运行下面的命令

.. code:: powershell

   wsl --export BdfServer BdfServer.tar.gz

输出文件 ``BdfServer.tar.gz`` 就是可分发镜像

3.3.2. 导出 virtual disk (vhdx) 格式的可分发镜像
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

请在 Windows PowerShell 中运行下面的命令

.. code:: powershell

   wsl --export BdfServer BdfServer.vhdx --vhd

输出文件 ``BdfServer.vhdx`` 就是可分发镜像

部署可分发镜像的步骤
========================================================================================================================

在将可分发镜像部署在用户计算机上时需运行下面的 Windows PowerShell 命令

.. code:: powershell

   wsl --import BdfServer <InstallLocation> BdfServer.tar.gz --version 2

或

.. code:: powershell

   wsl --import BdfServer <InstallLocation> BdfServer.vhdx --version 2 --hvd

.. note::

   -  请将 ``<InstallLocation>`` 替换为真正的安装路径.
   -  您不一定需要将其命名为 BdfServer.
   -  由此, 用户便可正常使用 BDF. 然而, 我们强烈建议用户在 ``BdfServer`` 添加一非 root 账户并将该账户设为默认登录账户. 该步骤的指南可参见\ `此处 <https://wsldl-pg.github.io/ArchW-docs/locale/zh-CN/How-to-Setup/#%E5%AE%8C%E6%88%90%E5%AE%89%E8%A3%85%E5%90%8E%E7%9A%84%E6%93%8D%E4%BD%9C>`__.

常用命令
========================================================================================================================

-  若需通过 PowerShell 来间接运行一个 BdfServer 上的命令, 如, ``htop``,
   可以使用下面的命令

.. code:: powershell

   wsl -d BdfServer htop

-  若需通过 PowerShell 来在当前 Windows 路径下运行一个
   BdfServer上的命令, 如 ``ls``, 可以使用下面的命令

.. code:: powershell

   wsl -d BdfServer ls

-  若需通过 PowerShell 来在一给定 Linux 路径 (如 ``~/tasks``) 下运行一个
   BdfServer 上的命令可使用下面的命令

.. code:: powershell

   wsl -d BdfServer --cd ~/tasks ls

-  如需将当前 Windows 路径下的文件复制或剪切至 BdfServer上的某一路径 (如
   ``~/tasks``) 可使用下面的 Windows PowerShell 命令

.. code:: powershell

   wsl -d BdfServer cp MyWindowsFile.txt ~/tasks/

或

.. code:: powershell

   wsl -d BdfServer mv MyWindowsFile.txt ~/tasks/

-  如需将 BdfServer 路径, 如 ``~/tasks``, 下的某一文件复制或剪切至当前
   Windows 路径可使用下面的 Windows PowerShell 命令

.. code:: powershell

   wsl -d BdfServer cp ~/tasks/MyLinuxFile.txt .

或

.. code:: powershell

   wsl -d BdfServer mv ~/tasks/MyLinuxFile.txt .

-  欲在一 Windows 路径下运行 BDF 计算任务可以使用下面的命令

.. code:: powershell

   wsl -d BdfServer bdf BdfCalculationInputFile.inp

-  如需使用 Windows File Explorer 来打开某一 BdfServer 路径, 如
   ``~/tasks``, 可执行下面的 Windows PowerShell 命令

.. code:: powershell

   wsl -d BdfServer --cd ~/tasks/ explorer.exe .

.. attention::

   根据 WSL 的版本不同直接在 Windows 路径下直接执行 BDF 计算可能是, 也可能不是一个好的方案. 对 WSL 1 来说, 如此行没有任何问题. 对 WSL2 来说, 由于 Windows 和 WSL 文件系统间的 IO 操作很慢, 使得此举不优. 因此, 对 WSL 2 来说, 我们建议 将BDF 输入文件复制至 BdfServer 的文件系统内并在 BdfServer 的文件系统内执行计算. 用于在 Windows 和 WSL 文件系统间进行文件复制和剪切的命令在上文已给出.

备注
========================================================================================================================

-  BDF Distributable Blank (BDB) 是一类似于可分发的 BDF WSL 镜像 (BDI). 它们的区别在于 BDB 上没有安装 BDF, 其上装有的是编译和安装 BDF 所需的依赖库及软件. 因此 BDB 的文件大小远远小于 BDI 且可被重用数年 (我们仍然建议每年更新 BDB 一次), 而 BDI 文件很大且每次 BDF 更新时都应被完全替换.
-  由于可分发镜像中不仅包含 BDF 且包含它的依赖项, 可分发镜像文件的的大小可达 10 GB. 分发者应合理选择分发介质.
