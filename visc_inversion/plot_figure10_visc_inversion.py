import matplotlib.pyplot as plt
import matplotlib
from matplotlib import colormaps, colors
import numpy as np
import pandas as pd
from matplotlib.cm import ScalarMappable



fig, ax = plt.subplots(5, 3, figsize=(8,13.3333), dpi=300, layout="constrained")

# fonts and linewidths etc
fs = 9
fs_lab = 10
ms = 0.75
lw = 0.75


steps = [0, 10, 50, 100, 200]

for i in range(len(steps)):
    # viscosity
    visc = plt.imread(f'visc_plots/visc3d_step{steps[i]}.png')
    ax[i,0].imshow(visc)
    ax[i,0].axis('off')

    
    # viscosity relative misfit
    visc_misfit = plt.imread(f'visc_misfit/visc3d_relative_misfit_loguovert_cs1_step_{steps[i]}.png')
    ax[i,1].imshow(visc_misfit)
    ax[i,1].axis('off') 
    
    
    if i == 0:
        vpos = 1
    elif i ==3:
        vpos = 1.05
    else:
        vpos=1.03

    ax[i,0].annotate(
            f"Step {steps[i]}",
            xy=(-0.03, vpos), xycoords='axes fraction',
            xytext=(+0.4, -0.4), textcoords='offset fontsize',
            fontsize=fs, verticalalignment='top',
            bbox=dict(facecolor='white', edgecolor='black', pad=3.8))

    
    # adjoint viscosity
    visc_adj = plt.imread(f'visc_adj/visc3d_adj_step{steps[i]}.png')
    ax[i,2].imshow(visc_adj)
    ax[i,2].axis('off') 


# Add colour bars
# visc cbar
visc_cmap = plt.get_cmap("inferno_r", 25)
visc_cbar = ScalarMappable(norm=colors.LogNorm(vmin=1e20, vmax=1e25), cmap=visc_cmap)
fig.colorbar(visc_cbar,
             ax=ax[4,0], orientation='horizontal', label='Viscosity (Pa s)',shrink=0.8) # ticks=[1e20, 1e21, 1e22, 1e23,1e24,1e25])

# visc misfit cbar
visc_misfit_cmap = plt.get_cmap("coolwarm", 25)
visc_misfit_cbar = ScalarMappable(norm=colors.Normalize(vmin=-1, vmax=1), cmap=visc_misfit_cmap)
#visc_misfit_cbar = ScalarMappable(norm=colors.LogNorm(vmin=1e19, vmax=1e25), cmap=visc_misfit_cmap)
fig.colorbar(visc_misfit_cbar,
             ax=ax[4,1], orientation='horizontal', label='log(Viscosity / Target viscosity)',shrink=0.8)
             #ax=ax[4,1], orientation='horizontal', label='Absolute misfit',shrink=0.8)

# adj visc cbar
visc_adj_cmap = plt.get_cmap("coolwarm", 25)

visc_adj_cbar = ScalarMappable(norm=colors.Normalize(vmin=-0.01, vmax=0.01), cmap=visc_adj_cmap)
fig.colorbar(visc_adj_cbar,
             ax=ax[4,2], orientation='horizontal', label='Adjoint viscosity ', shrink=0.8)
figname = "Figure_10_visc_inversion_20.06.25_log_uovertarg"
fig.savefig(f'{figname}.png')

