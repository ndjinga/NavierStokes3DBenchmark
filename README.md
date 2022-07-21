# Stokes and Navier-Stokes 3D benchmark
This is the git repository of the 3D benchmark for the minisymposium "Saddle point problems in fluid dynamics".  
The problem consists in solving the Stokes and/or incompressible Navier-Stokes equations in a channel.
The two geometries are the [Cube](Cube) and the [Nuclear Assembly](NuclearAssembly).
For each geometry there are families of meshes and matrices enabling to study the increase of linear solver iterations as the mesh is  refined.  

The meshes are given in [MED](https://docs.salome-platform.org/8/dev/MEDCoupling/med-file.html) and [GMSH](https://gmsh.info/) binary formats. Note that both formats can be opened and converted using the software GMSH available on Windows, MacOS and Linux [here](http://gmsh.info/bin/). Participants to the benchmark can design specific numerical solver adapting the discretisation technique and the linear solver in order to enhance the overall performance of the simulation.  

For participants who would rather focus on the linear system with a 'black-box' approach, we provide sparse matrices obtained using the PolyMAC discretisation on each of the early mentioned meshes. The matrices are in [binary PETSC format}(https://petsc.org/main/docs/manualpages/Sys/PetscBinaryRead.html).  

The benchmark is detailed in the document [DescriptionBenchmark.pdf](DescriptionBenchmark.pdf).

