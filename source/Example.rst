算例说明
************************************


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
       CAM-B3lyp      #杂化泛函
     numinttype       
      1
     $END     

示例4：检验非阿贝尔群和骨架矩阵法。算例下载链接 :download:`test029.zip <files/test029.zip>`  

.. code-block:: python

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

.. code-block:: python

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

示例6：势能面扫描。算例下载链接 :download:`test032.zip <files/test032.zip>`

.. code-block:: python

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

.. code-block:: python

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

.. code-block:: python

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
     
     
示例9：阿贝尔群对称结构的TD-DFT梯度计算。算例下载链接 :download:`test063.zip <files/test063.zip>`

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
     Skeleton
     $END
     
     $XUANYUAN
     direct
     $END
     
     $SCF
     RKS            #Restricted Kohn-Sham
     dft functional
      B3lyp
     $END
     
     #Full TDDFT
     $TDDFT
     imethod        # 指定基于哪种基态计算方法进行TDDFT计算，imethod=1为R-TDFDT, 基态为RHF/RKS方法
      1
     isf            # isf=0, no spin-flip
      0
     itda           #完全TDDDFT计算，使用TDA
      0
     idiag          #指定TDDFT的对角化方法，idiag=1为基于Davidson方法的迭代对角化
      1
     iprint
      3
     iexit          #每一次重复计算1个激发态，calculate 1 excitation state for every irrep
      1
     istore         # 指定波函数存储，save TDDFT wave function in 1st scratch file
     1 
     lefteig        #指定TDDFT计算，X-Y向量也保存到文件中
     crit_vec       #指定TDDFT计算波函数收敛阈值
     1.d-8 
     crit_e         #指定TDDFT计算能量收敛阈值
     1.d-14
     $END
     
     $resp
     geom
     norder         #解析梯度
     1
     method         #指定TD-DFT激发态计算
     2
     iroot          # 指定计算$tddft模块计算的第一个态的梯度，select the lowest state from all irreps, in this case the B2 state 
     1              # this is particularly useful if the user don't know which irrep to follow
     nfiles
     1
     $end

示例10：DFT基态梯度计算。算例下载链接 :download:`test065.zip <files/test065.zip>`

.. code-block:: python

     $COMPASS 
     Title
      H2O+ grad 
     Basis
      cc-pvdz
     Geometry
      O  0.000000000   0.000000000    0.369372944
      H  0.000000000  -0.783975899   -0.184686472 
      H  0.000000000   0.783975899   -0.184686472 
     End geometry
     skeleton
     group          #指定分子的对称点群
     c(2v)
     check
     $END
     
     $XUANYUAN
     $END
     
     $SCF
     UKS            #Unrestricted Kohn-Sham
     dft            # DFT exchange-correlation functional B3LYP
     B3LYP
     charge
     1
     spin          #指定计算电子态的自旋多重度，值为2S+1=2
     2
     $END
     
     $resp
     geom 
     norder        #解析梯度
     1
     method        #指定DFT基态计算
     1
     $end

示例11：非阿贝尔群对称性的条件下进行TD-DFT梯度的计算。算例下载链接 :download:`test068.zip <files/test068.zip>`

.. code-block:: python

     $COMPASS 
     Title
      C6H6 SF-TD-DFT gradient, lowest & second lowest triplet state
     Basis
      cc-pvdz
     Geometry
      C                  1.20809735    0.69749533   -0.00000000
      C                  0.00000000    1.39499067   -0.00000000
      C                 -1.20809735    0.69749533   -0.00000000
      C                 -1.20809735   -0.69749533   -0.00000000
      C                  0.00000000   -1.39499067   -0.00000000
      C                  1.20809735   -0.69749533   -0.00000000
      H                  2.16038781    1.24730049   -0.00000000
      H                  0.00000000    2.49460097   -0.00000000
      H                 -2.16038781    1.24730049   -0.00000000
      H                 -2.16038781   -1.24730049   -0.00000000
      H                  0.00000000   -2.49460097   -0.00000000
      H                  2.16038781   -1.24730049   -0.00000000
     End geometry
     Check
     thresh
     medium
     skeleton
     $END
     
     $XUANYUAN
     direct
     $END
     
     $SCF
     RKS
     dft functional
      # for SF-TD-DFT, a larger amount of HF exchange is required than
      # for spin-conserving TD-DFT. Thus, for most organic molecules, 
      # BHHLYP (cx=50%) is recommended over B3LYP (cx=20%).
      BHHLYP
     $END
     
     $TDDFT
     imethod      # imethod=1, starts from rhf/rks
      1
     isf          # isf=1, spin flip up
      1
     itda         # itda=0, TDDFT
      0
     idiag        # Davidson diagonalization for solving Casida equation
      1 
     iprint
      3
     iexit        #每一次重复计算1个激发态，calculate 1 excitation state for every irrep
      1
     istore       # save TDDFT wave function in 1st scratch file
      1
     ialda
      4 # collinear kernel
     lefteig     #指定TDDFT计算，X-Y向量也保存到文件中
     crit_vec    #指定TDDFT计算波函数收敛阈值
      1.d-6
     crit_e      #指定TDDFT计算能量收敛阈值
      1.d-8
     $END
     
     $resp
     geom
     norder      #解析梯度
      1
     method      #指定TD-DFT激发态计算
      2
     iroot
      1 2        # lowest and second lowest root
     nfiles
      1
     jahnteller
      1          # follow irrep component 1
     $end

示例12：基于TDDFT的非绝热耦合计算。算例下载链接 :download:`test081.zip <files/test081.zip>`

.. code-block:: python

     $compass
     title
      PhCOMe
     basis
      def2-SVP
     geometry
             C             -0.3657620861         4.8928163606         0.0000770328
             C             -2.4915224786         3.3493223987        -0.0001063823
             C             -2.2618953860         0.7463412225        -0.0001958732
             C              0.1436118499        -0.3999193588        -0.0000964543
             C              2.2879147462         1.1871091769         0.0000824391
             C              2.0183382809         3.7824607425         0.0001740921
             H             -0.5627800515         6.9313968857         0.0001389666
             H             -4.3630645857         4.1868310874        -0.0002094148
             H             -3.9523568496        -0.4075513123        -0.0003833263
             H              4.1604797959         0.3598389310         0.0001836001
             H              3.6948496439         4.9629708946         0.0003304312
             C              0.3897478526        -3.0915327760        -0.0002927344
             O              2.5733215239        -4.1533492423        -0.0002053903
             C             -1.8017552120        -4.9131221777         0.0003595831
             H             -2.9771560760        -4.6352720097         1.6803279168
             H             -2.9780678476        -4.6353463569        -1.6789597597
             H             -1.1205416224        -6.8569277129         0.0002044899
     end geometry
     skeleton
     unit        # Set unit of length as Bohr
      bohr
     nosymm
     check
     $end
     
     $XUANYUAN
     Direct      # ask for direct SCF
     Schwarz
     $END
     
     $SCF
     rks         # Restricted Kohn-Sham calculation
     dft         # ask for bhhlyp functional
      bhhlyp 
     $END
     
     $tddft
     imethod     # 指定基于哪种基态计算方法进行TDDFT计算，imethod=1为R-TDFDT, 基态为RHF/RKS方法
      1
     isf         # request for triplets (spin flip up)
      1
     itda
      0
     ialda       # use collinear kernel (NAC only supports collinear kernel)
      4
     iexit       #每一次重复计算2个激发态，calculate 2 excitation state for every irrep
      2
     crit_vec    #指定TDDFT计算波函数收敛阈值
      1.d-6
     crit_e      #指定TDDFT计算能量收敛阈值
      1.d-8
     partitiontype       #SSF分割
      1
     lefteig     #X-Y向量也保存到文件中
     istore      # 指定波函数存储，save TDDFT wave function in 1st scratch file
      1
     iguess      # use sTDDFT guess (and also sTDDFT preconditioner)
      20 
     iprt        #指定输出信息的详略程度
      2
     $end
     
     # EX-EX NAC
     $resp 
     iprt 
      1 
     QUAD        #指定resp进行二次响应计算
     FNAC        #指定resp计算一阶非绝热耦合向量
     double      #double为激发态-激发态非绝热耦合向量
     norder      #1为解析梯度
      1
     method      #指定TD-DFT激发态计算
      2
     nfiles
      1
     pairs       #指定计算那两组激发态之间的非绝热耦合向量
      1
      1 1 1 1 1 2
     noresp      #指定在Double和FNAC计算中忽略跃迁密度矩阵的响应项
     $end

示例13：限制性结构优化以及开壳层体系的SA-TDDFT计算。算例下载链接 :download:`test085.zip <files/test085.zip>`

.. code-block:: python

     $compass
     title
      NO2 constrainted geomopt
     basis
      6-31GP
     geometry
      N                 -1.94323539    0.95929024    0.00000000
      O                 -2.69323539    2.25832835    0.00000000
      O                 -0.44323539    0.95929024    0.00000000
     end geometry
     skeleton
     thresh
      medium
     check
     $end
     
     $bdfopt
     solver
      1
     constraint
      1           # Number of constraints
      1 2         # Fix the bond length between atom 1 and atom 2
     # If more constraints are included at the same time, simply add more lines
     # If angles are to be fixed, use 3 atom numbers
     # If dihedrals are to be fixed, use 4 atom numbers
     $end
     
     $xuanyuan
     direct
     $end
     
     $scf
     roks         #Restricted Open-shell Kohn-Sham
     dft
      b3lyp
     spin         
      2
     $end
     
     $TDDFT
     imethod      #2为U-TDDFT
      2
     itest        # must specified in SA-TDDFT
      1
     icorrect     # spin-adapted correction to U-TDDFT,must specified in SA-TDDFT
      1
     iprt
      3
     itda
      1
     iexit
      2
     istore       # save TDDFT wave function in 1st scratch file, must be specified
      1
     iguess       #控制TDDFT初始猜测波函数
      20          #紧束缚近似猜测,不存储Davidson迭代中间过程向量
     lefteig      #指定TDDFT计算，X-Y向量也保存到文件中
     crit_vec     #指定TDDFT计算波函数收敛阈值
      1.d-6
     crit_e       #指定TDDFT计算能量收敛阈值
      1.d-8
     gridtol      #产生自适应格点的阈值
      1.d-7
     $END
     
     $resp
     geom
     norder       #解析梯度
      1
     method       #指定TD-DFT激发态计算
      2
     nfiles
      1
     iroot        #指定计算$tddft模块计算的第一个态的梯度
      1
     $end
