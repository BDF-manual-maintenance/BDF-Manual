Kohn-Sham方法
================================================
BDF的Kohn-Sham密度泛函计算，支持限制性(restricted)、非限制性(unrestricted)和
限制性开壳层(restricted open-shell)Kohn-Sham计算，简称为RKS、UKS和ROKS。其输入与RHF、UHF和ROHF接近，
关键是要指定交换相关泛函。Kohn-Sham支持LDA，GGA，Meta-GGA，Hybrid，RS Hybrid和Hyrid Meta-GGA等泛函，
详见？？？？。

RKS/UKS和ROKS计算
-------------------------------------------------
限制性Kohn-Sham(Restricted Kohn-Sham -- RKS)方法，这里以简洁输入的模式给出一个H2O分子的DFT计算算例，使用了B3lyp泛函。

.. code-block:: python

  #!bdf.sh
  B3lyp/3-21G    

  geometry
  O
  H  1  R1 
  H  1  R1  2 109.

  R1=1.0     # OH bond length, unit is Angstrom
  end geometry

这个输入对应的高级模式的输入为



基于RS杂化泛函的Kohn-Sham计算
-------------------------------------------------

杂化泛函Hartree-Fock交换项的自定义
-------------------------------------------------


Grimme的色散矫正
-------------------------------------------------


改变Kohn-Sham计算的积分格点
-------------------------------------------------