不同基组扩展轨道 - EXPANDMO模块
================================================
EXPANDMO模块用于将小基组计算的MO扩展为大基组MO，扩展的MO可用于SCF的初始猜测，也可用于一些双基组(Dual Basis)的计算。此外，expandmo还可以利用原子价活性空间（atomic valance active space），自动构建MCSCF计算的活性空间和初始猜测轨道。

:guilabel:`Overlap` 参数类型：Bool型
------------------------------------------------
指定利用小基组与大基组的重叠积分扩展分子轨道。

Expandmo模块依赖文件如下：

+------------------+--------------------------+----------+----------+
| 文件名           | 描述                     | 文件格式 |          |
+------------------+--------------------------+----------+----------+
| $BDFTASK.chkfil1 | 小基组计算的Check文件    | 二进制   | 输入文件 |
+------------------+--------------------------+----------+----------+
| $BDFTASK.chkfil2 | 大基组计算的Check文件    | 二进制   | 输入文件 |
+------------------+--------------------------+----------+----------+
| inporb           | 小基组计算产生的MO文件   | 文本文件 | 输入文件 |
+------------------+--------------------------+----------+----------+
| $BDFTASK.exporb  | 扩展的MO系数文件，存储在 | 文本文件 | 输入文件 |
|                  | BDF_WORKDDIR中           |          |          |
+------------------+--------------------------+----------+----------+

.. code-block:: bdf

     #用cc-pVDZ基组计算CH2分子，并扩展分子轨道系数到aug-cc-pVDZ基组，用于SCF计算的初猜
     # First we perform a small basis set calculation by using CC-PVDZ.
     $COMPASS
     Title
       CH2 Molecule test run, cc-pvdz
     Basis
       cc-pvdz
     Geometry
     C     0.000000        0.00000        0.31399
     H     0.000000       -1.65723       -0.94197
     H     0.000000        1.65723       -0.94197
     End geometry
     UNIT
       Bohr
     Check
     $END

     $XUANYUAN
     $END

     $SCF
     RHF
     Occupied
     3  0  1  0
     $END

     #Change the name of check file.
     %mv $BDF_WORKDIR/ch2.chkfil $BDF_WORKDIR/ch2.chkfil1
     #Copy converged SCF orbital to work directory inporb.
     %mv $BDF_WORKDIR/ch2.scforb $BDF_WORKDIR/ch2.inporb

     # Then we init a large basis set calculation by using aug-CC-PVDZ
     $COMPASS
     Title
       CH2 Molecule test run, aug-cc-pvdz
     Basis
       aug-cc-pvdz
     Geometry
     C     0.000000        0.00000        0.31399
     H     0.000000       -1.65723       -0.94197
     H     0.000000        1.65723       -0.94197
     End geometry
     UNIT
       Bohr
     Check
     $END
