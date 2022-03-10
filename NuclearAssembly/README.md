The MED files where generated using SALOME and the python script GenerateMeshFromSalomeNetGen.py 
which reads the geometry in file assemblage.xao and meshes it thanks to the library NETGEN.  

The msh files where obtained by converting the MED files using the software gmsh via the command  
gmsh -1 ./my_mesh.med -save_all -o my_mesh.msh  
