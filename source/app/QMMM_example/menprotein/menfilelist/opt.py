"""
METHOD : BDF
SYSTEM : 
WRITE BY : GUO JIANPING
QC  : Res LEU 30
MM  : except LEU 30
Active : residue around LEU30 with the distance < 8A
MM_Inactive : MM - Active
Fixed Atom : (QC + MM_Inactive) - MM  - (QC + MM_Inactive) - MM - ... - MM_Inactive
"""

import glob, math, os.path

from pBabel           import AmberCrdFile_ToCoordinates3, \
                             AmberTopologyFile_ToSystem , \
                             SystemGeometryTrajectory   , \
                             AmberCrdFile_FromSystem    , \
                             PDBFile_FromSystem         , \
                             XYZFile_FromSystem

from pCore            import Clone, logFile, Selection

from pMolecule        import NBModelBDF, QCModelBDF, System

from pMoleculeScripts import LBFGSMinimize_SystemGeometry
                          


def opt_LBFGSMinimize ( molecule, selection):
    molecule.DefineFixedAtoms(selection)
    LBFGSMinimize_SystemGeometry ( molecule                    ,
                                   logFrequency         =  10 ,
                                   maximumIterations    =  1000,
                                   rmsGradientTolerance =  0.1,
                                   trajectories   = [ ( trajectory, 10 ) ])


# . Define the energy models.
nbModel = NBModelBDF ( )
nbModel.SetOptions (qcmmCoupling = 'Z1 Coupling')
qcModel = QCModelBDF ( "GB3LYP:6-31g" )

# . Read the data.
molecule              = AmberTopologyFile_ToSystem  ( "../kr2_mem.parm7" )
molecule.coordinates3 = AmberCrdFile_ToCoordinates3 ( "../kr2_mem.rst7" )
# . Close symmetry to a system
molecule.DefineSymmetry(crystalClass = None)

#. Define Atoms List 
natoms = len ( molecule.atoms )
qm_list = range (431, 452 )
activate_list = [118,119,120,121,122,123,124,125,126,127,128,129,130,131,
                 132,314,315,316,317,318,319,320,321,322,323,324,325,326,
                 327,328,329,330,331,332,333,334,335,336,337,338,339,340,
                 341,342,343,344,345,346,347,348,349,350,351,352,353,354,
                 355,356,357,358,359,360,361,362,363,364,365,366,367,368,
                 369,370,371,372,373,374,375,376,377,378,379,380,381,382,
                 383,384,385,386,387,388,389,390,391,392,393,394,395,396,
                 397,398,399,400,401,402,403,404,405,406,407,408,409,410,
                 411,412,413,414,415,416,417,418,419,420,421,422,423,424,
                 425,426,427,428,429,430,        452,453,454,455,456,457,
                 458,459,460,461,462,463,464,465,466,467,468,469,470,471,
                 472,473,474,475,476,477,478,479,480,481,482,483,484,485,
                 486,487,488,489,490,491,492,493,494,495,496,497,498,499,
                 500,501,502,503,504,505,506,507,508,509,510,511,512,513,
                 514,515,516,517,518,519,520,521,522,523,524,525,526,527,
                 528,529,530,531,532,533,534,535,536,537,538,539,540,541,
                 542,543,544,545,546,547,548,549,550,551,552,553,554,555,
                 1064,1065,1066,1067,1068,1069,1070,1071,1072,1073,1074,1075,
                 1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,
                 1088,1089,1090,1091,1092,1093,1113,1114,1115,1116,1117,1118,
                 1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,
                 1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,
                 1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,
                 1155,1156,1157,1158,1159,1160,1161,1162,1163,1164,1165,1166,
                 1167,1168,1169,1170,1171,1172,1173,1174,1175,1176,1177,1178,
                 1179,1180,1181,1182,1183,1184,1185,1186,1187,1188,1189,1190,
                 1191,1192,1193,1194,1195,1196,1197,1198,1199,1200,1201,1202,
                 1203,1204,1205,1206,1207,1208,1209,1210,1211,1212,1213,1214,
                 1215,1216,1217,1218,1219,1220,1221,1222,1223,1224,1225,1226,
                 1227,1228,1229,1230,1231,1232,1233,1234,1235,1236,1237,1238,
                 1239,1240,1241,1242,1243,1244,1245,1246,1247,1248,1249,1250,
                 1251,1252,1253,1254,1255,1256,1257,1258,1259,1260,1261,1262,
                 1263,1264,1265,1266,1267,1268,1269,1270,1271,1272,1273,1274,
                 1275,1276,1277,1300,1301,1302,1303,1304,1305,1306,1307,1308,
                 1309,1310,1311,1312,1313,1314,1315,1316,1317,1318,1319,1580,
                 1581,1582,1583,1584,1585,1586,1587,1588,1589,1590,1591,1592,
                 1593,1594,1595,1596,1597,1598,1599,1614,1615,1616,1617,1618,
                 1619,1620,1621,1622,1623,1624,1625,1626,1627,1635,1636,1637,
                 1638,1639,1640,1641,1642,1643,1644,1645,1646,1647,1648,1649,
                 1650,1651,1652,1653,1654,1655,1656,1657,1658,1659,1660,1661,
                 1662,1663,1664,1665,1666,1667,1668,1669,1670,1671,1672,1673,
                 1674,1675,1676,1677,1678,1679,3785,3786,3787,3788,3789,3790,
                 3791,3792,3793,3794,3795,3796,3797,3798,3799,3800,3801,3802,
                 3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813,3814,
                 3815,3816,3817,3828,3829,3830,3831,3832,3833,3834,3835,3836,
                 3837,3838,3839,3840,3841,3842,3843,3844,3845,3846,3847,3848,
                 3849,3850,3851,3852,3853,3854,3855,3856,3857,3858,3859,3860,
                 3861,3862,3863,3864,3865,3866,3867,3868,3869,3870,3871,3872,
                 3873,3874,3875,3876,3877,3878,3879,3880,3881,3882,3883,3884,
                 3885,3886,3887,3904,3905,3906,3907,3908,3909,3910,3911,3912,
                 3913,3914,3915,3916,3917,3918,3919,3920,3921,3922,3923,3924,
                 3925,3926,3927,3928,3929,3930,3931,3932,3933,3934,3935,3936,
                 3937,3938,3939,3940,3941,3942,3943,3944,3945,3946,3947,3948,
                 3949,3950,3951,3952,3953,3954,3955,3956,3957,3968,3969,3970,
                 3971,3972,3973,3974,3975,3976,3977,3978,3979,3980,3981,3982,
                 3983,3984,3985,3986,3987,3988,3989,3990,3991,3992,3993,3994,
                 3995,5503,5504,5505,5506,5507,5508,5509,5510,5511,5512,5513,
                 5514,5515,5516,5517,5518,5519,5520,5521,5522,5523,5524,5525,
                 5526,5527,5528,5529,5530,5531,5532,5533,5534,5535,5536,5537,
                 5538,5539,5540,6044,6045,6046,6047,6048,6049,6050,6051,6052,
                 6053,6054,6055,6056,6057,6058,6059,6060,6061,6062,6063,6064,
                 6110,6111,6112,6113,6114,6115,6116,6117,6118,6119,6120,6121,
                 6122,6123,6124,6125,6126,6127,6128,6129,6130,6131,6132,6133,
                 6134,6135,6136,6137,6138,6139,6140,6141,6142,6818,6819,6820,
                 6821,6822,6823,6824,6825,6826,6827,6828,6829,6830,6831,6832,
                 6833,6834,6835,6836,6837,6838,50511,50512,50513,50538,50539,
                 50540,50544,50545,50546,50547,50548,50549,50559,50560,50561,
                 50586,50587,50588,50619,50620,50621,50652,50653,50654,50748,
                 50749,50750,51009,51010,51011,51030,51031,51032]
mm_list = range ( natoms )
for i in qm_list :
    mm_list.remove( i )
mm_inactivate_list = mm_list[ : ]
for i in activate_list :
    mm_inactivate_list.remove( i )

# . Define the selection for the first molecule.
qmmmtest_qc = Selection.FromIterable ( qm_list )
    
# . Define Fixed Atoms
selection_qm_mm_inactivate = Selection.FromIterable ( qm_list + mm_inactivate_list )
selection_mm = Selection.FromIterable ( mm_list )
selection_mm_inactivate = Selection.FromIterable ( mm_inactivate_list )

# . Define the energy model.
molecule.DefineQCModel ( qcModel, qcSelection = qmmmtest_qc )
molecule.DefineNBModel ( nbModel )
molecule.Summary ( )

# . Determine the starting energy.
eStart = molecule.Energy ( )

# . Create a folder for output files
outlabel = 'opt'
if os.path.exists ( outlabel ):
    pass
else :
    os.mkdir ( outlabel )
outlabel = outlabel + '/' + outlabel

# . Create an output trajectory.
trajectory = SystemGeometryTrajectory ( outlabel + ".trj" , molecule, mode = "w" )

# . Optimization.
# . Define the number of iterations
iterations = 2
# . QM region and MM region were fixed in turn for optimization
for i in range ( iterations ):
    opt_LBFGSMinimize ( molecule, selection_qm_mm_inactivate )
    opt_LBFGSMinimize ( molecule, selection_mm)
# . QM region and MM region were optimized simultaneously
opt_LBFGSMinimize ( molecule, selection_mm_inactivate)

# . Determine the final energy.
eStop = molecule.Energy ( )

# . Save the coordinates.
XYZFile_FromSystem ( outlabel +  ".xyz", molecule )
AmberCrdFile_FromSystem ( outlabel +  ".crd" , molecule )
PDBFile_FromSystem ( outlabel +  ".pdb" , molecule )
