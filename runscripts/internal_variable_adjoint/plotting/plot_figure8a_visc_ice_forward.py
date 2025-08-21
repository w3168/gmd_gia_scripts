import matplotlib.pyplot as plt
import matplotlib
from matplotlib import colormaps, colors
import numpy as np
import pandas as pd
from matplotlib.cm import ScalarMappable



fig, ax = plt.subplots(1, 2, figsize=(5.75,3.5), dpi=300, layout="constrained")

# fonts and linewidths etc
fs = 7.5
fs_lab = 8
ms = 0.75
lw = 0.75


visc_1d = plt.imread('visc1d.png')
ax[0].imshow(visc_1d)
ax[0].axis('off')

ax[0].annotate(
            f"a",
            xy=(-0.01, 1.005), xycoords='axes fraction',
            xytext=(+0.4, -0.4), textcoords='offset fontsize',
            fontsize=fs, verticalalignment='top',
            bbox=dict(facecolor='white', edgecolor='black', pad=3.8))

ax[0].annotate(
            f"Axisym.",
            xy=(0.065, 1.005), xycoords='axes fraction',
            xytext=(+0.4, -0.4), textcoords='offset fontsize',
            fontsize=fs, verticalalignment='top',
            bbox=dict(facecolor='white', edgecolor='black', pad=3.8))

visc_3d = plt.imread('visc3d.png')
ax[1].imshow(visc_3d)
ax[1].axis('off')

ax[1].annotate(
            f"b",
            xy=(0.05, 1.005), xycoords='axes fraction',
            xytext=(+0.4, -0.4), textcoords='offset fontsize',
            fontsize=fs, verticalalignment='top',
            bbox=dict(facecolor='white', edgecolor='black', pad=3.8))

ax[1].annotate(
            f"LVV",
            xy=(0.13, 1.005), xycoords='axes fraction',
            xytext=(+0.4, -0.4), textcoords='offset fontsize',
            fontsize=fs, verticalalignment='top',
            bbox=dict(facecolor='white', edgecolor='black', pad=3.8))


# Add colour bars
# visc cbar
visc_cmap = plt.get_cmap("inferno_r", 25)
visc_cbar = ScalarMappable(norm=colors.LogNorm(vmin=1e20, vmax=1e25), cmap=visc_cmap)
visc_cbar2 = fig.colorbar(visc_cbar,
             ax=ax[0], orientation='horizontal', label='Viscosity (Pa s)', fraction=0.03, shrink=0.75) # ticks=[1e20, 1e21, 1e22, 1e23,1e24,1e25])

visc_cbar2.ax.tick_params(labelsize=fs)
visc_cbar2.set_label(label='Viscosity (Pa s)', size=fs_lab)
# visc misfit cbar
ice_cmap = plt.get_cmap("Blues", 25)
ice_cbar = ScalarMappable(norm=colors.Normalize(vmin=0, vmax=2000), cmap=ice_cmap)
ice_cbar2 = fig.colorbar(ice_cbar,
             ax=ax[1], orientation='horizontal', label='Ice thickness (m)', fraction=0.03, shrink=0.75)

ice_cbar2.ax.tick_params(labelsize=fs)
ice_cbar2.set_label(label='Ice thickness (m)', size=fs_lab)
figname = "Figure_8a_visc_ice_forward_21.08.25"
fig.savefig(f'{figname}.png')

