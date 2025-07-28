import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import pyvista as pv
fs = 8



steps = np.linspace(0,200, 201,dtype=int)

nsteps = len(steps)

cmap = mpl.colormaps['plasma']

# Take colors at regular intervals spanning the colormap.
colors = cmap(np.linspace(0, 1, nsteps))
smooth = '0.0'
damp = '0.0'
ice_df = pd.read_csv(f"adjoint-cylinder-2d-internalvariable-ctypeboth-lithvisc_icemesh_icesmooth0.0_icedamp0.0_viscsmooth1e-6_viscdamp1e-5_maxrad1e40_surface_ice.csv")


# Data contains halos but x and y in halo set to zero so can filter out by choosing a minimum radius
# since all our data is on the surface of the mesh. since used same number of cores 1d and 3d should be 
# the same?
x_halo_1d = np.array(ice_df['surface_x'])
y_halo_1d = np.array(ice_df['surface_y'])
r_halo_1d = np.sqrt(x_halo_1d**2 + y_halo_1d**2)
condition_1d = r_halo_1d>2.2
x_1d = x_halo_1d[condition_1d]
y_1d = y_halo_1d[condition_1d]
theta_unsorted_1d = np.atan2(y_1d,x_1d)
index_1d = np.argsort(theta_unsorted_1d)
theta_1d = theta_unsorted_1d[index_1d]*360/(2*np.pi)

radius = np.sqrt(x_1d[0]**2 + y_1d[0]**2)


normal = np.stack((x_1d, y_1d))/radius
tangent = np.stack((-y_1d, x_1d))/radius

diff_time_rad = []
diff_time_tang = []

# target
target_ice_halo = np.array(ice_df[f'surface_ice_target'])
target_ice_unsorted_1d = target_ice_halo[condition_1d]
target_ice = target_ice_unsorted_1d[index_1d]

for i in range(nsteps):
    
    ice_halo = np.array(ice_df[f'surface_ice_step{steps[i]}'])
    ice_unsorted_1d = ice_halo[condition_1d]
    ice = ice_unsorted_1d[index_1d]
    fig, axd = plt.subplots(figsize=(4,4), dpi=300)
    axd.plot(theta_1d, ice, color='b', linestyle='--', linewidth=0.75)
    axd.plot(theta_1d, target_ice, color='k', linestyle='--', linewidth=0.75)

    plt.savefig(f'ice_smooth{smooth}_damp{damp}/27.07.25_icemeshboth_rerun_mr1e40_viscsmooth_ice_step{i}.png')




