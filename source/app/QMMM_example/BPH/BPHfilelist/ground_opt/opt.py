"""
OPT Fixed Atom TEST
METHOD : BDF
SYSTEM : Benzophenone
WRITE BY : GUO JIANPING
QC  : BPH
MM  : Water 
Fixed Atom : QC - MM - QC - MM -...-None
"""

import glob, math, os.path

from pBabel           import AmberCrdFile_ToCoordinates3, \
                             AmberTopologyFile_ToSystem , \
                             SystemGeometryTrajectory   , \
                             AmberCrdFile_FromSystem    , \
                             PDBFile_FromSystem         , \
                             XYZFile_FromSystem

from pCore            import Clone, logFile, Selection

from pMolecule        import NBModelORCA, QCModelBDF, System

from pMoleculeScripts import ConjugateGradientMinimize_SystemGeometry, \
                             FIREMinimize_SystemGeometry             , \
                             LBFGSMinimize_SystemGeometry            , \
                             SteepestDescentMinimize_SystemGeometry


def opt_ConjugateGradientMinimize ( molecule, selection):
    molecule.DefineFixedAtoms(selection)
    ConjugateGradientMinimize_SystemGeometry ( molecule                    ,
                                             logFrequency         =  2,
                                             maximumIterations    =  100,
                                             rmsGradientTolerance =  0.1,
                                             trajectories   = [ ( trajectory, 2 ) ])


# . Define the energy models.
nbModel = NBModelORCA ( )
qcModel = QCModelBDF ( "GB3LYP:6-31g" )

# . Get the filename.
label = "BPH"

# . Read the data.
molecule              = AmberTopologyFile_ToSystem ( "../../BPH_new.top"  )
molecule.coordinates3 = AmberCrdFile_ToCoordinates3 (  "../../BPH_new.crd" )

#. Define Atoms List 
natoms = len ( molecule.atoms )
qm_list = range(24)
activate_list = [387,388,389,390,391,392,402,403,404,552,553,554,624,625,626,1104,1105,1106,
                 1203,1204,1205,1359,1360,1361,1419,1420,1421,1554,1555,1556,1572,1573,1574,
                 1611,1612,1613,1617,1618,1619,1845,1846,1847,1944,1945,1946,2139,2140,2141,
                 2262,2263,2264,2337,2338,2339,2460,2461,2462,2568,2569,2570,2736,2737,2738]
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
outlabel = 'opt_' + label
if os.path.exists ( outlabel ):
    pass
else :
    os.mkdir ( outlabel )
outlabel = outlabel + '/' + outlabel

# . Create an output trajectory.
trajectory = SystemGeometryTrajectory ( outlabel + ".trj" , molecule, mode = "w" )
'''
# . Optimization.
# . Define the number of iterations
iterations = 2
# . QM region and MM region were fixed in turn for optimization
for i in range ( iterations ):
    opt_ConjugateGradientMinimize ( molecule, selection_qm)
    opt_ConjugateGradientMinimize ( molecule, selection_mm)
# . QM region and MM region were optimized simultaneously
opt_ConjugateGradientMinimize ( molecule, None)
'''
# . QM region and MM region were optimized simultaneously
opt_ConjugateGradientMinimize ( molecule, selection_mm_inactivate)

eStop = molecule.Energy ( )

# . Save the coordinates.
XYZFile_FromSystem ( outlabel +  ".xyz", molecule )
AmberCrdFile_FromSystem ( outlabel +  ".crd" , molecule )
PDBFile_FromSystem ( outlabel +  ".pdb" , molecule )
