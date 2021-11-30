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

示例2：自动识别对称性&指认对称性。算例下载链接 :download:`test006.zip <files/test006.zip>`

.. code-block:: python

     $COMPASS    
     Title
       C6H6 Molecule test run, CC-PVDZ
     Basis
       CC-PVDZ
     Geometry
     C    0.00000000000000   1.39499100000000   0.00000000000000
     C   -1.20809764405066   0.69749550000000   0.00000000000000
     C    0.00000000000000  -1.39499100000000   0.00000000000000
     C   -1.20809764405066  -0.69749550000000   0.00000000000000
     C    1.20809764405066  -0.69749550000000   0.00000000000000
     C    1.20809764405066   0.69749550000000   0.00000000000000
     H    0.00000000000000   2.49460100000000   0.00000000000000
     H   -2.16038783830606   1.24730050000000   0.00000000000000
     H    0.00000000000000  -2.49460100000000   0.00000000000000
     H   -2.16038783830607  -1.24730050000000   0.00000000000000
     H    2.16038783830607  -1.24730050000000   0.00000000000000
     H    2.16038783830606   1.24730050000000   0.00000000000000
     End geometry
     Skeleton         #只计算“骨架”原子轨道积分 
     Check
     #Group
     #  D(6h)
     $END

     $xuanyuan
     $end

     $scf
     RHF
     $end

     $COMPASS    
     Title
       C6H6 Molecule test run, CC-PVDZ
     Basis
       CC-PVDZ
     Geometry
     C    0.00000000000000   1.39499100000000   0.00000000000000
     C   -1.20809764405066   0.69749550000000   0.00000000000000
     C    0.00000000000000  -1.39499100000000   0.00000000000000
     C   -1.20809764405066  -0.69749550000000   0.00000000000000
     C    1.20809764405066  -0.69749550000000   0.00000000000000
     C    1.20809764405066   0.69749550000000   0.00000000000000
     H    0.00000000000000   2.49460100000000   0.00000000000000
     H   -2.16038783830606   1.24730050000000   0.00000000000000
     H    0.00000000000000  -2.49460100000000   0.00000000000000
     H   -2.16038783830607  -1.24730050000000   0.00000000000000
     H    2.16038783830607  -1.24730050000000   0.00000000000000
     H    2.16038783830606   1.24730050000000   0.00000000000000
     End geometry
     Skeleton          
     Check
     Group
       D(6h)           #指定D6h点群
     $END

     $xuanyuan
     $end

     $scf
     RHF
     $end

     $COMPASS    
     Title
       C6H6 Molecule test run, CC-PVDZ
     Basis
       CC-PVDZ
     Geometry
     C    0.00000000000000   1.39499100000000   0.00000000000000
     C   -1.20809764405066   0.69749550000000   0.00000000000000
     C    0.00000000000000  -1.39499100000000   0.00000000000000
     C   -1.20809764405066  -0.69749550000000   0.00000000000000
     C    1.20809764405066  -0.69749550000000   0.00000000000000
     C    1.20809764405066   0.69749550000000   0.00000000000000
     H    0.00000000000000   2.49460100000000   0.00000000000000
     H   -2.16038783830606   1.24730050000000   0.00000000000000
     H    0.00000000000000  -2.49460100000000   0.00000000000000
     H   -2.16038783830607  -1.24730050000000   0.00000000000000
     H    2.16038783830607  -1.24730050000000   0.00000000000000
     H    2.16038783830606   1.24730050000000   0.00000000000000
     End geometry
     Skeleton          
     Check
     Group
       D(3h)          #指定D3h点群
     $END

     $xuanyuan
     $end

     $scf
     RHF
     $end 

     $COMPASS    
     Title
       C6H6 Molecule test run, CC-PVDZ
     Basis
       CC-PVDZ
     Geometry
     C    0.00000000000000   1.39499100000000   0.00000000000000
     C   -1.20809764405066   0.69749550000000   0.00000000000000
     C    0.00000000000000  -1.39499100000000   0.00000000000000
     C   -1.20809764405066  -0.69749550000000   0.00000000000000
     C    1.20809764405066  -0.69749550000000   0.00000000000000
     C    1.20809764405066   0.69749550000000   0.00000000000000
     H    0.00000000000000   2.49460100000000   0.00000000000000
     H   -2.16038783830606   1.24730050000000   0.00000000000000
     H    0.00000000000000  -2.49460100000000   0.00000000000000
     H   -2.16038783830607  -1.24730050000000   0.00000000000000
     H    2.16038783830607  -1.24730050000000   0.00000000000000
     H    2.16038783830606   1.24730050000000   0.00000000000000
     End geometry
     Skeleton          
     Check
     Group
       C(6v)          #指定C6v点群
     $END

     $xuanyuan
     $end

     $scf
     RHF
     $end  

     $COMPASS    
     Title
       C6H6 Molecule test run, CC-PVDZ
     Basis
       CC-PVDZ
     Geometry
     C    0.00000000000000   1.39499100000000   0.00000000000000
     C   -1.20809764405066   0.69749550000000   0.00000000000000
     C    0.00000000000000  -1.39499100000000   0.00000000000000
     C   -1.20809764405066  -0.69749550000000   0.00000000000000
     C    1.20809764405066  -0.69749550000000   0.00000000000000
     C    1.20809764405066   0.69749550000000   0.00000000000000
     H    0.00000000000000   2.49460100000000   0.00000000000000
     H   -2.16038783830606   1.24730050000000   0.00000000000000
     H    0.00000000000000  -2.49460100000000   0.00000000000000
     H   -2.16038783830607  -1.24730050000000   0.00000000000000
     H    2.16038783830607  -1.24730050000000   0.00000000000000
     H    2.16038783830606   1.24730050000000   0.00000000000000
     End geometry
     Skeleton          
     Check
     Group
       D(3d)          #指定D3d点群
     $END

     $xuanyuan
     $end

     $scf
     RHF
     $end 
    
     $COMPASS    
     Title
       C6H6 Molecule test run, CC-PVDZ
     Basis
       CC-PVDZ
     Geometry
     C    0.00000000000000   1.39499100000000   0.00000000000000
     C   -1.20809764405066   0.69749550000000   0.00000000000000
     C    0.00000000000000  -1.39499100000000   0.00000000000000
     C   -1.20809764405066  -0.69749550000000   0.00000000000000
     C    1.20809764405066  -0.69749550000000   0.00000000000000
     C    1.20809764405066   0.69749550000000   0.00000000000000
     H    0.00000000000000   2.49460100000000   0.00000000000000
     H   -2.16038783830606   1.24730050000000   0.00000000000000
     H    0.00000000000000  -2.49460100000000   0.00000000000000
     H   -2.16038783830607  -1.24730050000000   0.00000000000000
     H    2.16038783830607  -1.24730050000000   0.00000000000000
     H    2.16038783830606   1.24730050000000   0.00000000000000
     End geometry
     Skeleton          
     Check
     Group
       D(2h)          #指定D2h点群
     $END

     $xuanyuan
     $end

     $scf
     RHF
     $end 

     $COMPASS    
     Title
       C6H6 Molecule test run, CC-PVDZ
     Basis
       CC-PVDZ
     Geometry
     C    0.00000000000000   1.39499100000000   0.00000000000000
     C   -1.20809764405066   0.69749550000000   0.00000000000000
     C    0.00000000000000  -1.39499100000000   0.00000000000000
     C   -1.20809764405066  -0.69749550000000   0.00000000000000
     C    1.20809764405066  -0.69749550000000   0.00000000000000
     C    1.20809764405066   0.69749550000000   0.00000000000000
     H    0.00000000000000   2.49460100000000   0.00000000000000
     H   -2.16038783830606   1.24730050000000   0.00000000000000
     H    0.00000000000000  -2.49460100000000   0.00000000000000
     H   -2.16038783830607  -1.24730050000000   0.00000000000000
     H    2.16038783830607  -1.24730050000000   0.00000000000000
     H    2.16038783830606   1.24730050000000   0.00000000000000
     End geometry
     Skeleton          
     Check
     Group
       C(2v)          #指定C2v点群
     $END

     $xuanyuan
     $end

     $scf
     RHF
     $end  

     $COMPASS    
     Title
       C6H6 Molecule test run, CC-PVDZ
     Basis
       CC-PVDZ
     Geometry
     C    0.00000000000000   1.39499100000000   0.00000000000000
     C   -1.20809764405066   0.69749550000000   0.00000000000000
     C    0.00000000000000  -1.39499100000000   0.00000000000000
     C   -1.20809764405066  -0.69749550000000   0.00000000000000
     C    1.20809764405066  -0.69749550000000   0.00000000000000
     C    1.20809764405066   0.69749550000000   0.00000000000000
     H    0.00000000000000   2.49460100000000   0.00000000000000
     H   -2.16038783830606   1.24730050000000   0.00000000000000
     H    0.00000000000000  -2.49460100000000   0.00000000000000
     H   -2.16038783830607  -1.24730050000000   0.00000000000000
     H    2.16038783830607  -1.24730050000000   0.00000000000000
     H    2.16038783830606   1.24730050000000   0.00000000000000
     End geometry
     Skeleton          
     Check
     Group
       C(1)          #指定C1点群
     $END

     $xuanyuan
     $end

     $scf
     RHF
     $end  

示例3：DFT计算。算例下载链接 :download:`test012.zip <files/test012.zip>`

.. code-block:: python

     $COMPASS  
     Title
       H2O Molecule test run, cc-pvdz
     Basis
       cc-pvdz
     Geometry
     O  0.000000000   0.000000000    0.369372944
     H  0.000000000  -0.783975899   -0.184686472 
     H  0.000000000   0.783975899   -0.184686472 
     End geometry
     Check
     $END

     $XUANYUAN
     RS
     0.33d0          #指定Range-Speration泛函的系数
     $END

     $SCF
     RKS             #Restricted Kohn-Sham
     Occupied
     3 0 1 1         #对应每个不可约表示分子轨道中双电子占据的轨道数分别为3、0、1、1
     DFT
       CAM-B3lyp     #指定DFT计算的交换相关泛函
     numinttype      
      1              #指定数值积分计算方法
     $END

     $COMPASS 
     Title
       H2O Molecule test run, cc-pvdz
     Basis
       cc-pvdz
     Geometry
     O  0.000000000   0.000000000    0.369372944
     H  0.000000000  -0.783975899   -0.184686472 
     H  0.000000000   0.783975899   -0.184686472 
     End geometry
     Check
     Skeleton        #只计算“骨架”原子轨道积分
     $END

     $XUANYUAN
     RS
     0.33d0
     $END

     $SCF
     RKS
     Occupied
     3 0 1 1
     DFT
       CAM-B3lyp 
     numinttype
      1
     $END     

示例4：检验非阿贝尔群和骨架矩阵法。算例下载链接 :download:`test029.zip <files/test029.zip>`  

.. code-block: python

     # 1st task
     $COMPASS 
     Title
       N2 Molecule test run, CC-PVTZ 
     Basis
       CC-PVTZ 
     Geometry
     N   0.0000    0.000000    1.05445
     N   0.0000    0.000000   -1.05445
     End geometry
     Check
     Unit
       Bohr
     Group
       D(2h)
     $END

     $xuanyuan
     $end

     $SCF
     ROHF            #Restricted Open-shell Hartree-Fock
     charge
      1
     spin
      2
     $END


     # 2nd task
     $COMPASS 
     Title
     N2 Molecule test run, CC-PVTZ 
     Basis
       CC-PVTZ 
     Geometry
     N   0.0000    0.000000    1.05445
     N   0.0000    0.000000   -1.05445
     End geometry
     Check
     Unit
     Bohr
     skeleton
     Group
       D(2h)
     $END

     $xuanyuan
     $end

     $SCF
     ROHF
     charge
       1
     spin
       2
     $END


     # 3rd task
     $COMPASS 
     Title
       N2 Molecule test run, CC-PVTZ 
     Basis
       CC-PVTZ 
     # 3-21G
     Geometry
     N   0.0000    0.000000    1.05445
     N   0.0000    0.000000   -1.05445
     End geometry
     Check
     Unit
     Bohr
     skeleton
     $END

     $xuanyuan
     $end

     $SCF
     ROHF
     charge
       1
     spin
       2
     $END

示例5：自旋体系。算例下载链接 :download:`test031.zip <files/test031.zip>`  

.. code-block: python

     $COMPASS 
     Title
       C2H4 Molecule test run, aug-cc-pvdz 
     Basis
       aug-cc-pvdz
     Geometry
     C                 -0.66500000    0.00000000    0.00000000
     C                  0.66500000    0.00000000    0.00000000
     H                 -1.14678878    0.96210996    0.00000000
     H                 -1.14678878   -0.96210996    0.00000000
     H                  1.14678878   -0.96210996    0.00000000
     H                  1.14678878    0.96210996   -0.00000000
     End geometry
     Check
     $END

     $XUANYUAN
     $END

     $SCF
     UHF                #Unrestricted Hartree-Fock
     spin
     3                  #自旋多重度3
     Alpha
     3 0 1 1 0 2 1 1    #指定alpha或beta轨道每种不可约表示占据轨道数目
     Beta
     3 0 0 1 0 2 1 0
     $END

示例6：势能面扫描。算例下载链接 :download:`test032.zip <files/test032>`

.. code-block: python

     #!test032.bdf
     HF/cc-pvdz scan

     geometry
     O 
     H 1 R1
     H 1 R1 2 109.3

     R1 0.8 0.05 4
     end geometry

     $compass
     check
     $end

示例7：Cholesky分解。算例下载链接 :download:`test033.zip <files/test033.zip>`

.. code-block: python

     $COMPASS 
     Title
       CH2 Molecule test run, cc-pvqz 
     Basis
     # 3-21G
     cc-pvdz
     Geometry
     C     0.000000        0.00000        0.31399
     H     0.000000       -1.65723       -0.94197
     H     0.000000        1.65723       -0.94197
     End geometry
     UNIT
     Bohr
     Check
     skeleton
     Group
       C(1)
     $END

     $XUANYUAN
     $END

     $SCF
     RKS
     Dft functional
     SVWN5
     numinttype
     11
     $END

     $XUANYUAN
     Cholesky      
     S-CD 1.d-4             #对双电子积分做Cholesky分解，设置方法和阈值
     $END

     $scf
     RKS
     Dft functional
      SVWN5
     numinttype
      11
     $end

     $XUANYUAN
     Cholesky
     S-CD 1.d-5
     $END

     $scf
     RKS
     Dft functional
     SVWN5
     numinttype
     11
     $end

     $XUANYUAN
     Cholesky
     S-CD 1.d-6
     $END

     $scf
     RKS
     Dft functional
     SVWN5
     numinttype
     11
     $end

     $XUANYUAN
     Cholesky
     1C-CD  1.d-4
     $END

     $scf
     RKS
     Dft functional
     SVWN5
     numinttype
     11
     $end

     $XUANYUAN
     Cholesky
     1C-CD 1.d-6
     $END

     $scf
     RKS
     Dft functional
     SVWN5
     numinttype
     11
     $end

示例8：辅助基组的DFT计算。算例下载链接 :download:`test041.zip <files/test041.zip>`

.. code-block: python

     ######### C(2v) group is used
     $COMPASS 
     Title
      H2O Molecule test run, cc-pvdz
     Basis
     DEF2-SV(P)
     Geometry
     O  0.000000000   0.000000000    0.369372944
     H  0.000000000  -0.783975899   -0.184686472 
     H  0.000000000   0.783975899   -0.184686472 
     End geometry
     Check
     RI-J                 #库伦拟合基组加速计算
     DEF2-SV(P)           #密度拟合基组
     Skeleton
     Group
      C(2v)
     $END

     $XUANYUAN
     $END

     $SCF
     RKS                  #Restricted Kohn-Sham
     dft functional
     B3lyp
     gridtype             #指定DFT计算径向与角向布点方法
     100
     $END

     $SCF
     RKS
     dft functional
     svwn5 
     gridtype
     100
     $END
 
     $SCF
     UKS                  #Unrestricted Kohn-Sham
     dft functional
     B3lyp
     gridtype
     100
     $END

     $SCF
     UKS
     dft functional
     svwn5 
     gridtype
     100
     $END

     ############## C(1) group is used
     $COMPASS 
     Title
      H2O Molecule test run, cc-pvdz
     Basis
     DEF2-SV(P)
     Geometry
     O  0.000000000   0.000000000    0.369372944
     H  0.000000000  -0.783975899   -0.184686472 
     H  0.000000000   0.783975899   -0.184686472 
     End geometry
     Check
     RI-J
     DEF2-SV(P)
     Skeleton
     Group
      C(1)
     $END

     $XUANYUAN
     $END

     $SCF
     RKS
     dft functional
     B3lyp
     gridtype 
     100
     $END

     $SCF
     RKS
     dft functional
     svwn5 
     gridtype
     100
     $END
 
     $SCF
     UKS
     dft functional
     B3lyp
     gridtype
     100
     $END

     $SCF
     UKS
     dft functional
     svwn5 
     gridtype
     100
     $END
     