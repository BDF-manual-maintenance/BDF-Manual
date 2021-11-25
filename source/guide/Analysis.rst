波函数分析和单电子性质
================================================

BDFpro支持的波函数分析有：Mulliken布居分析和Lowdin布居分析，包括原子净电荷和原子自旋密度。

BDFpro支持的单电子性质有：偶极矩，各种光谱性质，以及sf-X2C/SCF情况下的穆斯堡尔有效接触密度。

更多的波函数分析及单电子性质，可以通过产生molden格式的数据文件，用第三方程序完成。

有效接触密度
------------------------------------------------
同质异能位移（isomer shift；:math:`\delta^{IS}`）是穆斯堡尔谱的一个重要观测参量，源于具有一定尺寸的原
子核与周围电子分布之间的库仑相互作用。当原子处在不同的外界环境，导致原子核附近的库仑能发生变化。
同质异能位移对原子所处外界环境非常敏感，因此可以用来研究原子的氧化态，
自旋态，以及配位环境。同质异能位移可以表示为重元素在测试体系A和参照体系R中“有效接触密度”（ECD）
变化量的线性函数，

.. math::
    \delta^{IS} = \alpha(\rho_{A}-\rho_{R}) = \alpha(\rho_{A}-C)+\beta

其中ECD可以通过理论计算获得。

计算ECD需要同时考虑相对论效应（在BDFpro中用X2C哈密顿，通过 ``heff`` =21，22，或23指认）和有限尺寸的原子核。
在sf-X2C-AU/B3LYP级别的输入示例如下：

.. code-block::

  $xuanyuan
  scalar
  heff
   23
  nuclear
    1
  $end

  $scf
   rks
   dft
    b3lyp
   grid
    sg1
   relprp relcd 20
  $end

其中，``relprp relcd`` 调用相对论性质分析中的ECD计算，``20`` 表示对原子序数小于20的轻元素不计算ECD，从而节省计算时间。
对于密度泛函计算，ECD的值对积分格点也比较敏感，建议用 ``ultra fine`` 或者更精密的 ``sg1`` 。

计算ECD需要非常陡峭（也就是高斯指数非常大）的s、p型高斯基函数才能准确描述电子在原子核附近的分布，而基组库中的标准基组通常不符合要求。
建议对所关心的重元素采用cc-pVnZ型或ANO型全电子相对论基组，并把其中的s和p函数进行非收缩处理。此外，对于4d以上的元素，
经验表明默认的高斯指数还不够，需要额外补充一些更陡峭的高斯指数。
例如，选择标准基组中最陡峭的4-6个s或p型高斯指数（α），它们近似满足以下线性关系：

.. math::
    \ln\alpha_i = A + i\,B, \qquad i = 1, 2, \ldots

通过线性拟合得到参数A、B，再通过外推（i的间隔取-0.5或-1），即可得到更陡峭的高斯指数。
一般加入2-5个更陡峭的s函数、1-3个更陡峭的p函数即可满足要求，但是要避免用1.0E+11以上的高斯指数，
因为这可能会造成数值不稳定。

molden2aim
------------------------------------------------
下载： https://github.com/zorkzou/Molden2AIM

molden2aim的用途是把BDFpro产生的molden文件转化为wfn，wfx，或NBO-47格式的数据文件，用于各种分析。

标准的molden格式仅支持spdfg型高斯基函数，但在BDFpro和molden2aim中已推广到h函数。

Multiwfn
------------------------------------------------
下载： http://sobereva.com/multiwfn/

Multiwfn是功能强大的波函分析程序。通过BDFpro产生的molden数据文件（支持spdfgh基函数和赝势）或经molden2aim转化的wfn、wfx数据文件，可以用Multiwfn进行各种波函数分析和绘图，
例如电子密度拓扑分析（也称量子理论的分子中原子；QTAIM），电子局域函数（ELF），布居分析，键级分析，原子电荷，等。
细节参见Multiwfn使用手册。

NBO分析
------------------------------------------------
BDFpro目前不包含NBO（ https://nbo7.chem.wisc.edu/ ）的接口，但是可以利用molden2aim，把BDFpro产生的molden文件（支持spdfgh基函数和赝势）转化为NBO-47格式的数据文件，
再利用NBO独立程序gennbo.exe进行NBO分析。

对于RHF/RKS和UHF/UKS类型的波函数（即，MO占据数只能是0，1，2三种），NBO可以计算“Second Order Perturbation Theory Analysis”，这需要在47文件中出现Fock矩阵。
为此需要在molden2aim的配置文件 ``m2a.ini`` 中设置 ``nbopro=1`` 。
