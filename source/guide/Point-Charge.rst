
点电荷模型
================================================
BDF支持将MM区原子电荷作为点电荷输入进行计算。点电荷以与计算任务同名的 ``$BDFTASK.extcharge`` 文件作为输入，具体格式如下：

.. code-block:: bdf

  $COMPASS
  Title
  water molecule in backgroud of exteral charges
  Basis
    6-31g
  Geometry
  O   0.000000   0.000000   0.106830
  H   0.000000   0.785178  -0.427319
  H   0.000000  -0.785178  -0.427319
  End Geometry
  Extcharge  #表示需要输入点电荷
    point      #表示输入电荷类型为点电荷
  $END
  
  $XUANYUAN
  $END

  $SCF
  RHF
  $END

点电荷输入文件（文件名 h2o.extcharge）如下：

.. code-block:: bdf

    External charge, Point charge   #第一行为标题和说明行
    6                               #要输入的点电荷数 
    C1     -0.732879     0.000000     5.000000     0.114039 
    C2      0.366440     0.000000     5.780843    -0.456155 
    C3      0.366440     0.000000     4.219157    -0.456155
    C4     -0.732879     0.000000     10.00000     0.114039 
    C5      0.366440     0.000000     10.78084    -0.456155 
    C6      0.366440     0.000000     9.219157    -0.456155

点电荷的默认输入格式为:  原子标签、  电荷、 和坐标\（ x\  y\  z）\  ; 坐标单位默认为埃。坐标输入单位也可以为Bohr，输入格式如下：

.. code-block:: bdf

    External charge, Point charge   # title line
    6    Bohr                       # Unit: Bohr  
    C1     -0.732879     0.000000     5.000000     0.114039 
    #     省略 # 


.. 本小节结束
