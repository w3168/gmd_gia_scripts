import matplotlib.pyplot as plt
import matplotlib
from matplotlib import colormaps
import numpy as np
import pandas as pd


# 1d visc ice 
ice_df_1d = pd.read_csv(f"adjoint-cylinder-2d-internalvariable-ctypeice-1dvisc_iceonly_icesmooth0.0_icedamp0.0_viscsmooth0.0_viscdamp0.0_surface_ice.csv")

# Data contains halos but x and y in halo set to zero so can filter out by choosing a minimum radius
# since all our data is on the surface of the mesh. since used same number of cores 1d and 3d should be 
# the same?
x_halo_1d = np.array(ice_df_1d['surface_x'])
y_halo_1d = np.array(ice_df_1d['surface_y'])
r_halo_1d = np.sqrt(x_halo_1d**2 + y_halo_1d**2)
condition_1d = r_halo_1d>2.2
x_1d = x_halo_1d[condition_1d]
y_1d = y_halo_1d[condition_1d]
theta_unsorted_1d = np.atan2(y_1d,x_1d)
index_1d = np.argsort(theta_unsorted_1d)
theta_1d = theta_unsorted_1d[index_1d]*360/(2*np.pi)

# target
target_ice_halo = np.array(ice_df_1d[f'surface_ice_target'])
target_ice_unsorted_1d = target_ice_halo[condition_1d]
target_ice = target_ice_unsorted_1d[index_1d]

# 1d visc ice
ice_halo_1d = np.array(ice_df_1d[f'surface_ice_step20'])
ice_unsorted_1d = ice_halo_1d[condition_1d]
ice_1d = ice_unsorted_1d[index_1d]

# 3d visc ice inversion
ice_df_3d = pd.read_csv(f"adjoint-cylinder-2d-internalvariable-ctypeice-3dvisc_iceonly_icesmooth0.0_icedamp0.0_viscsmooth0.0_viscdamp0.0_surface_ice.csv")

# Data contains halos but x and y in halo set to zero so can filter out by choosing a minimum radius
# since all our data is on the surface of the mesh. since used same number of cores 1d and 3d should be 
# the same?
x_halo_3d = np.array(ice_df_3d['surface_x'])
y_halo_3d = np.array(ice_df_3d['surface_y'])
r_halo_3d = np.sqrt(x_halo_3d**2 + y_halo_3d**2)
condition_3d = r_halo_3d>2.2
x_3d = x_halo_3d[condition_3d]
y_3d = y_halo_3d[condition_3d]
theta_unsorted_3d = np.atan2(y_3d,x_3d)
index_3d = np.argsort(theta_unsorted_3d)
theta_3d = theta_unsorted_3d[index_3d]*360/(2*np.pi)
ice_halo_3d = np.array(ice_df_3d[f'surface_ice_step20'])
ice_unsorted_3d = ice_halo_3d[condition_3d]
ice_3d = ice_unsorted_3d[index_3d]

fig, ax = plt.subplots(1, 2, figsize=(8,3.5), dpi=300, layout="constrained")

# fonts and linewidths etc
fs = 9
fs_lab = 10
ms = 0.75
lw = 0.75
ax[0].plot(theta_1d, ice_1d, color='r', linestyle='-', marker='o', markevery=4, markersize=ms, linewidth=lw, label='1D Viscosity')
ax[0].plot(theta_3d, ice_3d, color='b', linestyle='-', marker='o', markevery=4, markersize=ms, linewidth=lw, label='3D Viscosity')
ax[0].plot(theta_1d, target_ice, color='k', linestyle='--', linewidth=lw, label='Target')

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
# Plot short, 1D burgers
ax[0].set_xlabel(r'$\theta$ ($^\circ$)', fontsize=fs_lab)
ax[0].set_ylabel('Normalised ice thickness', fontsize=fs_lab)
ax[0].grid(True, linestyle='dotted')
ax[0].tick_params(axis='both', which='major', labelsize=fs)
ax[0].annotate(
        "a",
        xy=(0.01, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
ax[0].legend(loc='upper right', fontsize=fs-0.75, framealpha=1, facecolor='white', edgecolor='black', fancybox=False).get_frame().set_linewidth(lw)


# plot objective function through time

obj_1d = np.loadtxt('adjoint-cylinder-2d-internalvariable-ctypeice-1dvisc_iceonly_icesmooth0.0_icedamp0.0_viscsmooth0.0_viscdamp0.0_check_functional.txt')
obj_3d = np.loadtxt('adjoint-cylinder-2d-internalvariable-ctypeice-3dvisc_iceonly_icesmooth0.0_icedamp0.0_viscsmooth0.0_viscdamp0.0_check_functional.txt')

ax[1].semilogy(obj_1d[:50], color='r', linestyle='-', linewidth=lw, label='1D Viscosity')
ax[1].semilogy(obj_3d, color='b', linestyle='-', linewidth=lw, label='3D Viscosity')

# Plot short, 1D burgers
ax[1].set_xlabel('Iteration number', fontsize=fs_lab)
ax[1].set_ylabel('Normalised objective function', fontsize=fs_lab)
ax[1].grid(True, linestyle='dotted')
ax[1].tick_params(axis='both', which='major', labelsize=fs)
ax[1].annotate(
        "b",
        xy=(0.87, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
#ax[1].legend(loc='upper right', fontsize=fs-0.75, framealpha=1, facecolor='white', edgecolor='black', fancybox=False).get_frame().set_linewidth(lw)


figname = "Figure_8_ice_inversion_10.06.25"
fig.savefig(f'{figname}.png')

