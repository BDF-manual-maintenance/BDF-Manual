波函数分析和性质分析
================================================

BDF支持的波函数分析有：Mulliken布居分析和Lowdin布居分析，包括原子净电荷和原子自旋密度。

.. _1e-prop:

BDF支持的单电子性质有：

* SCF：偶极矩，极化率*，超极化率*，穆斯堡尔谱（有效接触密度、电场梯度），核磁共振\*\*
* TDDFT：激发态的偶极矩*，荧光吸收光谱的振子强度，磷光吸收光谱的振子强度

  \* 在 ``resp`` 模块中计算。\*\* 在 ``nmr`` 模块中计算。

更多的波函数分析及单电子性质，可以通过在 ``scf`` 模块中产生molden格式的数据文件，用第三方程序完成。输入示例：

.. code-block:: bdf

  $scf
  rks
  dft
   b3lyp
  molden
  $end

标准的molden格式仅支持spdfg型高斯基函数，但在BDF中已推广到h函数。

借助第三方程序LModeA-nano或LModeA，还可以对BDF的振动频率计算结果进行局域振动模式分析，并为分子力学计算提取内坐标的力常数。

有效接触密度
------------------------------------------------

计算有效接触密度（ED）需要同时考虑相对论效应（在BDF中用X2C哈密顿，通过 ``heff`` =21，22，或23指认）
和有限尺寸的原子核（ ``nuclear`` =1）。在sf-X2C-AU/B3LYP级别的输入示例如下：

.. code-block:: bdf

  $xuanyuan
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
    ultra fine
   reled
    20
  $end

其中，``reled`` 调用相对论性质ED的计算，``20`` 表示对原子序数小于20的轻元素不计算ED，从而节省计算时间。
对于密度泛函计算，ED的值对积分格点比较敏感，建议用精密的 ``ultra fine`` 。

ED需要对基组进行特殊处理，见 :ref:`穆斯堡尔谱<mossbauer>` 。

电场梯度
------------------------------------------------

计算电场梯度（EFG）的要求与ED类似，关键词为 ``relefg`` 。见 :ref:`穆斯堡尔谱<mossbauer>` 。

molden2aim
------------------------------------------------
下载： https://github.com/zorkzou/Molden2AIM

molden2aim的用途是把BDF产生的molden文件转化为wfn，wfx，或NBO-47格式的数据文件，用于各种分析。支持spdfgh型高斯基函数以及ECP。

Multiwfn
------------------------------------------------
下载： http://sobereva.com/multiwfn/

Multiwfn是功能强大的波函分析程序。通过BDF产生的molden数据文件（支持spdfgh基函数和赝势）或经molden2aim转化的wfn、wfx数据文件，
可以用Multiwfn进行各种波函数分析，例如电子密度拓扑分析（也称 *分子中原子的量子理论* ；QTAIM），电子局域函数（ELF），布居分析，
键级分析，原子电荷分析，等，也可以绘制分子轨道、电子密度和各种实空间函数的图像。
细节参见Multiwfn使用手册。

NBO分析
------------------------------------------------
BDF目前不包含NBO（ https://nbo7.chem.wisc.edu/ ）的接口，但是可以利用molden2aim，把BDF产生的molden文件（支持spdfgh基函数和赝势）转化为NBO-47格式的数据文件，
再利用NBO独立程序gennbo.exe进行NBO分析。

对于RHF/RKS和UHF/UKS类型的波函数（即，MO占据数只能是0，1，2三种），NBO可以计算“Second Order Perturbation Theory Analysis”，这需要在47文件中出现Fock矩阵。
为此需要在molden2aim的配置文件 ``m2a.ini`` 中设置 ``nbopro=1`` 。

力常数
------------------------------------------------
LModeA-nano（https://lmodea-nano.readthedocs.io/en/latest/）是PyMOL插件，用于固体和分子的局域振动模式分析，
计算化学键、键长、键角的力常数和谐振频率。
中文介绍见：http://bbs.keinsci.com/thread-28658-1-1.html

BDF振动频率计算任务产生的.umv数据文件可以直接被LModeA-nano程序读取。

