分子结构优化 - BDFOPT模块
================================================
BDFOPT模块是BDF程序的分子几何结构优化模块，可用来寻找能量极小点、过渡态、锥形交叉点等。与其他模块不同，包含bdfopt模块的输入文件，并不是按照模块的先后顺序线性执行的，详见“快速入门”部分结构优化相关章节。

:guilabel:`Solver` 参数类型：整型
------------------------------------------------
 * 默认值：0
 * 可选值：0、1

指定几何结构优化使用的求解器。

 * ``Solver=0`` ，BDF将使用外带的DL-Find优化器进行优化，该优化器支持在直角坐标或内坐标下，进行能量极小化、过渡态搜索、高阶鞍点搜索、锥形交叉点搜索、最小能量交叉点（MECP）搜索等。
 * ``Solver=1`` ，BDF将使用自带的优化器进行优化。

如果在冗余内坐标下（参见 ``ICoord`` 关键词）进行能量极小化、过渡态搜索，建议使用 ``Solver=1`` 。

.. attention::

  由于DL-FIND与BDF默认的坐标转动有冲突，必须在 ``compass`` 模块中加上关键词 ``norotate`` 禁止分子转动，或用 ``nosymm`` 关闭对称性；对于双原子和三原子分子，只能用 ``nosymm`` 。此冲突今后会解决。

:guilabel:`Imulti` 参数类型：整型
------------------------------------------------
 * 默认值：0
 * 可选值：0、1、2

用于圆锥交点（conical intersection；CI）、系间穿越（intersystem crossing；ISC）等的多态优化。目前仅支持DL-Find优化器。

 * ``Imulti = 0`` ，不执行多态优化（默认）
 * ``Imulti = 1`` ，用惩罚函数方法优化CI或ISC，不需要计算非绝热耦合或态间耦合梯度
 * ``Imulti = 2`` ，用梯度投影方法优化CI或ISC，其中CI优化需要计算非绝热耦合（默认），ISC优化需要设定 ``Noncoupl`` 关键词，跳过态间耦合梯度计算。

:guilabel:`Noncoupl` 参数类型：Bool
-----------------------------------------------
这个关键词不执行态间耦合梯度计算，用于ISC优化。

:guilabel:`Multistate` 参数类型：字符串
------------------------------------------------
 * 默认值：NONE
 * 可选值：NONE、2SOC、3SOC、...、9SOC、MECP、CI

指定多态计算的类型。支持DL-Find优化器和BDF自带的优化器。

 * ``NONE`` ，执行常规的单态优化或频率计算。 ``1SOC`` 是同义词。
 * ``2SOC`` [ ``chi`` ]，用多态自旋混合（MSSM）模型进行Truhlar等人建议的两态自旋混合模型 :cite:`Truhlar2018` 计算。通过模拟两个自旋态之间的自旋轨道耦合，得到自旋混合基态。支持结构优化和振动频率计算。
 * ``3SOC`` [ ``chi`` ]，用MSSM模型计算三个自旋态构成的自旋混合基态。类似地，有 ``4SOC`` [ ``chi`` ]、``5SOC`` [ ``chi`` ]、等，最多支持九个自旋不同的态构成的自旋混合态。
 * ``MECP`` ，优化两个态之间的最低能量交叉点（MECP）；暂不支持
 * ``CI`` ，优化两个态之间的锥形交叉点（CI）；暂不支持

``chi`` 是可选的旋轨耦合常数的经验值（单位： :math:`\rm cm^{-1}` ）；如果不提供，采用默认值 400。

 * 对于3d元素体系， ``chi`` 建议取值50至400。一般来说结果对取值不敏感 :cite:`Takayanagi2018` ，但成键非饱和的3d元素体系最大可以取到1800 :cite:`Truhlar2018` 。
 * 对于4d元素体系， ``chi`` 可以取50至800，但成键非饱和的4d元素体系最大可以取到2000。
 * 对于5d元素体系， ``chi`` 可以取500至3000，建议值2500 :cite:`Truhlar2018` 。
   如果涉及成键非饱和的5d元素，MSSM模型的能量可能不可靠，建议在优化的驻点结构上用二分量或四分量相对论方法进行单点能校正。
 * MSSM模型不适用于锕系以及更重元素的体系。

:guilabel:`Maxcycle` 参数类型：整型
---------------------------------------------------
指定最大优化步数。对于DL-Find优化器，默认值为50；对于BDF优化器，默认值为max(100, 6*原子数)。

:guilabel:`TolGrad` 参数类型：浮点型
------------------------------------------------
指定均方根梯度（RMS Gradient）的收敛标准，单位Hartree/Bohr。对于DL-Find优化器，默认值为2.D-4；对于BDF优化器，默认值为3.D-4。该参数同时还将梯度的最大分量（Max Gradient）的收敛标准设为TolGrad的1.5倍。

:guilabel:`TolEne` 参数类型：浮点型
---------------------------------------------------
 * 默认值：1.D-6

指定结构优化相邻两步能量变化的收敛标准，单位Hartree。该参数仅对DL-Find优化器有效。

:guilabel:`TolStep` 参数类型：浮点型
------------------------------------------------
 * 默认值：1.2D-3

均方根步长（RMS Step）的收敛标准，单位Bohr。该参数仅对BDF优化器有效。该参数同时还将步长的最大分量（Max Step）的收敛标准设为TolStep的1.5倍。

:guilabel:`IOpt` 参数类型：整型
---------------------------------------------------
 * 默认值：3
 * 可选值：3、10（当Solver=1时）；0、1、2、3、9、10、11、12、13、20、30、51、52（当Solver=0时）

指定优化目标。对于DL-Find优化器，该参数的意义与DL-Find的IOpt参数意义相同，其中常用的有3（L-BFGS）和10（P-RFO）；
对于BDF优化器，仅支持其中的2个IOpt值，IOpt=3（优化极小值点）和IOpt=10（优化过渡态）。

:guilabel:`Trust` 参数类型：浮点型
---------------------------------------------------
 * 默认值：0.3
 * 可选值：非零实数

建议范围：0.005 ~ 0.5或-0.5 ~ -0.005

指定优化的置信半径（trust radius）。当置信半径r设定为正数时，程序的初始置信半径将设为r，但在随后的结构优化步骤中可能会视优化情况而动态地增加或减少置信半径。当置信半径r设定为负数时，程序的初始置信半径将设为|r|，且随后的结构优化步骤中保证置信半径不会超过|r|。

:guilabel:`Update` 参数类型：整型
------------------------------------------------
 * 默认值：对于极小值点优化为3，对于过渡态优化为2
 * 可选值：0、1、2、3、9

指定几何优化过程中Hessian的更新方式。0为每步均重新计算数值Hessian；1为Powell更新法（仅DL-Find支持）；2为针对过渡态的Bofill更新法；3为指定L-BFGS更新法（优化器为DL-Find），否则指定BFGS更新法；9为针对极小值点的Bofill更新法。如选择0以外的值，则程序将在几何优化的第一步构造基于分子力场的初始Hessian。

:guilabel:`ICoord` 参数类型：整型
---------------------------------------------------
 * 可选值：0、1

本参数指定几何优化使用的坐标类型。如ICoord=0，采用直角坐标；如ICoord=1，采用冗余内坐标。对于DL-Find优化器，默认值为0；对于BDF优化器，默认值为1，且不支持1以外的值。

:guilabel:`ILine` 参数类型：整型
------------------------------------------------
 * 可选值：0、1

本参数指定是否在几何优化过程中进行线性搜索；如不进行线性搜索，则只进行二次搜索。ILine=0表示不进行线性搜索，否则表示进行线性搜索。对于DL-Find优化器，默认值为0；对于BDF优化器，默认值为1。

:guilabel:`Frozen` 参数类型：整数数列
---------------------------------------------------

本参数指定进行笛卡尔坐标约束性优化（constrained optimization），即在约束一个或多个原子的笛卡尔坐标的情况下，优化分子其余的自由度。该关键词后面的第一行应是一个整数，表示约束的数目，设其为N；第2行到第N+1行，每一行分别由2个整数组成，其中第一个是待冻结的原子编号，第二个的允许取值及其意义为：

.. code-block:: bdf

    0: 不冻结（默认值）
   -1: 冻结该原子的x、y、z坐标
   -2: 冻结该原子的x坐标
   -3: 冻结该原子的y坐标
   -4: 冻结该原子的z坐标
  -23: 冻结该原子的x、y坐标
  -24: 冻结该原子的x、z坐标
  -34: 冻结该原子的y、z坐标

其中当使用BDF优化器时，该数字仅允许取0或-1。

.. note::

     程序冻结的是用户指定的各原子之间的相对笛卡尔坐标，原子的绝对笛卡尔坐标仍可能因为分子标准取向的变化而变化。

:guilabel:`Constrain` 参数类型：整数数列
---------------------------------------------------

本参数指定进行约束性优化（constrained optimization），即在约束一个或多个原子的笛卡尔坐标、键长、键角或二面角的情况下，优化分子其余的自由度。目前本参数仅支持BDF优化器。该关键词后面的第一行应是一个整数，表示约束的数目，设其为N；第2行到第N+1行，每一行分别由1~4个整数组成。如某一行有1个整数，表示原子编号为该整数的原子的笛卡尔坐标被冻结；如某一行有2个整数，表示原子编号为这2个整数的原子之间的键被冻结；如某一行有3个整数，表示原子编号为这3个整数的原子之间的键角被冻结；如某一行有4个整数，表示原子编号为这4个整数的原子之间的二面角被冻结。

.. code-block:: bdf

     $bdfopt
     Constrain
     2
     1 5        #1号原子-5号原子之间的化学键被冻结
     1 4 8      #1号原子-4号原子-8号原子的键角被冻结
     $end

此外，也可先将键长、键角或二面角设定为用户给定值，再进行冻结。例如以下输入表示冻结5号原子和10号原子的距离（即保持这两个原子的距离等于初始结构里的距离）；与此同时将4号原子和5号原子的距离调整为1.5埃（而不管初始结构里这两个原子之间的距离是多少），然后冻结4号原子和5号原子的距离。

.. code-block:: bdf

     $bdfopt
     Constrain
     2
     5 10
     4 5 = 1.5 # 单位为Angstrom；注意即便初始坐标是以Bohr为单位输入的，这里的用户给定值的单位仍然为Angstrom
     $end

.. note::

     与其他某些量化程序不同，即使分子坐标是以直角坐标而非内坐标形式指定的，BDF仍然可以冻结分子的键长、键角或二面角。此外，当冻结笛卡尔坐标时，程序冻结的是用户指定的各原子之间的相对笛卡尔坐标，原子的绝对笛卡尔坐标仍可能因为分子标准取向的变化而变化。

:guilabel:`Hess` 参数类型：字符串
------------------------------------------------
 * 可选值：only、init、final、init+final

指定计算Hessian。如为only，则仅计算Hessian而不做几何结构优化。如Hessian计算正常结束，程序将把Hessian对角化并进行热化学分析，给出振动频率、振动简正模、零点能、内能、焓、熵、Gibbs自由能等数据。如为init，则首先计算Hessian，然后以其为初始Hessian进行几何结构优化。该方法主要应用于过渡态搜索中（因为默认的基于分子力场的初始Hessian缺乏虚频）。程序不对该Hessian进行热化学分析。如为final，则首先进行结构优化，如结构优化收敛，则在收敛的几何结构上计算Hessian，并进行频率分析和热化学分析。在其他量化程序中，这种计算模式常被称为opt+freq。如为init+final，则首先计算初始Hessian，然后进行几何结构优化，优化收敛后再计算Hessian。程序仅对后一个Hessian进行频率分析和热化学分析，而不对前一个Hessian进行这些分析。

.. attention::
    BDF目前仅支持HF/DFT的解析Hessian，使用TDDFT激发态结构优化使用数值Hessian。如果要HF/DFT也强制使用数值Hessian，可以使用 ``UseNumHess`` 关键词。

:guilabel:`UseNumHess` 参数类型：Bool
-----------------------------------------------
强行计算数值Hessian，即使某个方法的解析Hessian可以获得。解析Hessian方法仅支持HF/DFT，DFT目前支持LDA、GGA、Hybrid和RS-Hybrid泛函。

:guilabel:`ReCalcHess` 参数类型：整型
---------------------------------------------------
 * 可选值：非负整数

指定在几何优化中，每隔多少步计算一次数值Hessian。如不提供该关键词，默认在几何优化过程中不计算数值Hessian（除非指定了Update=0）。

:guilabel:`NumHessStep` 参数类型：浮点型
------------------------------------------------
 * 默认值：0.005
 * 可选值：正实数

建议范围：0.001 ~ 0.02

指定数值Hessian计算时，扰动分子的步长（单位：Bohr）。

.. note::
     NumHessStep只能在已经用其他关键词（如Hess、ReCalcHess、RmImag、Update等）指定计算Hessian的前提下，改变扰动分子的步长，其本身并没有指定计算Hessian的作用。因此，如果只指定NumHessStep而不搭配其他和计算Hessian有关的关键词，则NumHessStep不会有任何效果。

:guilabel:`ReadHess` 参数类型：Bool型
---------------------------------------------------
指定读取$BDFTASK.hess作为结构优化的初始Hessian（其中$BDFTASK为当前输入文件的名字去掉后缀.inp得到的字符串）。$BDFTASK.hess可以由其他的频率计算任务产生，而不一定需要和当前结构优化计算的理论级别一致。

:guilabel:`RestartHess` 参数类型：Bool型
---------------------------------------------------
指定对频率任务进行断点续算。

:guilabel:`RmImag` 参数类型：Bool型
---------------------------------------------------
对于极小值点优化，该关键字表示如果优化收敛后的结构存在虚频，则自动尝试消除虚频直至分子没有虚频为止；对于过渡态优化，该关键字表示如果优化收敛后的结构存在多于1个虚频，则自动尝试消除虚频直至分子恰有一个虚频为止。需要注意的是，消除虚频不能保证成功，所以计算结束后用户仍然需要手动检查虚频数目是否正确。对于过渡态优化收敛后的结构没有虚频的情形，用该关键字也有一定概率可以找到虚频数目为1的结构，但是成功率较低。

:guilabel:`QRRHO` 参数类型：Bool型
---------------------------------------------------
指定用Grimme的QRRHO方法 :cite:`QRRHO` ，而非默认的刚性转子-谐振子近似（RRHO）计算熵、Gibbs自由能。开启QRRHO会使得较大体系，尤其是涉及非共价相互作用和/或柔性的体系的自由能、熵的计算精度提高，对于刚性小体系的计算结果几乎没有影响。开启QRRHO后，自由能、熵结果与ORCA、Turbomole可比，但与Gaussian不可比。若所研究的课题涉及至少一个非共价相互作用很重要的体系的自由能计算，且不需要计算结果与Gaussian可比，则建议总是打开QRRHO。

.. note::
  开启QRRHO算出来的自由能、熵，与不开启QRRHO算出来的自由能、熵不可比，不能作差得到自由能变、熵变。

:guilabel:`NDeg` 参数类型：整型
---------------------------------------------------
 * 默认值：1
 * 可选值：正整数

指定当前电子态的电子简并度，用于计算热化学分析中的吉布斯自由能。电子简并度等于空间简并度乘以自旋简并度，其中空间简并度等于当前电子态所属不可约表示的维数（当分子属于阿贝尔群时，空间简并度等于1），自旋简并度对于非相对论计算和标量相对论计算等于自旋多重度（2S+1），而对考虑了旋轨耦合的计算等于2J+1，其中J为当前电子态的总角动量量子数。注意即使对于电子简并度不等于1的体系，NDeg的默认值仍然是1，用户必须手动指定正确的NDeg值，这一点对于开壳层体系的吉布斯自由能计算尤其重要。

:guilabel:`NTemp` 参数类型：整型
---------------------------------------------------
 * 默认值：1
 * 可选值：正整数

用户提供的温度值的个数。这些温度值由下面的 ``Temp`` 定义。 ``NTemp`` 必须出现在 ``Temp`` 之前才有意义，否则只能为 ``Temp`` 提供一个温度值。

:guilabel:`Temp` 参数类型：浮点型
---------------------------------------------------
 * 默认值：298.15
 * 可选值：正实数

指定在什么温度下进行热化学分析（单位：K）。

:guilabel:`NPress` 参数类型：整型
---------------------------------------------------
 * 默认值：1
 * 可选值：正整数

用户提供的压强值的个数。这些压强值由下面的 ``Press`` 定义。 ``NPress`` 必须出现在 ``Press`` 之前才有意义，否则只能为 ``Press`` 提供一个压强值。

 * 当 ``NTemp`` > 1， ``NPress`` = 1时，对给定压强下的各种温度进行热化学计算；
 * 当 ``NTemp`` = 1， ``NPress`` > 1时，对给定温度下的各种压强进行热化学计算；
 * 当 ``NTemp`` > 1， ``NPress`` > 1时，除了常温常压下的热化学计算之外，还对每一对温度值和压强值进行热化学计算，若 ``NTemp`` 与 ``NPress`` 不等，则用常温或常压补全。


:guilabel:`Press` 参数类型：浮点型
---------------------------------------------------
 * 默认值：1.0
 * 可选值：正实数

指定在什么压强下进行热化学分析（单位：atm）。

:guilabel:`Scale` 参数类型：浮点型
---------------------------------------------------
 * 默认值：1.0
 * 可选值：正实数

指定频率分析的校正因子。

:guilabel:`Scan` 参数类型：整数数列
---------------------------------------------------
指定进行柔性扫描计算。 ``Scan`` 后面的第一行应当是一个整数，或两个用空格分隔的整数，后续的写法视第一行是一个整数还是两个整数而有所不同。
（1）若 ``Scan`` 后面的第一行是一个正整数（记为N，N可以为1），则代表进行N维网格扫描，接下来应该再写N行，每行的格式采取以下三种之中的一种（其中A、B、C、D为正整数，startvalue、endvalue、interval为浮点数）：

.. code-block:: bdf

     # 以interval为步长，将第A个原子与第B个原子形成的键的键长从startvalue扫到endvalue（含）。单位：Angstrom
     A B = startvalue endvalue interval
     # 以interval为步长，将第A个原子、第B个原子、第C个原子形成的键角从startvalue扫到endvalue（含）。单位：度
     A B C = startvalue endvalue interval
     # 以interval为步长，将第A个原子、第B个原子、第C个原子、第D个原子形成的二面角从startvalue扫到endvalue（含）。单位：度
     A B C D = startvalue endvalue interval
     # 所有原子编号从1开始

（2）若 ``Scan`` 后面的第一行是两个正整数（记为M、N），则代表进行散点扫描，共需要改变M个内坐标，扫N个结构。此时应当首先在这行之后写M行，表示要扫描哪些内坐标，每行的格式采取以下三种之中的一种（其中A、B、C、D为正整数）：

.. code-block:: bdf

     # 假设这是M行之中的第i行，则第i个待扫描的内坐标为第A个原子与第B个原子形成的键的键长。单位：Angstrom
     A B
     # 假设这是M行之中的第i行，则第i个待扫描的内坐标为第A个原子、第B个原子、第C个原子形成的键角。单位：度
     A B C
     # 假设这是M行之中的第i行，则第i个待扫描的内坐标为第A个原子、第B个原子、第C个原子、第D个原子形成的二面角。单位：度
     A B C D
     # 所有原子编号从1开始

接着再写N行，每行M个数。若第i行的第j个数为x，则代表第i个希望扫描的结构里，第j个上述指定的内坐标的值为x。

.. note::
  （1）二面角A-B-C-D中，A、B、C、D各原子未必需要成键，利用这一点可以对分子偏离平面的程度进行扫描，例如可以将NH3分子的H-H-N-H二面角从180度往小于180度的方向扫描，即模拟NH3从平面构型逐渐变为三角锥构型的过程。
  （2）扫描若涉及大于180度的二面角，在显示时会被减去360度。例如若从150度扫描到210度、步长为30度，则得到一条3个点的扫描轨迹，二面角分别为150度、180度、-150度。
  （3）扫描的第N步会读取第N-1步的结构和波函数作为初猜。
  （4）扫描的第1步的内坐标可以和初始结构不严格相同，但若差异太大，有概率导致扫描失败。例如不宜在初始结构某个二面角为60度时，指定从-60度开始扫描这个二面角，但从50度开始扫描一般是没有问题的。
  （5）若希望从较大的键长/键角/二面角向较小数的方向扫描，则interval必须设为负值。
  （6）柔性扫描功能仅支持 ``solver=1`` ，不支持 ``solver=0`` 。
  （7）对于多维扫描，程序优先改变较后指定的内坐标。例如对于以下输入，扫描的顺序是 (1.0, 170) -> (1.0, 180) -> (1.0, -170) -> (1.1, 170) -> (1.1, 180) -> (1.1, -170) （其中第一个数表示1号原子和3号原子之间的键长，单位为Angstrom；第二个数表示1号、3号、5号、10号原子形成的二面角，单位为度）

.. code-block:: bdf

  $bdfopt
  solver
  1
  scan
  2
  1 3 = 1.0 1.1 0.1
  1 3 5 10 = 170 190 10
  $end

:guilabel:`Dimer` 参数类型：Bool型
---------------------------------------------------
用DL-FIND外部库 :cite:`dlfind2009` 的Dimer方法 :cite:`dimer1999,dimer2005,dimer2008` 优化过渡态。该方法只需要计算梯度，不需要计算Hessian。
如果修改Dimer方法的默认参数，需要改用下面的 ``Dimer-Block`` ... ``End Dimer`` 输入块。


:guilabel:`Dimer-Block` 参数类型：多个关键词
---------------------------------------------------
Dimer方法的另一种指定方式。在 ``Dimer-Block`` 中允许修改以下关键词，以 ``End Dimer`` 结束。

:guilabel:`NoInterpolation` 参数类型：Bool型

执行旋转Dimer步骤之后，重新计算梯度，这样或许能略微减少结构收敛的步数，但是额外的梯度计算会耗费更多的计算时间。默认为用内插方法估算梯度。

:guilabel:`Delta` 参数类型：浮点型

 * 默认值：0.01
 * 可选值：正实数

两个像点的间距，原子单位，仅对直角坐标优化有效。

:guilabel:`Crude` 参数类型：Bool型

把均方根梯度收敛标准（ ``TolGrad`` ）从默认的2.0D-4提高到1/750 = 1.33D-3。如果仅关心过渡态的能量和定性的几何结构，或者想把优化的过渡态结构用其它方法做进一步优化，可以加上该选项。

:guilabel:`NEB` 参数类型：Bool型
---------------------------------------------------
用DL-FIND外部库 :cite:`dlfind2009` 的CI-NEB方法 :cite:`neb2000` 计算反应路径，其中能量最高点对应过渡态（如果路径存在能垒的话）。

CI-NEB计算需要提供两个端点的坐标，其中第一个端点（例如，可以是反应物或中间体）的初始结构来自 ``Compass`` 模块的几何结构，
而第二个端点（例如，可以是产物或另一个中间体）的初始结构在 ``Geometry2`` ... ``End Geometry2`` 输入块（见下）提供。
需要注意两套坐标的原子顺序必须一致。此外还可以提供中间像点的坐标（见 ``NFrame`` ）。

如果修改CI-NEB方法的默认参数，需要改用下面的 ``NEB-Block`` ... ``End NEB`` 输入块。

:guilabel:`NEB-Block` 参数类型：多个关键词
---------------------------------------------------------
CI-NEB方法的另一种指定方式。在 ``NEB-Block`` 中允许修改以下关键词，以 ``End NEB`` 结束。

:guilabel:`NImage` 参数类型：整型

 * 默认值：5
 * 可选值：正整数

定义路径上的中间像点个数。在实际计算中，总像点数为MImage = ``NImage`` + 3，其中，1号、MImage-1号像点对应两个端点，2至MImage-2号为中间像点。
CI-NEB对能量最高的点执行CI步骤时，这个点的数据存放在MImage。

:guilabel:`NEBk` 参数类型：浮点型

 * 默认值：0.01
 * 可选值：正实数

定义CI-NEB的经验力常数。

:guilabel:`NEBMode` 参数类型：整型

 * 默认值：2
 * 可选值：0，1，2

两个端点的处理方式。包括：优化两个端点，达到能量最小化（0），仅在垂直于路径的方向优化两个端点（1），以及固定两个端点不做优化（2）。

:guilabel:`Crude` 参数类型：Bool型

把均方根梯度收敛标准（ ``TolGrad`` ）从默认的2.0D-4提高到1/750 = 1.33D-3。如果仅关心定性的结果，或 ``NImage`` 比较大时，可以加上该选项。

:guilabel:`NFrame` 参数类型：整型
---------------------------------------------------
 * 默认值：1
 * 可选值：1至 ``NImage`` +1 的正整数（CI-NEB计算）

在 ``Geometry2`` 中提供的坐标个数。 ``NFrame`` 必须出现在 ``Geometry2`` 之前才有意义，否则只能为 ``Geometry2`` 提供一个坐标。

:guilabel:`Geometry2` 参数类型：字符串数组
---------------------------------------------
为CI-NEB方法指定第二个端点的几何结构，目前仅支持直角坐标（有待今后完善），单位：埃。如果输入坐标为原子单位，可以加上 ``Bohr``，即 ``Geometry2 Bohr`` 。
本关键词以 ``End Geometry2`` 结束。
由于第二个端点与第一个端点的原子顺序必须一致，因此这里可以省略原子名称，仅输入直角坐标数据。

如果 ``NFrame`` > 1，可以在 ``Geometry2`` 中为CI-NEB计算提供中间像点的结构，按照像点的编号排序，第二个端点的结构放到最后。
