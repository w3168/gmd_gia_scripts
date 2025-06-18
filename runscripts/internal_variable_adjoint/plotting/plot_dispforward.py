import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import pyvista as pv
fs = 8

steps = [10,20,30,40, 50,100,  150,  200]

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

radius = np.sqrt(x_1d[0]**2 + y_1d[0]**2)


normal = np.stack((x_1d, y_1d))/radius
tangent = np.stack((-y_1d, x_1d))/radius

diff_time_rad = []
diff_time_tang = []
diff_time_rad_max = []
diff_time_tang_max = []

diff_time_rad_vel = []
diff_time_tang_vel = []
diff_time_rad_vel_max = []
diff_time_tang_vel_max = []


disp_normal_1d_old = np.zeros_like(theta_1d)
disp_tangent_1d_old = np.zeros_like(theta_1d)

disp_normal_3d_old = np.zeros_like(theta_1d)
disp_tangent_3d_old = np.zeros_like(theta_1d)


for i in range(1, 201):
    fig, ax = plt.subplots(1, 2, figsize=(8,3.5), dpi=300, layout="constrained")
    disp_x_halo_1d = np.array(disp_df_1d[f'surface_disp_x_step{i}'])
    disp_x_unsorted_1d = disp_x_halo_1d[condition_1d]
    disp_y_halo_1d = np.array(disp_df_1d[f'surface_disp_y_step{i}'])
    disp_y_unsorted_1d = disp_y_halo_1d[condition_1d]

    disp_unsorted_1d = np.stack((disp_x_unsorted_1d, disp_y_unsorted_1d))
    disp_normal_unsorted_1d =  normal[0] * disp_unsorted_1d[0] + normal[1] * disp_unsorted_1d[1]
    disp_normal_1d = disp_normal_unsorted_1d[index_1d]
    disp_tangent_unsorted_1d =  tangent[0] * disp_unsorted_1d[0] + tangent[1] * disp_unsorted_1d[1]
    disp_tangent_1d = disp_tangent_unsorted_1d[index_1d]
    ax[0].plot(theta_1d, disp_normal_1d, color='r', linestyle='--', linewidth=0.75)
    ax[1].plot(theta_1d, disp_tangent_1d, color='r', linestyle='--', linewidth=0.75)
    
    disp_x_halo_3d = np.array(disp_df_3d[f'surface_disp_x_step{i}'])
    disp_x_unsorted_3d = disp_x_halo_3d[condition_1d]
    disp_y_halo_3d = np.array(disp_df_3d[f'surface_disp_y_step{i}'])
    disp_y_unsorted_3d = disp_y_halo_3d[condition_1d]

    disp_unsorted_3d = np.stack((disp_x_unsorted_3d, disp_y_unsorted_3d))
    disp_normal_unsorted_3d =  normal[0] * disp_unsorted_3d[0] + normal[1] * disp_unsorted_3d[1]
    disp_normal_3d = disp_normal_unsorted_3d[index_1d]
    disp_tangent_unsorted_3d =  tangent[0] * disp_unsorted_3d[0] + tangent[1] * disp_unsorted_3d[1]
    disp_tangent_3d = disp_tangent_unsorted_3d[index_1d]
    
    

    ax[0].plot(theta_1d, disp_normal_3d, color='k', linestyle='-', linewidth=0.75)
    ax[1].plot(theta_1d, disp_tangent_3d, color='k', linestyle='-', linewidth=0.75)

    # accidentally ran 1d and 3d on different number of cores so distrbution is different
    #disp_3d_interp = np.interp(theta_1d, theta_3d, disp_3d)
#    diff = np.sqrt((disp_tangent_3d - disp_tangent_1d)**2 / 300**2)
    diff = disp_tangent_3d - disp_tangent_1d

    diff_tang_max = np.max(np.abs(diff))

#    diff_rad = (disp_normal_3d - disp_normal_1d)**2 / 300**2
    diff_rad = disp_normal_3d - disp_normal_1d
    diff_rad_max = np.max(np.abs(diff_rad))
    diff_time_tang.append(np.sqrt(np.dot(diff, diff))/len(diff))
    diff_time_rad.append(np.sqrt(np.dot(diff_rad, diff_rad))/len(diff_rad))


    diff_time_rad_max.append(diff_rad_max)
    diff_time_tang_max.append(diff_tang_max)
#    axd['f'].plot(theta_1d, diff, color=colors[i], linestyle='-', linewidth=0.75)
#    axd['d'].plot(theta_1d, diff_rad, color=colors[i], linestyle='--', linewidth=0.75)
#axd['d'].plot(steps, diff_time_tang, color=colors[i], linestyle='-', linewidth=0.75)
#axd['d'].plot(steps, diff_time_rad, color='red', linestyle='-', linewidth=0.75)

    ax[0].set_xlabel(r'Theta ($^\circ$)', fontsize=fs)
    ax[0].set_ylabel('Radial displacement (m)', fontsize=fs)
    ax[0].grid(True)
    ax[0].tick_params(axis='both', which='major', labelsize=fs)
    ax[0].set_ylim([-400, 100])

    ax[1].set_xlabel(r'Theta ($^\circ$)', fontsize=fs)
    ax[1].set_ylabel(r'Tangential displacement (m)', fontsize=fs)
    ax[1].grid(True)
    ax[1].tick_params(axis='both', which='major', labelsize=fs)
    ax[1].set_ylim([-400, 400])
    plt.savefig(f'disp_forward/17.06.25_1dvs3dvisc_disp_step{i}.png')
    plt.close()


    fig, ax = plt.subplots(1, 2, figsize=(8,3.5), dpi=300, layout="constrained")
    
    vel_normal_1d = (disp_normal_1d - disp_normal_1d_old) / 50
    vel_tangent_1d = (disp_tangent_1d - disp_tangent_1d_old) / 50
    
    vel_normal_3d = (disp_normal_3d - disp_normal_3d_old) / 50
    vel_tangent_3d = (disp_tangent_3d - disp_tangent_3d_old) / 50
    
    diff_tang_vel = vel_tangent_3d - vel_tangent_1d
    diff_tang_vel_max = np.max(np.abs(diff_tang_vel))

    diff_rad_vel = vel_normal_3d - vel_normal_1d
    diff_rad_vel_max = np.max(np.abs(diff_rad_vel))
    diff_time_tang_vel.append(np.sqrt(np.dot(diff_tang_vel, diff_tang_vel))/len(diff_tang_vel))
    diff_time_rad_vel.append(np.sqrt(np.dot(diff_rad_vel, diff_rad_vel))/len(diff_rad_vel))

    diff_time_rad_vel_max.append(diff_rad_vel_max)
    diff_time_tang_vel_max.append(diff_tang_vel_max)

    ax[0].plot(theta_1d, vel_normal_1d, color='r', linestyle='--', linewidth=0.75)
    ax[1].plot(theta_1d, vel_tangent_1d, color='r', linestyle='--', linewidth=0.75)
    
    ax[0].plot(theta_1d, vel_normal_3d, color='k', linestyle='-', linewidth=0.75)
    ax[1].plot(theta_1d, vel_tangent_3d, color='k', linestyle='-', linewidth=0.75)
    
    ax[0].set_xlabel(r'Theta ($^\circ$)', fontsize=fs)
    ax[0].set_ylabel('Radial velocity (m / yr)', fontsize=fs)
    ax[0].grid(True)
    ax[0].tick_params(axis='both', which='major', labelsize=fs)
    ax[0].set_ylim([-2.5, 0.5])

    ax[1].set_xlabel(r'Theta ($^\circ$)', fontsize=fs)
    ax[1].set_ylabel(r'Tangential velocity (m / yr)', fontsize=fs)
    ax[1].grid(True)
    ax[1].tick_params(axis='both', which='major', labelsize=fs)
    ax[1].set_ylim([-1, 1])
    plt.savefig(f'vel_forward/scale_early/17.06.25_1dvs3dvisc_vel_step{i}_scale.png')
    plt.close()

    disp_normal_1d_old = np.copy(disp_normal_1d)
    disp_tangent_1d_old = np.copy(disp_tangent_1d)

    disp_normal_3d_old = np.copy(disp_normal_3d)
    disp_tangent_3d_old = np.copy(disp_tangent_3d)

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



time = np.linspace(50, 10000, 200)/1000
fig, ax = plt.subplots(1, 2, figsize=(8,3.5), dpi=300, layout="constrained")


ax[0].plot(time, diff_time_rad, color='k', linestyle='-', linewidth=0.75)
ax[1].plot(time, diff_time_tang, color='k', linestyle='-', linewidth=0.75)

ax[0].set_xlabel(r'Time (kyr)', fontsize=fs)
ax[0].set_ylabel('(Average) radial displacement misfit (m)', fontsize=fs)
ax[0].grid(True)
ax[0].tick_params(axis='both', which='major', labelsize=fs)
#ax[0].set_ylim([-2.5, 0.5])

ax[1].set_xlabel(r'Time (kyr)', fontsize=fs)
ax[1].set_ylabel(r'(Average) tangential displacement misfit (m)', fontsize=fs)
ax[1].grid(True)
ax[1].tick_params(axis='both', which='major', labelsize=fs)
#ax[1].set_ylim([-1, 1])
plt.savefig(f'17.06.25_1dvs3dvisc_disp_misfit_average.png')
plt.close()


fig, ax = plt.subplots(1, 2, figsize=(8,3.5), dpi=300, layout="constrained")

ax[0].plot(time, diff_time_rad_max, color='k', linestyle='-', linewidth=0.75)
ax[1].plot(time, diff_time_tang_max, color='k', linestyle='-', linewidth=0.75)

ax[0].set_xlabel(r'Time (kyr)', fontsize=fs)
ax[0].set_ylabel('Maximum radial displacement misfit (m)', fontsize=fs)
ax[0].grid(True)
ax[0].tick_params(axis='both', which='major', labelsize=fs)
#ax[0].set_ylim([-2.5, 0.5])

ax[1].set_xlabel(r'Time (kyr)', fontsize=fs)
ax[1].set_ylabel(r'Maximum tangential displacement misfit (m)', fontsize=fs)
ax[1].grid(True)
ax[1].tick_params(axis='both', which='major', labelsize=fs)
#ax[1].set_ylim([-1, 1])
plt.savefig(f'17.06.25_1dvs3dvisc_disp_misfit_max.png')
plt.close()

fig, ax = plt.subplots(1, 2, figsize=(8,3.5), dpi=300, layout="constrained")


ax[0].plot(time, diff_time_rad_vel, color='k', linestyle='-', linewidth=0.75)
ax[1].plot(time, diff_time_tang_vel, color='k', linestyle='-', linewidth=0.75)

ax[0].set_xlabel(r'Time (kyr)', fontsize=fs)
ax[0].set_ylabel('(Average) radial velocity misfit (m / yr)', fontsize=fs)
ax[0].grid(True)
ax[0].tick_params(axis='both', which='major', labelsize=fs)
#ax[0].set_ylim([-2.5, 0.5])

ax[1].set_xlabel(r'Time (kyr)', fontsize=fs)
ax[1].set_ylabel(r'(Average) tangential velocity misfit (m / yr)', fontsize=fs)
ax[1].grid(True)
ax[1].tick_params(axis='both', which='major', labelsize=fs)
#ax[1].set_ylim([-1, 1])
plt.savefig(f'17.06.25_1dvs3dvisc_vel_misfit_average.png')
plt.close()


fig, ax = plt.subplots(1, 2, figsize=(8,3.5), dpi=300, layout="constrained")

ax[0].plot(time, diff_time_rad_vel_max, color='k', linestyle='-', linewidth=0.75)
ax[1].plot(time, diff_time_tang_vel_max, color='k', linestyle='-', linewidth=0.75)

ax[0].set_xlabel(r'Time (kyr)', fontsize=fs)
ax[0].set_ylabel('Maximum radial velocity misfit (m /yr)', fontsize=fs)
ax[0].grid(True)
ax[0].tick_params(axis='both', which='major', labelsize=fs)
#ax[0].set_ylim([-2.5, 0.5])

ax[1].set_xlabel(r'Time (kyr)', fontsize=fs)
ax[1].set_ylabel(r'Maximum tangential velocity misfit (m / yr)', fontsize=fs)
ax[1].grid(True)
ax[1].tick_params(axis='both', which='major', labelsize=fs)
#ax[1].set_ylim([-1, 1])
plt.savefig(f'17.06.25_1dvs3dvisc_vel_misfit_max.png')
plt.close()

