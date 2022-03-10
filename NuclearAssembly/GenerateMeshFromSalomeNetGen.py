#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.8.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'/volatile/catA/ndjinga/Logiciels/Meshes/GenerateAssemblyMesh')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
(imported, bundle_size_7_step_1, [], [Inlet, Outlet, Wall, fluide__inside], []) = geompy.ImportXAO("/volatile/catA/ndjinga/Logiciels/Meshes/GenerateAssemblyMesh/assemblage.xao")
None
[Inlet, Outlet, Wall, fluide__inside] = geompy.GetExistingSubObjects(bundle_size_7_step_1, False)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( bundle_size_7_step_1, 'bundle_size_7.step_1' )
geompy.addToStudyInFather( bundle_size_7_step_1, Inlet, 'Inlet' )
geompy.addToStudyInFather( bundle_size_7_step_1, Outlet, 'Outlet' )
geompy.addToStudyInFather( bundle_size_7_step_1, Wall, 'Wall' )
geompy.addToStudyInFather( bundle_size_7_step_1, fluide__inside, 'fluide__inside' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Mesh_1 = smesh.Mesh(bundle_size_7_step_1)
NETGEN_1D_2D_3D = Mesh_1.Tetrahedron(algo=smeshBuilder.NETGEN_1D2D3D)
NETGEN_3D_Simple_Parameters_1 = NETGEN_1D_2D_3D.Parameters(smeshBuilder.SIMPLE)
NETGEN_3D_Simple_Parameters_1.SetLocalLength( 10 )
NETGEN_3D_Simple_Parameters_1.LengthFromEdges()
NETGEN_3D_Simple_Parameters_1.LengthFromFaces()
Inlet_1 = Mesh_1.GroupOnGeom(Inlet,'Inlet',SMESH.FACE)
Outlet_1 = Mesh_1.GroupOnGeom(Outlet,'Outlet',SMESH.FACE)
Wall_1 = Mesh_1.GroupOnGeom(Wall,'Wall',SMESH.FACE)
fluide__inside_1 = Mesh_1.GroupOnGeom(fluide__inside,'fluide__inside',SMESH.VOLUME)
isDone = Mesh_1.Compute()
[ Inlet_1, Outlet_1, Wall_1, fluide__inside_1 ] = Mesh_1.GetGroups()
smesh.SetName(Mesh_1, 'Mesh_1')
try:
  Mesh_1.ExportMED( r'/volatile/catA/ndjinga/Logiciels/Meshes/GenerateAssemblyMesh/AssemblyMesh_1.med', 1, 41, 1, Mesh_1, 1, [], '',-1, 1 )
  pass
except:
  print('ExportPartToMED() failed. Invalid file name?')


## Set names of Mesh objects
smesh.SetName(NETGEN_1D_2D_3D.GetAlgorithm(), 'NETGEN 1D-2D-3D')
smesh.SetName(NETGEN_3D_Simple_Parameters_1, 'NETGEN 3D Simple Parameters_1')
smesh.SetName(Inlet_1, 'Inlet')
smesh.SetName(Outlet_1, 'Outlet')
smesh.SetName(Wall_1, 'Wall')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(fluide__inside_1, 'fluide__inside')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
