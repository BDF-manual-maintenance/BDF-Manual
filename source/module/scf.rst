Hartree-Fock及Kohn-Sham自洽场计算 - SCF模块
================================================
SCF模块是BDF的核心计算模块之一，进行Hartree-Fock和DFT计算。

**计算方法关键词**

:guilabel:`RHF` / :guilabel:`UHF` / :guilabel:`ROHF` 参数类型：Βοοl型
------------------------------------------------------------------------
如果做Hartree-Fock计算，这三个参数必须3选1，用于控制Hartree-Fock计算的类型。

 * ``RHF`` Restricted Hartree-Fock
 * ``UHF`` Unrestricted Hartree-Fock
 * ``ROHF`` Restricted Open-shell Hartree-Fock

:guilabel:`RKS` / :guilabel:`UKS` / :guilabel:`ROKS` 参数类型：Βοοl型
------------------------------------------------------------------------
如果做DFT计算，这三个参数必须3选1，用于控制DFT计算的类型。

 * ``RKS`` Restricted Kohn-Sham
 * ``UKS`` Unrestricted Kohn-Sham
 * ``ROKS`` Restricted Open-shell Kohn-Sham

**波函数与占据数关键词**

:guilabel:`Charge` 参数类型：整数
------------------------------------------------
 * 默认值：0

指定分子体系的净电荷数。

:guilabel:`Spinmulti` 参数类型：整数
---------------------------------------------------
 * 默认值：对偶数电子体系为1，对奇数电子体系为2

指定分子体系的自旋多重度。自旋多重度定义为2S+1（其中S是自旋角动量），可以由 | *自旋向上的单电子数* - *自旋向下的单电子数* | + 1 计算得到，因此当体系的所有单电子的自旋都彼此平行时，自旋多重度等于体系内的单电子数加1。

:guilabel:`Occupy` 参数类型：整数数组
------------------------------------------------
指定每个不可约表示分子轨道中双电子占据的轨道数目，用于RHF/RKS计算。

:guilabel:`Alpha` 参数类型：整数数组
---------------------------------------------------
见下述Beta条目。

:guilabel:`Beta` 参数类型：整数数组
---------------------------------------------------
Alpha和Beta两个关键词必须联用，用于UHF/UKS计算，分别指定alpha或beta轨道每种不可约表示占据轨道数目。

:guilabel:`Guess` 参数类型：字符串
---------------------------------------------------
 * 默认值：atom
 * 可选值：atom、Hcore、Huckel、Readmo

指定初猜的类型。一般情况下atom较Hcore、Huckel好，因此正常情况下无需选择Hcore或Huckel。若选择Readmo，则程序会依次检查下述文件是否存在：

 1. $BDF_TMPDIR/$BDFTASK.inporb
 2. $BDF_TMPDIR/inporb
 3. $BDF_WORKDIR/$BDFTASK.scforb

其中$BDF_TMPDIR为当前BDF计算的临时目录，$BDF_WORKDIR为当前BDF计算的工作目录，$BDFTASK为当前BDF任务的输入文件名去掉后缀.inp后剩余的字符串。程序会读取以上列表中第一个存在的文件里的轨道信息，如读取失败，或读取到的轨道信息与当前计算不兼容（例如基函数数目不同），则程序会自动改为atom猜测。读取到的轨道会先进行Lowdin正交归一化，然后才用于SCF迭代。

.. hint::
     读取的轨道文件必须和当前计算在以下方面相符：
     
     1. 原子的数目和种类必须相同；
     2. 原子的排列顺序必须相同；
     3. 使用的点群必须相同；
     4. 使用的基组必须相同；
     5. 要么两个计算均为RHF、RKS、ROHF或ROKS，要么两个计算均为UHF或UKS。
     
     除此之外的大多数方面不要求相同，例如原子坐标、电荷、自旋多重度、泛函等等均可以不同。其中如果（1）、（2）、（3）、（5）均满足，只有（4）不满足，可以用 ``expandmo`` 模块将轨道文件所用的基组投影到当前计算所用基组上，再读取轨道作为初猜（参见 :doc:`expandmo` ）。

例如，假如某输入文件mol-B3LYP-Energy.inp在B3LYP/def2-TZVP水平下计算了某分子在某个结构下的单点能，现改用M06-2X/def2-TZVP计算同一个分子在另一个结构下的单点能（输入文件名为mol-M062X-Energy.inp），则为节约计算时间，可以利用此前B3LYP/def2-TZVP水平下的收敛的SCF波函数：

.. code-block:: bash

     cp mol-B3LYP-Energy.scforb mol-M062X-Energy.scforb

并在mol-M062X-Energy.inp的$scf块里添加

.. code-block:: bdf

     guess
      readmo

此时运行mol-M062X-Energy.inp，即可读取B3LYP单点计算的波函数作为初猜（尽管B3LYP单点计算所用的分子结构和当前计算不同，泛函也不相同）。

:guilabel:`Mixorb` 参数类型：整数/浮点数组
---------------------------------------------------
将初猜轨道按一定比例进行混合。Mixorb后的第一行是一个整数（以下记为N），表示需要混合的轨道对的数目；第2行到第N+1行每行为5个数，给出需要混合的轨道对的信息。其中每一行的第一个数表示混合的是alpha还是beta轨道（1为alpha，2为beta；对于RHF/RKS/ROHF/ROKS计算，该数必须为1）；第二个数表示待混合轨道的不可约表示编号（对于不考虑点群对称性的计算，该数必须为1）；第三、第四个数表示待混合轨道在所指定不可约表示下的序号；第五个数（以下记为 :math:`\theta` ，单位：度）表示将这两个轨道按以下公式进行混合：

 * 新的第一个轨道 = :math:`\cos\theta\times` 原来的第一个轨道 + :math:`\sin\theta\times` 原来的第二个轨道
 * 新的第二个轨道 = :math:`\sin\theta\times` 原来的第一个轨道 - :math:`\cos\theta\times` 原来的第二个轨道

一般使用较多的是 :math:`\theta=45` 和 :math:`\theta=90` 的情况，由以上公式可以看出， :math:`\theta=45` 相当于把两个轨道按等比例混合，得到一个同相位组合轨道和一个反相位组合轨道； :math:`\theta=90` 相当于把两个轨道交换。以下算例将第3个不可约表示的第10个beta轨道和第11个beta轨道进行等比例混合（例如为了进行自旋对称性破缺的计算）：

.. code-block:: bdf

     $scf
     UHF
     guess
      readmo
     mixorb
      1
      2,3,10,11,45
     $end

以下算例将第5个不可约表示的第7个轨道和第8个轨道交换，同时还将第6个不可约表示的第3个轨道和第4个轨道交换：

.. code-block:: bdf

     $scf
     ROHF
     guess
      readmo
     mixorb
      2
      1,5,7,8,90
      1,6,3,4,90
     $end

注意一般只有在Guess设定为Readmo时，才能使用Mixorb，否则用户撰写输入文件时尚不清楚初猜轨道的成分，因此无法知道应当混合哪些轨道。

**DFT交换相关泛函关键词**

:guilabel:`DFT` 参数类型：字符串
---------------------------------------------------
指定DFT计算的交换相关泛函。参见BDF支持的交换相关泛函列表。

:guilabel:`D3` 参数类型：Bool型
------------------------------------------------
指定对DFT计算加入Grimme的D3色散矫正。

:guilabel:`FACEX` 参数类型：浮点型
---------------------------------------------------
指定泛函的HF交换项比例。注意目前只有SVWN、SVWN5、PBE、PBE0、PW91、BP86、BLYP、B3LYP、GB3LYP、B3PW91、BHHLYP、SF5050、B2PLYP泛函允许用户自定义FACEX。例如以下输入将PBE的HF交换项比例由默认的0%改为37.5%，得到PBE38泛函：

.. code-block:: bdf

 $scf
 ...
 DFT
  PBE
 facex
  0.375
 $end

:guilabel:`FACCO` 参数类型：浮点型
---------------------------------------------------
指定泛函的MP2相关项比例。注意目前只有B2PLYP泛函允许用户自定义FACCO。例如以下输入通过改变B2PLYP的FACEX和FACCO，同时自定义MP2模块里的spin component scaling参数FSS和FOS（参见 :doc:`mp2` ），自定义了DSD-BLYP泛函：

.. code-block:: bdf

 $scf
 ...
 dft
  B2PLYP
 facex
  0.75
 facco
  0.47
 $end

 $mp2
 fss
  0.60
 fos
  0.46
 $end

:guilabel:`RSOMEGA` / :guilabel:`RS` 参数类型：浮点型
-------------------------------------------------------------------
指定Range-Separated泛函如CAM-B3LYP等的 :math:`\omega` （某些文献称 :math:`\mu` ）系数。
``RS`` 是 ``RSOMEGA`` 的同义词。本关键词在 **scf** 模块中仅用于调试，建议在 :ref:`xuanyuan<xuanyuan>` 模块中设置。

**DFT数值积分格点控制参数关键词**

:guilabel:`NPTRAD` 参数类型：整型
---------------------------------------------------
指定数值积分的径向格点数。本参数一般用于调试程序，正常计算不需要指定该参数。

:guilabel:`NPTANG` 参数类型：整型
------------------------------------------------
指定数值积分的角向格点数。本参数一般用于调试程序，正常计算不需要指定该参数。

:guilabel:`Grid` 参数类型：字符串
------------------------------------------------
 * 默认值：Medium
 * 可选值：Ultra Coarse、Coarse、Medium、Fine、Ultra Fine

指定DFT计算的格点类型。

:guilabel:`Gridtol` 参数类型：浮点型
------------------------------------------------
 * 默认值：1.0E-6（对于meta-GGA为1.0E-8）
 
 指定产生DFT自适应格点的截断阈值。该值越低，格点数越多，因此数值积分精度越高，但计算量也越大。

:guilabel:`Gridtype` 参数类型：整型
------------------------------------------------
 * 默认值：0
 * 可选值：0、1、2、3

指定DFT计算的径向与角向布点方法。

:guilabel:`Partitiontype` 参数类型：整型
---------------------------------------------------
 * 默认值：1
 * 可选值：0、1

指定DFT格点分割类型。0为Becke分割；1为Stratmann-Scuseria-Frisch分割。一般用户无需改变该参数。

:guilabel:`Numinttype` 参数类型：整型
------------------------------------------------
 * 默认值：0

指定数值积分计算方法。本参数一般用于调试程序，正常计算不需要指定该参数。

:guilabel:`NosymGrid` 参数类型：Bool型
---------------------------------------------------
指定数值积分不使用分子对称性，仅用于程序调试。

:guilabel:`DirectGrid` / :guilabel:`NoDirectGrid` 参数类型：Bool型
--------------------------------------------------------------------
指定数值积分采用直接积分的模式，不保存基组值等信息。对于DirectSCF必须使用DirectGrid。只有非DirectSCF情况下才有必要使用NoDirectGrid。本参数一般用于调试程序，正常计算不需要指定该参数。

:guilabel:`NoGridSwitch` 参数类型：Bool型
------------------------------------------------
指定数值积分过程不变换格点。为了降低计算量，BDF默认使用ultra coarse类型格点迭代几次DFT，到了一定的阈值，再使用用户设置的积分格点。NoGridSwitch参数强制不变换积分格点。

:guilabel:`ThreshRho` & :guilabel:`ThreshBSS` 参数类型：浮点型
---------------------------------------------------------------------
控制积分格点的预筛选精度，仅用于程序调试。

**SCF加速算法**

:guilabel:`MPEC+COSX` 参数类型：Bool型
------------------------------------------------
指定利用多级展开库伦势（Multipole expansion of Coulomb potential, MPEC）方法计算J矩阵， COSX（Chain-of-sphere exchange）方法计算K矩阵。
在 ``Scf`` 模块中保留该关键词只是为了向下兼容，建议在 ``Compass`` 模块中设定该关键词。

:guilabel:`Coulpot` 参数类型：整型
------------------------------------------------
 * 默认值：0
 * 可选值：0、1、2

控制MPEC计算产生库伦势Vc与原子核吸引势Vn矩阵的方法。0为利用解析积分计算Vc与Vn；1为利用多级展开计算Vc，利用解析积分计算Vn；2为利用多级展开计算Vc，数值积分计算Vn。

:guilabel:`Coulpotlmax` 参数类型：整型
---------------------------------------------------
 * 默认值：8
 
定义 **MPEC** 方法多级展开最高的角动量L值。


:guilabel:`Coulpottol` 参数类型：整型
------------------------------------------------
 * 默认值：8， 含义为 1.0E-8

定义多级展开的精度阈值，越大越精确。

:guilabel:`MPEC` 参数类型：Bool型
------------------------------------------------
指定用MPEC方法计算J矩阵。

:guilabel:`COSX` 参数类型：Bool型
------------------------------------------------
指定用COSX方法计算K矩阵。

**SCF收敛控制关键词**

:guilabel:`Maxiter` 参数类型：整型
---------------------------------------------------
 * 默认值：100

定义SCF计算的最大迭代次数。

:guilabel:`Vshift` 参数类型：浮点型
------------------------------------------------
 * 默认值：0
 * 可选值：非负实数
 * 建议范围（当取值不为0时）：0.2~1.0
 
指定分子轨道能级移动值。人为地将虚轨道能量加上用户指定数值，以加大HOMO-LUMO能隙，加速收敛。Vshift值越大，收敛过程越不容易出现振荡，但Vshift值太大会导致收敛变慢。一般只有在分子的HOMO-LUMO能隙较小（如小于2 eV），且SCF迭代时能量非单调降低时，才需要设置Vshift。

:guilabel:`Damp` 参数类型：浮点型
---------------------------------------------------
 * 默认值：0
 * 可选值：大于等于0、小于1的实数
 * 建议范围（当取值不为0时）：0.5~0.99
 
指定本次SCF迭代与上次迭代的密度矩阵以一定比例混合（P(i):=(1-C)*P(i)+C*P(i-1)），从而加速SCF收敛。Damp值越大，收敛过程越不容易出现振荡，但Damp值太大会导致收敛变慢。一般只有在SCF迭代能量非单调降低的时候，才需要设置Damp。

:guilabel:`ThrEne` 参数类型：浮点型
------------------------------------------------
 * 默认值：1.d-8

指定SCF收敛的能量阈值（单位：Hartree）。

:guilabel:`ThrDen` 参数类型：浮点型
------------------------------------------------
 * 默认值：5.d-6

指定SCF收敛的均方根密度矩阵元阈值。

:guilabel:`ThreshConv` 参数类型：浮点型
---------------------------------------------------
同时指定SCF收敛的能量和密度矩阵阈值。例：

.. code-block:: bdf

     $scf
     ...
     ThreshConv
      1.d-6 1.d-4
     $end
 
等价于

.. code-block:: bdf

     $scf
     ...
     ThrEne
      1.d-6
     ThrDen
      1.d-4
     $end

.. hint::

 当且仅当以下任何一条满足时，程序认为SCF收敛：（1）能量变化小于ThrEne，且RMS密度矩阵元变化小于ThrDen；（2）能量变化小于ThrEne的0.1倍，且RMS密度矩阵元变化小于ThrDen的1.5倍；（3）最大密度矩阵元变化小于ThrDen。

:guilabel:`NoDiis` 参数类型：Bool型
------------------------------------------------
指定不使用DIIS加速SCF收敛。一般只有在SCF能量以较大幅度（> 1.0E-5）振荡不收敛，且Damp和Vshift效果不明显时，才需要指定NoDiis。

:guilabel:`MaxDiis` 参数类型：整型
---------------------------------------------------
 * 默认值：8

指定DIIS方法的子空间维数。

:guilabel:`SMH` 参数类型：Bool型
------------------------------------------------
指定使用Semiempirical Model Hamiltonian（SMH）方法加速SCF收敛。该方法对于一般的有机体系，可节省约10~15 %的SCF迭代步数，对于具有显著电荷转移、自旋极化的体系，加速收敛效果更为显著。此外该方法还可增加收敛到稳定波函数的概率。对于满足以下情况之一的计算，不支持使用SMH：（1）ROHF/ROKS计算；（2）用户指定了Smeartemp时；（3）基组存在线性相关时。除这些情况外，SMH一律默认开启。

:guilabel:`NoSMH` 参数类型：Bool型
------------------------------------------------
指定不使用SMH方法加速SCF收敛。

:guilabel:`Smeartemp` 参数类型：浮点型
---------------------------------------------------
 * 默认值：0
 * 可选值：非负实数（单位：Kelvin）

指定体系的电子温度，也即通过费米展宽（Fermi Smearing）方法改变前线轨道的占据数。注意BDF如果使用Fermi Smearing方法，最终的能量包含了电子熵能（the electronic entropy）的贡献，名为-TS_ele，从E_tot中间减掉这一项（注意这一项是负的，也就是说需要加上这一项的绝对值）可以得到电子能量。Smeartemp不可与Vshift或SMH同时使用，也不可在FLMO或iOI计算中使用。

该关键词主要有以下几类应用场景：

 * 用于研究温度对电子结构的影响，以及由此导致的对能量、各种性质的影响。例如将Smeartemp设为1000进行结构优化，可以得到1000 K下分子的平衡结构，理论上会和0 K下的平衡结构有少许区别。注意大部分实验（如X射线单晶衍射、微波光谱等）测得的结构是热平均结构而不是平衡结构，而热平均结构对温度的敏感性远较平衡结构更高，所以用户不应盲目利用Smeartemp关键词试图重现实验上观察到的分子结构随温度的变化情况，除非已知所用实验手段测得的是平衡结构。
 * 对于HOMO-LUMO能隙非常小或者前线轨道能级简并的体系，该方法能改善DFT的收敛性，但会轻微改变收敛的结果，为了得到和0 K下相同的SCF结果，需要在Fermi Smearing计算收敛或几乎收敛后，读取波函数作为初猜，继续做一个不使用Fermi Smearing的计算。一般为了达到明显改进收敛的效果，需要设定较高的电子温度，如对纯泛函设定为5000 K左右，对杂化泛函设定为10000 K左右，对HF设定为20000 K左右。
 * 对于HF或DFT破坏分子空间对称性的情况，Smeartemp有助于得到符合空间对称性的轨道。例如环丁二烯的Kohn-Sham波函数仅有 :math:`D_{2h}` 对称性，但在适当的电子温度下计算，可以得到符合 :math:`D_{4h}` 对称性的轨道。

**Fock矩阵对角化控制关键词**

:guilabel:`Sylv` 参数类型：Bool型
---------------------------------------------------
控制在SCF迭代中利用求解Sylvester方程的方法进行块对角化，代替全对角化，以节省计算时间。例如：

.. code-block:: bdf

     $scf
     ...
     sylv
     $end

对于特别大的体系（例如原子数大于1000、基函数数目大于10000）的计算，Fock矩阵对角化占总计算的时间常常不可忽略，此时以上写法通常可以降低计算量，因为用较快的块对角化代替了全对角化，并且可以充分利用Fock矩阵的稀疏性加速计算。但需要注意的是，此时SCF收敛得到的轨道不是正则轨道（特别地，当初猜为FLMO、iOI等计算得到的局域轨道时，收敛的轨道也是局域轨道），不过收敛的占据轨道张成的空间和正则占据轨道张成的空间相同，能量、密度矩阵等也和传统全对角化计算的结果一致。如需要得到正则轨道，应当另写一个不带sylv关键词的BDF输入文件，读取当前计算的收敛轨道作为初猜，进行全对角化计算。

:guilabel:`Iviop` 参数类型：整型
---------------------------------------------------
 * 默认值：无
 * 可选值：1~3
 * 建议值：1

控制在SCF迭代中使用iVI方法，需要与Blkiop=7联用。

:guilabel:`Blkiop` 参数类型：整型
------------------------------------------------
 * 默认值：当指定Sylv时，默认值为3，否则无默认值
 * 可选值：1~8，分别代表SAI、DDS、DNR、DGN、FNR、FGN、iVI、CHC
 * 建议值：3

指定块对角化的方法，通常用于iVI或FLMO计算。如不指定该关键词，默认进行全对角化。

**打印与分子轨道输出控制参数**

:guilabel:`Print` 参数类型：整型
------------------------------------------------
 * 默认值：0
 * 可选值：0、1

仅用于程序调试，控制SCF的打印级别。

:guilabel:`IprtMo` 参数类型：整型
------------------------------------------------
 * 默认值：0
 * 可选值：0、1、2

控制是否打印分子轨道系数。若设为0，不打印分子轨道；若设为1（默认），打印前线轨道（每个不可约表示的HOMO-5到LUMO+5）的占据数、能量、系数；若设为2，打印所有轨道的占据数、能量、系数。

:guilabel:`Noscforb` 参数类型：Bool型
---------------------------------------------------
强制不将分子轨道存入.scforb文件。

:guilabel:`Pyscforb` 参数类型：Bool型
------------------------------------------------
控制将SCF收敛轨道存储为Pyscf轨道格式。

:guilabel:`Molden` 参数类型：Bool型
---------------------------------------------------
控制将分子轨道输出为Molden格式，以做后续的波函数分析。

**相对论单电子性质计算**

相对论单电子性质计算支持sf-X2C哈密顿及其局域变体（ ``xuanyuan`` 模块中 ``Heff`` 设置为 21，22，或23）。

:guilabel:`Reled` 参数类型：整型
---------------------------------------------------
对于原子序数大于等于此值的元素计算 **有效接触密度** 。无默认值。
必须结合 ``xuanyuan`` 模块中的有限核模型 ``nuclear`` = 1 一起使用。

:guilabel:`Relefg` 参数类型：整型
---------------------------------------------------
对于原子序数大于等于此值的元素计算 **电场梯度** （EFG）张量；对于有核四极矩实验值的同位素 :cite:`NQM2018` ，还计算 **核四极耦合常数** （NQCC）。无默认值。
必须结合 ``xuanyuan`` 模块中的有限核模型 ``nuclear`` = 1 一起使用。

**基组线性相关检查关键词**

:guilabel:`Checklin` 参数类型：Bool型
------------------------------------------------
强制SCF进行基组线性相关检查。BDF默认对DirectSCF进行基组线性相关检查，以提高使用弥散基函数时的SCF收敛性。

:guilabel:`Tollin` 参数类型：浮点型
---------------------------------------------------
 * 默认值：1.0E-7

控制基组线性相关检查的阈值。

**mom方法控制关键词**

mom是一种ΔSCF方法，可以通过强制SCF每次迭代的占据轨道与初始占据轨道最大重叠来使SCF收敛到激发态。mom方法通常比基态收敛困难。

:guilabel:`Iaufbau` 参数类型：整型
------------------------------------------------
 * 默认值：当用户设定了Occupy、Alpha或Beta时为0，否则为1
 * 可选值：0、1、2、3

定义用什么方法指定轨道占据数。0表示轨道占据数始终与初猜一致；1表示按照Aufbau规则指定轨道占据数；2表示按照mom方法指定轨道占据数，即令占据数尽可能和初始猜测轨道保持一致，结合前述Mixorb关键词可以实现用DeltaSCF方法计算激发态；3用于程序调试，正式计算一般无需使用。

:guilabel:`IfPair` & :guilabel:`hpalpha` & :guilabel:`hpbeta` 参数类型：整型
-----------------------------------------------------------------------------
Ifpair参数指定电子如何激发，确定mom方法的电子占初态，必须与hpalpha和hpbeta参数联用。电子激发通过相对于基态通过指定从占据轨道到虚轨道的激发确定。

.. code-block:: bdf

      #一个分子，其分子轨道分属4个不可约表示。下面的输入激发不可约表示1的alpha轨道5、6上的电子
      #到alpha轨道7、8，不可约表示3的alpha轨道3上的电子到alpha轨道4，不可约表示1的beta轨道7上
      #的电子到beta轨道8.
      $scf
      Ifpair
      Hpalpha
      2
      5 0 3 0
      8 0 4 0
      6 0 0 0
      9 0 0 0
      Hbeta
      1
      7 0 0 0
      8 0 0 0     
      ...
      $end

:guilabel:`Pinalpha` & :guilabel:`Pinbeta` 参数类型：整型
-----------------------------------------------------------
指定固定的分子轨道。

:guilabel:`EnableSecondOrderScf` 参数类型: Bool 型
-----------------------------------------------------------
指定启用二阶 SCF 并使用默认设置. 二阶收敛应仅在无法通过其它收敛算法得到稳定解时使用.

.. hint::
    * 二阶 SCF 目前不支持 iOI 等算法
    * 二阶 SCF 目前不支持限制性开壳层计算
    * 二阶 SCF 目前不支持相对论计算

:guilabel:`DisableSecondOrderScf` 参数类型: Bool 型
-----------------------------------------------------------
指定禁用二阶SCF.

:guilabel:`SecondOrderConfig` 参数类型: 字符串
-----------------------------------------------------------
指定二阶 SCF 所用的高级设置. 一般用户仅需指定 ``EnableSecondOrderScf`` 关键词, 无需指定该项.

.. code-block:: bdf

    $Scf
        ...
        SecondOrderConfig
            Enable
            EnableExpression
                AfterIteration 10
            LevelShiftGradientThreshold
                1e-3
            ConvergeGradientThreshold
                1e-6
            ConvergeRotationThreshold
                1e-9
            MaxIterationCycle
                16
            InitialTrustRadius
                0.4
            MaxTrustRadius
                5
            MaxConjugateGradientIterationCycle
                16
            MaxDavidsonIterationCycle
                16
            CorrectionType
                Olsen
            LinearSolverTolerance
                1e-4
            AllowConverge
            ScfConvergeGradientThreshold
                1e-7
        EndSecondOrderConfig
        ...
    $End

* ``Enable``: 指定启用二阶 SCF 并将启用表达式将为默认设置
* ``Disable``: 指定禁用二阶 SCF
* ``EnableExpression``: 指定启用表达式
    指定启用表达式将隐式设定 ``Enable`` 关键词. 其内容可为

    - ``AfterIteration`` + 整型数: 指定在一定标准 SCF 迭代后启用
    - ``AfterDeltaEnergyLessThan`` + 浮点数: 指定在执行标准SCF迭代至能量误差低于一定值后启用
    - ``AfterDeltaRmsDensityLessThan`` + 浮点数: 指定在执行标准SCF迭代至密度矩阵之误差低于一定值后启用
    - 自定义逻辑表达式. 注, 我们提供自定义表达式的目的是为方便开发人员调试程序及为高级用户提供更灵活的选项, 如果您对其感觉不适请考虑使用上文所述的默认选项或预设选项. 自定义表达式可用关键词为 ``Iteration``, ``DeltaEnergy``, 及 ``DeltaRmsDensity``. 可用算符有 ``&``, ``|``, ``!``, ``>``, ``<``, ``=``, 及 ``[]``. 算符均不可串联, 并在作用至变量后必须以逻辑求值算符 ``[]`` 括起. 表达式不区分大小写, 忽略全部空格字符, 这意味着 "DeltaRmsDensity" 与 "Delta RMS Density" 等价. 例:
     ``[ [ Iteration > 10 ] & [ [ DeltaEnergy < 1e-3 ] | [![ DeltaRmsDensity > 2.5e-3 ]] ] ]``
* ``LevelShiftGradientThreshold``, 浮点型: 指定在能量-轨道梯度低于一定值后解除可信半径, 改用 Newton-Raphson 法计算旋转矢量
* ``ConvergeGradientThreshold``, 浮点型: 指定在能量-轨道梯度值模低于一定值后停止二次 SCF 微迭代
* ``ConvergeRotationThreshold``, 浮点型: 指定在旋转矢量之模长低于一定值后停止二次 SCF 微迭代
* ``MaxIterationCycle``, 整型: 指定最大二阶 SCF 微迭代次数直到做一次标准 SCF 更新
* ``InitialTrustRadius``, 浮点型: 指定用 Levenberg-Marquardt 法求旋转矢量时所用的初始可信半径
* ``MaxTrustRadius``, 浮点型: 指定用 Levenberg-Marquardt 法求旋转矢量时所用的最大可信半径
* ``MaxConjugateGradientIterationCycle``, 整型: 指定用共轭梯度法求解 Newton-Raphson 方程时所用的最大迭代次数. 最终矢量将被用作旋转矢量即使未收敛
* ``MaxDavidsonIterationCycle``, 整型: 指定用 Davidson 对角化求解 Levenberg-Marquardt 方程时所用的最大迭代次数. 最终矢量将被用作旋转矢量即使未收敛
* ``CorrectionType``, 字符串: 指定 Davidson 对角化所用的矫正方法, 可选项为 ``DavidsonDPR`` (也作 ``DPR``), ``JacobiDavidson``, 及 ``Olsen``
* ``LinearSolverTolerance``, 浮点型: 指定 Davidson 对角化所用线性方程求解器所用收敛阈值
* ``ExcludeNonOccupiesFromRotation``:  指定将在构造原理下本该为占据轨道但用户明确指定为非占据轨道的轨道从轨道旋转对中排除, 以防止塌陷至构造原理所表示的态. 该选项只在做 ΔSCF 计算时生效.
* ``IncludeNonOccupiesInRotation``: 指定将所有轨道都包含至旋转对中. 该选项只在做 ΔSCF 时生效.
* ``AllowConverge``: 允许 SCF 于二次收敛迭代过程中宣布 SCF 已收敛
* ``ForbidConverge``: 禁止 SCF 于二次收敛迭代过程中宣布 SCF 已收敛
* ``ScfConvergeGradientThreshold``, 浮点型: 指定在能量-轨道梯度之模低于一定值后认为 SCF 已收敛. 仅在已设 ``AllowConverge`` 时生效
