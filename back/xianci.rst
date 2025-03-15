xianci模块
================================================
xianci模块来自Xi'an-CI程序包，执行ucMRCI, icMRCI，XSDSCI, CB-MRPT2/3，MS-CASPT2, XMS-CASPT2, XDW-CASPT2, RMS-CASPT2, MS-NEVPT2，SS-NEVPT3, SDSPT2f, SDSPT2, SDSCIf, SDSCI等计算。

**基本控制参数**

:guilabel:`Roots` 参数类型：整型
------------------------------------------------
指定计算的根（电子态）的数目。
* 若mcscf只算同一种空间与自旋对称性，xianci模块将读取mcscf模块计算的根的数目作为默认值，进而不需要设置此参数。
* 默认值：1

:guilabel:`Istate` 参数类型：整型
------------------------------------------------
指定计算的根的数目并设置需要计算的根的编号。若使用此关键词，关键词``Roots``将失效。

.. attention::
 此关键词只可以用于所有CASPT2,NEVPT2, SDSPT2, SDSCI and XSDSCI类方法。

示例如下：第一行1个整数，设置需要计算的态的数目，第二行设置所选电子态（根）的编号。

.. code-block:: bdf

     $xianci
     ...
     istate
     2
     1 3 
     $end

:guilabel:`Spin` 参数类型：整型
------------------------------------------------
指定计算电子态的自旋多重度2S+1。
* 若mcscf只算同一种空间与自旋对称性，xianci模块将读取mcscf模块计算的根的数目作为默认值，进而不需要设置此参数。
* 默认值：1
:guilabel:`Symmetry` 参数类型：整型
------------------------------------------------
指定计算电子态的对称性。
* 若mcscf只算同一种空间与自旋对称性，xianci模块将读取mcscf模块计算的根的数目作为默认值，进而不需要设置此参数。
* 默认值：1

:guilabel:`Frozen` 参数类型：整型数组
------------------------------------------------
指定计算冻结的每个不可约表示的双占据（inactive）轨道数。建议冻结原子的Core轨道。 
* 默认是不冻结双占据轨道。

:guilabel:`Core` 参数类型：整型数组
------------------------------------------------
指定计算冻结的每个不可约表示的双占据（inactive）轨道数。建议冻结原子的Core轨道。 
* 默认是不冻结双占据轨道。

:guilabel:`Dele` 参数类型：整型数组
------------------------------------------------
指定计算冻结的每个不可约表示的未占据（virtual）轨道数。
* 默认是不冻结未占据轨道。

:guilabel:`Electron` 参数类型：整型
------------------------------------------------
计算相关轨道电子数。
* 默认值源自mcscf模块，可以不用输入。

:guilabel:`Inactive` 参数类型：整型数组
------------------------------------------------
指定计算每个不可约表示的双占据轨道数。
* 默认值来源于mcscf模块，可以不用输入。

:guilabel:`Active` 参数类型：整型数组
------------------------------------------------
指定计算每个不可约表示活性轨道数。
* 默认值来源于mcscf模块，可以不用输入。

:guilabel:`XvrUse` 参数类型：Bool型
------------------------------------------------
当未使用关键词 'Dele' 设置需删除的分子轨道（MOs）时，关键字 'XvrUse' 用于通过 MCSCF XVR 方法选择性删除虚轨道。
.. attention::
 若同时指定了 'Dele' 和 'XvrUse'，则 'Dele' 关键字优先于 'XvrUse'。

* 完整输入逻辑参见示例：test126.inp

:guilabel:`Rootprt` 参数类型：整型
------------------------------------------------
指定采用numgrad模块计算数值梯度的所需设定的电子态编号。
* 默认值：1

:guilabel:`Orbtxt` 参数类型：字符串型
------------------------------------------------
指定读取分子轨道文件的后缀名。

:guilabel:`CVS` 参数类型：Bool型
------------------------------------------------
指定计算时生成Core Valence Separation的DRT，并使用此DRT计算Core Valence激发态。
  
:guilabel:`ReadDRT` 参数类型：Bool型
------------------------------------------------
指定计算时读取工作目录中$WORKDIR/$BDFTASK.cidrt中存储的DRT信息，从而减少DRT生成所需时间。
* 推荐在计算大活性空间体系使用。
  
:guilabel:`Nexci` 参数类型：整型
------------------------------------------------
指定从参考组态激发的电子数。
* 默认值：2
* 可选值：1 （仅单激发）,>=3（相对于参考组态的活性轨道内三电子以上激发）

:guilabel:`Readref` 参数类型：整型
------------------------------------------------
自动从$WORKDIR/BDFTASK.select_*_#中读取参考组态，其中*表示自旋多重度，#代表不可约表示。
* 默认值来源于mcscf模块，可以不用输入。
* 若mcscf模块未设定关键词"iCI"或"iCIPT2"，而需要选定参考组态，则需要设定此关键词。

:guilabel:`Node` 参数类型：整型
------------------------------------------------
指定存储生成CAS为参考空间（P空间）的sub-DRTs中的结点所需数组的初始大小。对于选态方法生成的sub-DRTs所需数组不需要预设。
* 默认值：1000000

:guilabel:`Pmin` 参数类型：浮点型
------------------------------------------------
指定$WORKDIR/BDFTASK.select_*_#中组态系数大于此值的参考组态为用于构造激发组态的参考组态。
* 默认值: Pmin=0.0, 若mcscf模块加入关键词iCI或iCIPT2，则默认值为Pmin=Cmin （Cmin来源于mcscf模块）。
* 建议值：Pmin=1.d-3

:guilabel:`QminDV` 参数类型：浮点型
------------------------------------------------
指定裁剪Q子空间（\bar{D}V，双电子激发算符中包括3个活性轨道和1个双占据轨道）未收缩激发组态的一级相互作用空间（FOIS）值的阈值。
* 默认值: 0.0 
* 建议值：1.d-5

:guilabel:`QminVD` 参数类型：浮点型
------------------------------------------------
指定裁剪Q子空间（\bar{V}D，双电子激发算符中包括3个活性轨道和1个未占据轨道）未收缩激发组态的一级相互作用空间（FOIS）值的阈值。
* 默认值: 0.0 
* 建议值：1.d-5

:guilabel:`Qnex` 参数类型：Bool型
------------------------------------------------
指定不选择DVD近似。DVD近似：在生成\bar{D}V与\bar{V}D的激发组态时，部分3活性轨道参与的双激发组态将被忽略。
* 默认值: .false.

:guilabel:`Epic` 参数类型：浮点型
------------------------------------------------
指定系数矩阵存储内收缩函数系数的阈值。
* 默认值: QminVD=0.0 
* 建议值：QminVD=1.d-5

:guilabel:`Seleref` 参数类型：整型
------------------------------------------------
指定MRCI计算的参考轨道组态（orbital configuration, oCFG）。该参数有nref+1行，nref是参考轨道组态的数目。
* 默认值：若使用关键词“readref”选参考组态，则可以不用此关键词。
* 若用户想重新指定oCFG，则需要设定此关键词及nref个选定oCFG。

.. code-block:: python

     $xianci
     ...
     seleref
     3 
     2200
     2110
     2020
     $end

第一行：1个整数，指定参考态数目nref。
第二至nref+1行给出参考轨道组态。

:guilabel:`Prtcri` 参数类型：浮点型
------------------------------------------------
指定打印输出的CSF的阈值。
* 默认值：0.05

:guilabel:`Ethres` 参数类型：浮点型
------------------------------------------------
指定H0矩阵对角化的能量（本征值）收敛阈值。
* 默认值：1.D-8

:guilabel:`Conv` 参数类型：浮点型数组
------------------------------------------------
指定MRCI计算H矩阵迭代对角化的收敛阈值。输入三个浮点数，分别控制MRCI的迭代大的能量、波函数和残余向量收敛阈值。
* 默认值：1.D-8、1.D-6、1.D-8

:guilabel:`Maxiter` 参数类型：整型
------------------------------------------------
指定H0或H矩阵迭代对角化最大迭代次数。
* 默认值：200

:guilabel:`InitHDav` 参数类型：整型
------------------------------------------------
指定在MRCI的迭代对角化过程中，设置初始向量的方式：
* 默认值：1  使用与能量最低的组态函数（CSFs）耦合最大的激发组态作为初始向量。
* 可选值：2  根据CI哈密顿对角元的从低到高的能级顺序选择初始向量。
* 可选值：3  利用参考波函数作为Davidson对角化的初始向量。

:guilabel:`InitH0Dav` 参数类型：整型
------------------------------------------------
指定在H0的迭代对角化过程中，设置初始向量的方式：
* 默认值：2  根据CI哈密顿对角元的从低到高的能级顺序选择初始向量。
* 可选值：1  使用与能量最低的组态函数（CSFs）耦合最大的激发组态作为初始向量。

:guilabel:`Cipro` 参数类型：Bool型
------------------------------------------------
指定计算单电子约化密度矩阵及相关的性质，如偶极矩等。

:guilabel:`DCRI` 参数类型：浮点型
------------------------------------------------
指定内收缩组态函数的正交化阈值。
* 默认值：1.D-12

:guilabel:`EPCC` 参数类型：浮点型
------------------------------------------------
设置忽略的收缩组态耦合系数阈值。较大的值有利于提高icMRCI的计算效率，但会降低精度。
* 默认值：1.D-20

:guilabel:`Qfix` 参数类型：浮点型
------------------------------------------------
指定iCMRCI迭代对角化过程中需要优化的组态。由SDSPT2(f)计算得到的一阶波函数中的系数大于此阈值的激发组态的系数才需要优化。 
* 默认值：0.0

:guilabel:`Ncisave` 参数类型：整型
------------------------------------------------
指定可以完全对角化的H0矩阵的维数。对于内存空间较大的计算机可以增大此值以减少矩阵元的重复计算。
* 默认值：50000

:guilabel:`Saveact` 参数类型：Bool型
------------------------------------------------
指定H0迭代对角化计算时存储耦合系数至内存，从而提高计算效率，但在计算大活性空间时可能出现所需内存空间不足的问题。
  
:guilabel:`Setlpact` 参数类型：整型
------------------------------------------------
指定H0迭代对角化计算时用于存储所有耦合系数的数组的初始大小。
初始输入越大，动态增大数组的次数越少，计算效率越高，但在计算大活性空间时可能出现所需内存空间不足的问题。
* 默认值: 100000000
 
:guilabel:`Setblkact` 参数类型：整型
------------------------------------------------
指定H0迭代对角化计算时用于存储耦合系数类的数组的初始大小。
初始输入越大，动态增大数组的次数越少，计算效率越高，但在计算大活性空间时可能出现所需内存空间不足的问题。
* 默认值: 10000000
 
:guilabel:`Nosavelp` 参数类型：Bool型
------------------------------------------------
指定icMRCI计算时不存储（内收缩）耦合系数，使用会降低计算效率，但能在计算大活性空间时节省硬盘存储空间。

:guilabel:`Setloop` 参数类型：整型
------------------------------------------------
指定MRCI迭代对角化计算时用于存储一类耦合系数的数组的初始大小。
初始输入越大，动态增大数组的次数越少，计算效率越高，但在计算大活性空间时可能出现所需内存空间不足的问题。
* 默认值: 10000000
 
:guilabel:`Setblk` 参数类型：整型
------------------------------------------------
指定MRCI迭代对角化计算时用于存储耦合系数类的数组的初始大小。
初始输入越大，动态增大数组的次数越少，计算效率越高，但在计算大活性空间时可能出现所需内存空间不足的问题。
* 默认值: 10000000

**内收缩CI方法选择参数**

:guilabel:`FCCI` 参数类型：Bool型
------------------------------------------------
指定执行激发态空间（Q）全内收缩MRCI（icMRCI）计算，但参考态空间（P）不收缩，微扰计算会收缩参考态空间。
* 默认采用此方法。

:guilabel:`XSDSCI` 参数类型：Bool型
------------------------------------------------
指定执行FCCI计算。
* 初始猜测的激发波函数的系数源自基于SDSPT2计算（Dyall哈密顿作为H0），在计算低激发态时，可以完全避免Intruder State问题。

:guilabel:`VSD` 参数类型：Bool型
------------------------------------------------
虚拟空间分解(VSD)通过将大基组虚轨道(MOs)投影到小基组空间，
利用奇异值分解(SVD)筛选出强关联空间，从而将高维虚轨道空间划分为物理意义明确的子空间。
该方法与XSDSCI相结合，可显著提升多参考态计算的效率。
* 示例见test126.inp

:guilabel:`NoVDVP` 参数类型：Bool型
------------------------------------------------
指定跳过Q子空间\bar{V}D和\bar{V}P与零级波函数之间的CI哈密顿矩阵元计算。

:guilabel:`SDSCI` 参数类型：Bool型
------------------------------------------------
指定执行SDSCI计算。
* 激发波函数的系数源自基于SDSPT2计算（Dyall哈密顿作为H0），在计算低激发态时，可以完全避免Intruder State问题。
* 推荐使用此方法，是目前xianci模块中计算量最小的MRCI方法。

:guilabel:`SDSCIf` 参数类型：Bool型
------------------------------------------------
指定执行SDSCIf计算。
* 激发波函数的系数源自基于SDSPT2f计算（广义Fock算符作为H0），可能出现Intruder State问题。

:guilabel:`UCCI` 参数类型：Bool型
------------------------------------------------
指定执行非收缩MRCISD（ucMRCI）计算。

:guilabel:`NICI` 参数类型：Bool型
------------------------------------------------
指定执行不收缩全内空间激发的icMRCI计算。

:guilabel:`CWCI` 参数类型：Bool型
------------------------------------------------
指定执行Celani-Werner收缩的icMRCI计算。

:guilabel:`WKCI` 参数类型：Bool型
------------------------------------------------
指定执行Werner-knowles收缩的WicMRCI计算。

:guilabel:`SDCI` 参数类型：Bool型
------------------------------------------------
指定执行SDCI模式的icMRCI计算，收缩程度与精度介于CWCI与WKCI之间。

**多参考态微扰计算相关参数**

:guilabel:`CASPT2` 参数类型：Bool型
------------------------------------------------
指定执行MS-CASPT2（Multi-State CASPT2），对每个参考态构建自己的Q空间。

:guilabel:`RMSCASPT2` 参数类型：Bool型
------------------------------------------------
指定执行RMS-CASPT2（Rotated Multi-State CASPT2），对每个参考态构建自己的Q空间。

:guilabel:`XMSCASPT2` 参数类型：Bool型
------------------------------------------------
指定执行RMS-CASPT2（Extened Multi-State CASPT2），对每个参考态构建自己的Q空间。

:guilabel:`XDWCASPT2` 参数类型：Bool型
------------------------------------------------
指定执行XDW-CASPT2（Extened Dynamic Weight Multi-State CASPT2），对每个参考态构建自己的Q空间。

:guilabel:`XDWPara` 参数类型：浮点型
------------------------------------------------
指定执行XDW-CASPT2（Extened Dynamic Weight Multi-State CASPT2）所需参数。
* 默认值：50
* 0: XMS-CASPT2; 无穷大：RMS-CASPT2。

:guilabel:`SDSPT2f` 参数类型：Bool型
------------------------------------------------
指定执行SDSPT2f计算。
* 激发波函数的系数采用微扰方法（广义Fock算符作为H0），可能出现Intruder State问题。

:guilabel:`Rshift` 参数类型：浮点型
------------------------------------------------
指定弱化CASPT2等基于广义Fock算符作为H0方法的Intruder State问题所需Real Level Shift参数。
** 默认值：0.0
* 建议值: 0.3

:guilabel:`Ishift` 参数类型：浮点型
------------------------------------------------
指定弱化CASPT2等基于广义Fock算符作为H0方法的Intruder State问题所需Imaginary Level Shift参数。
* 默认值：0.0
* 建议值: 0.1

:guilabel:`NEVPT2` 参数类型：Bool型
------------------------------------------------
指定执行MS-NEVPT2（Multi-State NEVPT2），对每个参考态构建自己的Q空间。

:guilabel:`SDSPT2` 参数类型：Bool型
------------------------------------------------
指定执行SDSPT2计算。
* 激发波函数的系数采用微扰方法（Dyall哈密顿作为H0），在计算低激发态时，可以完全避免Intruder State问题。

:guilabel:`DVRLS` 参数类型：浮点型
------------------------------------------------
指定弱化NEVPT2等基于Dyall哈密顿作为H0方法在计算高激发态时Q子空间（\bar{D}V）的Intruder State问题所需Real Level Shift参数。
* 默认值：0.0
* 建议值: 0.3

:guilabel:`VDRLS` 参数类型：浮点型
------------------------------------------------
指定弱化NEVPT2等基于Dyall哈密顿作为H0方法在计算高激发态时Q子空间（\bar{V}D）的Intruder State问题所需Real Level Shift参数。
* 默认值：0.0
* 建议值: 0.3

:guilabel:`DDRLS` 参数类型：浮点型
------------------------------------------------
指定弱化NEVPT2等基于Dyall哈密顿作为H0方法在计算高激发态时Q子空间（\bar{D}D）的Intruder State问题所需Real Level Shift参数。
* 默认值：0.0
* 建议值: 0.3

:guilabel:`DVILS` 参数类型：浮点型
------------------------------------------------
指定弱化NEVPT2等基于Dyall哈密顿作为H0方法在计算高激发态时Q子空间（\bar{D}V）的Intruder State问题所需Imaginary Level Shift参数。
* 默认值：0.0
* 建议值: 0.1
* 不建议使用此参数。  

:guilabel:`VDILS` 参数类型：浮点型
------------------------------------------------
指定弱化NEVPT2等基于Dyall哈密顿作为H0方法在计算高激发态时Q子空间（\bar{V}D）的Intruder State问题所需Imaginary Level Shift参数。
* 默认值：0.0
* 建议值: 0.1
* 不建议使用此参数。  

:guilabel:`DDILS` 参数类型：浮点型
------------------------------------------------
指定弱化NEVPT2等基于Dyall哈密顿作为H0方法在计算高激发态时Q子空间（\bar{D}D）的Intruder State问题所需Imaginary Level Shift参数。
* 默认值：0.0
* 建议值: 0.1
* 不建议使用此参数。  

:guilabel:`SAFock` 参数类型：Bool型
------------------------------------------------
指定在NEVPT2、SDSPT2、SDSCI计算中采用态平均（SA）的分子轨道能量和积分。
* 默认值：.true.

:guilabel:`SDFock` 参数类型：Bool型
------------------------------------------------
指定在NEVPT2、SDSPT2、SDSCI计算中采用态指定（SS）的分子轨道能量和与态平均（SA）的分子轨道积分。
* 默认值：.false.

:guilabel:`SSFock` 参数类型：Bool型
------------------------------------------------
指定在NEVPT2计算中采用态指定（SS）的分子轨道能量和积分。
* 默认值：.false.

:guilabel:`Dylan` 参数类型：Bool型
------------------------------------------------
指定截断近似计算SDSPT2(f)与SDSCI(f)所需Secondary states。
* 默认使用此方案生成
* 对于活性空间较大的SDSPT2(f)和SDSCI(f)计算，可以采用关键词“Dylan”截断能量较高的Ps函数对Secondary states的贡献。
  基于此的SDSPT2(f)和SDSCI(f)方法构建的有效哈密顿矩阵的维数为3N维。
  一般情况下可以保持计算精度，但不同的分子构型所选Ps函数数目不同。
  
:guilabel:`Nolan` 参数类型：Bool型
------------------------------------------------
指定不计算SDSPT2(f)与SDSCI(f)所需Secondary states。
* 对于活性空间较大的SDSPT2(f)和SDSCI(f)计算，可以采用关键词“Nolan”取消计算量较大的构建Ps波函数的计算过程。
  基于此的SDSPT2(f)和SDSCI(f)方法构建的有效哈密顿矩阵的维数为2N维，一般情况下计算精度降低较小。
  但需要强调的是：在计算过程中出现电子态相交（如圆锥相交点）时，计算精度可能有一定程度的降低。

:guilabel:`Dolan` 参数类型：Bool型
------------------------------------------------
指定采用Lanczos方法计算SDSPT2(f)与SDSCI(f)所需Secondary states。
* 对于活性空间较大的SDSPT2(f)和SDSCI(f)计算，采用关键词“Dolan”计算Secondary states的计算量非常大。
  基于此的SDSPT2(f)和SDSCI(f)方法构建的有效哈密顿矩阵的维数为3N维。
  一般情况下可以保持计算精度，但较大的计算量使得不推荐使用此方案。
 
:guilabel:`DEPENST` 参数类型：Bool型
------------------------------------------------
指定在Dyall哈密顿中使用态指定的Fock对角元。默认：态平均的Fock矩阵对角元。

:guilabel:`MR-NEVPT2` 参数类型：Bool型
------------------------------------------------
指定执行Multi-reference NEVPT2计算。
* 对所有的参考态构建全局正交的组态空间。

:guilabel:`NEVPT3` 参数类型：Bool型
------------------------------------------------
指定执行SS-NEVPT3计算。
* 对每个态是独立的Q空间。

:guilabel:`CBMPRT2` 参数类型：Bool型
------------------------------------------------
指定执行CBMRPT2计算。

:guilabel:`MR-CBMRPT2` 参数类型：Bool型
------------------------------------------------
指定执行MR-CBMPRT2计算。
* 对所有的参考态构建全局正交的组态空间。

:guilabel:`CBMRPT3` 参数类型：Bool型
------------------------------------------------
指定执行CBMRPT3计算。
* 对每个态是独立的Q空间。

**算例**

:guilabel:`test069.inp`
------------------------------------------------
.. attention::
   SDSPT2(f)，SDSCI(f)，XSDSCI，icMRCI的能量取+Q1（Pople Correction）的结果。
   ucMRCI的能量取+Q3（Davdison Correction）的结果。   

.. code-block:: bdf

     $xianci
     core 
     2 0 0 2  
     nroots
     1
     spin
     1 
     symmetry
     1
     pmin
     1.d-3
     qmindv
     1.d-5
     qminvd
     1.d-5
     epic
     1.d-5
     CASPT2 # MS-CASPT2 with generalized Fock as H0
     DBLOCH # the threshold of solving BLOCH equation
     1.d-4  # default : 1.d-4
     RLS    # Real Level Shift
     0.0    # default : 0.0
     #ILS    # Imaginary Level Shift
     #0.0    # default : 0.0
     $end

     Output :

     CASPT2 calculation is completed.

     NROOT        MC ENERGY       SS-CASPT2 ENERGY    MS-CASPT2 ENERGY    SS-CASPT3 ENERGY    MS-CASPT3 ENERGY
       1       -154.98370235       -155.47704723       -155.47704723          0.00000000          0.00000000
 
.. code-block:: bdf

     $xianci
     core
     2 0 0 2
     nroots
     1
     spin
     1
     symmetry
     1
     nevpt2 
     $end

     Output:

     NEVPT2 calculation is completed.

     NROOT        MC ENERGY       SS-NEVPT2 ENERGY    MS-NEVPT2 ENERGY    SS-NEVPT3 ENERGY    MS-NEVPT3 ENERGY
       1       -154.98370416       -155.47772092       -155.47772092          0.00000000          0.00000000

.. code-block:: bdf
 
     $xianci
     core
     2 0 0 2
     nroots
     1
     spin
     1
     symmetry
     1
     sdspt2f 
     dbloch 
     1.d-4 
     rls 
     0.0 
     $end
 
     Output:

     MRPT2 calculation is completed.

     NROOT   MC ENE      SS-CASPT2 ENE   MS-CASPT2 ENE    SDSPT2 ENE  SDSPT2+Q1 ENE  SDSPT2+Q2 ENE   SDSPT2+Q3 ENE   DAVCOEF
       1  -154.98370416  -155.47702635   -155.47702635 -155.41225671  -155.47144162  -155.47211363  -155.46852939   0.883932
   
.. code-block:: bdf
 
     $xianci
     core
     2 0 0 2
     nroots
     1
     spin
     1
     symmetry
     1
     sdspt2 
     $end

     Output:

     MRPT2 calculation is completed.

     NROOT   MC ENE     SS-NEVPT2 ENE  MS-NEVPT2 ENE  SDSPT2 ENE    SDSPT2+Q1 ENE  SDSPT2+Q2 ENE   SDSPT2+Q3 ENE   DAVCOEF
       1  -154.98370416 -155.47772092  -155.47772092  -155.41222583 -155.47205111  -155.47273880   -155.46903845   0.882941

.. code-block:: bdf

     $xianci
     core
     2 0 0 2
     nroots
     1
     spin
     1
     symmetry
     1
     sdscif 
     $end

     Output:

     MRPT2 calculation is completed.

     NROOT   MC ENE    SS-CASPT2 ENE  MS-CASPT2 ENE  SDSCI  ENE    SDSCI+Q1  ENE  SDSCI+Q2  ENE   SDSCI+Q3  ENE   DAVCOEF
       1 -154.98370416 -155.47702635  -155.47702635  -155.43865322 -155.51060490  -155.51155875   -155.50597757   0.871094
     
.. code-block:: bdf

     $xianci
     core
     2 0 0 2
     nroots
     1
     spin
     1
     symmetry
     1
     sdsci 
     $end
     
     Output:

     MRPT2 calculation is completed.

     NROOT   MC ENE     SS-NEVPT2 ENE  MS-NEVPT2 ENE  SDSCI  ENE    SDSCI+Q1  ENE   SDSCI+Q2  ENE   SDSCI+Q3  ENE   DAVCOEF
       1  -154.98370416 -155.47772092  -155.47772092  -155.43734298 -155.50941634   -155.51037685   -155.50474252   0.870644

.. code-block:: bdf
     
     $xianci
     core
     2 0 0 2
     nroots
     1
     spin
     1
     symmetry
     1
     xsdsci 
     ncisave
     10
     $end

     Output:

     Roots of Heff are calculated are listed below: 
 
                     ENE             ENE + Pople       ENE + App Pople       ENE + DAV           ENE + MEISS
     root   1   -155.44999113       -155.52660992       -155.52767146       -155.52133469       -155.51198622
    

.. code-block:: bdf

     $xianci
     core
     2 0 0 2
     nroots
     1
     spin
     1
     symmetry
     1
     $end

     Output:  
     Roots of Heff are calculated are listed below:  
                       ENE           ENE + Pople       ENE + App Pople       ENE + DAV           ENE + MEISS
     root   1    -155.45099589       -155.52816454       -155.52923990       -155.52280494       -155.51339548
 

:guilabel:`test080.inp`
------------------------------------------------

:guilabel:`test095.inp`
------------------------------------------------

:guilabel:`test126.inp`
------------------------------------------------

:guilabel:`test131.inp`
------------------------------------------------

:guilabel:`test139.inp`
------------------------------------------------

:guilabel:`test148.inp`
------------------------------------------------


