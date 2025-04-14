"""
This runs the optimisation portion of the adjoint test case. A forward run first sets up
the tape with the adjoint information, then a misfit functional is constructed to be
used as the goal condition for nonlinear optimisation using ROL.

annulus_taylor_test is also added to this script for testing the correctness of the gradient for the inverse problem.
    taylor_test(alpha_T, alpha_u, alpha_d, alpha_s):
            alpha_T (float): The coefficient of the temperature misfit term.
            alpha_u (float): The coefficient of the velocity misfit term.
            alpha_d (float): The coefficient of the initial condition damping term.
            alpha_s (float): The coefficient of the smoothing term.
            float: The minimum convergence rate from the Taylor test. (Should be close to 2)
"""
from gadopt import *
from gadopt.inverse import *
import numpy as np
# from checkpoint_schedules import SingleDiskStorageSchedule
import sys
from mpi4py import MPI
import argparse
from gadopt.utility import CombinedSurfaceMeasure
from gadopt.utility import vertical_component as vc
parser = argparse.ArgumentParser()
parser.add_argument("--ncells", default=90, type=float, help="Number of cells in the horizontal surface mesh", required=False)
parser.add_argument("--DG0_layers", default=5, type=int, help="Number of cells per layer for DG0 discretisation of background profiles", required=False)
parser.add_argument("--dt_years", default=1000, type=float, help="Timestep in years", required=False)
parser.add_argument("--Tend", default=10e3, type=float, help="Simulation end time in years", required=False)
parser.add_argument("--bulk_shear_ratio", default=1.94, type=float, help="Ratio of Bulk modulus / Shear modulus", required=False)
parser.add_argument("--write_output", action='store_true', help="Write out Paraview VTK files")
parser.add_argument("--optional_name", default="", type=str, help="Optional string to add to simulation name for outputs", required=False)
parser.add_argument("--output_path", default="/data/viscoelastic/internal_variable_adjoint/adjoint/", type=str, help="Optional output path", required=False)
parser.add_argument("--control", default="ice", type=str, help="Specify which control, ice/viscosity/both", required=False)
parser.add_argument("--solution_checkpoint", default="/data/viscoelastic/internal_variable_adjoint/adjoint/", type=str, help="Solution checkpoint", required=False)
args = parser.parse_args()

name = f"adjoint-cylinder-2d-internalvariable-un0bottombulkoff-{args.optional_name}"



def inverse(): #alpha_T=1e0, alpha_u=1e-1, alpha_d=1e-2, alpha_s=1e-1):

    # For solving the inverse problem we the reduced functional, any callback functions,
    # and the initial guess for the control variable
    inverse_problem = generate_inverse_problem() #alpha_u=alpha_u, alpha_d=alpha_d, alpha_s=alpha_s)

    
    minimisation_problem = MinimizationProblem(inverse_problem["reduced_functional"], bounds=inverse_problem["bounds"])

#    minimisation_parameters["Status Test"]["Iteration Limit"] = 15
#    minimisation_parameters["Step"]["Trust Region"]["Initial Radius"] = 1e4

    optimiser = LinMoreOptimiser(
        minimisation_problem,
        minimisation_parameters,
        checkpoint_dir="optimisation_checkpoint",
    )

    
    # Restart file for optimisation...
    updated_solution_file = VTKFile("updated_both_dt1000_test_dispvel_noreg.pvd")
    updated_out_file = VTKFile("updated_out.pvd")
    functional_values = []

    #optimiser.add_callback(inverse_problem["callback"])
    optimiser.run()
    
    with open("functional.txt", "w") as f:
        f.write("\n".join(str(x) for x in functional_values))

    # If we're performing multiple successive optimisations, we want
    # to ensure the annotations are switched back on for the next code
    # to use them
    continue_annotation()


def visc_taylor_test(): #alpha_T, alpha_u, alpha_d, alpha_s):
    """
    Perform a Taylor test to verify the correctness of the gradient for the inverse problem.

    This function calls a main function to populate the tape for the inverse problem
    with specified regularization parameters, generates a random perturbation for the control variable,
    and performs a Taylor test to ensure the gradient is correct. Finally, it ensures that annotations
    are switched back on for any subsequent tests.

    Returns:
        minconv (float): The minimum convergence rate from the Taylor test.
    """

    # For solving the inverse problem we the reduced functional, any callback functions,
    # and the initial guess for the control variable
    inverse_problem = generate_inverse_problem() #alpha_T, alpha_u, alpha_d, alpha_s)

    # generate perturbation for the control variable
    h = Function(inverse_problem["control"].function_space(), name="perturbation")
    h.dat.data[:] = np.random.random(h.dat.data.shape)

    # Perform a taylor test to ensure the gradient is correct
    minconv = taylor_test(
        inverse_problem["reduced_functional"],
        inverse_problem["control"],
        h
    )

    # If we're performing mulitple successive tests we want
    # to ensure the annotations are switched back on for the next code to use them
    continue_annotation()

    return minconv


def generate_inverse_problem(): # alpha_T=1.0, alpha_u=-1, alpha_d=-1, alpha_s=-1):
    """
    Use adjoint-based optimisation to solve for the initial condition of the cylindrical
    problem.

    Parameters:
        alpha_u: The coefficient of the velocity misfit term
        alpha_d: The coefficient of the initial condition damping term
        alpha_s: The coefficient of the smoothing term
    """

    # Get working tape
    tape = get_working_tape()
    tape.clear_tape()

    # # Writing to disk for block variables
    # enable_disk_checkpointing()

    # # Using SingleDiskStorageSchedule
    # if any([alpha_T > 0, alpha_u > 0]):
    #     tape.enable_checkpointing(SingleDiskStorageSchedule())

    # If we are not annotating, let's switch on taping
    if not annotate_tape():
        continue_annotation()
    # +
    # Set up geometry:
    radius_values = [6371e3, 6301e3, 5951e3, 5701e3, 3480e3]
    D = radius_values[0]-radius_values[-1]
    radius_values_tilde = np.array(radius_values)/D
     
    DG0_layers = args.DG0_layers

    # Set up geometry:
    #checkpoint_file = "displacement-objective-forward-cylinder-2d-internalvariable-un0bottombulkoff--ncells180-nz5perlayer-dt200.0years-bulk1.94-nondim.h5"
    #checkpoint_file = "displacement-objective-forward-cylinder-2d-internalvariable-un0bottombulkoff-direct_rotnull-ncells90.0-nz5perlayer-dt1000.0years-bulk1.94-nondim.h5"
    #checkpoint_file = "displacement-objective-forward-cylinder-2d-internalvariable-un0bottombulkoff--ncells180-nz10perlayer-dt100.0years-bulk1.94-nondim.h5"
    checkpoint_file = "displacement-objective-forward-cylinder-2d-internalvariable-dispvel--ncells360.0-nz20perlayer-dt50.0years-bulk1.94-nondim.h5"
    with CheckpointFile(checkpoint_file, 'r') as afile:
        mesh = afile.load_mesh(name='surface_mesh_extruded')

    mesh.cartesian = False
    boundary = get_boundary_ids(mesh)
    nz = f"{DG0_layers}perlayer"

    ds = CombinedSurfaceMeasure(mesh, degree=6)

    log("Area of annulus: ", assemble(Constant(1) * dx(domain=mesh)))
    log("Length of top: ", assemble(Constant(1) * ds(boundary.top, domain=mesh)))
    log("Length of bottom: ", assemble(Constant(1) * ds(boundary.bottom, domain=mesh)))

    # -

    # Set up function spaces:
    V = VectorFunctionSpace(mesh, "CG", 2)  # Displacement function space (vector)
    S = TensorFunctionSpace(mesh, "DQ", 1)  # (Discontinuous) Stress tensor function space (tensor)
    DG0 = FunctionSpace(mesh, "DG", 0)  # (Discontinuous) Stress tensor function space (tensor)
    DG1 = FunctionSpace(mesh, "DG", 1)  # (Discontinuous) Stress tensor function space (tensor)
    P1 = FunctionSpace(mesh, "CG", 1)  
    R = FunctionSpace(mesh, "R", 0)  # Real function space (for constants)

    # Function spaces can be combined in the natural way to create mixed
    # function spaces, combining the incremental displacement and pressure spaces to form
    # a function space for the mixed Stokes problem, `Z`.

    Z = MixedFunctionSpace([V, S])  # Mixed function space.

    # We also specify functions to hold our solutions: `z` in the mixed
    # function space, noting that a symbolic representation of the two
    # parts – incremental displacement and pressure – is obtained with `split`. For later
    # visualisation, we rename the subfunctions of `z` to *Incremental Displacement* and *Pressure*.
    #
    # We also need to initialise two functions `displacement` and `stress_old` that are used when timestepping the constitutive equation.

    # +
    z = Function(Z)  # A field over the mixed function space Z.
    # Function to store the solutions:
    u, m = split(z)  # Returns symbolic UFL expression for u and m
    # Next rename for output:
    z.subfunctions[0].rename("Displacement")
    z.subfunctions[1].rename("Internal variable")
    # -

    # We can output function space information, for example the number of degrees
    # of freedom (DOF).

    # Output function space information:
    log("Number of Displacement DOF:", V.dim())
    log("Number of Internal variable  DOF:", S.dim())
    log("Number of Velocity and internal variable DOF:", V.dim()+S.dim())

    # Let's start initialising some parameters. First of all Firedrake has a helpful function to give a symbolic representation of the mesh coordinates.

    X = SpatialCoordinate(mesh)

    # Now we can set up the background profiles for the material properties.
    # In this case the density, shear modulus and viscosity only vary in the vertical direction.
    # We will approximate the series of layers using a smooth tanh function with a width of 20 km.
    # The layer properties specified are from spada et al. (2011).
    # N.b. that we have modified the viscosity of the Lithosphere viscosity from
    # Spada et al. (2011) because we are using coarse grid resolution.


    # +
    density_values = [3037, 3438, 3871, 4978]
    shear_modulus_values = [0.50605e11, 0.70363e11, 1.05490e11, 2.28340e11]
    viscosity_values = [1e25, 1e21, 1e21, 2e21]

    density_scale = 4500
    shear_modulus_scale = 1e11
    viscosity_scale = 1e21

    density_values_tilde = np.array(density_values)/density_scale
    shear_modulus_values_tilde = np.array(shear_modulus_values)/shear_modulus_scale
    viscosity_values_tilde = np.array(viscosity_values)/viscosity_scale


    def initialise_background_field(field, background_values):
        for i in range(0, len(background_values)):
            field.interpolate(conditional(vc(X) >= radius_values_tilde[i+1],
                              conditional(vc(X) <= radius_values_tilde[i],
                              background_values[i], field), field))



    density = Function(DG0, name="density")
    initialise_background_field(density, density_values_tilde)

    shear_modulus = Function(DG0, name="shear modulus")
    initialise_background_field(shear_modulus, shear_modulus_values_tilde)

    # if Pseudo incompressible set bulk modulus to a constant...
    # Otherwise use same jumps from shear modulus multiplied by a factor

    bulk_modulus = Function(DG0, name="bulk modulus")
    initialise_background_field(bulk_modulus, shear_modulus_values_tilde)

    background_viscosity = Function(DG0, name="background viscosity")
    initialise_background_field(background_viscosity, viscosity_values_tilde)

    background_viscosity_DG1 = Function(DG1, name="background viscosity DG1").interpolate(background_viscosity)

    # Defined lateral viscosity regions
    def bivariate_gaussian(x, y, mu_x, mu_y, sigma_x, sigma_y, rho, normalised_area=False):
        arg = ((x-mu_x)/sigma_x)**2 - 2*rho*((x-mu_x)/sigma_x)*((y-mu_y)/sigma_y) + ((y-mu_y)/sigma_y)**2
        numerator = exp(-1/(2*(1-rho**2))*arg)
        if normalised_area:
            denominator = 2*pi*sigma_x*sigma_y*(1-rho**2)**0.5
        else:
            denominator = 1
        return numerator / denominator


    def setup_heterogenous_viscosity(viscosity):
        heterogenous_viscosity_field = Function(viscosity.function_space(), name='viscosity')
        antarctica_x, antarctica_y = -2e6/D, -5.5e6/D

        low_visc = 1e20/viscosity_scale
        high_visc = 1e22/viscosity_scale

        low_viscosity_antarctica = bivariate_gaussian(X[0], X[1], antarctica_x, antarctica_y, 1.5e6/D, 0.5e6/D, -0.4)
        heterogenous_viscosity_field.interpolate(low_visc*low_viscosity_antarctica + viscosity * (1-low_viscosity_antarctica))

        llsvp1_x, llsvp1_y = 3.5e6/D, 0
        llsvp1 = bivariate_gaussian(X[0], X[1], llsvp1_x, llsvp1_y, 0.75e6/D, 1e6/D, 0)
        heterogenous_viscosity_field.interpolate(low_visc*llsvp1 + heterogenous_viscosity_field * (1-llsvp1))

        llsvp2_x, llsvp2_y = -3.5e6/D, 0
        llsvp2 = bivariate_gaussian(X[0], X[1], llsvp2_x, llsvp2_y, 0.75e6/D, 1e6/D, 0)
        heterogenous_viscosity_field.interpolate(low_visc*llsvp2 + heterogenous_viscosity_field * (1-llsvp2))

        slab_x, slab_y = 3e6/D, 4.5e6/D
        slab = bivariate_gaussian(X[0], X[1], slab_x, slab_y, 0.7e6/D, 0.35e6/D, 0.7)
        heterogenous_viscosity_field.interpolate(high_visc*slab + heterogenous_viscosity_field * (1-slab))

        high_viscosity_craton_x, high_viscosity_craton_y = 0, 6.2e6/D
        high_viscosity_craton = bivariate_gaussian(X[0], X[1], high_viscosity_craton_x, high_viscosity_craton_y, 1.5e6/D, 0.5e6/D, 0.2)
        heterogenous_viscosity_field.interpolate(high_visc*high_viscosity_craton + heterogenous_viscosity_field * (1-high_viscosity_craton))

        return heterogenous_viscosity_field


    target_viscosity = setup_heterogenous_viscosity(background_viscosity_DG1)

    control_viscosity = Function(P1, name="control viscosity")
    control1 = Control(control_viscosity)

    viscosity = background_viscosity * 10**control_viscosity


    # -

    # Next let's define the length of our time step. If we want to accurately resolve the elastic response we should choose a
    # timestep lower than the Maxwell time, $\alpha = \eta / \mu$. The Maxwell time is the time taken for the viscous deformation
    # to 'catch up' with the initial, instantaneous elastic deformation.
    #
    # Let's print out the Maxwell time for each layer

    year_in_seconds = 8.64e4 * 365.25
    characteristic_maxwell_time = viscosity_scale / shear_modulus_scale
    for layer_visc, layer_mu in zip(viscosity_values, shear_modulus_values):
        log(f"Maxwell time: {float(layer_visc/layer_mu/year_in_seconds):.0f} years")
        log(f"Ratio to characteristic maxwell time: {float(layer_visc/layer_mu/characteristic_maxwell_time)}")


    # +
    # Timestepping parameters
    Tstart = 0
    time = Function(R).assign(Tstart * year_in_seconds/ characteristic_maxwell_time)

    dt_years = args.dt_years
    dt = Constant(dt_years * year_in_seconds/characteristic_maxwell_time)
    Tend_years = args.Tend
    Tend = Constant(Tend_years * year_in_seconds/characteristic_maxwell_time)
    dt_out_years = 1e3
    dt_out = Constant(dt_out_years * year_in_seconds/characteristic_maxwell_time)

    max_timesteps = round((Tend - Tstart * year_in_seconds/characteristic_maxwell_time) / dt)
    log("max timesteps: ", max_timesteps)

    output_frequency = round(dt_out / dt)
    log("output_frequency:", output_frequency)
    log(f"dt: {float(dt)} maxwell times")
    log(f"dt: {float(dt * characteristic_maxwell_time / year_in_seconds)} years")
    log(f"Simulation start time: {Tstart} maxwell times")
    log(f"Simulation end time: {Tend} maxwell times")
    log(f"Simulation end time: {float(Tend * characteristic_maxwell_time / year_in_seconds)} years")
    # -


    # Initialise ice loading
    rho_ice = 931 / density_scale
    g = 9.815
    Vi = Constant(density_scale * D * g / shear_modulus_scale)
    log("Ratio of buoyancy/shear = rho g D / mu = ", float(Vi))
    Hice1 = 1000 / D
    Hice2 = 2000 / D
    # Disc ice load but with a smooth transition given by a tanh profile
    disc_halfwidth1 = (2*pi/360) * 10  # Disk half width in radians
    disc_halfwidth2 = (2*pi/360) * 20  # Disk half width in radians
    surface_dx_smooth = 200*1e3
    ncells_smooth = 2*pi*radius_values[0] / surface_dx_smooth
    surface_resolution_radians_smooth = 2*pi / ncells_smooth
    colatitude = atan2(X[0], X[1])
    disc1_centre = (2*pi/360) * 25  # centre of disc1
    disc2_centre = pi  # centre of disc2
    disc1 = 0.5*(1-tanh((abs(colatitude-disc1_centre) - disc_halfwidth1) / (2*surface_resolution_radians_smooth)))
    disc2 = 0.5*(1-tanh((abs(abs(colatitude)-disc2_centre) - disc_halfwidth2) / (2*surface_resolution_radians_smooth)))

    #P1 = FunctionSpace(mesh, "CG", 1)

    #discfunc = Function(P1).interpolate(disc)
    
    #discfile = VTKFile(f"{args.output_path}discfile.pvd").write(discfunc)
    target_normalised_ice_thickness = Function(P1, name="target normalised ice thickness")
    target_normalised_ice_thickness.interpolate(disc1 + Hice2/Hice1 * disc2)
    
    # defining the control
    control_ice_thickness = Function(P1, name="control normalised ice thickness")
    control2 = Control(control_ice_thickness)

    # the ice thickness that will be actually used in simulation
    normalised_ice_thickness = Function(P1, name="normalised ice thickness")
    normalised_ice_thickness.project(control_ice_thickness, bcs=[InteriorBC(P1, 0, boundary.top)])
    ice_load = Vi * rho_ice * Hice1 * normalised_ice_thickness 
    
#    ice_load = Vi * rho_ice * (Hice1 * disc1 + Hice2 * disc2)

    # We can now define the boundary conditions to be used in this simulation.  Let's set the bottom and
    # side boundaries to be free slip with no normal flow $\textbf{u} \cdot \textbf{n} =0$. By passing
    # the string `ux` and `uy`, G-ADOPT knows to specify these as Strong Dirichlet boundary conditions.
    #
    # For the top surface we need to specify a normal stress, i.e. the weight of the ice load, as well as
    # indicating this is a free surface.
    #
    # +
    # Setup boundary conditions
    stokes_bcs = {
        boundary.bottom: {'un': 0},
        boundary.top: {'normal_stress': ice_load, 'free_surface': {}},
    }

    gd = GeodynamicalDiagnostics(z, density, boundary.bottom, boundary.top)
    # -


    # We also need to specify a G-ADOPT approximation which sets up the various parameters and fields
    # needed for the viscoelastic loading problem.

    approximation = CompressibleInternalVariableApproximation(bulk_modulus=bulk_modulus, density=density, shear_modulus=shear_modulus, viscosity=viscosity, Vi=Vi, bulk_shear_ratio=args.bulk_shear_ratio)

    # We finally come to solving the variational problem, with solver
    # objects for the Stokes system created. We pass in the solution fields `z` and various fields
    # needed for the solve along with the approximation, timestep and boundary conditions.
    #

    direct_stokes_solver_parameters = {
        "snes_monitor": None,
        "mat_type": "aij",
        "ksp_type": "preonly",
        "pc_type": "lu",
        "pc_factor_mat_solver_type": "mumps",
    }

    iterative_parameters = {"mat_type": "matfree",
                            "snes_type": "ksponly",
                            "ksp_type": "gmres",
                            "ksp_rtol": 1e-7,
                            "ksp_converged_reason": None,
                            "ksp_monitor": None,
                            "pc_type": "fieldsplit",
                            "pc_fieldsplit_type": "symmetric_multiplicative",

                            "fieldsplit_0_ksp_converged_reason": None,
                            "fieldsplit_0_ksp_monitor": None,
                            "fieldsplit_0_ksp_type": "gmres",
                            "fieldsplit_0_pc_type": "python",
    #                        "fieldsplit_0_pc_python_type": "gadopt.SPDAssembledPC",
                            "fieldsplit_0_pc_python_type": "firedrake.AssembledPC",
                            "fieldsplit_0_assembled_pc_type": "gamg",
                            "fieldsplit_0_assembled_mg_levels_pc_type": "sor",
                            "fieldsplit_0_ksp_rtol": 1e-5,
                            "fieldsplit_0_assembled_pc_gamg_threshold": 0.01,
                            "fieldsplit_0_assembled_pc_gamg_square_graph": 100,
                            "fieldsplit_0_assembled_pc_gamg_coarse_eq_limit": 1000,
                            "fieldsplit_0_assembled_pc_gamg_mis_k_minimum_degree_ordering": True,

                            "fieldsplit_1_ksp_converged_reason": None,
                            "fieldsplit_1_ksp_monitor": None,
                            "fieldsplit_1_ksp_type": "cg",
                            "fieldsplit_1_pc_type": "python",
                            "fieldsplit_1_pc_python_type": "firedrake.AssembledPC",
                            "fieldsplit_1_assembled_pc_type": "sor",
                            "fieldsplit_1_ksp_rtol": 1e-5,
                            }

    Z_nullspace = create_stokes_nullspace(Z, closed=False, rotational=True)
    Z_near_nullspace = create_stokes_nullspace(Z, closed=True, rotational=True, translations=[0, 1])

    coupled_solver = InternalVariableSolver(z, approximation, coupled_dt=dt, bcs=stokes_bcs,
                                            solver_parameters=direct_stokes_solver_parameters,
     #                                       solver_parameters=iterative_parameters,
                                            nullspace=Z_nullspace, transpose_nullspace=Z_nullspace,
                                            near_nullspace=Z_near_nullspace)


    # We next set up our output, in VTK format. This format can be read by programs like pyvista and Paraview.

    # +
    # Create output file
    OUTPUT = args.write_output
    vertical_displacement = Function(V.sub(1), name="radial displacement")  # Function to store vertical displacement for output

    if OUTPUT:
        output_file = VTKFile(f"{args.output_path}{name}-ncells{args.ncells}-nz{nz}-dt{dt_years}years-bulk{args.bulk_shear_ratio}-nondim.pvd")
        output_file.write(*z.subfunctions, vertical_displacement)

    plog = ParameterLog(args.output_path+"params.log", mesh)
    plog.log_str(
        "timestep time dt u_rms u_rms_surf ux_max disp_min disp_max"
    )
    
    velocity = Function(z.subfunctions[0], name="velocity")
    disp_old = Function(z.subfunctions[0], name="old_disp").assign(z.subfunctions[0])

    checkpoint_filename = f"{args.output_path}{name}-ncells{args.ncells}-nz{nz}-dt{dt_years}years-bulktoshear{args.bulk_shear_ratio}-nondim-chk.h5"

    displacement_filename = f"{args.output_path}displacement-{name}-ncells{args.ncells}-nz{nz}-dt{dt_years}years-bulk{args.bulk_shear_ratio}-nondim.dat"

    # Initial displacement at time zero is zero
    displacement_min_array = [[0.0, 0.0]]

    def integrated_time_misfit(timestep, velocity_misfit, displacement_misfit):
        with CheckpointFile(checkpoint_file, 'r') as afile:
            target_displacement = afile.load_function(mesh, name="Displacement", idx=timestep)
            target_velocity = afile.load_function(mesh, name="Velocity", idx=timestep)
        circumference = 2 * pi * radius_values[0]
        velocity_error = velocity - target_velocity
        velocity_scale = 1e-8
        velocity_misfit += assemble(dot(velocity_error, velocity_error) / (circumference * velocity_scale**2) * ds(boundary.top))

        displacement_error = z.subfunctions[0] - target_displacement
        displacement_scale = 1e-8
        displacement_misfit += assemble(dot(displacement_error, displacement_error) / (circumference * displacement_scale**2) * ds(boundary.top))
        return velocity_misfit, displacement_misfit
    
    velocity_misfit = 0
    displacement_misfit = 0

    # -

    # Now let's run the simulation! We are going to control the ice thickness using the `ramp` parameter.
    # At each step we call `solve` to calculate the incremental displacement and pressure fields. This
    # will update the displacement at the surface and stress values accounting for the time dependent
    # Maxwell consitutive equation.

    for timestep in range(1, max_timesteps+1):
        # update time first so that ice load begins
        time.assign(time+dt)
        coupled_solver.solve()
        
        velocity.interpolate((z.subfunctions[0] - disp_old)/dt)
        disp_old.assign(z.subfunctions[0]) 
        
        velocity_misfit, displacement_misfit = integrated_time_misfit(timestep, velocity_misfit, displacement_misfit)

        # Log diagnostics:
        # Compute diagnostics:
        # output dimensional vertical displacement
        vertical_displacement.interpolate(vc(z.subfunctions[0])*D)
        bc_displacement = DirichletBC(vertical_displacement.function_space(), 0, boundary.top)
        displacement_z_min = vertical_displacement.dat.data_ro_with_halos[bc_displacement.nodes].min(initial=0)
        displacement_min = vertical_displacement.comm.allreduce(displacement_z_min, MPI.MIN)  # Minimum displacement at surface (should be top left corner with greatest (-ve) deflection due to ice loading
        log("Greatest (-ve) displacement", displacement_min)
        displacement_z_max = vertical_displacement.dat.data_ro_with_halos[bc_displacement.nodes].max(initial=0)
        displacement_max = vertical_displacement.comm.allreduce(displacement_z_max, MPI.MAX)  # Minimum displacement at surface (should be top left corner with greatest (-ve) deflection due to ice loading
        log("Greatest (+ve) displacement", displacement_max)
        displacement_min_array.append([float(characteristic_maxwell_time*time/year_in_seconds), displacement_min])

    #    disp_norm_L2surf = assemble((z.subfunctions[0][vertical_component])**2 * ds(boundary.top))
     #   log("L2 surface norm displacement", disp_norm_L2surf)

      #  disp_norm_L1surf = assemble(abs(z.subfunctions[0][vertical_component]) * ds(boundary.top))
       # log("L1 surface norm displacement", disp_norm_L1surf)

        #integrated_disp = assemble(z.subfunctions[0][vertical_component] * ds(boundary.top))
        #log("Integrated displacement", integrated_disp)

        if timestep % output_frequency == 0:
            log("timestep", timestep)

            if OUTPUT:
                output_file.write(*z.subfunctions, vertical_displacement)

            with CheckpointFile(checkpoint_filename, "w") as checkpoint:
                checkpoint.save_function(z, name="Stokes")

            if MPI.COMM_WORLD.rank == 0:
                np.savetxt(displacement_filename, displacement_min_array)

            plog.log_str(f"{timestep} {float(time)} {float(dt)} "
                         f"{gd.u_rms()} {gd.u_rms_top()} {gd.ux_max(boundary.top)} "
                         )

    circumference = 2 * pi * radius_values[0]
    area =  assemble(Constant(1) * dx(domain=mesh))

    alpha_smoothing = 0
    alpha_damping = 0
    damping = assemble((control_viscosity) ** 2 / area  * dx)
    smoothing = assemble(dot(grad(control_viscosity), grad(control_viscosity)) / area * dx)

    objective = (displacement_misfit + velocity_misfit) / max_timesteps + alpha_damping * damping + alpha_smoothing * smoothing
    log("J = ", objective)
    
    pause_annotation()
    
    # storing adjoint results
    updated_ice_thickness = Function(normalised_ice_thickness, name="updated ice thickness")
    updated_viscosity = Function(target_viscosity, name="updated viscosity")
    updated_solution_file = VTKFile("updated_both_dt1000_test_dispvel_noreg.pvd")
    updated_displacement = Function(z.subfunctions[0], name="updated displacement")
    updated_velocity = Function(z.subfunctions[0], name="updated velocity")
    updated_out_file = VTKFile("updated_out.pvd")

    functional_values = []
    
    with CheckpointFile(checkpoint_file, 'r') as afile:
        final_target_displacement = afile.load_function(mesh, name="Displacement", idx=max_timesteps)
    
    def eval_cb(J, m):
        if functional_values:
            functional_values.append(min(J, min(functional_values)))
        else:
            functional_values.append(J)

        circumference = 2 * pi * radius_values[0]
        area =  assemble(Constant(1) * dx(domain=mesh))
        # Define the component terms of the overall objective functional
        log("displacement misfit", displacement_misfit.block_variable.checkpoint / max_timesteps)
        log("velocity misfit", velocity_misfit.block_variable.checkpoint / max_timesteps)
        damping = alpha_damping * assemble((control_viscosity.block_variable.checkpoint) ** 2 / circumference /area * dx)
        smoothing = alpha_smoothing * assemble(dot(grad(control_viscosity.block_variable.checkpoint), grad(control_viscosity.block_variable.checkpoint)) / area * dx)
        log("damping", damping)
        log("smoothing", smoothing)
        '''
        damping = alpha_damping * assemble((normalised_ice_thickness.block_variable.checkpoint) ** 2 / circumference * ds(boundary.top))
        smoothing = alpha_smoothing * assemble(dot(grad(normalised_ice_thickness.block_variable.checkpoint), grad(normalised_ice_thickness.block_variable.checkpoint)) / circumference * ds(boundary.top))
        log("damping", damping)
        log("smoothing", smoothing)
        '''
             # Write out values of control and final forward model results
        updated_ice_thickness.assign(m[1])
#        updated_velocity.interpolate(z.subfunctions[0].block_variable.checkpoint / dt)
        
        # Write out values of control and final forward model results
        updated_viscosity.interpolate(background_viscosity * 10**m[0])
        updated_solution_file.write(updated_ice_thickness, target_normalised_ice_thickness, m[0], updated_viscosity, target_viscosity)
        updated_displacement.interpolate(z.subfunctions[0].block_variable.checkpoint)
        updated_out_file.write(updated_displacement, final_target_displacement)
    ice_thickness_lb = Function(normalised_ice_thickness.function_space(), name="Lower bound ice thickness")
    ice_thickness_ub = Function(normalised_ice_thickness.function_space(), name="Upper bound ice thickness")
    ice_thickness_lb.assign(0.0)
    ice_thickness_ub.assign(5)

    ice_bounds = [ice_thickness_lb, ice_thickness_ub]
    
    viscosity_lb = Function(control_viscosity.function_space(), name="Lower bound ice thickness")
    viscosity_ub = Function(control_viscosity.function_space(), name="Upper bound ice thickness")
    viscosity_lb.assign(-3)
    viscosity_ub.assign(6)

    viscosity_bounds = [viscosity_lb, viscosity_ub]
    bounds = [viscosity_bounds, ice_bounds]
    inverse_problem = {}

    # Keep track of what the control function is
    inverse_problem["control"] = [control_viscosity, control_ice_thickness]

    # The ReducedFunctional that is to be minimised
    inverse_problem["reduced_functional"] = ReducedFunctional(objective, [control1, control2], eval_cb_post=eval_cb)
    inverse_problem["bounds"] = bounds


    return inverse_problem



#visc_taylor_test()
inverse()
