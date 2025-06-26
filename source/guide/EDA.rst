能量分解分析
========================================

得益于BDF的自动分片引擎autofrag，自2025年6月起，BDF支持基于sobEDA、sobEDAw方法 :cite:`sobEDA` ，对共价或非共价复合物进行能量分解分析。

在sobEDA方法中，给定一个体系XY，程序首先可自动将XY根据键连关系分为X和Y两个片段，依次对X、Y进行计算。然后将X和Y的局域轨道拼接在一起，计算X和Y之间的静电作用能Eels、交换作用能Ex、DFT相关作用能Edftc、色散校正贡献Edc、溶剂校正贡献Esolv等。接下来对X和Y的局域轨道进行Löwdin正交化，并进行SCF迭代至收敛，由两步的能量变化又可得到Pauli排斥能Erep和轨道作用能Eorb。由此即将X和Y的相互作用能分解成了不同来源的贡献之和。其中X和Y不仅可以是两个完整的分子（即彼此之间只有非共价相互作用），也可以是两个彼此成键的片段，两者之间甚至可以有不止一根共价/配位键，但此时片段必须是开壳层的，也就是说断键处必须处理成自由基，而非添加缓冲原子/氢原子/PHO原子进行饱和。程序还可以对不止2个片段的体系进行分析，但不管是Eels、Ex、Edftc、Edc、Esolv、Erep、Eorb，都只能得到所有片段对的贡献的总和，而无法得到某一对片段的作用能。在sobEDAw方法中，程序在sobEDA分析的基础上还会进一步将Edftc按一定的比例分配到Edc和Ex中，所得结果可作为SAPT能量分解分析结果的近似，但sobEDAw仅适用于非共价相互作用的分析。

相比其他能量分解分析方法，sobEDA、sobEDAw具有如下优势：

 * 计算量小，与总体系的DFT单点能计算所需时间相似，较LED、SAPT等方法快1~2个数量级；
 * 能量分解分析得到的各项之和，严格等于两个片段间的作用能；
 * 分解结果的物理意义清晰。

此外，BDF里实现的sobEDA、sobEDAw方法，相比原版sobEDA、sobEDAw方法，还具有以下额外优势：

 * 作为计算的副产品，可以得到片段和总体系的局域分子轨道（LMO），可进行可视化或进一步的分析；
 * 当分析非共价相互作用时，程序可以自动识别体系由哪些分子组成，无需手动指定原子编号；
 * 支持一部分范围分离泛函（CAM-B3LYP、LC-BLYP）；
 * 可以分析溶剂对相互作用能的贡献。

另一方面，sobEDA、sobEDAw方法（或其BDF实现）也有一些局限性：

 * 未考虑片段变形能（片段从平衡结构变形为其在复合物中的结构所带来的能量升高），以及零点能、焓校正、熵校正的贡献。用户若需要得到这些贡献，需要根据定义自行求算；
 * sobEDA仅有搭配如B3LYP-D3这样的“无法考虑色散的泛函+色散校正”的理论级别，得到的分析结果才是有意义的。sobEDAw不受该限制，但为了尽量避免自行拟合经验参数，如无特殊需求仍然建议采用GB3LYP-D3；
 * sobEDAw涉及3个和理论级别有关的经验参数（c, a, r），文献中能查到的、已经拟合了这些参数的理论级别比较有限，若搭配其他理论级别使用，需自行拟合参数；
 * BDF里实现的sobEDA、sobEDAw方法暂不支持采用复合物基组（CB）进行计算；
 * BDF里实现的sobEDA、sobEDAw方法仅支持一部分泛函，详见 :ref:`BDF支持的交换相关泛函<XCFunctional>` 。注意此处所谓的“支持”并不代表程序能够自动选取正确的sobEDAw经验参数，用户一般仍需要手动输入sobEDAw经验参数。

sobEDA示例：分析乙炔中两个HC基团的相互作用能
--------------------------------------------

本算例取自sobEDA原始文献 :cite:`sobEDA` 表5：

.. code-block:: bdf

  $autofrag
  method
  sobeda
  fragdef
  0 4 0 -4 # charge1 spinmult1 charge2 spinmult2. Negative spinmult indicates beta spins
  1,2 # fragment 1: atom 1,2 (HC)
  3,4 # fragment 2: atom 3,4 (CH)
  $end
  
  $compass
  title
    sobEDA analysis of acetylene (GB3LYP-D3/def2-TZVP)
  geometry
        H          -0.00000000      -0.00000000       1.66144913
        C          -0.00000000      -0.00000000       0.59846873
        C           0.00000000       0.00000000      -0.59846873
        H           0.00000000       0.00000000      -1.66144913
  end geometry
  basis
  def2-TZVP # for non-covalent complexes, diffuse basis sets (e.g. def2-TZVPD) are recommended
  mpec+cosx # not necessary for molecules of this size, but helpful for large systems
  $end
  
  $xuanyuan
  $end
  
  $scf
  # even if the total system is closed-shell, if some of the fragments
  # are open-shell, one should still write UKS instead of RKS here
  uks
  dft
  gb3lyp
  d3 # dispersion correction is necessary for sobEDA. "D3" defaults to B-J damping, not zero damping
  $end
  
  $localmo
  flmo # necessary even if the user does not need LMOs
  $end

注意因为HC是开壳层的，需要在autofrag模块中用fragdef关键词指定每个片段包含哪些原子（否则程序不知道应当切断哪根或哪些键），及每个片段的电荷和自旋多重度。每个片段的原子编号用逗号分隔，连续的若干个原子编号可以写作“起始编号-终止编号”的形式，如"1,3,6-10,12-13,15"等价于"1,3,6,7,8,9,10,12,13,15"。虽然HC的基态是二重态，但两个HC基团之间形成的是三重键，需要将HC激发到四重态才能形成三重键，因此此处基于四重态HC进行能量分解分析。第二个HC片段的自旋多重度写为-4而非4，以表示其单电子自旋方向与第一个片段（自旋多重度为正数）相反。若分析非共价复合物，即程序无需切断任何键即可完成分片的情况，可以不指定fragdef，但用户必须检查程序自动识别的各个片段和自旋多重度是否合理，如不合理，则仍需用fragdef关键字指定各个片段的电荷和自旋多重度，以及各个片段的原子组成。

程序首先调用autofrag模块进行分片，然后依次对两个片段进行SCF计算，结果分别输出到*.fragment1.out和*.fragment2.out中；片段的局域轨道（LMO）输出到*.fragment1.flmo.molden和*.fragment2.flmo.molden中，可用任何支持molden格式的轨道可视化软件打开。接下来程序进行三次全局SCF计算，第一次既不正交化pFLMO也不做SCF迭代，第二次正交化pFLMO但不做SCF迭代，第三次正交化pFLMO并做SCF迭代至收敛。最后，程序整合5个计算的结果，输出能量分解分析结果：

.. code-block:: bdf

      *** Energy decomposition analysis result ***
  Total interaction      energy:   -275.837 kcal/mol
  Of these:
   - Electrostatic       energy:   -143.258 kcal/mol
   - Exchange-repulsion  energy:    248.908 kcal/mol
     Of these:
      > Exchange         energy:    -58.637 kcal/mol
      > Repulsion        energy:    307.545 kcal/mol
   - Orbital interaction energy:   -336.724 kcal/mol
   - Correlation         energy:    -44.763 kcal/mol
     Of these:
      > DFT correlation        :    -43.872 kcal/mol
      > Dispersion correction  :     -0.891 kcal/mol
   - Implicit solvation  energy:      0.000 kcal/mol

其中：
 * Electrostatic energy为静电作用能，对于本体系静电作用能是绝对值很大的负值，这是因为两个碳原子距离很近，一个碳原子的电子云会钻穿到另一个碳原子的电子云内部，感受到后者的核吸引势。
 * Exchange-repulsion energy为交换排斥能，可以用来表征位阻的贡献。表面上看，乙炔作为一个极其小的分子，并无位阻可言，但这是因为只有对于非共价相互作用，即轨道作用能的贡献较小的场合，交换排斥能才能占据主导，并表现为位阻排斥；当待研究的两个原子直接成键时，原子间并非没有位阻，只是轨道作用能较位阻的贡献更大而已，导致很多场合下不谈论位阻对共价键的贡献。
 * Orbital interaction energy为轨道作用能，对于共价键为绝对值很大的负值，对于非共价相互作用其绝对值较小。该项代表了共价作用、极化作用、电荷转移对作用能的贡献。注意这三种贡献的边界是模糊的，甚至可能有一定的重叠，因此在sobEDA的框架下无法进一步将轨道作用能分解为共价、极化、电荷转移的贡献。
 * Correlation energy为电子相关能，分为泛函自身的电子相关能（DFT correlation）及色散校正（dispersion correction）的贡献。对于B3LYP等不能描述色散作用的泛函，sobEDA得到的色散校正贡献可以认为是色散能对相互作用能的贡献。但注意这样得到的色散能的绝对值比某些高级别能量分解分析方法（如LED, SAPT）得到的往往更小，对于共价相连的体系更是常常有数量级的差别，这是因为色散能在片段间距离较近时的定义不唯一导致的，并不代表sobEDA的结果不可靠 :cite:`LED` 。若要获得和LED、SAPT大致可比的结果，应当改用sobEDAw（见下文）。
 * Implicit solvation energy为隐式溶剂模型对作用能的贡献，对于未添加隐式溶剂模型的计算，该项精确为0（即使用户添加了QM或MM的显式溶剂也是如此）。注意当用户考虑了溶剂模型的非静电项，或采用SMD溶剂模型时，该项包含了溶剂化熵的贡献，因此应当称作溶解自由能（而非溶剂化能）对相互作用的贡献。

可以看出，sobEDA不仅可以用来分析非共价复合物及以单键相连的片段，还可以分析以多重键相连的片段。类似地，片段之间所成的键可以不止一根。但当片段间有共价键/配位键时，用户在定义片段的自旋多重度时，必须考虑到断键所引入的单电子，必要时甚至还要检查片段有没有收敛到正确的波函数（例如通过自旋布居判断），仅仅确认自旋多重度的奇偶性正确是不够的。

若在以上输入文件的$scf块中添加关键词molden，还可产生总体系的pFLMO轨道和FLMO轨道的molden文件，分别为*.global.pflmo.molden和*.global.cflmo.molden。由此可以比较分子片的LMO与pFLMO、FLMO的区别。LMO与pFLMO的形状区别代表了轨道正交化的影响，对应以上能量分解分析的排斥能；pFLMO与FLMO的形状区别代表了片段间轨道混合的影响，对应以上能量分解分析的轨道作用能。例如下图展示了上述例子中HC的一个p轨道的形状变化历程，可以看到轨道正交化使得LMO略微往远离另一个片段的方向收缩，而轨道混合则使得LMO向另一个片段上离域。可以明显地看出，轨道离域的贡献较轨道正交化更大。计算所得的FLMO不是纯粹的pi轨道，而是混有少量sigma成分，这是正常现象。在$localmo模块中加入pipek关键词，即改用Pipek-Mezey局域化，往往有助于得到纯粹的sigma、pi轨道，但仍无法严格保证sigma和pi没有混合。

.. figure:: /images/HCCH-FLMO.png
   :width: 800
   :align: center


sobEDAw示例：水分子二聚体的能量分解分析
--------------------------------------------

对于待分析体系为非共价复合物，且不受本章节开头所述各局限性影响的情形，推荐采用sobEDAw代替sobEDA进行能量分解分析。例如以下输入文件对液态水环境下水分子二聚体中两个水分子之间的相互作用能进行分解，计算时用隐式溶剂模型等效考虑了周围其他水分子的贡献：

.. code-block:: bdf

  $autofrag
  method
  sobedaw
  # parameters for GB3LYP/6-31+G(d,p)
  # JPCA, 2023, 127, 7023
  # Note that this is a rather poor level of theory for sobEDAw;
  # for accurate results, diffuse TZ basis sets are recommended
  sobedaw_c
  0.638
  sobedaw_a
  0.124
  sobedaw_r
  3.523
  $end
  
  $compass
  geometry
     O         -1.65542061     -0.12330038      0.00000000
     O          1.24621244      0.10268870      0.00000000
     H         -0.70409026      0.03193167      0.00000000
     H         -2.03867273      0.75372294      0.00000000
     H          1.57598558     -0.38252146     -0.75856129
     H          1.57598558     -0.38252146      0.75856129
  end geometry
  basis
  6-31+G(d,p)
  $end
  
  $xuanyuan
  $end
  
  $scf
  rks
  dft
  gb3lyp
  d3
  solvent
  water
  $end
  
  $localmo
  flmo
  $end

可以看出sobEDAw需要的c、a、r参数需要从sobEDA原始文献中查阅，或自行拟合得到。分析结果为

.. code-block:: bdf

  sobEDAw parameters:
  c = 0.63800000
  a = 0.12400000
  r = 3.52300000
  dEdc/dEels = 0.05722559
  w = 1.00000000
  
      *** Energy decomposition analysis result ***
  Total interaction      energy:     -4.775 kcal/mol
  Of these:
   - Electrostatic       energy:    -11.166 kcal/mol
   - Exchange-repulsion  energy:      9.531 kcal/mol
   - Orbital interaction energy:     -2.801 kcal/mol
   - Dispersion          energy:     -2.964 kcal/mol
   - Implicit solvation  energy:      2.625 kcal/mol

可以看到sobEDAw不分别打印交换能和排斥能，也不打印DFT相关能，这是因为sobEDAw将DFT相关能以一定比例分配到了交换排斥能和色散能中。由能量分析结果可以发现，静电相互作用是水分子能够形成二聚体的主要原因，但静电吸引的贡献大部分被位阻排斥抵消掉了；轨道相互作用（即氢键的共价成分）及色散作用对水分子之间的结合能也有不小的贡献。因水的介电常数较高，液态水环境对水分子之间的静电作用有屏蔽作用，削弱了水分子之间的相互作用，因此溶剂化能对作用能的贡献表现为排斥。

当体系由3个或更多分子组成时，程序打印的每项能量均为所有的分子间相互作用之和。例如由A、B、C三个分子组成的体系ABC，程序可以打印体系的总分子间静电能、总交换排斥能等，但无法打印A和B之间的静电能、交换排斥能等。不过sobEDA、sobEDAw的特点决定了，当不存在隐式溶剂时，ABC的总分子间静电能等于单独算A和B、单独算B和C、单独算C和A得到的静电能之和。因此此时仅需在不存在C的情况下对AB复合物进行能量分解，即可得到A和B之间的静电能。但对于除静电能、交换能（注意不是交换排斥能）外的各项而言，单独算A和B、单独算B和C、单独算C和A得到的能量贡献之和均不等于ABC的总贡献。某些情况下用户可能希望对AC作为一个整体与B的作用能进行分解，此时需要用fragdef关键字将AC定义为一个片段，将B定义为另一个片段。

与sobEDA类似，在sobEDAw方法分析中也可对体系的片段LMO、pFLMO、FLMO作图，可视化地表现局域轨道在相互作用时的形状变化，此处不再赘述。
