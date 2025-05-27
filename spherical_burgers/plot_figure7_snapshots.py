import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import colormaps
import matplotlib.patches as patches
import numpy as np
import pandas as pd
import pyvista as pv

fs = 8.5
fs_lab = 10
ms = 5
lw = 0.75
cmap = colormaps['Set1']
colours = cmap.colors

colour_burgers_10 = colours[4]

fig, axs = plt.subplots(2,1, figsize=(5,7), dpi=300, layout='constrained')
burgers_panels = plt.imread('snapshots/grouped_burger_sphere_label.png')
axs[0].imshow(burgers_panels)
axs[0].axis('off') 
axs[0].annotate(
        "a",
        xy=(0.965, 1.0), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))


dtconst = '3d/const_dt/'
dt_50 = np.loadtxt(f'{dtconst}displacement-sphere-burgers-3d-internalvariable-3d-reflevel6.0-nz10perlayer-dt50.0years-bulk1.94-nondim.dat')
axs[1].plot(dt_50[:,0], dt_50[:, 1], color=colour_burgers_10, lw=lw)

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
# Plot short, 1D burgers
axs[1].set_xlabel('Time (kyr)', fontsize=fs_lab)
axs[1].set_ylabel('Maximum vertical displacement (m)', fontsize=fs_lab)
axs[1].grid(True, linestyle='dotted')
axs[1].tick_params(axis='both', which='major', labelsize=fs)
axs[1].annotate(
        "b",
        xy=(0.92, 1.0), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))


min_x = 0.132
min_y = 0.53
max_x = 0.992
max_y = 0.992

rect = patches.Rectangle((min_x, min_y), max_x - min_x, max_y - min_y,
                         transform=fig.transFigure,
                         fill=False, edgecolor='black', linewidth=lw)
# Create a rectangle patch
#rect = patches.Rectangle((bbox.x0, bbox.y0), bbox.width, bbox.height,
#                         linewidth=1, edgecolor='r', facecolor='none')

# Add the rectangle to the figure
fig.patches.extend([rect])
#fig.add_patch(rect)

plt.savefig("Figure7_disp_spherical_burgers_27.05.25.png")
