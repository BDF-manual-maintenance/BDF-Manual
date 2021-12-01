对称性与分子点群
================================================

BDF支持在计算中考虑分子点群对称性。除某些计算任务（如开壳层TDDFT、TDDFT/SOC等）仅支持 :math:`D_{2h}` 及其子群（即 :math:`C_1, C_i, C_s, C_2, D_2, C_{2h}, C_{2v}, D_{2h}` ，一般统称为阿贝尔群）以外，大部分计算任务支持任何的实表示点群（所有的阿贝尔群，以及 :math:`C_{nv}, D_{n}, D_{nh}, D_{nd}, T_d, O, O_h, I, I_h` ；其中特殊点群 :math:`C_{\infty v}, D_{\infty h}` 虽然名义上支持，但是是分别当作 :math:`C_{20v}` 和 :math:`D_{20h}` 来处理的，而单原子分子按 :math:`O_{h}` 群处理），但不支持复表示点群（ :math:`C_n, C_{nh} (n \ge 3); S_{2n} (n \ge 2); T, T_h` ）。程序可以自动根据用户在COMPASS模块输入的分子坐标来判断分子所属的点群，并在分子属于复表示点群时自动改用合适的子群。确定分子所属点群以后，程序即可产生该点群的群操作算符、特征标表、不可约表示等信息，以备后续计算使用。以氨分子为例：

.. code-block:: bdf

  $COMPASS
  Title
   NH3
  Basis
   cc-pvdz
  Geometry
   N                 -0.00000000   -0.00000000   -0.10000001
   H                  0.00000000   -0.94280900    0.23333324
   H                 -0.81649655    0.47140450    0.23333324
   H                  0.81649655    0.47140450    0.23333324
  End geometry
  thresh
   medium
  skeleton
  $END

注意因为初始结构不严格满足 :math:`C_{3v}` 对称性，这里用``thresh medium``选择较松的判断对称性的阈值（默认为``tight``，也可选择更松的``loose``）。由输出文件可以看到，程序自动识别出该分子属于 :math:`C_{3v}` 点群：

.. code-block:: 

  gsym: C03V, noper=    6
   Exiting zgeomsort....
   Representation generated
    Point group name C(3V)                        6
    User set point group as C(3V)
    Largest Abelian Subgroup C(S)                         2

注意点群名称的下标需要用括号括起来，诸如 :math:`C_{\infty v}, D_{\infty h}` 群的 :math:`\infty` 需要写作INF。接下来打印不可约表示信息、CG系数表等。在COMPASS部分输出的最后，程序给出该点群下不可约表示的列表，以及属于每个不可约表示的轨道的数目：

.. code-block:: 

  |--------------------------------------------------|
            Symmetry adapted orbital

    Total number of basis functions:      29      29

    Number of irreps:   3
    Irrep :   A1        A2        E1
    Norb  :     10         1        18
  |--------------------------------------------------|

很多时候，用户需要在输入文件中指定诸如每个不可约表示的轨道占据数（在SCF模块的输入中指定），以及每个不可约表示下计算多少个激发态（在TDDFT模块的输入中指定）等信息，而这些信息一般是以数组的形式输入的，例如

.. code-block:: bdf

  $TDDFT
  Nroot
   3 1 2
  $END

表示第一个不可约表示计算3个激发态，第二个不可约表示计算1个激发态，第三个不可约表示计算2个激发态（详见本手册的TDDFT章节）。这就势必要求用户在撰写输入文件时即知道各个不可约表示在BDF程序内部的排列顺序。以下给出BDF支持的所有点群下各个不可约表示的排列顺序：

 * C(1): A
 * C(i): Ag, Au
 * C(s): A', A''
 * C(2): A, B
 * C(2v): A1, A2, B1, B2
 * C(2h): Ag, Bg, Au, Bu
 * D(2): A, B1, B3, B2
 * D(2h): Ag, B1g, B3g, B2g, Au, B1u, B3u, B2u
 * C(nv) (n=2k+1, k>=1): A1, A2, E1, ..., Ek
 * C(nv) (n=2k+2, k>=1): A1, A2, B1, B2, E1, ..., Ek
 * D(n) (n=2k+1, k>=1): A1, A2, E1, ..., Ek
 * D(n) (n=2k+2, k>=1): A1, A2, B1, B2, E1, ..., Ek
 * D(nh) (n=2k+1, k>=1): A1', A2', E1', ..., Ek', A1'', A2'', E1'', ..., Ek'', 
 * D(nh) (n=2k+2, k>=1): A1g, A2g, B1g, B2g, E1g, ..., Ekg, A1u, A2u, B1u, B2u, E1u, ..., Eku
 * D(nd) (n=2k+1, k>=1): A1g, A2g, E1g, ..., Ekg, A1u, A2u, E1u, ..., Eku
 * D(nd) (n=2k+2, k>=1): A1', A2', B1', B2', E1', ..., Ek', A1'', A2'', B1'', B2'', E1'', ..., Ek''
 * T(d): A1, A2, E, T1, T2
 * O: A1, A2, E, T1, T2
 * O(h): A1g, A2g, Eg, T1g, T2g, A1u, A2u, Eu, T1u, T2u
 * I: A, T1, T2, F, H
 * I(h): Ag, T1g, T2g, Fg, Hg, Au, T1u, T2u, Fu, Hu

用户也可强制程序在分子所属点群的某个子群下计算，方法是在COMPASS模块的输入里使用group关键词，如：

.. code-block:: bdf

  $COMPASS
  Title
   N2
  Basis
   def2-TZVP
  Geometry
   N 0. 0. 0.
   N 0. 0. 1.1
  End geometry
  Skeleton
  Group
   D(2h)
  $END

即强制程序在 :math:`D_{2h}` 点群下计算N2分子，尽管N2分子实际上属于 :math:`D_{\infty h}` 点群。注意程序会自动检查用户输入的点群是否是分子实际所属点群的子群，如否，则程序报错退出。

To be done...
