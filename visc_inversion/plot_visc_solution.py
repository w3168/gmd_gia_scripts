import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyvista as pv

dpi = 300
width_inches = 5
height_inches = 5
width = round(width_inches*dpi)
height = round(height_inches*dpi)

# camera setting
radius = 2.2
zoom = 3.8

steps = [0, 1, 5, 10, 20, 30, 40, 50, 100, 200]

# read disc file to add outline at top and bottom surface of domain
reader_disc = pv.get_reader('discfile_0.vtu')
data_disc = reader_disc.read()
surf = data_disc.extract_feature_edges(boundary_edges=True, non_manifold_edges=False,
                                  feature_edges=False, manifold_edges=False)
sphere = pv.Sphere(radius=0.8*radius)
clipped_surf = surf.clip_surface(sphere, invert=False)
lw = 5

for s in steps:
    # Read the PVD file
    visc_file = f"/data/viscoelastic/internal_variable_adjoint/adjoint/setonix/visc_only/adjoint-cylinder-2d-internalvariable-ctypeviscosity-visconly_icesmooth0.0_icedamp0.0_viscsmooth1e-6_viscdamp1e-5_checkmisfit3_sol/adjoint-cylinder-2d-internalvariable-ctypeviscosity-visconly_icesmooth0.0_icedamp0.0_viscsmooth1e-6_viscdamp1e-5_checkmisfit3_sol_{s}.pvtu"

    reader = pv.get_reader(visc_file)
    data = reader.read()  # MultiBlock mesh with only 1 block


    data['updated viscosity'] *= 1e21

    # Make a colour map
    boring_cmap = plt.get_cmap("inferno_r", 25)

    plotter = pv.Plotter(window_size=(width, height),  border=False, notebook=False, off_screen=True)
    
    # add outline of domain
    plotter.add_mesh(surf, color='black',line_width=lw, lighting=False,show_scalar_bar=False)
    
    # add viscosity plot
    plotter.add_mesh(
        data,
        scalars='updated viscosity',
        component=None,
        lighting=False,
        show_edges=False,
        cmap=boring_cmap,
        clim=[1e20, 1e25],
        log_scale=True,
        show_scalar_bar=False,
    )
    plotter.camera_position = [(0, 0, radius*zoom),
                                     (0.0, 0.0, 0.0),
                                     (0.0, 1.0, 0.0)]

    plotter.screenshot(f"visc_plots/visc3d_step{s}.png")
   

    # Plot misfit
    data['viscosity'] *= 1e21
    
    #data['viscosity misfit'] = np.sqrt((data['updated viscosity']-data['viscosity'])**2/data['viscosity']**2)
    #data['viscosity misfit'] = (data['updated viscosity']-data['viscosity'])/data['viscosity']
#    data['viscosity misfit'] = np.abs(data['updated viscosity']-data['viscosity'])
#    data['viscosity misfit'] = np.log(data['updated viscosity'])-np.log(data['viscosity'])
#    data['viscosity misfit'] = np.log(np.abs(data['updated viscosity']-data['viscosity'])/data['viscosity'])
    data['viscosity misfit'] = np.log10(data['updated viscosity']/data['viscosity'])

    
    # Make a colour map
    reds_cmap = plt.get_cmap("coolwarm", 25)

    plotter = pv.Plotter(window_size=(width, height),  border=False, notebook=False, off_screen=True)

    # add outline of domain
    plotter.add_mesh(surf, color='black',line_width=lw, lighting=False,show_scalar_bar=False)

    # add misfit plot
    plotter.add_mesh(
        data,
        scalars='viscosity misfit',
        component=None,
        lighting=False,
        show_edges=False,
        cmap=reds_cmap,
        clim=[-1, 1],
        show_scalar_bar=False,
        log_scale=False,
    )
    plotter.camera_position = [(0, 0, radius*zoom),
                                     (0.0, 0.0, 0.0),
                                     (0.0, 1.0, 0.0)]

    plotter.screenshot(f"visc_misfit/visc3d_relative_misfit_loguovert_cs1_step_{s}.png")
   

    # Plot adjoints
    # Read the PVD file
    visc_file = f"/data/viscoelastic/internal_variable_adjoint/adjoint/setonix/visc_only/adjoint-cylinder-2d-internalvariable-ctypeviscosity-visconly_icesmooth0.0_icedamp0.0_viscsmooth1e-6_viscdamp1e-5_checkmisfit3_adjvisc/adjoint-cylinder-2d-internalvariable-ctypeviscosity-visconly_icesmooth0.0_icedamp0.0_viscsmooth1e-6_viscdamp1e-5_checkmisfit3_adjvisc_{s}.pvtu"

    reader = pv.get_reader(visc_file)
    data = reader.read()  # MultiBlock mesh with only 1 block

    # Make a colour map
    boring_cmap = plt.get_cmap("coolwarm", 25)

    plotter = pv.Plotter(window_size=(width, height),  border=False, notebook=False, off_screen=True)
    
    # add outline of domain
    plotter.add_mesh(surf, color='black',line_width=lw, lighting=False,show_scalar_bar=False)
    
    # add adjoint viscosity plot
    plotter.add_mesh(
        data,
        scalars='adjoint_control viscosity',
        component=None,
        lighting=False,
        show_edges=False,
        cmap=boring_cmap,
        clim=[-0.01, 0.01],
        show_scalar_bar=False,
    )
    plotter.camera_position = [(0, 0, radius*zoom),
                                     (0.0, 0.0, 0.0),
                                     (0.0, 1.0, 0.0)]

    plotter.screenshot(f"visc_adj/visc3d_adj_step{s}.png")
