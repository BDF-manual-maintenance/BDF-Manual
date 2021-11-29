自洽场计算的其它技巧
=====================================

自洽场计算的初始猜测
------------------------------------------------
自洽场计算的初始猜测轨道，对计算的收敛性有很大的影响。BDF支持多种初始猜测，如下所示：

  * Atom : 利用原子密度矩阵组合分子密度矩阵猜测，默认选项。
  * Huckel : 半经验Huckel方法猜测；
  * Hcore : 对角化单电子哈密顿猜测；
  * Read  : 读入分子轨道做为初始猜测。

BDF默认的是Atom猜测。改变BDF的初始猜测，简洁输入模式下可以使用关键词 ``guess`` , 如下所示

.. code-block:: python

    #! ch3cho.sh
    HF/6-31G guess=Hcore unit=Bohr
    
    geometry    # notice: unit in Bohr 
    C       0.1727682300       -0.0000045651       -0.8301598059
    C      -2.3763311896        0.0000001634        0.5600567139
    H       0.0151760290        0.0000088544       -2.9110013387
    H      -2.0873396672        0.0000037621        2.5902220967
    H      -3.4601725077       -1.6628370597        0.0320271859
    H      -3.4601679801        1.6628382651        0.0320205364
    O       2.2198078005        0.0000024315        0.2188182082
    end geometry

这里，我们在第二行是用了关键词 ``guess=hore`` 指定使用 ``Hcore`` 猜测。SCF迭代了18次收敛。

.. code-block:: python

    Iter.   idiis  vshift       SCF Energy            DeltaE          RMSDeltaD          MaxDeltaD      Damping    Times(S) 
   1      0    0.000    -130.4887395291     174.6809293768       0.4015311621       5.3256687709    0.0000      0.03
   2      1    0.000    -115.5957867849      14.8929527443       0.4074026953       5.3238046781    0.0000      0.02
   3      2    0.000    -126.8237488344     -11.2279620496       0.1153005175       1.5916468002    0.0000      0.03
   4      3    0.000    -150.8706367857     -24.0468879513       0.0113947989       0.1548134263    0.0000      0.02
   5      4    0.000    -151.1218291697      -0.2511923840       0.0044983982       0.0378757845    0.0000      0.03
   6      5    0.000    -150.9001239894       0.2217051803       0.0084834364       0.1198652668    0.0000      0.02
   7      6    0.000    -151.5820061335      -0.6818821441       0.0118923459       0.1220639062    0.0000      0.02
   8      7    0.000    -152.4416568905      -0.8596507570       0.0079078878       0.0621137174    0.0000      0.03
   9      8    0.000    -152.7292298384      -0.2875729479       0.0033185298       0.0378846766    0.0000      0.02
  10      2    0.000    -152.7953749193      -0.0661450810       0.0059517726       0.0546256520    0.0000      0.02
  11      3    0.000    -152.8392767258      -0.0439018065       0.0008604884       0.0102102107    0.0000      0.03
  12      4    0.000    -152.8411314720      -0.0018547462       0.0007339517       0.0076787306    0.0000      0.02
  13      5    0.000    -152.8417529214      -0.0006214494       0.0003489373       0.0035199506    0.0000      0.02
  14      6    0.000    -152.8418162382      -0.0000633168       0.0000532884       0.0007875921    0.0000      0.03
  15      7    0.000    -152.8418191806      -0.0000029424       0.0000212068       0.0001575336    0.0000      0.02
  16      8    0.000    -152.8418195056      -0.0000003250       0.0000047962       0.0000316945    0.0000      0.02
  17      2    0.000    -152.8418195223      -0.0000000166       0.0000006987       0.0000054977    0.0000      0.03
  18      3    0.000    -152.8418195226      -0.0000000003       0.0000002363       0.0000022763    0.0000      0.02
 diis/vshift is closed at iter =  18
  19      0    0.000    -152.8418195227      -0.0000000000       0.0000000781       0.0000008485    0.0000      0.03

.. warning:: 
   这个算例分子输入坐标的单位是Bohr，必须使用关键词 ``unit=Bohr`` 指定坐标的长度单位为 ``Bohr`` 。

这个算例对应的高级输入为

.. code-block:: python

   $compass
   geometry
     C 0.1727682300 -0.0000045651 -0.8301598059
     C -2.3763311896 0.0000001634 0.5600567139
     H 0.0151760290 0.0000088544 -2.9110013387
     H -2.0873396672 0.0000037621 2.5902220967
     H -3.4601725077 -1.6628370597 0.0320271859
     H -3.4601679801 1.6628382651 0.0320205364
     O 2.2198078005 0.0000024315 0.2188182082
   end geometry
   skeleton
   unit # Set unit of length as Bohr
     bohr
   basis
     6-31g
   $end

   $xuanyuan
   direct
   maxmem
   512mw
   $end

   $scf
   rhf
   guess # ask for hcore guess
     hcore
   $end

读入初始猜测轨道
------------------------------------------------------------------------------------------
BDF的SCF计算默认采用原子计算密度矩阵构建分子密度矩阵的方式产生初始猜测轨道。实际在计算中，用户常读入已经收敛
的分子轨道，做为计算的初始猜测。这里，我们先计算一个中性的H2O分子，得到收敛轨道后，做为H2O+离子的初始猜测。

第一步，计算H2O分子, 准备输入文件，并命名为 ``h2o.inp`` , 内容如下：

.. code-block:: python

    #!bdf.sh
    RKS/B3lyp/cc-pvdz     
    
    geometry
    O
    H  1  R1
    H  1  R1  2 109.
    
    R1=1.0     # OH bond length in angstrom 
    end geometry

执行计算后，工作目录生成可读文件 ``h2o.scforb`` ，保存了SCF计算收敛的轨道.


第二步，利用H2O分子的收敛轨道做为H2O+离子的初始猜测, 准备输入文件 h2o+.inp, 内容如下：

.. code-block:: python

    #!bdf.sh
    ROKS/B3lyp/cc-pvdz guess=read charge=1
    
    geometry
    O
    H  1  R1
    H  1  R1  2 109.
    
    R1=1.0     # OH bond length in angstrom
    end geometry
    
    %cp $BDF_WORKDIR/h2o.scforb $BDF_TMPDIR/inporb


这里，使用了关键词 ``guess=read`` ，指定要读入初始猜测轨道。初始猜测轨道是用 ``%`` 引导的拷贝命令从
环境变量 ``BDF_WORKDIR`` 定义的文件夹中的h2o.scforb复制为 ``BDF_TMPDIR`` 中的 ``inporb`` 文件。
这里， ``BDF_WORKDIR`` 是执行计算任务的目录， ``BDF_TMPDIR`` 是BDF存储临时文件的目录。


扩展小基组收敛轨道为大基组初始猜测
------------------------------------------------
扩展小基组计算的收敛轨道为大基组的收敛轨道可以加速计算收敛，一般的，基组扩展应该采用同组的轨道，如cc-pVXZ系列的，ANO-RCC系列的等。
目前，不同基组的扩展轨道只支持BDF的高级输入模式。对于CH3CHO分子，先用cc-pVDZ计算，然后将轨道扩展为cc-pVQZ基组计算的初始猜测轨道，
输入如下：

.. code-block:: python

    # First SCF calcualtion using small basis set cc-pvdz
    $compass
    geometry
    C       0.1727682300       -0.0000045651       -0.8301598059
    C      -2.3763311896        0.0000001634        0.5600567139
    H       0.0151760290        0.0000088544       -2.9110013387
    H      -2.0873396672        0.0000037621        2.5902220967
    H      -3.4601725077       -1.6628370597        0.0320271859
    H      -3.4601679801        1.6628382651        0.0320205364
    O       2.2198078005        0.0000024315        0.2188182082
    end geometry
     skeleton
    basis
     cc-pvdz
    unit
     Bohr
    $end
     
    $xuanyuan
    direct
    $end
     
    $scf
    rhf
    $end
    
    #change chkfil name into chkfil1
    %mv $BDF_WORKDIR/$BDFTASK.chkfil $BDF_WORKDIR/$BDFTASK.chkfil1
    
    $compass
    geometry
    C       0.1727682300       -0.0000045651       -0.8301598059
    C      -2.3763311896        0.0000001634        0.5600567139
    H       0.0151760290        0.0000088544       -2.9110013387
    H      -2.0873396672        0.0000037621        2.5902220967
    H      -3.4601725077       -1.6628370597        0.0320271859
    H      -3.4601679801        1.6628382651        0.0320205364
    O       2.2198078005        0.0000024315        0.2188182082
    end geometry
     skeleton
    basis
     cc-pvqz
    unit
     Bohr
    $end
    
    #change chkfil name into chkfil1. notice, should use cp command since we will use "$BDFTASK.chkfil" in next calculation
    %cp $BDF_WORKDIR/$BDFTASK.chkfil $BDF_WORKDIR/$BDFTASK.chkfil2
    
    #copy converge SCF orbital as input orbital of the module expandmo
    %cp $BDF_WORKDIR/$BDFTASK.scforb $BDF_WORKDIR/$BDFTASK.inporb
    
    #Expand orbital to large basis set, output file is $BDFTASK.exporb
    $expandmo
    overlap
    $end
     
    $xuanyuan
    Direct
    $end
    
    #use expanded orbital as initial guess orbital
    %cp $BDF_WORKDIR/$BDFTASK.exporb $BDF_WORKDIR/$BDFTASK.scforb
    $scf
    RHF
    guess
     read
    iprtmo
     2
    $end

上面的输入中，先执行使用了cc-pVDZ基组第一个RHF计算，然后利用 expandmo 模块，将第一次SCF计算的收敛轨道扩展到cc-pVTZ基组，
最后做为利用 guess=read 做为SCF的要读入的初始猜测轨道。

expandmo模块的输出为，

.. code-block:: python

    |******************************************************************************|
    
        Start running module expandmo
        Current time   2021-11-29  22:20:50
    
    |******************************************************************************|
     $expandmo                                                                                                                                                                                                                                                       
     overlap                                                                                                                                                                                                                                                         
     $end                                                                                                                                                                                                                                                            
     /Users/bsuo/check/bdf/bdfpro/ch3cho_exporb.chkfil1
     /Users/bsuo/check/bdf/bdfpro/ch3cho_exporb.chkfil2
     /Users/bsuo/check/bdf/bdfpro/ch3cho_exporb.inporb
      Expanding MO from small to large basis set or revise ...
    
     1 Small basis sets
    
     Number of  basis functions (NBF):      62
     Maxium NBF of shell :        6
    
     Number of basis functions of small basis sets:       62
    
     2 Large basis sets
    
     Number of  basis functions (NBF):     285
     Maxium NBF of shell :       15
    
      Overlap expanding :                     1
     Read guess orb
     Read orbital title:  TITLE - SCF Canonical Orbital
    nsbas_small  62
    nsbas_large 285
    ipsmall   1
    iplarge   1
      Overlap of dual basis ...
      Overlap of large basis ...
     Write expanded MO to scratch file ...
    |******************************************************************************|
    
        Total cpu     time:          0.42  S
        Total system  time:          0.02  S
        Total wall    time:          0.47  S
    
        Current time   2021-11-29  22:20:51
        End running module expandmo
    |******************************************************************************|

可以看出，小基组有82个轨道，大基组有285个轨道，expandmo读入了SCF收敛的正则轨道，扩展到大基组并写入临时文件。

第二次SCF计算的输出为，

.. code-block:: python

    /Users/bsuo/check/bdf/bdfpro/ch3cho_exporb.scforb
    Read guess orb:  nden=1  nreps= 1  norb=  285  lenmo=  81225
    Read orbital title:  TITLE - orthognal Expand CMO
    Orbitals initialization is completed.
 
    ........

    Iter.   idiis  vshift       SCF Energy            DeltaE          RMSDeltaD          MaxDeltaD      Damping    Times(S) 
       1      0    0.000    -152.9529768928     122.5475220340       0.0022189851       0.2467358590    0.0000     16.30
       2      1    0.000    -152.9834628815      -0.0304859887       0.0003672457       0.0261961005    0.0000     16.83
       3      2    0.000    -152.9839760454      -0.0005131640       0.0000864297       0.0068568317    0.0000     17.18
       4      3    0.000    -152.9840120624      -0.0000360169       0.0000167630       0.0014729395    0.0000     17.02
       5      4    0.000    -152.9840197284      -0.0000076660       0.0000104007       0.0010127885    0.0000     17.42
       6      5    0.000    -152.9840217739      -0.0000020456       0.0000033965       0.0003281788    0.0000     17.28
       7      6    0.000    -152.9840221974      -0.0000004235       0.0000010821       0.0000759141    0.0000     17.40
       8      7    0.000    -152.9840222421      -0.0000000447       0.0000001542       0.0000086457    0.0000     17.28
       9      8    0.000    -152.9840222435      -0.0000000014       0.0000000663       0.0000050879    0.0000     19.38
     diis/vshift is closed at iter =   9
      10      0    0.000    -152.9840222436      -0.0000000001       0.0000000072       0.0000005845    0.0000     18.95
    
      Label              CPU Time        SYS Time        Wall Time
     SCF iteration time:       517.800 S        0.733 S      175.617 S





指定占据数计算激发态
------------------------------------------------


分子轨道最大重叠方法计算激发态
------------------------------------------------


处理自洽场计算的不收敛问题
------------------------------------------------


自洽场计算的加速算法
------------------------------------------------


