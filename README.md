# Navier-Stokes 3D benchmark
This is the git repository of the 3D benchmark for the minisymposium "Saddle point problems in fluid dynamics".  
The problem consists in solving the incompressible Navier-Stokes equation in a channel.
The two geometries are the [Cube](Cube) and the [Nuclear Assembly](NuclearAssembly).
For each geometry there are families of meshes enabling to study the increase of linear solver iterations as the mesh is  refined. The meshes are given in [MED](https://docs.salome-platform.org/8/dev/MEDCoupling/med-file.html) and [GMSH](https://gmsh.info/) binary formats. Note that both formats can be opened and converted using the software GMSH available on Windows, MacOS and Linux [here](http://gmsh.info/bin/).  
The benchmark is detailed in the document [DescriptionBenchmark.pdf](DescriptionBenchmark.pdf).

