简洁输入
************************************

.. tip::

   BDF 简洁输入（Easyinput）的完整用户手册现已独立发布，请访问：

   .. raw:: html

      <p><a class="reference external" href="https://bdfeasyinputmanual.readthedocs.io/zh-cn/latest/" target="_blank">📖 BDF Easyinput 用户手册 →</a></p>

   涵盖语法详解、基组说明、计算类型、几何结构、溶剂化模型、Module Setting、
   完整示例与算例集，以及关键词速查表等内容。

.. note::

   本手册中凡涉及简洁输入的示例，均采用新版简洁输入格式。其要点为：

   * 控制行形如 ``方法/基组 计算类型``（计算类型默认 ``energy``，可省略）；
   * 电荷、自旋多重度、坐标单位、点群等全局参数以 ``关键词 值`` 形式
     写在控制行之后、 ``Geometry`` 之前的全局参数区；
   * 对具体计算模块的精细控制，统一用 ``Module Setting`` ... ``End Setting``
     包装块，内含若干 ``$模块名`` ... ``$end`` 子块。

   完整关键词列表与语法细节请查阅上述独立手册。
