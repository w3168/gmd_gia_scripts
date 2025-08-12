import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyvista as pv

dpi = 300
width_inches = 5
height_inches = 5
width = round(width_inches*dpi)
height = round(height_inches*dpi)

# Read the PVD file
visc_1d_file = "forward-cylinder-2d-internalvariable-dispvel--1dviscTrue-visc/forward-cylinder-2d-internalvariable-dispvel--1dviscTrue-visc_0.pvtu"
visc_3d_file = "forward-cylinder-2d-internalvariable-dispvel-lithvisc-1dviscFalse-visc/forward-cylinder-2d-internalvariable-dispvel-lithvisc-1dviscFalse-visc_0.pvtu"

ice_file = 'discfile_0.vtu'

radius = 2.2
zoom =4.25
lw = 5
reader_1d = pv.get_reader(visc_1d_file)
reader_3d = pv.get_reader(visc_3d_file)
data_1d = reader_1d.read()  # MultiBlock mesh with only 1 block
data_3d = reader_3d.read()  # MultiBlock mesh with only 1 block

reader_ice = pv.get_reader(ice_file)
data_ice = reader_ice.read()

# Make ice ring: Extract boundary surface, remove inner surface and expand ring width
surf = data_ice.extract_feature_edges(boundary_edges=True, non_manifold_edges=False,
                                  feature_edges=False, manifold_edges=False)
sphere = pv.Sphere(radius=0.8*radius)
clipped_surf = surf.clip_surface(sphere, invert=False)

# Stretch line by 20%
stretch = 1.1
transform_matrix = np.array(
    [
        [stretch, 0, 0, 0],
        [0, stretch, 0, 0],
        [0, 0, stretch, 0],
        [0, 0, 0, 1],
    ])
transformed_surf = clipped_surf.transform(transform_matrix)
ice_cmap = plt.get_cmap("Blues", 25)
ice_lw = 28


data_1d['viscosity'] *= 1e21
data_3d['viscosity'] *= 1e21

# Make a colour map
boring_cmap = plt.get_cmap("inferno_r", 25)
# Create a plotter object
plotter = pv.Plotter(window_size=(width, height),  border=False, notebook=False, off_screen=True)
# add outline of domain
plotter.add_mesh(surf, color='black',line_width=lw, lighting=False,show_scalar_bar=False)

# Plot viscosity
# Add the warped displacement field to the frame
plotter.add_mesh(
    data_1d,
    component=None,
    lighting=False,
    show_edges=False,
    cmap=boring_cmap,
    clim=[1e20, 1e25],
    log_scale=True,
    show_scalar_bar=False,
)


# add ice ring to image
plotter.add_mesh(transformed_surf,color='black', line_width=ice_lw+2, lighting=False, show_scalar_bar=False)
plotter.add_mesh(transformed_surf, line_width=ice_lw, clim=[0, 2000], cmap=ice_cmap, lighting=False, show_scalar_bar=False)

plotter.camera_position = [(0, 0, radius*zoom),
                                 (0.0, 0.0, 0.0),
                                 (0.0, 1.0, 0.0)]

plotter.screenshot("visc1d.png")

plotter = pv.Plotter(window_size=(width, height),  border=False, notebook=False, off_screen=True)

# add outline of domain
plotter.add_mesh(surf, color='black',line_width=lw, lighting=False,show_scalar_bar=False)

# add viscosity
plotter.add_mesh(
    data_3d,
    component=None,
    lighting=False,
    show_edges=False,
    cmap=boring_cmap,
    clim=[1e20, 1e25],
    log_scale=True,
    show_scalar_bar=False,
)

# Add slightly thicker black ring first to get outline of ice...
plotter.add_mesh(transformed_surf,color='black', line_width=ice_lw+2, lighting=False, show_scalar_bar=False)
# add ice ring to image
plotter.add_mesh(transformed_surf, line_width=ice_lw, clim=[0, 2000], cmap=ice_cmap, lighting=False, show_scalar_bar=False)
plotter.camera_position = [(0, 0, radius*zoom),
                                 (0.0, 0.0, 0.0),
                                 (0.0, 1.0, 0.0)]

plotter.screenshot("visc3d.png")
