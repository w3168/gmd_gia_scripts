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

obj = np.loadtxt('adjoint-cylinder-2d-internalvariable-ctypeviscosity-lithvisc_functional.txt')
obj = obj / obj[0]
ax.semilogy(obj[:101], color='k', linestyle='-', linewidth=lw)

# Plot short, 1D burgers
ax.set_xlabel('Iteration number', fontsize=fs_lab)
ax.set_ylabel('Objective function', fontsize=fs_lab)
ax.grid(True, linestyle='dotted')
ax.tick_params(axis='both', which='major', labelsize=fs)


figname = "Figure_11_visc_objfunc_inversion_lim100_12.08.25"
fig.savefig(f'{figname}.png')

