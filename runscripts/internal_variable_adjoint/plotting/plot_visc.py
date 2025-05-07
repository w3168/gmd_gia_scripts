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
visc_3d_file = "forward-cylinder-2d-internalvariable-dispvel--1dviscFalse-visc/forward-cylinder-2d-internalvariable-dispvel--1dviscFalse-visc_0.pvtu"

radius = 2.2
zoom = 3.8
reader_1d = pv.get_reader(visc_1d_file)
reader_3d = pv.get_reader(visc_3d_file)
data_1d = reader_1d.read()  # MultiBlock mesh with only 1 block
data_3d = reader_3d.read()  # MultiBlock mesh with only 1 block


data_1d['viscosity'] *= 1e21
data_3d['viscosity'] *= 1e21

# Make a colour map
boring_cmap = plt.get_cmap("inferno_r", 25)
# Create a plotter object
plotter = pv.Plotter(window_size=(width, height),  border=False, notebook=False, off_screen=True)
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
plotter.camera_position = [(0, 0, radius*zoom),
                                 (0.0, 0.0, 0.0),
                                 (0.0, 1.0, 0.0)]

plotter.screenshot("visc1d.png")

plotter = pv.Plotter(window_size=(width, height),  border=False, notebook=False, off_screen=True)
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
plotter.camera_position = [(0, 0, radius*zoom),
                                 (0.0, 0.0, 0.0),
                                 (0.0, 1.0, 0.0)]

plotter.screenshot("visc3d.png")
