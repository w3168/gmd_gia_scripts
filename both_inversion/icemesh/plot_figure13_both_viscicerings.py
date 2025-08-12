import matplotlib.pyplot as plt
from matplotlib import colormaps, colors
from matplotlib.cm import ScalarMappable

dpi = 300
# fonts and linewidths etc
fs = 7.5
fs_lab = 8
ms = 0.75
lw = 0.75

fig, ax = plt.subplots(1,2, figsize=(5.75,3.5), dpi=dpi, layout="constrained")
# plot viscosity at iteration 10
visc_10 = plt.imread(f'visc_plots/both_visc_noreg_lithvisc_icering_step10.png')
ax[0].imshow(visc_10)
ax[0].axis('off')
# Add colour bars
# visc cbar
visc_cmap = plt.get_cmap("inferno_r", 25)
visc_cbar = ScalarMappable(norm=colors.LogNorm(vmin=1e20, vmax=1e25), cmap=visc_cmap)
visc_cbar2 = fig.colorbar(visc_cbar,
             ax=ax[0], orientation='horizontal', label='Viscosity (Pa s)', fraction=0.03, shrink=0.75) # ticks=[1e20, 1e21, 1e22, 1e23,1e24,1e25])

visc_cbar2.ax.tick_params(labelsize=fs)
visc_cbar2.set_label(label='Viscosity (Pa s)', size=fs_lab)

# plot viscosity at iteration 10
visc_100 = plt.imread(f'visc_plots/both_visc_noreg_lithvisc_icering_step100.png')
ax[1].imshow(visc_100)
ax[1].axis('off')
# Add colour bars
# visc cbar
ice_cmap = plt.get_cmap("Blues", 25)
ice_cbar = ScalarMappable(norm=colors.Normalize(vmin=0, vmax=2000), cmap=ice_cmap)
ice_cbar2 = fig.colorbar(ice_cbar,
             ax=ax[1], orientation='horizontal', label='Ice thickness (m)', fraction=0.03, shrink=0.75)

ice_cbar2.ax.tick_params(labelsize=fs)
ice_cbar2.set_label(label='Ice thickness (m)', size=fs_lab)


ax[0].annotate(
        "a",
        xy=(0.01, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))

ax[1].annotate(
        "b",
        xy=(0.87, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))

plt.savefig('Figure_13_icevisc_rings_its10vs100_12.08.25.png')

