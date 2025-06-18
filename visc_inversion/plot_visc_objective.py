import matplotlib.pyplot as plt
import matplotlib
from matplotlib import colormaps
import numpy as np
import pandas as pd



fig, ax = plt.subplots(1, 1, figsize=(4,3.5), dpi=300, layout="constrained")

# fonts and linewidths etc
fs = 9
fs_lab = 10
ms = 0.75
lw = 0.75

obj = np.loadtxt('adjoint-cylinder-2d-internalvariable-ctypeviscosity-visconly_icesmooth0.0_icedamp0.0_viscsmooth1e-6_viscdamp1e-5_checkmisfit3_functional.txt')

ax.semilogy(obj, color='k', linestyle='-', linewidth=lw)

# Plot short, 1D burgers
ax.set_xlabel('Iteration number', fontsize=fs_lab)
ax.set_ylabel('Normalised objective function', fontsize=fs_lab)
ax.grid(True, linestyle='dotted')
ax.tick_params(axis='both', which='major', labelsize=fs)


figname = "Figure_11_visc_objfunc_inversion_18.06.25"
fig.savefig(f'{figname}.png')

