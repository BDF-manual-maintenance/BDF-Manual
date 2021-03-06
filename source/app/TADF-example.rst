
.. _TADF-example:

理论揭示DPO-TXO2的热激活延迟荧光（TADF）发光机制
=====================================================

热激活延迟荧光（TADF）材料是继荧光材料和贵金属磷光材料之后发展起来的第三代纯有机延迟荧光材料，其典型的特征是较小的单三重态能隙（ΔES-T）和温度正相关性。

2012年，日本九州大学的Chiahaya Adachi课题组首次报道外量子效率（EQE）超过20%的4CzIPN 分子[ ]，该材料的单线态和三线态能级差几乎为0，在室温下(298 K)的这样的热扰动下激子完全能够从三线态再回到单线态而发射荧光，因此命名为TADF（Thermally activated delayed fluorescence）。

当S1与T1的激发都是HOMO->LUMO特征，二者的能量差为2*K，K是HOMO与LUMO间的交换积分。随着HOMO与LUMO分离的增加，K会迅速减小。所以分离较大的时候，S1与T1 gap就较小，易于发生TADF需要的RISC。

.. figure:: /TADF-example/TADF.jpg
    :width: 800
    :align: center

为了保证高效的RISC，TADF材料需要具有较小的单三重态能隙，对应其HOMO/LUMO的有效分离，因此，TADF材料一般采用给体（D）−受体（A）、D−A−D的结构以不同的给受体作用实现HOMO/LUMO分离，同时兼顾其跃迁振子强度。

不同给受体的电子特性、三重态能级、结构刚性及扭曲程度等均均会影响材料的△EST、振子强度、态密度、激子寿命等，最终反映在材料的光物理性能和对应OLED器件的光电性能上。

本专题将以一个典型的TADF分子DPO-TXO2为例，介绍如何计算结构优化、频率、单点能、激发能、自旋轨道耦合等。同时介绍如何读取数据用于结果分析，帮助用户深入了解BDF软件的使用。

结构优化和频率计算
-------------------------------------------------

生成结构优化和频率输入文件
########################################################

在Device Studio中导入准备的分子结构DPO-TXO2.xyz得到如图1.1-1所示界面，选中 Simulator → BDF → BDF，在弹出的界面中设置参数。

.. figure:: /TADF-example/fig1.1-1.png
.. centered:: 1.1-1

计算结构优化时计算类型选择Opt+Freq，方法、泛函、基组等选项用户可根据计算需要设置参数。例如Basic Settings面板设置为图1.1-2，SCF面板取消“Use MPEC+COSX”勾选（图1.1-3）、OPT 、Freq等面板的参数使用推荐的默认值，不需要做修改。之后点击 Generate files 即可生成对应计算的输入文件。

.. figure:: /TADF-example/fig1.1-2.png
.. centered:: 1.1-2 

.. figure:: /TADF-example/fig1.1-3.png
.. centered:: 1.1-3 

生成的输入文件 bdf.inp参数部分如下： 

.. code-block:: bdf

  $compass
  Title
    C39H28N2O4S
  Geometry
  C          3.86523        0.67704        0.08992
  C          2.59676        1.19847       -0.21677
  C          1.38236        0.46211       -0.14538
  C          1.50274       -0.90633        0.05433
  C          2.74673       -1.48909        0.32003
  C          3.89360       -0.68925        0.41062
  C          0.05129        1.23073       -0.21431
  C         -1.26041        0.42556       -0.14322
  C         -1.34326       -0.94957        0.03351
  S          0.09634       -1.96093       -0.00226
  C         -2.49139        1.13510       -0.19404
  C         -3.75015        0.57230        0.07933
  C         -3.75167       -0.80689        0.33485
  C         -2.57699       -1.57032        0.24960
  N          5.05789        1.50514        0.05106
  N         -4.95552        1.38707        0.07338
  C          5.09111        2.89319        0.50297
  C          6.28464        3.63010        0.39676
  O          7.47953        3.08357        0.01235
  C          7.47002        1.78524       -0.41733
  C          6.30967        0.99832       -0.48773
  C          8.72243        1.30821       -0.82591
  C          8.84826        0.02519       -1.33737
  C          7.70856       -0.74821       -1.50329
  C          6.45512       -0.24869       -1.12362
  C          4.01062        3.58921        1.07620
  C          4.07062        4.96296        1.37442
  C          5.24860        5.67030        1.18784
  C          6.36600        4.99303        0.72541
  C         -6.19457        0.91553       -0.52385
  C         -7.33964        1.73082       -0.48834
  O         -7.34248        3.01488       -0.01720
  C         -6.17443        3.51502        0.46887
  C         -4.99409        2.75189        0.59422
  C         -6.34490       -0.31630       -1.18638
  C         -7.59189       -0.76699       -1.64640
  C         -8.71481        0.03325       -1.52666
  C         -8.57997        1.30489       -0.97531
  C         -6.24475        4.86124        0.86098
  C         -5.14195        5.49110        1.41274
  C         -3.98465        4.75621        1.61916
  C         -3.93157        3.39823        1.25512
  O          0.11666       -2.61281       -1.29752
  O          0.10373       -2.72112        1.23297
  C          0.03300        2.06197       -1.51772
  C          0.04308        2.16169        1.03932
  H          2.54886        2.24058       -0.51595
  H          2.82840       -2.56453        0.47286
  H          4.82173       -1.17141        0.70878
  H         -2.46593        2.19212       -0.44272
  H         -4.67197       -1.32502        0.59460
  H         -2.63456       -2.65479        0.35810
  H          9.59544        1.95023       -0.74373
  H          9.82187       -0.35477       -1.63187
  H          7.78471       -1.74349       -1.93391
  H          5.60034       -0.87480       -1.35499
  H          3.08415        3.09348        1.32929
  H          3.19316        5.47421        1.76453
  H          5.30763        6.72822        1.42899
  H          7.31255        5.51704        0.61863
  H         -5.50297       -0.96874       -1.38412
  H         -7.67454       -1.75102       -2.10194
  H         -9.68032       -0.30389       -1.89032
  H         -9.43942        1.96697       -0.92291
  H         -7.17589        5.40700        0.73318
  H         -5.19606        6.53771        1.70383
  H         -3.11983        5.23203        2.07660
  H         -3.02635        2.86997        1.52459
  H          0.02919        1.39736       -2.38952
  H          0.89268        2.72961       -1.61468
  H         -0.84000        2.71525       -1.59635
  H          0.04113        1.57168        1.96645
  H         -0.82598        2.82200        1.07532
  H          0.91163        2.82447        1.08397
  End Geometry
  Basis
    Def2-SVP
  Skeleton
  Group
    C(1)
  $end
  
  $bdfopt
  Solver
    1
  MaxCycle
    444
  IOpt
    3
  Hess
    final
  $end
  
  $xuanyuan
  Direct
  $end
  
  $scf
  RKS
  Charge
    0
  SpinMulti
    1
  DFT
    PBE0
  Molden
  $end
  
  $resp
  Geom
  $end

此时Device Studio图形界面如图1.1-4所示

.. figure:: /TADF-example/fig1.1-4.png
.. centered:: 1.1-4 

.. note::

    此处为保证结构优化和频率计算的条件相同，计算类型选择Opt+Freq，可以的单独做Opt计算或Freq计算。

BDF计算
########################################################
在做BDF计算之前，需连接装有BDF的服务器，具体配置过程见鸿之微云操作指南。

连接好服务器，在做计算之前，用户可根据需要打开输入文件并查看文件中的参数设置是否合理，若不合理，则可选择直接在文件中编辑或重新生成，再进行BDF计算。

在图1.1-4所示的界面中，选中 bdf.inp → 右击 → Run。在弹出的界面导入相应的脚本，点击Run提交作业，如图1.1-5。

.. figure:: /TADF-example/fig1.1-5.png
.. centered:: 1.1-5

计算完成后点击下载按钮弹出计算结果界面如图1.1-6所示。选择.out结果文件，点击 Download下载。（提交作业操作为重复内容，在后面的计算中将不再赘述）

.. figure:: /TADF-example/fig1.1-6.png
.. centered:: 1.1-6


结构优化结果分析
########################################################
右击下载后的out文件，选择Open with/Open containing folder即可查看结果文件。找到如下所示部分。

.. code-block:: 

                   Force-RMS    Force-Max     Step-RMS     Step-Max
    Conv. tolerance :  0.2000E-03   0.3000E-03   0.8000E-03   0.1200E-02
    Current values  :  0.7369E-05   0.4013E-04   0.1843E-03   0.1041E-02
    Geom. converge  :     Yes          Yes          Yes          Yes

当Geom.converge的4个值均为YES时，证明结构优化收敛。上方和下方分别为收敛的分子结构笛卡尔坐标和内坐标。优化后的坐标信息可以作为初始结构用于后续计算。

检查频率，若不存在虚频证明结构已经优化到极小点。


单点能计算
-------------------------------------------------

生成单点能输入文件
########################################################

将优化后的坐标导入Device Studio，名字改为DPO-TXO2-sp.xyz，此时图形界面如图1.2-1。

.. figure:: /TADF-example/fig1.2-1.png
.. centered:: 1.2-1 

选中 Simulator → BDF → BDF，在弹出的界面中计算类型选择Single Point（默认值），方法、泛函、基组等选项用户可根据计算需要设置参数。例如泛函选PBE0，基组Def2-TZVP，其他参数仍为默认值，之后点击 Generate files 即可生成对应计算的输入文件。
生成的输入文件bdf.inp参数部分如下：

.. code-block:: bdf

    $compass
    Title
      C39H28N2O4S
    Geometry
    C       3.470732   -0.452949    0.333229
    C       2.350276   -0.443126   -0.503378
    C       1.255134   -1.275716   -0.258388
    C       1.358849   -2.111496    0.851996
    C       2.440432   -2.124490    1.711142
    C       3.517727   -1.285828    1.451230
    C      -0.000048   -1.278142   -1.147435
    C      -1.255154   -1.275779   -0.258269
    C      -1.358725   -2.111574    0.852120
    S       0.000118   -3.243604    1.269861
    C      -2.350358   -0.443230   -0.503130
    C      -3.470738   -0.453151    0.333573
    C      -3.517603   -1.286054    1.451551
    C      -2.440223   -2.124643    1.711370
    N       4.564102    0.414026    0.042506
    N      -4.564206    0.413761    0.042962
    C       4.451652    1.797113    0.288414
    C       5.529066    2.638200   -0.032130
    O       6.712474    2.137493   -0.580518
    C       6.813862    0.759847   -0.795860
    C       5.755871   -0.112762   -0.496962
    C       7.999623    0.286590   -1.327509
    C       8.161221   -1.076261   -1.582122
    C       7.118160   -1.950624   -1.301513
    C       5.922124   -1.471078   -0.764717
    C       3.313452    2.367422    0.857787
    C       3.242304    3.742953    1.084847
    C       4.311909    4.564914    0.751035
    C       5.460487    4.001069    0.193102
    C      -5.755562   -0.112971   -0.497448
    C      -6.813628    0.759568   -0.796285
    O      -6.712738    2.137080   -0.579852
    C      -5.529582    2.637766   -0.030885
    C      -4.452105    1.796731    0.289592
    C      -5.921333   -1.471159   -0.766141
    C      -7.116971   -1.950658   -1.303865
    C      -8.160095   -1.076369   -1.584473
    C      -7.998981    0.286358   -1.328883
    C      -5.461319    4.000541    0.194998
    C      -4.313011    4.564332    0.753554
    C      -3.243348    3.742416    1.087286
    C      -3.314166    2.366978    0.859540
    O       0.000119   -4.563841    0.371547
    O       0.000187   -3.483649    2.840945
    C      -0.000061   -2.561317   -2.024419
    C      -0.000112   -0.071391   -2.097897
    H       2.353966    0.240214   -1.341805
    H       2.400109   -2.768057    2.584222
    H       4.382110   -1.260026    2.103052
    H      -2.354159    0.240153   -1.341521
    H      -4.381950   -1.260326    2.103422
    H      -2.399783   -2.768226    2.584432
    H       8.781734    1.005474   -1.536628
    H       9.092578   -1.440924   -1.998141
    H       7.222431   -3.011204   -1.498846
    H       5.108894   -2.153421   -0.550989
    H       2.483350    1.726165    1.126879
    H       2.346598    4.161499    1.529031
    H       4.264620    5.633193    0.924336
    H       6.321189    4.600814   -0.074686
    H      -5.108047   -2.153429   -0.552391
    H      -7.220889   -3.011140   -1.501914
    H      -9.091141   -1.440996   -2.001221
    H      -8.781175    1.005175   -1.537926
    H      -6.322045    4.600258   -0.072770
    H      -4.265977    5.632537    0.927382
    H      -2.347852    4.160920    1.531932
    H      -2.484014    1.725744    1.128541
    H      -0.000061   -3.470168   -1.414898
    H       0.891657   -2.554225   -2.661972
    H      -0.891789   -2.554218   -2.661957
    H      -0.000071    0.880895   -1.555239
    H      -0.877870   -0.116199   -2.750591
    H       0.877553   -0.116195   -2.750715
    End Geometry
    Basis
      Def2-TZVP
    Skeleton
    Group
      C(1)
    $end
    
    $xuanyuan
    Direct
    RS
      0.33
    $end
    
    $scf
    RKS
    Charge
      0
    SpinMulti
      1
    DFT
      CAM-B3LYP
    MPEC+COSX
    Molden
    $end


BDF计算
########################################################
同结构优化计算相同，连接好装有BDF的服务器后，选中 bdf.inp → 右击 → Run，检查脚本没有问题，点击Run提交作业。计算完成后点击下载按钮弹出计算结果，选择.out结果文件，点击 Download下载。


单点能结果分析
########################################################

右击下载后的out文件，选择Open with/Open containing folder即可查看结果文件。找到E_tot为系统总能量，E_tot=E_ele + E_nn，本例中系统总能量为-2310.04883102 Hartree。E_ele是电子能量，E_nn是原子核排斥能，E_1e是单电子能量，E_ne 是原子核对电子的吸引能，E_kin 是电子动能，E_ee 是双电子能，E_xc 是交换相关能。

.. code-block:: bdf

     Final scf result
     E_tot =             -2311.25269871
     E_ele =             -7827.28555013
     E_nn  =              5516.03285142
     E_1e  =            -14125.30142654
     E_ne  =            -16425.97927385
     E_kin =              2300.67784730
     E_ee  =              6514.27065120
     E_xc  =              -216.25477479
     Virial Theorem      2.004596

下方为轨道的占据情况，以及轨道能、HUMO-LOMO gap等信息。HOMO为-5.358 eV，LUMO为-1.962 eV，HOMO-LUMO gap为3.396 eV，Irrep为不可约表示，代表分子轨道对称性，本例中HOMO、LUMO不可约表示序号均为A。

.. code-block:: bdf

     [Final occupation pattern: ]

     Irreps:        A
     detailed occupation for iden/irep:      1   1
    1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00
    1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00
    1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00
    1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00
    ...
     Alpha   HOMO energy:      -0.24254414 au      -6.59996455 eV  Irrep: A
     Alpha   LUMO energy:      -0.04116321 au      -1.12010831 eV  Irrep: A
     HOMO-LUMO gap:       0.20138093 au       5.47985625 eV


最底部为Mulliken和Lowdin电荷布局、偶极矩信息。

.. code-block:: bdf

     [Mulliken Population Analysis]
  Atomic charges:
     1C      -0.0009
     2C      -0.3029
     3C       0.2227
     4C      -0.0143
     5C      -0.1228
     6C      -0.1890
     7C       0.0046
     8C       0.2227
     9C      -0.0150
    10S       0.7787
    11C      -0.3023
    12C      -0.0022
    13C      -0.1888
    14C      -0.1223
    15N      -0.0121
    16N      -0.0121
    17C       0.0563
    ...

.. code-block:: bdf

     [Lowdin Population Analysis]
  Atomic charges:
     1C      -0.1574
     2C      -0.0592
     3C      -0.0682
     4C      -0.2154
     5C      -0.1050
     6C      -0.0869
     7C      -0.2270
     8C      -0.0682
     9C      -0.2154
    10S       1.0012
    11C      -0.0591
    12C      -0.1574
    13C      -0.0869
    14C      -0.1050
    ...

.. code-block:: bdf

     [Dipole moment: Debye]
              X          Y          Z         |u|
   Elec:-.3535E+01 0.8441E-03 -.1954E+01
   Nucl:-.1254E-12 -.4210E-12 -.2935E-13
   Totl:   -3.5348     0.0008    -1.9541     4.0389


查看HOMO轨道图
########################################################

为了更清楚的了解电子结构，往往需要做前线分子轨道分析。目前发布的版本BDF2022A中还无法实现数据的后处理，HOMO、LUMO轨道图可以用第三方软件Multiwfn+VMD渲染，需要用到scf.molden文件，软件的使用方法在量化论坛有专门的帖子可以学习，此文不做涉及。

.. figure:: /TADF-example/HOMO.png
.. centered:: HOMO轨道分布图

.. figure:: /TADF-example/LUMO.png
.. centered:: LUMO轨道分布图

得到的最高占据轨道(HOMO)与最低非占据轨道（LUMO）如图所示，由于两侧对称分布的吩恶嗪杂环是一个典型的给电子结构，而中心的磺酰化的四氢化萘是一个典型的吸电子的结构，因此整个分子是非常典型的D-A-D结构。可以看到HOMO轨道主要分布在两翼，LUMO轨道分布在中心，HOMO和LUMO轨道几乎没有重叠，符合TADF分子的电子结构特征。当然并不是所有HOMO和LUMO轨道分离的分子都具有TADF的光电特性，还需要满足S1和T1激发都是HOMO->LUMO轨道跃迁才行，因此我们可以进一步用BDF软件计算该分子的激发态电子结构。


激发态计算
-------------------------------------------------

生成激发态计算输入文件
########################################################
读取优化好的结构做TDDFT计算，右键复制导入的优化后结构，命名为DPO-TXO2-td。计算类型选择TDDFT，方法、泛函、基组等选项用户可根据计算需要设置参数，前面的单点计算显示HOMO和LUMO轨道明显分离，对于这类具有明显D-A结构的分子，其激发态往往也会呈现电荷转移的特征，因此这儿我们选择最适合这类体系的范围分离泛函，如cam-B3LYP或者ω-B97xd。例如将Basic Settings面板按图1.3-1设置，TDDFT面板按图1.3-2设置，之后点击 Generate files 即可生成对应计算的输入文件。

.. figure:: /TADF-example/fig1.3-1.png
.. centered:: 1.3-1


.. figure:: /TADF-example/fig1.3-2.png
.. centered:: 1.3-2


生成的输入文件 bdf.inp参数部分如下：

.. code-block:: bdf

     $compass
     Title
       C39H28N2O4S
     Geometry
     C 3.56215000 -0.34631300 0.45361300
     C 2.39970800 -0.43121500 -0.31807500
     C 1.26327600 -1.11500900 0.12738900
     C 1.35885600 -1.69579600 1.40258100
     C 2.49771000 -1.60285400 2.19867100
     C 3.61595700 -0.93278100 1.71813300
     C 0.00021500 -1.24592200 -0.73874600
     C -1.26297700 -1.11486500 0.12717900
     C -1.35882900 -1.69562600 1.40235700
     S -0.00010100 -2.61984500 2.07323100
     C -2.39926700 -0.43096700 -0.31848800
     C -3.56181100 -0.34590900 0.45301500
     C -3.61589000 -0.93235000 1.71754500
     C -2.49780200 -1.60255300 2.19826800
     N 4.68577300 0.35565000 -0.05695800
     N -4.68524700 0.35616500 -0.05781800
     C 4.85522500 1.71734000 0.22325100
     C 5.96987000 2.38879800 -0.31382300
     O 6.88491700 1.74830700 -1.09915200
     C 6.71947900 0.41903200 -1.36430000
     C 5.62682300 -0.30753500 -0.85481400
     C 7.67346300 -0.19823700 -2.15908800
     C 7.56580700 -1.55645700 -2.46709500
     C 6.49405000 -2.28575300 -1.96795600
     C 5.53176100 -1.66610500 -1.16680600
     C 3.96124200 2.44515800 1.01262100
     C 4.17031100 3.80330200 1.26473400
     C 5.27551600 4.45343400 0.73047600
     C 6.17535900 3.73680700 -0.06194800
     C -5.62705300 -0.30735400 -0.85450500
     C -6.71928700 0.41938500 -1.36464300
     O -6.88329900 1.74927200 -1.10167600
     C -5.96897100 2.38946600 -0.31526500
     C -4.85474100 1.71783400 0.22245400
     C -5.53310000 -1.66639800 -1.16475900
     C -6.49610200 -2.28636200 -1.96480800
     C -7.56751800 -1.55693200 -2.46448300
     C -7.67406700 -0.19823400 -2.15820200
     C -6.17456800 3.73743100 -0.06324300
     C -5.27514800 4.45388200 0.72982000
     C -4.17031500 3.80359400 1.26465900
     C -3.96122400 2.44545700 1.01253300
     O -0.00015400 -3.96830000 1.50483700
     O -0.00019500 -2.47109100 3.52665800
     C 0.00020300 -2.64509100 -1.40495400
     C 0.00034300 -0.20466000 -1.86117000
     H 2.41118900 0.06372500 -1.28828500
     H 2.48620300 -2.04935500 3.19547800
     H 4.52498100 -0.84886800 2.31658900
     H -2.41056900 0.06394100 -1.28871700
     H -4.52499700 -0.84831800 2.31586200
     H -2.48649200 -2.04903700 3.19508500
     H 8.50056300 0.41098100 -2.52869800
     H 8.32203900 -2.03354800 -3.09349600
     H 6.39429300 -3.34933700 -2.19485600
     H 4.69465500 -2.24580100 -0.77484200
     H 3.09145400 1.94045700 1.43579900
     H 3.45545900 4.34652000 1.88647900
     H 5.44614600 5.51436800 0.92329600
     H 7.05577600 4.20903800 -0.50207500
     H -4.69625700 -2.24619000 -0.77237400
     H -6.39717200 -3.35029700 -2.19042200
     H -8.32431800 -2.03427800 -3.09000200
     H -8.50081300 0.41112900 -2.52836600
     H -7.05465600 4.20980200 -0.50387800
     H -5.44580600 5.51480700 0.92266800
     H -3.45579100 4.34667900 1.88689800
     H -3.09175200 1.94062000 1.43619700
     H 0.00013000 -3.45332000 -0.66309300
     H 0.89243900 -2.75169300 -2.04060300
     H -0.89196300 -2.75164000 -2.04071100
     H 0.00033500 0.82736500 -1.47979800
     H -0.87501100 -0.33812800 -2.51032400
     H 0.87579000 -0.33816300 -2.51019000
     End Geometry
     Basis
       Def2-TZVP
     Skeleton
     Group
       C(1)
     $end
     
     $xuanyuan
     Direct
     RS
       0.33
     $end
     
     $scf
     RKS
     Charge
       0
     SpinMulti
       1
     DFT
       CAM-B3LYP
     D3
     MPEC+COSX
     Molden
     $end
     
     $tddft
     Imethod
       1
     Isf
       0
     Idiag
       1
     Iroot
       6
     MPEC+COSX
     Istore
       1
     $end
     
     $tddft
     NtoAnalyze
       0
     $end
     
     $tddft
     Imethod
       1
     Isf
       1
     Idiag
       1
     Iroot
       6
     MPEC+COSX
     Istore
       2
     $end
     
     $tddft
     NtoAnalyze
       0
     $end


.. note::

  1.	Device studio中同名文件会被覆盖，输入文件默认名皆为bdf.inp。因此为避免数据被覆盖，我们每次计算需新建一个项目。
  2.	TDDFT面板Method一般建议选TDDFT，Multiplicity可选单重或三重或单重加三重。激发态数目默认计算6个，建议计算数目比实际想要的激发态数目多3个，如想计算10个态，此处可写13。
  3.	若想做NTO分析，TDDFT面板需勾选“Perform NTO Analyze”。



BDF计算
########################################################
连接好装有BDF的服务器后，选中 bdf.inp → 右击 → Run，检查脚本没有问题，点击Run提交作业。计算完成后点击下载按钮弹出计算结果，选择.out结果文件，点击 Download下载。

激发态结果分析
########################################################

激发能分析
^^^^^^^^^^^^^^^^^^^^^^^
右击下载后的out文件，选择Open with/Open containing folder即可查看结果文件。得到单重和三重激发能、振子强度、跃迁偶极矩等信息，isf=0为单重激发态信息，isf=1为三重激发态信息。

.. code-block:: bdf

           No. Pair   ExSym   ExEnergies     Wavelengths      f     D<S^2>          Domin
     ant Excitations             IPA   Ova     En-E1
     
         1   A    2   A    3.4840 eV        355.86 nm   0.0023   0.0000  69.9%  CV(0)
     :   A( 162 )->   A( 163 )   5.584 0.164    0.0000
         2   A    3   A    3.4902 eV        355.24 nm   0.0005   0.0000  69.3%  CV(0)
     :   A( 161 )->   A( 163 )   5.592 0.167    0.0061
         3   A    4   A    3.8143 eV        325.05 nm   0.0003   0.0000  31.6%  CV(0)
     :   A( 162 )->   A( 164 )   6.182 0.482    0.3302
         4   A    5   A    3.8152 eV        324.97 nm   0.0040   0.0000  31.0%  CV(0)
     :   A( 161 )->   A( 164 )   6.189 0.485    0.3312
         5   A    6   A    4.1185 eV        301.05 nm   0.0163   0.0000  30.7%  CV(0)
     :   A( 161 )->   A( 168 )   6.944 0.583    0.6344
         6   A    7   A    4.1229 eV        300.72 nm   0.1369   0.0000  30.8%  CV(0)
     :   A( 162 )->   A( 168 )   6.936 0.582    0.6388
     
      *** Ground to excited state Transition electric dipole moments (Au) ***
         State          X           Y           Z          Osc.
            1       0.0003      -0.1642       0.0004       0.0023       0.0023
            2       0.0579      -0.0010       0.0549       0.0005       0.0005
            3       0.0019       0.0580      -0.0012       0.0003       0.0003
            4      -0.1789       0.0007       0.1034       0.0040       0.0040
            5      -0.0070      -0.4020       0.0039       0.0163       0.0163
            6       1.0339      -0.0028      -0.5353       0.1369       0.1369
     
     
         ---------------------------------------------
         ---- End TD-DFT Calculations for isf = 0 ----
         ---------------------------------------------
     ...
       No. Pair   ExSym   ExEnergies     Wavelengths      f     D<S^2>          Domin
     ant Excitations             IPA   Ova     En-E1
     
         1   A    1   A    2.7522 eV        450.49 nm   0.0000   2.0000  25.3%  CV(1)
     :   A( 162 )->   A( 167 )   6.920 0.659    0.0000
         2   A    2   A    2.7522 eV        450.49 nm   0.0000   2.0000  25.1%  CV(1)
     :   A( 161 )->   A( 167 )   6.928 0.659    0.0000
         3   A    3   A    3.3404 eV        371.17 nm   0.0000   2.0000  33.1%  CV(1)
     :   A( 154 )->   A( 163 )   8.200 0.672    0.5882
         4   A    4   A    3.3862 eV        366.15 nm   0.0000   2.0000  20.9%  CV(1)
     :   A( 154 )->   A( 165 )   8.983 0.649    0.6340
         5   A    5   A    3.4620 eV        358.13 nm   0.0000   2.0000  50.3%  CV(1)
     :   A( 162 )->   A( 163 )   5.584 0.322    0.7098
         6   A    6   A    3.4757 eV        356.72 nm   0.0000   2.0000  32.5%  CV(1)
     :   A( 161 )->   A( 163 )   5.592 0.466    0.7235
     
      *** Ground to excited state Transition electric dipole moments (Au) ***
         State          X           Y           Z          Osc.
            1       0.0000       0.0000       0.0000       0.0000       0.0000
            2       0.0000       0.0000       0.0000       0.0000       0.0000
            3       0.0000       0.0000       0.0000       0.0000       0.0000
            4       0.0000       0.0000       0.0000       0.0000       0.0000
            5       0.0000       0.0000       0.0000       0.0000       0.0000
            6       0.0000       0.0000       0.0000       0.0000       0.0000
     
     
         ---------------------------------------------
         ---- End TD-DFT Calculations for isf = 1 ----
         ---------------------------------------------


绘制成表格如下：

.. table::


    ================== ========== ========== ======== ======== ========= ============
     主要跃迁轨道      激发能/eV   振子强度   贡献    偶极矩   波长/nm   绝对重叠积分
    ================== ========== ========== ======== ======== ========= ============
     A(162) -> A(163)    3.4840     0.0023    69.9%    0.1642   355.86   0.164
     A(161) -> A(163)    3.4902     0.0005    69.3%    0.0798   355.24   0.167
     A(162) -> A(164)    3.8143     0.0003    31.6%    0.0580   325.05   0.482
     A(162) -> A(167)    2.7522     0.0000    25.1%    0.0000   450.49   0.659
     A(161) -> A(167)    2.7522     0.0000    25.3%    0.0000   450.49   0.659
     A(154) -> A(163)    3.3404     0.0000    33.1%    0.0000   371.17   0.672
    ================== ========== ========== ======== ======== ========= ============

表中依次给出激发态由低到高排序、多重度、不可约表示、占主要贡献的电子-空穴对激发、激发能、振子强度、跃迁轨道贡献占比、偶极矩、波长和绝对重叠积分。从表中我们能够看出，所研究的6个单激发态能级在2.7-4.0eV之间，分布较密集，其中前两个单重激发态波长在355nm左右，主要组分跃迁分别由HOMO→LUMO和HOMO-1→LUMO，表现出电荷转移特征。

.. figure:: /TADF-example/Wavelength.png
    :width: 800
    :align: center

文献报道的DPO-TXO2在溶剂环境下的能量最低吸收峰大约位于380nm左右，且随着溶剂极性的增大而红移。这主要是因为在极性越大的溶剂对极性越高的激发态稳定化程度也越高。n轨道极性最大，pi*次之，pi轨道极性最小。

计算显示DPO-TXO2分子的基态偶极矩是2.842 D，S1态的激发态偶极矩是19.4 D，显然激发态偶极矩明显大于基态偶极矩，因此激发态与溶剂环境的静电作用导致的能量降低比基态能量的降低更大，所以吸收光谱发生红移。

.. figure:: /TADF-example/energy.png
    :width: 800
    :align: center

NTO分析
^^^^^^^^^^^^^^^^^^^^^^^
在激发态计算后，有时我们想更清楚的了解激发态跃迁的结果，此时可以做自然跃迁轨道（NTO）分析，对NTO分析的原理感兴趣的读者可以参考相关的博文（http://sobereva.com/91）。

假设我们对S1态感兴趣，可以单独对S1态做NTO分析。Basic Settings面板仍然按图1.3-1设置，TDDFT面板此时需要勾选“Perform NTO Analyze”，如图1.3-6所示。

.. figure:: /TADF-example/fig1.3-6.png
.. centered:: 1.3-6

.. note::
    生成的输入文件第二个tddft模块也可手动修改为如下形式：


.. code-block:: bdf

     $tddft
     NtoAnalyze
       1       #对一个态NTO分析
       1       #指定对第一个激发态做NTO分析
     $end

计算结束后会产生nto1_1.molden格式文件，此文件中记录的已经不是scf.molden中MO轨道的信息了，而是NTO轨道信息，我们直接通过第三方软件Multiwfn主功能0并调整orbital info处理，得到的即为NTO轨道对的本征值与轨道图，软件的使用方法在科音论坛有专门的帖子可以学习，此文不做涉及。

DPO-TXO2分子的S1激发态的电子跃迁需要用两组NTO轨道才能较好地描述，下面是用VMD软件渲染出来的两组hole-particle轨道。


.. figure:: /TADF-example/hole1-1.png
    :width: 300
    :align: left
.. figure:: /TADF-example/hole1-2.png
    :width: 300
    :align: right

.. centered:: Hole1->particle1(73.26%)


.. figure:: /TADF-example/hole2-1.png
    :width: 300
    :align: left
.. figure:: /TADF-example/hole2-2.png
    :width: 300
    :align: right

.. centered:: Hole2->particle2(26.59%)


S1态NTO分析后可以看到占据轨道NTO1→非占据轨道NTO3的跃迁起主导，贡献为73.26%，占据轨道NTO2→非占据轨道NTO4贡献为26.59%。S1激发态的电子从两侧的吩恶嗪给电子基团跃迁到了中心的吸电子基团。

吸收光谱分析
^^^^^^^^^^^^^^^^^^^^^^^

对于激发态我们往往需要理论预测吸收谱，也就是将每个激发态按一定的半峰宽进行高斯展宽。在TDDFT计算正常结束后，我们需要进入终端用命令调用BDF安装路径下的plotspec.py脚本执行计算。若用户使用鸿之微云算力资源，进入命令端方式请查阅鸿之微云指南，此文不做赘述。
进入终断后，在目录下运行$BDFHOME/sbin/plotspec.py bdf.out，会产生两个文件，分别为bdf.stick.csv和bdf.spec.csv，前者包含所有激发态的吸收波长和摩尔消光系数，可以用来作棒状图，后者包含高斯展宽后的吸收谱（默认的展宽FWHM为0.5 eV），将bdf.spec.csv用第三方软件Origin作图如下：

.. figure:: /TADF-example/fig1.3-8.png
    :width: 800
    :align: center
    :alt: 图1.3-8

说明位于基态的电子更容易吸收300nm波长的光发生跃迁。


激发态优化计算
-------------------------------------------------

生成激发态优化输入文件
########################################################

导入优化好的基态结构，计算类型选择TDDFT-OPT，泛函PBE0，基组Def2-SVP，此时Basic Settings面板如图1.4-1所示，SCF面板同样消除“Use MPEC+COSX”勾选，如上图1.1-3。在优化S1态时，TDDFT面板的多重度选择Singlet，Target State为1，此时注意勾选“Calculate Dipole Moments of Target State”，如图1.4-2，OPT面板均保持默认值，点击 Generate files 即可生成对应计算的输入文件。

.. figure:: /TADF-example/fig1.4-1.png
.. centered:: 1.4-1

.. figure:: /TADF-example/fig1.4-2.png
.. centered:: 1.4-2

生成的输入文件 bdf.inp参数如下：

.. code-block:: bdf

     $compass
     Title
       C39H28N2O4S
     Geometry
     C 3.56215000 -0.34631300 0.45361300
     C 2.39970800 -0.43121500 -0.31807500
     C 1.26327600 -1.11500900 0.12738900
     C 1.35885600 -1.69579600 1.40258100
     C 2.49771000 -1.60285400 2.19867100
     C 3.61595700 -0.93278100 1.71813300
     C 0.00021500 -1.24592200 -0.73874600
     C -1.26297700 -1.11486500 0.12717900
     C -1.35882900 -1.69562600 1.40235700
     S -0.00010100 -2.61984500 2.07323100
     C -2.39926700 -0.43096700 -0.31848800
     C -3.56181100 -0.34590900 0.45301500
     C -3.61589000 -0.93235000 1.71754500
     C -2.49780200 -1.60255300 2.19826800
     N 4.68577300 0.35565000 -0.05695800
     N -4.68524700 0.35616500 -0.05781800
     C 4.85522500 1.71734000 0.22325100
     C 5.96987000 2.38879800 -0.31382300
     O 6.88491700 1.74830700 -1.09915200
     C 6.71947900 0.41903200 -1.36430000
     C 5.62682300 -0.30753500 -0.85481400
     C 7.67346300 -0.19823700 -2.15908800
     C 7.56580700 -1.55645700 -2.46709500
     C 6.49405000 -2.28575300 -1.96795600
     C 5.53176100 -1.66610500 -1.16680600
     C 3.96124200 2.44515800 1.01262100
     C 4.17031100 3.80330200 1.26473400
     C 5.27551600 4.45343400 0.73047600
     C 6.17535900 3.73680700 -0.06194800
     C -5.62705300 -0.30735400 -0.85450500
     C -6.71928700 0.41938500 -1.36464300
     O -6.88329900 1.74927200 -1.10167600
     C -5.96897100 2.38946600 -0.31526500
     C -4.85474100 1.71783400 0.22245400
     C -5.53310000 -1.66639800 -1.16475900
     C -6.49610200 -2.28636200 -1.96480800
     C -7.56751800 -1.55693200 -2.46448300
     C -7.67406700 -0.19823400 -2.15820200
     C -6.17456800 3.73743100 -0.06324300
     C -5.27514800 4.45388200 0.72982000
     C -4.17031500 3.80359400 1.26465900
     C -3.96122400 2.44545700 1.01253300
     O -0.00015400 -3.96830000 1.50483700
     O -0.00019500 -2.47109100 3.52665800
     C 0.00020300 -2.64509100 -1.40495400
     C 0.00034300 -0.20466000 -1.86117000
     H 2.41118900 0.06372500 -1.28828500
     H 2.48620300 -2.04935500 3.19547800
     H 4.52498100 -0.84886800 2.31658900
     H -2.41056900 0.06394100 -1.28871700
     H -4.52499700 -0.84831800 2.31586200
     H -2.48649200 -2.04903700 3.19508500
     H 8.50056300 0.41098100 -2.52869800
     H 8.32203900 -2.03354800 -3.09349600
     H 6.39429300 -3.34933700 -2.19485600
     H 4.69465500 -2.24580100 -0.77484200
     H 3.09145400 1.94045700 1.43579900
     H 3.45545900 4.34652000 1.88647900
     H 5.44614600 5.51436800 0.92329600
     H 7.05577600 4.20903800 -0.50207500
     H -4.69625700 -2.24619000 -0.77237400
     H -6.39717200 -3.35029700 -2.19042200
     H -8.32431800 -2.03427800 -3.09000200
     H -8.50081300 0.41112900 -2.52836600
     H -7.05465600 4.20980200 -0.50387800
     H -5.44580600 5.51480700 0.92266800
     H -3.45579100 4.34667900 1.88689800
     H -3.09175200 1.94062000 1.43619700
     H 0.00013000 -3.45332000 -0.66309300
     H 0.89243900 -2.75169300 -2.04060300
     H -0.89196300 -2.75164000 -2.04071100
     H 0.00033500 0.82736500 -1.47979800
     H -0.87501100 -0.33812800 -2.51032400
     H 0.87579000 -0.33816300 -2.51019000
     End Geometry
     Basis
       Def2-TZVP
     Skeleton
     Group
       C(1)
     $end
     
     $bdfopt
     Solver
       1
     MaxCycle
       444
     IOpt
       3
     $end
     
     $xuanyuan
     Direct
     $end
     
     $scf
     RKS
     Charge
       0
     SpinMulti
       1
     DFT
       PBE0
     D3
     Molden
     $end
     
     $tddft
     Imethod
       1
     Isf
       0
     Ialda
       4  
     Idiag
       1
     Iroot
       4
     MPEC+COSX
     Istore
       1
     $end
     
     $resp
     Geom
     Method
       2
     Nfiles
       1
     Iroot
       1
     $end  


.. note::
    对T1态优化时，将TDDFT面板的多重度改为Triplet，其余参数同S1优化。


BDF计算
########################################################

连接好装有BDF的服务器后，选中 bdf.inp → 右击 → Run，检查脚本没有问题，点击Run提交作业。计算完成后点击下载按钮弹出计算结果，选择.out结果文件，点击 Download下载。

激发态优化结果分析
右击下载后的out文件，选择Open with/Open containing folder即可查看结果文件。类似基态结构优化，当Geom.converge的4个值均为YES时，证明结构优化收敛，如上图1.1-8。将优化后的T1与S1能量相减，粗略计算ΔEST=2.425 eV。

.. figure:: /TADF-example/T1-S1.png
    :width: 800
    :align: center
 
自旋轨道耦合计算
-------------------------------------------------


生成自旋轨道耦合输入文件
########################################################

对优化好的结构做SOC计算。计算类型选择TDDFT-SOC，哈密顿选择sf-x2c，方法、泛函可根据计算需要设置，基组选择相对论基组，例如cc-pVDZ-DK，此时Basic Settings面板如图1.5-1设置，SCF、TDDFT面板仍为默认值，之后点击 Generate files 即可生成对应计算的输入文件。
  
.. figure:: /TADF-example/fig1.5-1.png
.. centered:: 1.5-1

生成的输入文件 bdf.inp参数如下：

.. code-block:: bdf

     $compass
     Title
       C39H28N2O4S
     Geometry
     C 3.56214999 -0.34631300 0.45361300
     C 2.39970799 -0.43121500 -0.31807500
     C 1.26327600 -1.11500899 0.12738900
     C 1.35885600 -1.69579600 1.40258100
     C 2.49771000 -1.60285400 2.19867100
     C 3.61595699 -0.93278100 1.71813299
     C 0.00021500 -1.24592199 -0.73874600
     C -1.26297700 -1.11486500 0.12717899
     C -1.35882900 -1.69562600 1.40235700
     S -0.00010100 -2.61984500 2.07323099
     C -2.39926700 -0.43096700 -0.31848800
     C -3.56181100 -0.34590900 0.45301500
     C -3.61588999 -0.93235000 1.71754500
     C -2.49780200 -1.60255299 2.19826800
     N 4.68577300 0.35565000 -0.05695800
     N -4.68524700 0.35616500 -0.05781800
     C 4.85522499 1.71734000 0.22325100
     C 5.96987000 2.38879800 -0.31382300
     O 6.88491699 1.74830700 -1.09915199
     C 6.71947899 0.41903200 -1.36430000
     C 5.62682299 -0.30753500 -0.85481400
     C 7.67346299 -0.19823700 -2.15908800
     C 7.56580700 -1.55645700 -2.46709500
     C 6.49404999 -2.28575300 -1.96795600
     C 5.53176100 -1.66610499 -1.16680600
     C 3.96124200 2.44515800 1.01262099
     C 4.17031099 3.80330200 1.26473400
     C 5.27551599 4.45343399 0.73047600
     C 6.17535900 3.73680700 -0.06194800
     C -5.62705300 -0.30735400 -0.85450500
     C -6.71928699 0.41938500 -1.36464300
     O -6.88329900 1.74927200 -1.10167600
     C -5.96897099 2.38946600 -0.31526500
     C -4.85474099 1.71783400 0.22245400
     C -5.53310000 -1.66639800 -1.16475900
     C -6.49610199 -2.28636200 -1.96480800
     C -7.56751799 -1.55693200 -2.46448300
     C -7.67406700 -0.19823400 -2.15820200
     C -6.17456799 3.73743100 -0.06324299
     C -5.27514799 4.45388200 0.72982000
     C -4.17031500 3.80359399 1.26465899
     C -3.96122400 2.44545700 1.01253299
     O -0.00015400 -3.96830000 1.50483700
     O -0.00019500 -2.47109099 3.52665799
     C 0.00020300 -2.64509099 -1.40495400
     C 0.00034300 -0.20466000 -1.86117000
     H 2.41118899 0.06372500 -1.28828499
     H 2.48620300 -2.04935499 3.19547800
     H 4.52498100 -0.84886800 2.31658900
     H -2.41056900 0.06394100 -1.28871699
     H -4.52499699 -0.84831800 2.31586200
     H -2.48649200 -2.04903700 3.19508500
     H 8.50056299 0.41098100 -2.52869799
     H 8.32203900 -2.03354800 -3.09349600
     H 6.39429300 -3.34933699 -2.19485600
     H 4.69465500 -2.24580100 -0.77484200
     H 3.09145400 1.94045700 1.43579900
     H 3.45545899 4.34651999 1.88647900
     H 5.44614599 5.51436800 0.92329600
     H 7.05577599 4.20903799 -0.50207500
     H -4.69625700 -2.24618999 -0.77237400
     H -6.39717200 -3.35029699 -2.19042199
     H -8.32431799 -2.03427800 -3.09000200
     H -8.50081300 0.41112900 -2.52836600
     H -7.05465599 4.20980199 -0.50387800
     H -5.44580600 5.51480700 0.92266800
     H -3.45579100 4.34667899 1.88689800
     H -3.09175200 1.94062000 1.43619699
     H 0.00012999 -3.45332000 -0.66309300
     H 0.89243900 -2.75169300 -2.04060299
     H -0.89196300 -2.75164000 -2.04071099
     H 0.00033500 0.82736500 -1.47979799
     H -0.87501100 -0.33812800 -2.51032400
     H 0.87579000 -0.33816300 -2.51019000
     End Geometry
     Basis
       cc-pVDZ-DK
     Skeleton
     Group
       C(1)
     $end
     
     $xuanyuan
     Heff
       21
     Hsoc
       2
     Direct
     RS
       0.33
     $end
     
     $scf
     RKS
     Charge
       0
     SpinMulti
       1
     DFT
       CAM-B3LYP
     D3
     MPEC+COSX
     Molden
     $end
     
     $tddft
     Imethod
       1
     Isf
       0
     Idiag
       1
     Iroot
       6
     MPEC+COSX
     Istore
       1
     $end
     
     $tddft
     Imethod
       1
     Isf
       1
     Idiag
       1
     Iroot
       6
     MPEC+COSX
     Istore
       2
     $end
     
     $tddft
     Isoc
       2
     Nfiles
       2
     Imatsoc
       -1
     Imatrsf
       -1
     Imatrso
       -1
     $end  


BDF计算
########################################################
连接好装有BDF的服务器后，选中 bdf.inp → 右击 → Run，检查脚本没有问题，点击Run提交作业。计算完成后点击下载按钮弹出计算结果，选择.out结果文件，点击 Download下载。

耦合矩阵元结果分析
########################################################
右击下载后的out文件，选择Open with/Open containing folder即可查看结果文件。在Print selected matrix elements of [Hsoc]部分打印耦合矩阵元信息。

.. code-block:: bdf

     SocPairNo. =    8   SOCmat = <  0  0  0 |Hso|  2  1  1 >     Dim =    1    3
       mi/mj          ReHso(au)       cm^-1               ImHso(au)       cm^-1
      0.0 -1.0     -0.0000018883     -0.4144393040     -0.0000012470     -0.2736747987
      0.0  0.0      0.0000000000      0.0000000000     -0.0000076582     -1.6807798007
      0.0  1.0     -0.0000018883     -0.4144393040      0.0000012470      0.2736747987
   
     SocPairNo. =    9   SOCmat = <  0  0  0 |Hso|  2  1  2 >     Dim =    1    3
       mi/mj          ReHso(au)       cm^-1               ImHso(au)       cm^-1
      0.0 -1.0      0.0000038630      0.8478326909     -0.0000006073     -0.1332932016
      0.0  0.0      0.0000000000      0.0000000000     -0.0000037537     -0.8238381363
      0.0  1.0      0.0000038630      0.8478326909      0.0000006073      0.1332932016
    ...

绘制表格

.. table:: 
    :widths: 30 20 20


    =================  =======  =======
     矩阵元的模/cm^-1     T1	   T2
    =================  =======  =======
           S0           1.822	 1.467
           S1           0.522	 0.842
    =================  =======  =======

计算得到S0态与T1态旋轨耦合1.822 cm^-1 ，如果能隙足够小，就会引起系间窜越的发生。
