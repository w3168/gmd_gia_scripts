import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import pyvista as pv
fs = 8

fig, axd = plt.subplot_mosaic([["a", "c"],
                               ["b", "d"]],
                               figsize=(7,9), dpi=300)
visc1d = plt.imread('visc1d.png')
axd["a"].imshow(visc1d)
axd["a"].axis('off') 
visc3d = plt.imread('visc3d.png')
axd["b"].imshow(visc3d)
axd["b"].axis('off') 



steps = [1, 10, 20, 30, 40, 50,]

nsteps = len(steps)
cmap = mpl.colormaps['Set2']
colors = cmap.colors

disp_df_1d = pd.read_csv("surface-displacement-forward-cylinder-2d-internalvariable-dispvel--1dviscTrue-ncells360.0-nz20perlayer-dt50.0years-bulk1.94-nondim.csv")
disp_df_3d = pd.read_csv("surface-displacement-forward-cylinder-2d-internalvariable-dispvel--1dviscFalse-ncells360.0-nz20perlayer-dt50.0years-bulk1.94-nondim.csv")

# Data contains halos but x and y in halo set to zero so can filter out by choosing a minimum radius
# since all our data is on the surface of the mesh. since used same number of cores 1d and 3d should be 
# the same?
x_halo_1d = np.array(disp_df_1d['surface_x'])
y_halo_1d = np.array(disp_df_1d['surface_y'])
r_halo_1d = np.sqrt(x_halo_1d**2 + y_halo_1d**2)
condition_1d = r_halo_1d>2.2
x_1d = x_halo_1d[condition_1d]
y_1d = y_halo_1d[condition_1d]
theta_unsorted_1d = np.atan2(y_1d,x_1d)
index_1d = np.argsort(theta_unsorted_1d)
theta_1d = theta_unsorted_1d[index_1d]*360/(2*np.pi)

for i in range(nsteps):
    disp_halo_1d = np.array(disp_df_1d[f'surface_disp_step{steps[i]}'])
    disp_unsorted_1d = disp_halo_1d[condition_1d]
    disp_1d = disp_unsorted_1d[index_1d]
    axd['c'].plot(theta_1d, disp_1d, color=colors[i], linestyle='--', linewidth=0.75)
    
    disp_halo_3d = np.array(disp_df_3d[f'surface_disp_step{steps[i]}'])
    disp_unsorted_3d = disp_halo_3d[condition_1d]
    disp_3d = disp_unsorted_3d[index_1d]
    axd['c'].plot(theta_1d, disp_3d, color=colors[i], linestyle='-', linewidth=0.75)

    # accidentally ran 1d and 3d on different number of cores so distrbution is different
    #disp_3d_interp = np.interp(theta_1d, theta_3d, disp_3d)
    diff = abs(disp_3d - disp_1d)
    axd['d'].plot(theta_1d, diff, color=colors[i], linestyle='-', linewidth=0.75)

axd['c'].set_xlabel(r'Theta ($^\circ$)', fontsize=fs)
axd['c'].set_ylabel('Vertical displacement (m)', fontsize=fs)
axd['c'].grid(True)
axd['c'].tick_params(axis='both', which='major', labelsize=fs)
#ax.annotate(
#        "Analytical solution",
#        xy=(0.0375, 1), xycoords='axes fraction',
#        xytext=(+0.5, -0.5), textcoords='offset fontsize',
#        fontsize=30, verticalalignment='top',
#        bbox=dict(facecolor='white', edgecolor='black', pad=5.0))

# 3d viscosity
'''
# Data contains halos but x and y in halo set to zero so can filter out by choosing a minimum radius
# since all our data is on the surface of the mesh
x_halo = np.array(disp_df['surface_x'])
y_halo = np.array(disp_df['surface_y'])
r_halo = np.sqrt(x_halo**2 + y_halo**2)
condition = r_halo>2.2
x = x_halo[condition]
y = y_halo[condition]
theta_unsorted = np.atan2(y,x)
index = np.argsort(theta_unsorted)
theta_3d = theta_unsorted[index]*360/(2*np.pi)

steps = [1, 10, 50, 100, 200]
for s in steps:
    disp_halo = np.array(disp_df[f'surface_disp_step{s}'])
    disp_unsorted = disp_halo[condition]
    disp_3d = disp_unsorted[index]
    axd['d'].plot(theta_3d, disp_3d, linestyle='--', linewidth=1)

axd['d'].set_xlabel(r'Theta ($^\circ$)', fontsize=fs)
axd['d'].set_ylabel('Vertical displacement (m)', fontsize=fs)
axd['d'].grid(True)
axd['d'].tick_params(axis='both', which='major', labelsize=fs)
#ax.annotate(
#        "Analytical solution",
#        xy=(0.0375, 1), xycoords='axes fraction',
#        xytext=(+0.5, -0.5), textcoords='offset fontsize',
#        fontsize=30, verticalalignment='top',
#        bbox=dict(facecolor='white', edgecolor='black', pad=5.0))
'''
plt.show()
