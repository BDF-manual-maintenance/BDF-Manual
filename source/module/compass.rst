compass模块
================================================
Compass模块主要完成计算任务的初始化工作，包括读入用户定义的分子结构、基组等基本信息，判断分子的对称性及其分子点群，产生对称匹配的轨道等，并将其转换为BDF内部的数据存储起来。Compass模块的主要参数有：

:guilabel:`Basis` 参数类型：字符串
----------------------------------------------
指定计算所用的基组名称。BDF基组存储在$BDFHOME/basis_library中，当前计算任务中所有原子的基组应被放置在本参数指定的文件中。由于基组通过本参数指定的文件读入，用户可以通过自定义基组（见自定义基组说明）文件为不同原子指定不同的基组。

 .. code-block:: python

     $Compass
     Basis
     cc-pVDZ
     Geometry
     H   0.00  0.00   0.707
     H   0.00  0.00   -0.707
     End of Geometry
     $End

:guilabel:`RI-J/RI-K/RI-C` 参数类型：字符串
---------------------------------------------
指定RI(Resolution of Identity)计算的冗余基组。RI-J：库伦拟合，RI-K：交换拟合基组，RI-C：相关拟合基组。

 .. code-block:: python

     $Compass
     Basis
     DEF2-SVP
     RI-J
     DEF2-SVP
     Geometry
     H   0.00  0.00   0.707
     H   0.00  0.00   -0.707
     End of Geometry
     $End

:guilabel:`Geometry` 参数类型：字符串数组
---------------------------------------------
指定计算的分子结构，可以是直角坐标模式，也可以是内坐标模式。分子坐标的定义从Geometry参数下一行开始，以End of Geometry前一行结束。

