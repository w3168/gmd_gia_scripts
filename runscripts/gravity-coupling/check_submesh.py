from gadopt import *
from math import pi
full_mesh = Mesh("unstructured_annulus_refined_surface_gravity.msh")



    
Rg = 31855e3
Re = 6371e3
grav_mesh_depth = Rg-Re
Rc = 3480e3
D = Re-Rc

Rg_tilde = Rg/D
Re_tilde = Re/D
Rc_tilde = Rc/D
grav_mesh_depth_tilde = grav_mesh_depth/D

log("Area of annulus should be: ", pi*(Rg_tilde**2-Rc_tilde**2))
log("Area of annulus: ", assemble(Constant(1) * dx(domain=full_mesh)))

log("Area of exterior grav: ", assemble(Constant(1) * dx(102, domain=full_mesh)))
log("Area of mantle: ", assemble(Constant(1) * dx(101, domain=full_mesh)))


log("Circumference of CMB should be: ", 2*pi*Rc_tilde)
log("Circumference of CMB: ", assemble(Constant(1) * ds(1, domain=full_mesh)))
log("Circumference of Earth: ", assemble(Constant(1) * dS(2, domain=full_mesh)))
log("Circumference of grav mesh: ", assemble(Constant(1) * ds(3, domain=full_mesh)))


#log("Area of annulus gravity mesh: ", assemble(Constant(1) * dx(domain=mesh_grav)))
#log("Length of top gravity mesh: ", assemble(Constant(1) * ds_grav(boundary_grav.top, domain=mesh_grav)))
#log("Length of bottom gravity mesh: ", assemble(Constant(1) * ds_grav(boundary_grav.bottom, domain=mesh_grav)))

DG0 = FunctionSpace(full_mesh, "DG", 0)
mantle_id = 101
exterior_grav_id = 102
# Heaviside step function in mantle
I_mantle = Function(DG0)
par_loop(("{[i] : 0 <= i < f.dofs}", "f[i, 0] = 1.0"),
         dx(mantle_id),
         {"f": (I_mantle, WRITE)})


mantle_indicator_file = VTKFile("mantle_indicator.pvd").write(I_mantle)
dim = 2
full_mesh.mark_entities(I_mantle, 999)
full_mesh = RelabeledMesh(full_mesh, [I_mantle], [999])
mesh = Submesh(full_mesh, dim, 999)

V = FunctionSpace(mesh, "CG", 1)
DG0 = FunctionSpace(mesh, "DG", 0)

testfunc = Function(V)




density = Function(DG0).assign(1)

density2 = Function(DG0).interpolate(density)

testfile2 = VTKFile("testmantle_interp.pvd").write(density, density2)



