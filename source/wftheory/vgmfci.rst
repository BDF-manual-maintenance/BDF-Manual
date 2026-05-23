振动广义平均场方法  - VGMFCI 模块
=======================================================================
VGMFCI模块执行双原子分子的振动广义平均场理论。该方法利用Kratz势的本征函数做为振动波函数基矢，执行非绝热的振动-电子耦合计算。

**基本控制参数**

:guilabel:`Emethod` 类型: 字符串
------------------------------------------------
指定电子结构计算方法，可选方法为: SCF, MCSCF和MRCI。
对于MCSCF方法，并不优化分子轨道，只执行CASCI计算。


:guilabel:`Nstate` 类型: 整数
-----------------------------------------------
指定要打印并分析的振动-电子耦合态数目。

.. code-block:: bdf

   $COMPASS 
   Title
     H2 Molecule. vgmfci example 
   Basis
    cc-pvdz
   Geometry
    H 0.000  0.000    0.70018162
    H 0.000  0.000   -0.70018162
    X 0.000  0.000    0.80018162
    X 0.000  0.000   -0.80018162
    X 0.000  0.000    0.60018162
    X 0.000  0.000   -0.60018162
   End geometry
   Check
   Unit
    Bohr
   nosymm
   Kratzer
   # maxnu maxj ngausslag re         de
    10   0   50 1.40036324  0.365148     
   $END
   
   $XUANYUAN
   #masspol
   $END
   
   $vgmfci
   emethod
    mcscf  # scf mrci
   maxiter
    1
   Nstate
    20
   $end
   
   $SCF
   RHF
   checklinear
   tollin
    1.d-6
   $END
   
   $MCSCF
   close
    0
   actele
    2
   spin
    1
   roots
    1 40 
   CASCI
   mcvgmfci
   #diagcimat
   $END

 
