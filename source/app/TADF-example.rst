
.. _TADF-example:

理论揭示DPO-TXO2的热激活延迟荧光（TADF）发光机制
=====================================================

热激活延迟荧光（TADF）材料是继荧光材料和贵金属磷光材料之后发展起来的第三代纯有机延迟荧光材料，其典型的特征是较小的单三重态能隙（ΔES-T）和温度正相关性。
2012年，日本九州大学的Chiahaya Adachi课题组首次报道外量子效率（EQE）超过20%的4CzIPN 分子[ ]，该材料的单线态和三线态能级差几乎为0，在室温下(298 K)的这样的热扰动下激子完全能够从三线态再回到单线态而发射荧光，因此命名为TADF（Thermally activated delayed fluorescence）。
当S1与T1的激发都是HOMO->LUMO特征，二者的能量差为2*K，K是HOMO与LUMO间的交换积分。随着HOMO与LUMO分离的增加，K会迅速减小。所以分离较大的时候，S1与T1 gap就较小，易于发生TADF需要的RISC。

.. figure:: TADF-example/前言-TADF.jpg
   :width: 800
   :align: center

为了保证高效的RISC，TADF材料需要具有较小的单三重态能隙，对应其HOMO/LUMO的有效分离，因此，TADF材料一般采用给体（D）−受体（A）、D−A−D的结构以不同的给受体作用实现HOMO/LUMO分离，同时兼顾其跃迁振子强度。
不同给受体的电子特性、三重态能级、结构刚性及扭曲程度等均均会影响材料的△EST、振子强度、态密度、激子寿命等，最终反映在材料的光物理性能和对应OLED器件的光电性能上。
本专题将以一个典型的TADF分子DPO-TXO2为例，介绍如何计算结构优化、频率、单点能、激发能、自旋轨道耦合等。同时介绍如何读取数据用于结果分析，帮助用户深入了解BDF软件的使用。

结构优化和频率计算
-------------------------------------------------

生成结构优化和频率输入文件
########################################################

在Device Studio中导入准备的分子结构DPO-TXO2.xyz得到如图1.1-1所示界面，选中 Simulator → BDF → BDF，在弹出的界面中设置参数。计算结构优化时计算类型选择Opt+Freq，方法、泛函、基组等选项用户可根据计算需要设置参数。例如Basic Settings面板设置为图1.1-2，SCF面板消除“Use MPEC+COSX”勾选（图1.1-3）、OPT 、Freq面板仍为默认值，之后点击 Generate files 即可生成对应计算的输入文件。生成的输入文件 bdf.inp参数部分如图1.1-4所示 ，此时Device Studio图形界面如图1.1-5所示。

.. figure:: TADF-example/图1.1-1.png
   :width: 800
   :align: center
   :alt: 图1.1-1


.. figure:: TADF-example/图1.1-2.png
   :width: 800
   :align: center
   :alt: 图1.1-2 

.. figure:: TADF-example/图1.1-2.png；图1.1-3.png；图1.1-4.png；图1.1-5.png
   :width: 800
   :align: center
   :alt: 图1.1-2 


.. note::

    此处为保证结构优化和频率计算的条件相同，计算类型选择Opt+Freq，可以的单独做Opt计算或Freq计算。

BDF计算
########################################################
在做BDF计算之前，需连接装有BDF的服务器，具体配置过程见鸿之微云操作指南。连接好服务器，在做计算之前，用户可根据需要打开输入文件并查看文件中的参数设置是否合理，若不合理，则可选择直接在文件中编辑或重新生成，再进行BDF计算。
在图1.1-5所示的界面中，选中 bdf.inp → 右击 → Run，在弹出的界面导入相应的脚本，点击Run提交作业，如图1.1-6。计算完成后点击下载按钮弹出计算结果界面如图1.1-7所示，选择.out结果文件，点击 Download下载。（提交作业操作为重复内容，在后面的计算中将不再赘述）

.. figure:: TADF-example/图1.1-6.png；图1.1-7.png
   :width: 800
   :align: center
   :alt: 图1.1-2 


结构优化结果分析
########################################################
右击下载后的out文件，选择Open with/Open containing folder即可查看结果文件。找到如图1.1-8所示部分，当Geom.converge的4个值均为YES时，证明结构优化收敛。上方和下方分别为收敛的分子结构笛卡尔坐标和内坐标。优化后的坐标信息可以作为初始结构用于后续计算。

.. figure:: TADF-example/图1.1-8.png
   :width: 800
   :align: center
   :alt: 图1.1-2 

检查频率，若不存在虚频证明结构稳定。


单点能计算
-------------------------------------------------

生成单点能输入文件
########################################################

将优化后的坐标导入Device Studio，名字改为DPO-TXO2-sp.xyz，此时图形界面如图1.2-1。

.. figure:: TADF-example/图1.2-1.png
   :width: 800
   :align: center
   :alt: 图1.2-1 

选中 Simulator → BDF → BDF，在弹出的界面中计算类型选择Single Point（默认值），方法、泛函、基组等选项用户可根据计算需要设置参数。例如泛函选PBE0，基组Def2-TZVP，其他参数仍为默认值，之后点击 Generate files 即可生成对应计算的输入文件。生成的输入文件 bdf.inp参数部分如图1.2-2所示。

.. figure:: TADF-example/图1.2-2.png
   :width: 800
   :align: center
   :alt: 图1.2-2 


BDF计算
########################################################
同结构优化计算相同，连接好装有BDF的服务器后，选中 bdf.inp → 右击 → Run，检查脚本没有问题，点击Run提交作业。计算完成后点击下载按钮弹出计算结果，选择.out结果文件，点击 Download下载。


单点能结果分析
########################################################

右击下载后的out文件，选择Open with/Open containing folder即可查看结果文件。找到E_tot为系统总能量(图1.2-3)，E_tot=E_ele + E_nn，本例中系统总能量为-2310.04883102 Hartree。E_ele是电子能量，E_nn是原子核排斥能，E_1e是单电子能量，E_ne 是原子核对电子的吸引能，E_kin 是电子动能，E_ee 是双电子能，E_xc 是交换相关能。

.. figure:: TADF-example/图1.2-3.png
   :width: 800
   :align: center
   :alt: 图1.2-3

下方为轨道的占据情况，以及轨道能、HUMO-LOMO gap等信息，如图1.2-4。HOMO为-5.358 eV，LUMO为-1.962 eV，HOMO-LUMO gap为3.396 eV，Irrep为不可约表示，代表分子轨道对称性，本例中HOMO、LUMO不可约表示序号均为A。

.. figure:: TADF-example/图1.2-4.png
   :width: 800
   :align: center
   :alt: 图1.2-4


最底部为Mulliken和Lowdin电荷布局、偶极矩信息。图1.2-5为部分截取。

.. figure:: TADF-example/图1.2-5.png
   :width: 800
   :align: center
   :alt: 图1.2-5


查看HOMO轨道图
########################################################

为了更清楚的了解电子结构，往往需要做前线分子轨道分析。目前发布的版本BDF2022A中还无法实现数据的后处理，HOMO、LUMO轨道图可以用第三方软件Multiwfn+VMD渲染，需要用到scf.molden文件，软件的使用方法在量化论坛有专门的帖子可以学习，此文不做涉及。

.. figure:: TADF-example/HOMO.png
   :width: 800
   :align: center
   :alt: HOMO轨道分布图

.. figure:: TADF-example/LUMO.png
   :width: 800
   :align: center
   :alt: LUMO轨道分布图

得到的最高占据轨道(HOMO)与最低非占据轨道（LUMO）如图所示，由于两侧对称分布的吩恶嗪杂环是一个典型的给电子结构，而中心的磺酰化的四氢化萘是一个典型的吸电子的结构，因此整个分子是非常典型的D-A-D结构。可以看到HOMO轨道主要分布在两翼，LUMO轨道分布在中心，HOMO和LUMO轨道几乎没有重叠，符合TADF分子的电子结构特征。当然并不是所有HOMO和LUMO轨道分离的分子都具有TADF的光电特性，还需要满足S1和T1激发都是HOMO->LUMO轨道跃迁才行，因此我们可以进一步用BDF软件计算该分子的激发态电子结构。


激发态计算
-------------------------------------------------

生成激发态计算输入文件
########################################################
读取优化好的结构做TDDFT计算，右键复制导入的优化后结构，命名为DPO-TXO2-td。计算类型选择TDDFT，方法、泛函、基组等选项用户可根据计算需要设置参数，前面的单点计算显示HOMO和LUMO轨道明显分离，对于这类具有明显D-A结构的分子，其激发态往往也会呈现电荷转移的特征，因此这儿我们选择最适合这类体系的范围分离泛函，如cam-B3LYP或者ω-B97xd。例如将Basic Settings面板按图1.3-1设置，TDDFT面板按图1.3-2设置，之后点击 Generate files 即可生成对应计算的输入文件。生成的输入文件 bdf.inp参数部分tddft模块如图1.3-3所示。

.. figure:: TADF-example/图1.3-1.png
   :width: 800
   :align: center
   :alt: 图1.3-1

.. figure:: TADF-example/图1.3-2.png
   :width: 800
   :align: center
   :alt: 图1.3-2

.. figure:: TADF-example/图1.3-3.png
   :width: 800
   :align: center
   :alt: 图1.3-3

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
右击下载后的out文件，选择Open with/Open containing folder即可查看结果文件。得到单重和三重激发能、振子强度、跃迁偶极矩等信息，图1.3-4为单重激发态信息，isf=0；图1.3-5为三重激发态信息，isf=1。

.. figure:: TADF-example/图1.3-4.png
   :width: 800
   :align: center
   :alt: 图1.3-4

.. figure:: TADF-example/图1.3-5.png
   :width: 800
   :align: center
   :alt: 图1.3-5

绘制成表格如下：

.. table:: 
   :widths: 40 110

    ============== ============== ====== ======================  ============ ===================== =============================== ============== ============= ==========================
    Excited state	 Multiplicity	 Irrep	Dominant Excitations	  ExEnergies	Oscillator Strength   Transition orbital contribution	Dipole moment	Wavelengths	   Absolute Overlap Integral
    ============== ============== ====== ======================  ============ ===================== =============================== ============== ============= ==========================
     1                 	1           A     A( 162 )->   A( 163 )	 3.4840 eV	       0.0023	                  69.9%	                   0.1642       	355.86 nm             0.164
     2                 	1           A     A( 161 )->   A( 163 )	 3.4902 eV	       0.0005	                  69.3%	                   0.0798       	355.24 nm	          0.167
     3                 	1           A     A( 162 )->   A( 164 )	 3.8143 eV	       0.0003	                  31.6%	                   0.0580       	325.05 nm	          0.482
     1                 	3           A     A( 162 )->   A( 167 )	 2.7522 eV	       0.0000	                  25.1%	                   0.0000       	450.49 nm	          0.659
     2                 	3           A     A( 161 )->   A( 167 )	 2.7522 eV	       0.0000	                  25.3%	                   0.0000       	450.49 nm	          0.659
     3                 	3           A     A( 154 )->   A( 163 )	 3.3404 eV	       0.0000	                  33.1%	                   0.0000       	371.17 nm	          0.672
    ============== ============== =====  ======================  ============ ===================== =============================== ============== ============= ==========================

表中依次给出激发态由低到高排序、多重度、不可约表示、占主要贡献的电子-空穴对激发、激发能、振子强度、跃迁轨道贡献占比、偶极矩、波长和绝对重叠积分。从表中我们能够看出，所研究的6个单激发态能级在2.7-4.0eV之间，分布较密集，其中前两个单重激发态波长在355nm左右，主要组分跃迁分别由HOMO→LUMO和HOMO-1→LUMO，表现出电荷转移特征。

.. figure:: TADF-example/Wavelength.png
   :width: 800
   :align: center

文献报道的DPO-TXO2在溶剂环境下的能量最低吸收峰大约位于380nm左右，且随着溶剂极性的增大而红移。这主要是因为在极性越大的溶剂对极性越高的激发态稳定化程度也越高。n轨道极性最大，pi*次之，pi轨道极性最小。

计算显示DPO-TXO2分子的基态偶极矩是2.842 D，S1态的激发态偶极矩是19.4 D，显然激发态偶极矩明显大于基态偶极矩，因此激发态与溶剂环境的静电作用导致的能量降低比基态能量的降低更大，所以吸收光谱发生红移。

.. figure:: TADF-example/energy.png
   :width: 800
   :align: center

NTO分析
^^^^^^^^^^^^^^^^^^^^^^^
在激发态计算后，有时我们想更清楚的了解激发态跃迁的结果，此时可以做自然跃迁轨道（NTO）分析，对NTO分析的原理感兴趣的读者可以参考相关的博文（http://sobereva.com/91）。

假设我们对S1态感兴趣，可以单独对S1态做NTO分析。Basic Settings面板仍然按图1.3-1设置，TDDFT面板此时需要勾选“Perform NTO Analyze”，如图1.3-6所示。

.. figure:: TADF-example/图1.3-6.png
   :width: 800
   :align: center
   :alt: 图1.3-6

.. note::
    生成的输入文件第二个tddft模块也可手动修改为图1.3-7所示。


.. figure:: TADF-example/图1.3-7.png
   :width: 800
   :align: center
   :alt: 图1.3-7

计算结束后会产生nto1_1.molden格式文件，此文件中记录的已经不是scf.molden中MO轨道的信息了，而是NTO轨道信息，我们直接通过第三方软件Multiwfn主功能0并调整orbital info处理，得到的即为NTO轨道对的本征值与轨道图，软件的使用方法在科音论坛有专门的帖子可以学习，此文不做涉及。

DPO-TXO2分子的S1激发态的电子跃迁需要用两组NTO轨道才能较好地描述，下面是用VMD软件渲染出来的两组hole-particle轨道。


.. figure:: TADF-example/hole1-1.png；hole1-2.png
   :width: 800
   :align: center
   :alt: hole1->particle1(73.26%)



.. figure:: TADF-example/hole2-1.png；hole2-2.png
   :width: 800
   :align: center
   :alt: Hole2->particle2(26.59%)

S1态NTO分析后可以看到占据轨道NTO1→非占据轨道NTO3的跃迁起主导，贡献为73.26%，占据轨道NTO2→非占据轨道NTO4贡献为26.59%。S1激发态的电子从两侧的吩恶嗪给电子基团跃迁到了中心的吸电子基团。

吸收光谱分析
^^^^^^^^^^^^^^^^^^^^^^^

对于激发态我们往往需要理论预测吸收谱，也就是将每个激发态按一定的半峰宽进行高斯展宽。在TDDFT计算正常结束后，我们需要进入终端用命令调用BDF安装路径下的plotspec.py脚本执行计算。若用户使用鸿之微云算力资源，进入命令端方式请查阅鸿之微云指南，此文不做赘述。
进入终断后，在目录下运行$BDFHOME/sbin/plotspec.py bdf.out，会产生两个文件，分别为bdf.stick.csv和bdf.spec.csv，前者包含所有激发态的吸收波长和摩尔消光系数，可以用来作棒状图，后者包含高斯展宽后的吸收谱（默认的展宽FWHM为0.5 eV），将bdf.spec.csv用第三方软件Origin作图如下：

.. figure:: TADF-example/图1.3-8.png
   :width: 800
   :align: center
   :alt: 图1.3-8

说明位于基态的电子更容易吸收300nm波长的光发生跃迁。


激发态优化计算
-------------------------------------------------

生成激发态优化输入文件
########################################################

导入优化好的基态结构，计算类型选择TDDFT-OPT，泛函PBE0，基组Def2-SVP，此时Basic Settings面板如图1.4-1所示，SCF面板同样消除“Use MPEC+COSX”勾选，如上图1.1-3。在优化S1态时，TDDFT面板的多重度选择Singlet，Target State为1，此时注意勾选“Calculate Dipole Moments of Target State”，如图1.4-2，OPT面板均保持默认值，点击 Generate files 即可生成对应计算的输入文件。生成的输入文件 bdf.inp参数tddft部分如图1.4-3所示。

.. figure:: TADF-example/图1.4-1.png
   :width: 800
   :align: center
   :alt: 图1.4-1

.. figure:: TADF-example/图1.4-2.png
   :width: 800
   :align: center
   :alt: 图1.4-2

.. figure:: TADF-example/图1.4-3.png
   :width: 800
   :align: center
   :alt: 图1.4-3

.. note::
    对T1态优化时，将TDDFT面板的多重度改为Triplet，其余参数同S1优化。



BDF计算
########################################################

连接好装有BDF的服务器后，选中 bdf.inp → 右击 → Run，检查脚本没有问题，点击Run提交作业。计算完成后点击下载按钮弹出计算结果，选择.out结果文件，点击 Download下载。

激发态优化结果分析
右击下载后的out文件，选择Open with/Open containing folder即可查看结果文件。类似基态结构优化，当Geom.converge的4个值均为YES时，证明结构优化收敛，如上图1.1-8。将优化后的T1与S1能量相减，粗略计算ΔEST=2.425 eV。

.. figure:: TADF-example/T1-S1.png
   :width: 800
   :align: center
 
自旋轨道耦合计算
-------------------------------------------------


生成自旋轨道耦合输入文件
########################################################

对优化好的结构做SOC计算。计算类型选择TDDFT-SOC，哈密顿选择sf-x2c，方法、泛函可根据计算需要设置，基组选择相对论基组，例如cc-pVDZ-DK，此时Basic Settings面板如图1.5-1设置，SCF、TDDFT面板仍为默认值，之后点击 Generate files 即可生成对应计算的输入文件。生成的输入文件 bdf.inp参数tddft部分如图1.5-2所示。
  
.. figure:: TADF-example/图1.5-1.png
   :width: 800
   :align: center
   :alt: 图1.5-1

.. figure:: TADF-example/图1.5-2.png
   :width: 800
   :align: center
   :alt: 图1.5-2


BDF计算
########################################################
连接好装有BDF的服务器后，选中 bdf.inp → 右击 → Run，检查脚本没有问题，点击Run提交作业。计算完成后点击下载按钮弹出计算结果，选择.out结果文件，点击 Download下载。

耦合矩阵元结果分析
########################################################
右击下载后的out文件，选择Open with/Open containing folder即可查看结果文件。在Print selected matrix elements of [Hsoc]部分打印耦合矩阵元信息。

.. figure:: TADF-example/图1.5-3.png
   :width: 800
   :align: center
   :alt: 图1.5-3

绘制表格

.. table:: 
   :widths: 30 40


    ===============  =======  =======
    矩阵元的模/cm^-1   	T1	      T2
    ===============  =======  =======
           S0         1.822	 1.467
           S1         0.522	 0.842
    ===============  =======  =======

计算得到S0态与T1态旋轨耦合1.822 cm^-1 ，如果能隙足够小，就会引起系间窜越的发生。
