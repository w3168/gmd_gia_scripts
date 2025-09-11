README

This readme provides information associated with the manuscript 
Automated forward and adjoint modelling of viscoelastic deformation of the solid Earth

William Scott, Mark Hoggard, Thomas Duvernay, Sia Ghelichkhan, Angus Gibson,
Dale Roberts, Stephan C. Kramer, and D. Rhodri Davies


##############################################

# Installation


Instructions for installing Firedrake can be found here 
https://www.firedrakeproject.org/install.html

Section 2 of the manuscript describes two formulations for solving 
viscoelastic deformation in G-ADOPT referred to as the 'substitute' (Eq. 32)
and 'coupled' approach (Eqs. 33 and 34). 

With the Firedrake venv activated the necessary g-adopt code can be installed using pip. 

To run cases using the 'substitute' method  

 > pip install -e g-adopt-substitute
 
 Or to run cases using the 'coupled' method:
 
 >  pip install -e g-adopt-coupled

################################################

# Runscripts

To run cases from the following sections the commands are as follows:

## Section 3.1

The runscript for the 'substitute' case can be found

g-adopt-coupled/tests/glacial_isostatic_adjustment/iv_ve_fs.py

To run the elastic case used in Figure 1

> python iv_ve_fs.py --case "elastic-compressible-visc1e21-shear1e11-bulk2e11-lam8-compahpFalse"

To run the viscoelastic case used in Figure 1

python iv_ve_fs.py --case "viscoelastic-compressible-visc1e21-shear1e11-bulk2e11-lam8-dtfstart16alpha-compahpFalse_160alpha"


The equivalent runscript for the 'coupled' case can be found 

g-adopt-coupled/tests/glacial_isostatic_adjustment/iv_ve_fs.py

Plotting scripts for Figure 1 can be found here

gmd_gia_scripts/analytical/Fig1/plot_figure1_mosaic.py


## Section 3.2

The surface unstructured mesh files can be generated using the script which relies on 
a GMSH installation (https://gmsh.info/)

The GMSH .geo file for creating the surface mesh is

g-adopt-substitute/tests/glacial_isostatic_adjustment/weerdesteijn_box_refined_surface_nondim.geo

A bash script to generate the 3 surface meshes used for Figure 4 is

g-adopt-substitute/tests/glacial_isostatic_adjustment/generate_surface_meshes.sh

Compressed surface .msh files are included in this zenodo repository if you do not have 
GMSH installation. i.e. the *.msh.gz files can be unzipped using gunzip and moved to the relevant directory.

For the incompressible cases (Fig. 3) we use the 'coupled' formulation. The runscript can be found

g-adopt-coupled/tests/glacial_isostatic_adjustment/3d_weerdesteijn/3d_weerdesteijn_nondim.py

To run the short loading, 1D viscosity case

> python 3d_weerdesteijn_nondim.py --dx 5 --refined_surface --bulk_shear_ratio 1000 --DG0_layers 10 --dt_years 10 --dt_out_years 20 --short_simulation --Tend 200

To run the short loading, 3D viscosity case

> python 3d_weerdesteijn_nondim.py --dx 5 --refined_surface --bulk_shear_ratio 1000 --DG0_layers 10 --dt_years 10 --dt_out_years 20 --short_simulation --Tend 200 --lateral_viscosity

To run the long loading, 1D viscosity case

> python 3d_weerdesteijn_nondim.py --dx 5 --refined_surface --bulk_shear_ratio 1000 --DG0_layers 10 --dt_years 1000

To run the long loading, 3D viscosity case

> python 3d_weerdesteijn_nondim.py --dx 5 --refined_surface --bulk_shear_ratio 1000 --DG0_layers 10 --dt_years 1000 --lateral_viscosity

Results from Fig. 4 can be obtained by varying dx, DG0_layers (number of cells per rheological layer), bulk_shear_ratio, dt_years

The equivalent 'substitute' formulation runscript can be found

g-adopt-substitute/tests/glacial_isostatic_adjustment/3d_weerdesteijn/3d_weerdesteijn_nondim.py

N.b. this was run on the GADI supercomputer on ~832 cores.

Plotting scripts for Figure 3 can be found here

gmd_gia_scripts/weerdesteijn_data/Fig3/plot_figure3.py

Plotting scripts for Figure 4 can be found here
gmd_gia_scripts/weerdesteijn_data/Fig4/plot_figure4.py


## Section 3.3 

Surface mesh files are the same as Section 3.2.

The runscript for the compressible Burgers case is

g-adopt-substitute/tests/glacial_isostatic_adjustment/3d_weerdesteijn_burgers/3d_weerdesteijn_burgers_nondim.py

To run the short loading, compressible Burgers case (with viscosity_2/viscosity_1 = 0.5)

> python 3d_weerdesteijn_burgers_nondim.py --dx 5 --refined_surface --bulk_shear_ratio 1.94 --DG0_layers 10 --dt_years 10 --dt_out_years 20 --short_simulation --Tend 200 --viscosity_ratio 0.5

The long loading case does not reqire the Tend and short_simulation options as in Section 3.2.

N.b. this was run on the GADI supercomputer on ~832 cores.

Plotting scripts for Figure 5 can be found 
gmd_gia_scripts/weerdesteijn_data/Fig5/plot_figure5.py

## Section 3.4

The runscript for the spherical Burgers case with lateral viscosity variations is

g-adopt-substitute/tests/glacial_isostatic_adjustment/3d_sphere_burgers/3d_sphere_burgers.py

To run the simulation

> python 3d_sphere_burgers.py --reflevel 6 --bulk_shear_ratio 1.94 --DG0_layers 10 --dt_years 50 --dt_out_years 1000 --viscosity_ratio 0.1

N.b. this was run on the GADI supercomputer on ~832 cores.

The 'coupled' script can be found here 

g-adopt-coupled/tests/glacial_isostatic_adjustment/3d_sphere_burgers/3d_sphere_burgers.py

Figure 6 was created using Paraview (https://www.paraview.org/)


##  Section 3.5.1

The runscript for the forward cylindrical case with lateral viscosity variations via the 'substitute' method is

gmd_gia_scripts/runscripts/internal_variable_adjoint/forward_sub.py

To run the laterally varying viscosity case 

> python forward_sub.py --dt_years 50 --ncells 360 --DG0_layers 20

To run the purely radial viscosity case 

> python forward_sub.py --dt_years 50 --ncells 360 --DG0_layers 20 --radial_visc

The equivlalent script using the 'coupled' method is 

/gmd_gia_scripts/runscripts/internal_variable_adjoint/forward.py

Plotting scripts can be found here

gmd_gia_scripts/runscripts/internal_variable_adjoint/plotting

Figure 7 can be plotted with 

plot_figure7_visc_ice_forward.py 

Figure 8 can be plotted with 

plot_figure_dispvel_misfits.py


## Section 3.5.2

The runscript for the ice inversion is 

gmd_gia_scripts/runscripts/internal_variable_adjoint/adjoint_both_iterative_icemesh_sub.py

To run the ice inversion with the correct (laterally varying) viscosity structure

> python adjoint_both_iterative_icemesh_sub.py --ncells 360 --DG0_layers 20 --dt_years 50 --controls ice --true_visc --opt_its 100

To run the ice inversion with the incorrect (radial) viscosity structure

> python adjoint_both_iterative_icemesh_sub.py --ncells 360 --DG0_layers 20 --dt_years 50 --controls ice --opt_its 100

The 'coupled' version of this script is 

gmd_gia_scripts/runscripts/internal_variable_adjoint/adjoint_both_iterative_icemesh.py

Figure 9 can be plotted with 

gmd_gia_scripts/ice_inversion/plot_figure9_iceinverse.py


## Section 3.5.3

The runscript for the viscosity inversion is the same as Section 3.5.2

/gmd_gia_scripts/runscripts/internal_variable_adjoint/adjoint_both_iterative_icemesh_sub.py

To run the ice inversion with the correct (laterally varying) viscosity structure

> python adjoint_both_iterative_icemesh_sub.py --ncells 360 --DG0_layers 20 --dt_years 50 --controls viscosity --true_ice --opt_its 100

As in Section 3.5.2 the 'coupled' version of the script is

gmd_gia_scripts/runscripts/internal_variable_adjoint/adjoint_both_iterative_icemesh.py

Figure 10 can be plotted with 

gmd_gia_scripts/visc_inversion/plot_visc_solution.py

and 

gmd_gia_scripts/visc_inversion/plot_figure10_visc_inversion.py

Figure 11 can be plotted with 

gmd_gia_scripts/visc_inversion/plot_visc_objective.py


## Section 3.5.4

The runscript inverting for both ice thickness and viscosity is the same as Section 3.5.2 and 3.5.3

/gmd_gia_scripts/runscripts/internal_variable_adjoint/adjoint_both_iterative_icemesh_sub.py

To run the inversion 

> python adjoint_both_iterative_icemesh_sub.py --ncells 360 --DG0_layers 20 --dt_years 50 --controls both --opt_its 100

As in Section 3.5.2 and 3.5.3 the 'coupled' version of the script is

gmd_gia_scripts/runscripts/internal_variable_adjoint/adjoint_both_iterative_icemesh.py

Figure 12 can be plotted with 

gmd_gia_scripts/both_inversion/icemesh/plot_figure12_both_icevisc_inversion.py

Figure 13 can be plotted with 

gmd_gia_scripts/both_inversion/icemesh/plot_figure13_both_viscicerings.py
