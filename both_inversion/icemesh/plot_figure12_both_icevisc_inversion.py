import matplotlib.pyplot as plt
import matplotlib
from matplotlib import colormaps, colors
import numpy as np
import pandas as pd
from matplotlib.cm import ScalarMappable


# Ice inversion (alongside viscosity starting 1d)
ice_df_1d = pd.read_csv(f"adjoint-cylinder-2d-internalvariable-ctypeboth-lithvisc_icemesh_icesmooth0.0_icedamp0.0_viscsmooth0.0_viscdamp0.0_surface_ice.csv")

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

# 10 iterations ice
ice_halo_1d_10 = np.array(ice_df_1d[f'surface_ice_step10'])
ice_unsorted_1d_10 = ice_halo_1d_10[condition_1d]
ice_1d_10 = ice_unsorted_1d_10[index_1d]

# 100 iterations ice
ice_halo_1d = np.array(ice_df_1d[f'surface_ice_step100'])
ice_unsorted_1d = ice_halo_1d[condition_1d]
ice_1d = ice_unsorted_1d[index_1d]

fig, ax = plt.subplots(2, 2, figsize=(6.5,6.5), dpi=300, layout="constrained")

# fonts and linewidths etc
fs = 9
fs_lab = 10
ms = 0.75
lw = 0.75
ax[0,0].plot(theta_1d, ice_1d_10, color='g', linestyle='-', linewidth=lw+0.5,alpha=0.3, label='Step 10')
ax[0,0].plot(theta_1d, ice_1d, color='b', linestyle='-', linewidth=lw+0.5,alpha=0.4, label='Step 100')
ax[0,0].plot(theta_1d, target_ice, color='k', linestyle='--', linewidth=lw, label='Target')

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
# Plot short, 1D burgers
ax[0,0].set_xlabel(r'$\theta$ ($^\circ$)', fontsize=fs_lab)
ax[0,0].set_ylabel('Normalised ice thickness', fontsize=fs_lab)
ax[0,0].grid(True, linestyle='dotted')
ax[0,0].tick_params(axis='both', which='major', labelsize=fs)
ax[0,0].annotate(
        "a",
        xy=(0.01, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
ax[0,0].legend(loc='upper right', fontsize=fs-0.75, framealpha=1, facecolor='white', edgecolor='black', fancybox=False).get_frame().set_linewidth(lw)

# plot objective function through time

obj = np.loadtxt('adjoint-cylinder-2d-internalvariable-ctypeboth-lithvisc_icemesh_icesmooth0.0_icedamp0.0_viscsmooth0.0_viscdamp0.0_functional.txt')

ax[0,1].semilogy(obj[:101], color='k', linestyle='-', linewidth=lw, )
ax[0,1].set_xlabel('Iteration number', fontsize=fs_lab)
ax[0,1].set_ylabel('Normalised objective function', fontsize=fs_lab)
ax[0,1].grid(True, linestyle='dotted')
ax[0,1].tick_params(axis='both', which='major', labelsize=fs)
ax[0,1].annotate(
        "b",
        xy=(0.87, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
#ax[1].legend(loc='upper right', fontsize=fs-0.75, framealpha=1, facecolor='white', edgecolor='black', fancybox=False).get_frame().set_linewidth(lw)

# plot viscosity at iteration 100
visc_10 = plt.imread(f'visc_plots/both_visc_noreg_rerunlithvisc_step10.png')
ax[1,0].imshow(visc_10)
ax[1,0].axis('off')

# plot viscosity at iteration 100
visc = plt.imread(f'visc_plots/both_visc_noreg_rerunlithvisc_step100.png')
ax[1,1].imshow(visc)
ax[1,1].axis('off')

# Add colour bars
# visc cbar
visc_cmap = plt.get_cmap("inferno_r", 25)
visc_cbar = ScalarMappable(norm=colors.LogNorm(vmin=1e20, vmax=1e25), cmap=visc_cmap)
fig.colorbar(visc_cbar,
             ax=ax[1,0], orientation='horizontal', label='Viscosity (Pa s)',shrink=0.7) # ticks=[1e20, 1e21, 1e22, 1e23,1e24,1e25])
ax[1,0].annotate(
        "c",
        xy=(0.01, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))

ax[1,1].annotate(
        "d",
        xy=(0.87, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))


figname = "Figure_12_both_ice_visc_obj_inversion_step10v100_29.07.25"
fig.savefig(f'{figname}.png')

