算例说明
************************************

算例下载链接 :download:`input.zip <files/input.zip>`

示例1：计算SCF能量梯度、结构优化。算例下载链接 :download:`test003.zip <files/test003.zip>`

.. code-block:: python

     $COMPASS 
     Title
      H2O Molecule test run, cc-pvdz
     Basis
     #3-21G
     cc-pvdz
     Geometry
     O  0.000000000   0.000000000    0.369372944
     H  0.000000000  -0.783975899   -0.184686472 
     H  0.000000000   0.783975899   -0.184686472 
     End geometry
     Check
     $END

     $XUANYUAN
     $END

     $SCF
     RHF              #Restricted Hartree-Fock
     Occupied         
     3 0 1 1          #对应每个不可约表示分子轨道中双电子占据的轨道数分别为3、0、1、1
     $END

     $GRAD            
     $END

     $BDFOPT
     $END