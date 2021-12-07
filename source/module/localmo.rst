 分子轨道定域化 - localmo模块
================================================
localmo模快用于产生定域化的分子轨道，包含了Boys，Pipek-Maye，改进的Boys定域化等方法。localmo还用于为FLMO和Local MCSCF方法产生初始的分子片定域轨道。

**基本控制参数**

:guilabel:`Boys` 参数类型：Bool型
------------------------------------------------
指定使用Boys定域化方法定域轨道。Boys是Localmo模块默认的方法。

:guilabel:`Mboys` 参数类型：整型
------------------------------------------------
指定使用改进的Boys定域化方法，下一行为一个整数，指定改进Boys方法的指数因子。

:guilabel:`Pipek` 参数类型：Bool型
------------------------------------------------
指定使用Pipek-mezey定域化方法。默认用Mulliken电荷，如果设置了Lowdin参数，Pipek-Mezey方法用Lowdin电荷。本方法默认用雅可比旋转定域化轨道，如果用于指定用Trust-Region方法 ，需要使用关键词Trust。

:guilabel:`Mulliken` 参数类型：Bool型
------------------------------------------------
指定Pipek-Mezey方法使用Mulliken电荷。默认选项。

:guilabel:`Lowdin` 参数类型：Bool型
------------------------------------------------
参数指定Pipek-Mezey方法使用Lowdin电荷。

:guilabel:`Jacobi` 参数类型：Bool型
------------------------------------------------
指定Pipek-Mezey方法利用雅可比旋转定域轨道。

:guilabel:`Trust` 参数类型：Bool型
------------------------------------------------
指定Pipek-Mezey方法利用Trust Region方法定域轨道。

:guilabel:`Hybridboys` 参数类型：整型
------------------------------------------------
可选值：-100、100

指定Pipek-Mezey或Boys定域化方法混合使用雅可比旋转与Trust Region方法定域轨道。默认不使用混合方法，如果加入了这个参数，下一行输入必须为整数。
-100: 仅将虚轨道先用雅可比旋转定域化100次或者定域化达到收敛阈值Hybridthre后，转换为Trust Region方法继续定域化。
100: 将占据轨道与虚轨道都先利用雅可比旋转定域化100次或者定域化达到收敛阈值Hybridthre后，转换为Trust Region方法继续定域化。

:guilabel:`Hybridthre` 参数类型：浮点型
------------------------------------------------
指定混合定域化方法的转换阈值。

:guilabel:`Thresh` 参数类型：浮点型
------------------------------------------------
指定定域化方法收敛的阈值，输入为两个浮点数。

:guilabel:`Tailcut` 参数类型：浮点型
------------------------------------------------
默认值：1.D-2

指定忽略FLMO尾巴的阈值。

:guilabel:`Threshpop` 参数类型：浮点型
------------------------------------------------
默认值：1.D-1

指定Lowdin布居的阈值。

:guilabel:`Maxcycle` 参数类型：整型
------------------------------------------------
指定Boys定域化允许的最大循环次数。

:guilabel:`Rohfloc` 参数类型：Bool型
------------------------------------------------
指定定域化ROHF/ROKS轨道。

:guilabel:`Mcscffloc` 参数类型：Bool型
------------------------------------------------
指定定域化MCSCF轨道。

:guilabel:`Orbital` 参数类型：字符串
------------------------------------------------
指定在MCSCF定域化中从那个文件读入轨道。

.. code-block:: bdf

     $LocalMO
     Orbital
     mcorb       # 指定从MCSCF计算存储的mcorb读入轨道
     $End

:guilabel:`Orbread` 参数类型：Bool型
------------------------------------------------
指定从BDF_TMPDIR中的文本文件inporb读入分子轨道。

:guilabel:`Flmo` 参数类型：Bool型
------------------------------------------------
指定投影LMO到pFLMO。

:guilabel:`Frozocc` 参数类型：整型
------------------------------------------------
指定不定域化的双占据轨道数目。

:guilabel:`Frozvir` 参数类型：整型
------------------------------------------------
指定不定域化的虚轨道数目。

:guilabel:`Anaylze` 参数类型：Bool型
------------------------------------------------
指定分析用户给定的定域轨道，计算占据-空轨道对的数目和MOS（Molecular Orbital Spread）。分析定域轨道需要从BDF_TMPDIR读入名为bdftask.testorb的文件，并进行轨道分析。这一轨道文件与SCF的bdftask.scforb格式相同，均为文本文件。

:guilabel:`Momatch` 参数类型：Bool型
------------------------------------------------
指定分析两组分子轨道的相似，两组轨道分别存储在$BDFTASK.testorb与$BDFTASK.checkorb中。如果是UHF/UKS轨道，默认将分析alpha 与beta轨道的相似性。如果$BDFTASK.checkorb不存在，该关键词将被忽略。

.. code-block:: bdf

     %cp $BDF_WORKDIR/$BDFTASK.flmoorb $BDF_WORKDIR/$BDFTASK.testorb
     %cp $BDF_WORKDIR/$BDFTASK.canorb $BDF_WORKDIR/$BDFTASK.checkorb
     $localmo
     mcscfloc
     analyze
     8 4
     momatch
     $end

:guilabel:`Lapair` 参数类型：浮点型
------------------------------------------------
指定统计占据-空轨道对大的阈值，默认占据-空轨道对的绝对重叠>1.D-4。

:guilabel:`Directgrid` 参数类型：Bool型
------------------------------------------------
指定利用直接数值积分的方法计算占据-空轨道对的绝对重叠。

:guilabel:`Nolmocls` 参数类型：整型
------------------------------------------------
指定不定域化SCF的占据轨道或MCSCF的双占据轨道。

:guilabel:`Nolmoact` 参数类型：整型
------------------------------------------------
指定不定域化MCSCF的活性轨道。

:guilabel:`Nolmovir` 参数类型：整型
------------------------------------------------
指定不定域化SCF的空轨道或MCSCF的空轨道。
