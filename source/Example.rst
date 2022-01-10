算例说明
************************************

示例1：计算SCF能量梯度、结构优化
------------------------------------------------
算例下载链接 :download:`test003.zip <files/test003.zip>`

.. code-block:: bdf

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
     $END

     $XUANYUAN
     $END

     $SCF
     RHF              #Restricted Hartree-Fock
     Occupied         
     3 0 1 1          #对应每个不可约表示分子轨道中双电子占据的轨道数分别为3、0、1、1
                      #注：如果只需要指定总电子数，而不关心每个不可约表示分别的占据数，则建议用
                      #Charge、SpinMulti而非Occupied来指定，见后续示例4等
     $END

     $GRAD            #计算HF梯度。注意DFT梯度需要用$RESP而非$GRAD，具体见示例11
     $END

     $BDFOPT          #结构优化。$BDFOPT模块既可以写在最后，也可以写在$COMPASS块和$XUANYUAN块之间
     $END

示例2：自动识别对称性&指认对称性
------------------------------------------------
算例下载链接 :download:`test006.zip <files/test006.zip>`

.. code-block:: bdf

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
     # 默认用最高点群计算，即D(6h)
     $END

     $xuanyuan
     $end

     $scf
     RHF              #Restricted Hartree-Fock
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
     Group
       D(6h)           #指定D6h点群
     $END

     $xuanyuan
     $end

     $scf
     RHF               #Restricted Hartree-Fock
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
     Group
       C(1)          #指定C1点群
     $END

     $xuanyuan
     $end

     $scf
     RHF
     $end  

示例3：DFT计算
------------------------------------------------
算例下载链接 :download:`test012.zip <files/test012.zip>`

.. code-block:: bdf

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
     $END

     $XUANYUAN
     RS
     0.33d0          #指定Range-Seperated泛函的系数
     $END

     $SCF
     RKS             #Restricted Kohn-Sham
     Occupied
     3 0 1 1         #对应每个不可约表示分子轨道中双电子占据的轨道数分别为3、0、1、1
     DFT
       CAM-B3lyp     #指定DFT计算的交换相关泛函
     $END

示例4：检验非阿贝尔群和骨架矩阵法
------------------------------------------------
算例下载链接 :download:`test029.zip <files/test029.zip>`  

.. code-block:: bdf

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
     Unit
       Bohr          #指定坐标长度单位
     Group
       D(2h)         #指定D2h点群
     $END

     $xuanyuan
     $end

     $SCF
     ROHF            #Restricted Open-shell Hartree-Fock
     charge          #电荷数1
      1
     spinmulti       #自旋多重度2
      2
     $END


     # 2nd task
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
     Unit
       Bohr
     $END

     $xuanyuan
     $end

     $SCF
     ROHF
     charge
       1
     spinmulti
       2
     $END

示例5：开壳层体系
------------------------------------------------
算例下载链接 :download:`test031.zip <files/test031.zip>`  

.. code-block:: bdf

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
     $END

     $XUANYUAN
     $END

     $SCF
     UHF                #Unrestricted Hartree-Fock
     spinmulti
     3                  #自旋多重度3
     Alpha
     3 0 1 1 0 2 1 1    #指定alpha或beta轨道每种不可约表示占据轨道数目
     Beta
     3 0 0 1 0 2 1 0
     $END

示例6：势能面扫描
------------------------------------------------
算例下载链接 :download:`test032.zip <files/test032.zip>`

.. code-block:: bdf

     #!test032.bdf
     HF/cc-pvdz scan

     geometry
     O 
     H 1 R1
     H 1 R1 2 109.3

     R1 0.8 0.05 4
     end geometry

示例7：基于双电子积分Cholesky分解的SCF计算
------------------------------------------------
算例下载链接 :download:`test033.zip <files/test033.zip>`

.. code-block:: bdf

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
     UNIT                #指定坐标长度单位
       Bohr
     Group
       C(1)              #指定C1点群
     $END

     $XUANYUAN
     $END

     $SCF
     RKS                 #Restricted Kohn-Sham
     Dft functional
     SVWN5
     numinttype          #数值积分
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


示例8：基于RI-J的DFT计算
------------------------------------------------
算例下载链接 :download:`test041.zip <files/test041.zip>`

.. code-block:: bdf

     ######### C(2v) group is used
     $COMPASS 
     Title
      H2O Molecule test run, DEF2-SV(P)
     Basis
     DEF2-SV(P)
     Geometry
     O  0.000000000   0.000000000    0.369372944
     H  0.000000000  -0.783975899   -0.184686472 
     H  0.000000000   0.783975899   -0.184686472 
     End geometry
     RI-J                 #库伦拟合加速计算
      DEF2-SV(P)          #密度拟合基组
     Group
      C(2v)               #指定C2v点群
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
      H2O Molecule test run, DEF2-SV(P)
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

示例9：计算电荷转移，库仑和交换积分
------------------------------------------------
算例下载链接 :download:`test062.zip <files/test062.zip>`

.. code-block:: bdf

     $COMPASS 
     Title
       Elecoup test run
     Basis
     cc-pvdz
     Geometry
     C      0.000000    0.000000  0.000000  
     C      1.332000    0.000000  0.000000  
     H     -0.574301   -0.928785  0.000000  
     H     -0.574301    0.928785  0.000000  
     H      1.906301    0.928785  0.000000  
     H      1.906301   -0.928785  0.000000  
     End geometry
     Group
       C(1)
     $END

     $xuanyuan
     $end

     $scf
     RKS                           #Restricted Kohn-Sham
     dft functional
       PBE0
     threshconv                    #指定SCF收敛的能量和密度矩阵阈值
       1.d-10 1.d-8
     $end
  
     %cp $BDFTASK.scforb $BDF_WORKDIR/$BDFTASK.scforb1
     %cp $BDFTASK.scforb $BDF_WORKDIR/$BDFTASK.scforb2
     
     $COMPASS 
     Title
       Elecoup test run
     Basis
       cc-pvdz
     Geometry
     C      0.000000    0.000000  0.000000  
     C      1.332000    0.000000  0.000000  
     H     -0.574301   -0.928785  0.000000  
     H     -0.574301    0.928785  0.000000  
     H      1.906301    0.928785  0.000000  
     H      1.906301   -0.928785  0.000000  
     C     -0.000000    0.000000  3.500000  
     C      1.332000   -0.000000  3.500000  
     H     -0.574301    0.928785  3.500000  
     H     -0.574301   -0.928785  3.500000  
     H      1.906301   -0.928785  3.500000  
     H      1.906301    0.928785  3.500000  
     End geometry
     Group
      C(1)
     Nfragment
      2
     $END
     
     $xuanyuan
     $end
     
     # calculate Electron and hole transfer integrals
     # Hole transfer: Donor HOMO to Acceptor HOMO
     # Electron transfer: Donor LUMO to Acceptor LUMO
     $elecoup
     electrans
      2                          #计算2对轨道间的迁移积分
      8 8 1
      9 9 1
     dft
      pbe0
     $END

     # calculate excitation energy transfer integrals
     # S-S and T-T coupling: Donor HOMO->LUMO Excitation to Acceptor HOMO->LUMO excitation
     $elecoup
     enertrans 
      2
      8  9 8  9 1
      8 10 8 10 1
     dft
      pbe0
     iprint
      1
     $END
     
     $elecoup
     enertrans 
      2
      8  9 8  9 1
      8 10 8 10 1
     dft
      pbe0
     orthmo
     iprint
      1
     $END
     
     $xuanyuan
     rs                             #指定Range-Seperated泛函
     0.33
     $end

     $elecoup
     electrans
      2
      8 8 1
      9 9 1
     dft # note: this calculates CAM-B3LYP coupling matrix elements upon PBE0 orbitals
      cam-b3lyp
     $END
     
     $elecoup
     enertrans 
      2
      8  9 8  9 1
      8 10 8 10 1
     dft
      cam-b3lyp
     iprint
      1
     $END
     
     $elecoup
     enertrans 
      2
      8  9 8  9 1
      8 10 8 10 1
     dft
      cam-b3lyp
     orthmo
     iprint
      1
     $END
     
     &database
     fragment 1  6
      1 2 3 4 5 6
     fragment 2 6
      7 8 9 10 11 12
     &end  
     
示例10：阿贝尔群对称结构的TD-DFT梯度计算
------------------------------------------------
算例下载链接 :download:`test063.zip <files/test063.zip>`

.. code-block:: bdf

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
     $END
     
     $XUANYUAN
     $END
     
     $SCF
     RKS            #Restricted Kohn-Sham
     dft functional
      B3lyp
     $END
     
     #Full TDDFT
     $TDDFT
     iprint
      3
     iroot          #每一个不可约表示计算1个激发态
      1
     istore         #指定将TDDFT计算结果存储在第1个TDDFT结果文件里，以备后续TDDFT梯度计算使用
      1 
     crit_vec       #指定TDDFT计算波函数收敛阈值
      1.d-8 
     crit_e         #指定TDDFT计算能量收敛阈值
      1.d-14
     $END
     
     $resp
     geom
     method         #指定TD-DFT激发态计算
      2
     iroot          #指定计算$tddft模块计算的能量最低的态（即第1个态）的梯度（在本算例里为1B2态）
      1
     nfiles         #此处的值（1）需要和以上$TDDFT模块设置的istore值一致
      1
     $end

示例11：DFT基态梯度计算
------------------------------------------------
算例下载链接 :download:`test065.zip <files/test065.zip>`

.. code-block:: bdf

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
     group          #指定分子的对称点群
      c(2v)
     $END
     
     $XUANYUAN
     $END
     
     $SCF
     UKS            #Unrestricted Kohn-Sham
     dft            # DFT exchange-correlation functional B3LYP
     B3LYP
     charge
     1
     spinmulti          #指定计算电子态的自旋多重度，值为2S+1=2
     2
     $END
     
     $resp
     geom 
     $end

示例12：非阿贝尔群对称性下进行TD-DFT梯度的计算
------------------------------------------------
算例下载链接 :download:`test068.zip <files/test068.zip>`

.. code-block:: bdf

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
     thresh        #判断分子对称性的阈值
      medium
     $END
     
     $XUANYUAN
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
     isf          # isf=1, spin flip up
      1
     iprint
      3
     iroot        #每一个不可约表示计算1个激发态
      1
     istore       # save TDDFT wave function in 1st scratch file
      1
     ialda
      4          # collinear kernel
     crit_vec    #指定TDDFT计算波函数收敛阈值
      1.d-6
     crit_e      #指定TDDFT计算能量收敛阈值
      1.d-8
     $END
     
     $resp
     geom
     method      #指定TD-DFT激发态计算
      2
     iroot
      1 2        # the first and the second lowest roots
     nfiles
      1
     jahnteller  
      1          # follow irrep component 1
     $end

示例13：基于TDDFT的非绝热耦合计算
------------------------------------------------
算例下载链接 :download:`test081.zip <files/test081.zip>`

.. code-block:: bdf

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
     unit        # Set unit of length as Bohr
      bohr
     nosymm
     $end
     
     $XUANYUAN
     $END
     
     $SCF
     rks         # Restricted Kohn-Sham calculation
     dft         # ask for bhhlyp functional
      bhhlyp 
     $END
     
     $tddft
     isf         # request for triplets (spin flip up)
      1
     ialda       # use collinear kernel (NAC only supports collinear kernel)
      4
     iroot       #每一个不可约表示计算2个激发态
      2
     crit_vec    #指定TDDFT计算波函数收敛阈值
      1.d-6
     crit_e      #指定TDDFT计算能量收敛阈值
      1.d-8
     istore      # 指定波函数存储，save TDDFT wave function in 1st scratch file
      1
     iprt        #指定输出信息的详略程度
      2
     $end
     
     # EX-EX NAC
     $resp 
     iprt 
      1 
     QUAD        #指定resp进行二阶响应计算
     FNAC        #指定resp计算一阶非绝热耦合向量
     double      #double为激发态-激发态非绝热耦合向量
     method      #指定TD-DFT激发态计算
      2
     nfiles
      1
     pairs       #指定计算哪两组激发态之间的非绝热耦合向量
      1
      1 1 1 1 1 2
     noresp      #指定在Double和FNAC计算中忽略跃迁密度矩阵的响应项
     $end

示例14：限制性结构优化以及开壳层体系的SA-TDDFT计算
----------------------------------------------------
算例下载链接 :download:`test085.zip <files/test085.zip>`

.. code-block:: bdf

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
     thresh
      medium
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
     $end
     
     $scf
     roks         #Restricted Open-shell Kohn-Sham
     dft
      b3lyp
     spinmulti         
      2
     $end
     
     $TDDFT
     imethod      #2为U-TDDFT
      2
     itest        # must specified in SA-TDDFT
      1
     icorrect     # spin-adapted correction to U-TDDFT, must be specified in SA-TDDFT
      1
     iprt
      3
     itda
      1
     iroot
      2
     istore       # save TDDFT wave function in 1st scratch file, must be specified
      1
     crit_vec     #指定TDDFT计算波函数收敛阈值
      1.d-6
     crit_e       #指定TDDFT计算能量收敛阈值
      1.d-8
     gridtol      #产生自适应格点的阈值
      1.d-7
     $END
     
     $resp
     geom
     method       #指定TD-DFT激发态计算
      2
     nfiles
      1
     iroot        #指定计算tddft模块计算的第一个态的梯度
      1
     $end


示例15：计算自旋翻转(spin-flip)的TDA
------------------------------------------------
算例下载链接 :download:`test098.zip <files/test098.zip>`

.. code-block:: bdf

     $COMPASS
     Title
      N2+ 
     Basis
      aug-cc-pvtz
     Geometry
      N     0.00000        0.00000       0.5582
      N     0.00000        0.00000      -0.5582 
     End geometry
     group
      d(2h)
     $END
     
     $XUANYUAN
     $END
     
     % echo "SVWN SCF "
     $SCF
     ROKS           #Restricted Open-shell Kohn-Sham 
     DFT 
     svwn5
     charge 
      1
     spinmulti
      2
     $END
     
     % echo "SVWN spin-flip TDA "
     $TDDFT
     IMETHOD    #ask for U-TDDFT
      2
     ISF               # ask for spin-flip up TDDFT calculation
      1
     ITDA            #ask for TDA
      1
     ialda
      2
     iroot
      20
     MemJKOP
      2048
     $END
     
     % echo "BLYP SCF "
     $SCF
     ROKS
     DFT 
     blyp
     charge 
      1
     spinmulti
      2
     $END
     
     % echo "BLYP spin-flip TDA "
     $TDDFT
     IMETHOD     # ask for U-TDDFT
      2
     ISF         # ask for spin-flip up TDDFT calculation
      1
     ITDA          #TDA
      1
     ialda
      2
     iroot
      20
     MemJKOP
      2048
     $END
     
     % echo "B3LYP SCF "
     $SCF
     ROKS
     DFT 
     b3lyp
     charge 
      1
     spinmulti  
      2
     $END
     
     % echo "B3LYP spin-flip TDA "
     $TDDFT
     IMETHOD
      2
     ISF
      1
     ITDA
      1
     ialda
      2
     iroot
      20
     MemJKOP
      2048
     $END
     
     $XUANYUAN
     rs
      0.33
     $END
     
     % echo "cam-B3LYP SCF "
     $SCF
     ROKS
     DFT 
     cam-b3lyp
     charge 
      1
     spinmulti
      2
     $END
     
     % echo "cam-B3LYP spin-flip TDA "
     $TDDFT
     IMETHOD
      2
     ISF
      1
     ITDA
      1
     IDIAG
      1
     ialda
      2
     iroot
      20
     MemJKOP
      2048
     $END

示例16：iOI计算（基于分片方法的大体系SCF计算）
------------------------------------------------
算例下载链接 :download:`test106.zip <files/test106.zip>`

.. code-block:: bdf

     # autofrag: a Python-based automatic fragmentation driver. Automatically
     # fragments an arbitrary molecule, and prepares the BDF input files of the
     # fragments (xxx.fragmentyyy.inp) and the global system (xxx.global.inp).
     $autofrag
     method
      ioi # To request a conventional FLMO calculation, change ioi to flmo
     nprocs
      2 # Use at most 2 parallel processes in calculating the subsystems
     $end

     $compass
     Title
      hydroxychloroquine (diprotonated)
     Basis
      6-31G(d)
     Geometry # snapshot of GFN2-xTB molecular dynamics at 298 K
     C    -4.2028   -1.1506    2.9497 
     C    -4.1974   -0.4473    4.1642 
     C    -3.7828    0.9065    4.1812 
     C    -3.4934    1.5454    2.9369 
     C    -3.4838    0.8240    1.7363 
     C    -3.7584   -0.5191    1.7505 
     H    -4.6123   -0.8793    5.0715 
     C    -3.3035    3.0061    2.9269 
     H    -3.1684    1.2214    0.8030 
     H    -3.7159   -1.1988    0.9297 
     C    -3.1506    3.6292    4.2183 
     C    -3.3495    2.9087    5.3473 
     H    -2.8779    4.6687    4.2878 
     H    -3.2554    3.3937    6.3124 
     N    -3.5923    1.5989    5.4076 
     Cl   -4.6402   -2.7763    3.0362 
     H    -3.8651    1.0100    6.1859 
     N    -3.3636    3.6632    1.7847 
     H    -3.4286    2.9775    1.0366 
     C    -3.5305    5.2960   -0.0482 
     H    -2.4848    5.4392   -0.0261 
     H    -3.5772    4.3876   -0.6303 
     C    -4.1485    6.5393   -0.7839 
     H    -3.8803    6.3760   -1.8559 
     H    -5.2124    6.5750   -0.7031 
     C    -3.4606    7.7754   -0.2653 
     H    -2.3720    7.6699   -0.3034 
     H    -3.7308    7.9469    0.7870 
     N    -3.8415    8.9938   -1.0424 
     H    -3.8246    8.8244   -2.0837 
     C    -2.7415    9.9365   -0.7484 
     H    -1.7736    9.4887   -0.8943 
     H    -2.8723   10.2143    0.3196 
     C    -2.7911   11.2324   -1.6563 
     H    -1.7773   11.3908   -2.1393 
     H    -3.5107   10.9108   -2.4646 
     H    -3.0564   12.0823   -1.1142 
     C    -5.1510    9.6033   -0.7836 
     H    -5.5290    9.1358    0.1412 
     H    -5.0054   10.6820   -0.6847 
     C    -6.2224    9.3823   -1.8639 
     H    -6.9636   10.1502   -1.7739 
     H    -5.8611    9.4210   -2.8855 
     O    -6.7773    8.0861   -1.6209 
     H    -7.5145    7.9086   -2.2227 
     C    -4.0308    4.9184    1.3736 
     H    -3.7858    5.6522    2.1906 
     C    -5.5414    4.6280    1.3533 
     H    -5.8612    3.8081    0.7198 
     H    -5.9086    4.3451    2.3469 
     H    -6.1262    5.5024    1.0605 
     End geometry
     MPEC+cosx
     $end

     $xuanyuan
     rs # the range separation parameter omega (a.k.a. mu) of wB97X
      0.3
     $end

     $scf
     rks
     dft
      wB97X
     iprt
      2
     charge
      2
     $end

     $localmo
     FLMO
     $end

示例17：双杂化泛函基态单点能计算
------------------------------------------------
算例下载链接 :download:`test116.zip <files/test116.zip>`

.. code-block:: bdf

     $compass
     title
      NH3...H2O B2PLYP-D3/def2-TZVP
     basis
      def2-TZVP
     RI-C
      def2-TZVP # RI-MP2 auxiliary basis = def2-TZVP/C
     geometry
             N             -0.6347196970        -2.4888833088        -0.0001987285
             H             -2.5637570606        -2.5802060356        -0.0187542806
             H             -0.0589873685        -3.4710591095         1.5591466837
             H             -0.0283791648        -3.4872452297        -1.5375008955
             O              0.5661204194         2.8752419284         0.0000247838
             H              0.1735090569         1.0640211402        -0.0014981011
             H              2.3916890605         2.8947369696        -0.0002005778
     end geometry
     unit
      bohr
     MPEC+cosx
     $end

     $xuanyuan
     $end

     $scf
     rks
     dft
      B2PLYP
     D3
     $end

     $mp2
     $end

