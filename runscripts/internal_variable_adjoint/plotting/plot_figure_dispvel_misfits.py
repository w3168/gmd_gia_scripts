import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import pyvista as pv
# fonts and linewidths etc
fs = 9
fs_lab = 10
ms = 3
lw = 0.75

fig, ax = plt.subplots(3, 2, figsize=(8,9),  dpi=300, layout="constrained")

#plt.xticks(fontsize=fs)
#plt.yticks(fontsize=fs)

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

plot=False
for i in range(1, 201):
    disp_x_halo_1d = np.array(disp_df_1d[f'surface_disp_x_step{i}'])
    disp_x_unsorted_1d = disp_x_halo_1d[condition_1d]
    disp_y_halo_1d = np.array(disp_df_1d[f'surface_disp_y_step{i}'])
    disp_y_unsorted_1d = disp_y_halo_1d[condition_1d]

    disp_unsorted_1d = np.stack((disp_x_unsorted_1d, disp_y_unsorted_1d))
    disp_normal_unsorted_1d =  normal[0] * disp_unsorted_1d[0] + normal[1] * disp_unsorted_1d[1]
    disp_normal_1d = disp_normal_unsorted_1d[index_1d]
    disp_tangent_unsorted_1d =  tangent[0] * disp_unsorted_1d[0] + tangent[1] * disp_unsorted_1d[1]
    disp_tangent_1d = disp_tangent_unsorted_1d[index_1d]

    disp_mag_1d = np.sqrt(disp_normal_1d**2 + disp_tangent_1d**2)

    disp_x_halo_3d = np.array(disp_df_3d[f'surface_disp_x_step{i}'])
    disp_x_unsorted_3d = disp_x_halo_3d[condition_1d]
    disp_y_halo_3d = np.array(disp_df_3d[f'surface_disp_y_step{i}'])
    disp_y_unsorted_3d = disp_y_halo_3d[condition_1d]

    disp_unsorted_3d = np.stack((disp_x_unsorted_3d, disp_y_unsorted_3d))
    disp_normal_unsorted_3d =  normal[0] * disp_unsorted_3d[0] + normal[1] * disp_unsorted_3d[1]
    disp_normal_3d = disp_normal_unsorted_3d[index_1d]
    disp_tangent_unsorted_3d =  tangent[0] * disp_unsorted_3d[0] + tangent[1] * disp_unsorted_3d[1]
    disp_tangent_3d = disp_tangent_unsorted_3d[index_1d]
    
    disp_mag_3d = np.sqrt(disp_normal_3d**2 + disp_tangent_3d**2)

    diff_tang = disp_tangent_3d - disp_tangent_1d

    diff_tang_max = np.max(np.abs(diff_tang))

#    diff_rad = (disp_normal_3d - disp_normal_1d)**2 / 300**2
    diff_rad = disp_normal_3d - disp_normal_1d
    diff_rad_max = np.max(np.abs(diff_rad))
    diff_time_tang.append(np.sqrt(np.dot(diff_tang, diff_tang))/len(diff_tang))
    diff_time_rad.append(np.sqrt(np.dot(diff_rad, diff_rad))/len(diff_rad))

    diff_time_rad_max.append(diff_rad_max)
    diff_time_tang_max.append(diff_tang_max)

    # calcualte velocities (and convert to mm/yr)
    dt = 50
    vel_normal_1d = 1000*(disp_normal_1d - disp_normal_1d_old) / dt
    vel_tangent_1d = 1000*(disp_tangent_1d - disp_tangent_1d_old) / dt
    vel_mag_1d = np.sqrt(vel_normal_1d**2 + vel_tangent_1d**2)
    
    vel_normal_3d = 1000*(disp_normal_3d - disp_normal_3d_old) / dt
    vel_tangent_3d = 1000*(disp_tangent_3d - disp_tangent_3d_old) / dt
    vel_mag_3d = np.sqrt(vel_normal_3d**2 + vel_tangent_3d**2)
    
    diff_tang_vel = vel_tangent_3d - vel_tangent_1d
    diff_tang_vel_max = np.max(np.abs(diff_tang_vel))

    diff_rad_vel = vel_normal_3d - vel_normal_1d
    diff_rad_vel_max = np.max(np.abs(diff_rad_vel))
    diff_time_tang_vel.append(np.sqrt(np.dot(diff_tang_vel, diff_tang_vel))/len(diff_tang_vel))
    diff_time_rad_vel.append(np.sqrt(np.dot(diff_rad_vel, diff_rad_vel))/len(diff_rad_vel))

    diff_time_rad_vel_max.append(diff_rad_vel_max)
    diff_time_tang_vel_max.append(diff_tang_vel_max)
    
    # update old displacements
    disp_normal_1d_old = np.copy(disp_normal_1d)
    disp_tangent_1d_old = np.copy(disp_tangent_1d)

    disp_normal_3d_old = np.copy(disp_normal_3d)
    disp_tangent_3d_old = np.copy(disp_tangent_3d)

    # start plotting
    if i == 60:
        # normal displacement
        ax[0,0].plot(theta_1d, disp_normal_1d, color='r', linestyle='-', linewidth=lw, label='Axisym.')
        ax[0,0].plot(theta_1d, disp_normal_3d, color='k', linestyle='-', linewidth=lw, label='LVV')
        #ax[0,0].set_xlabel(r'Theta ($^\circ$)', fontsize=fs)
        ax[0,0].set_ylabel('Radial displacement (m)', fontsize=fs_lab)
        ax[0,0].grid(True, linestyle='dotted')
        ax[0,0].tick_params(axis='both', which='major', labelsize=fs)
        ax[0,0].set_ylim([-400, 120])
        ax[0,0].sharex(ax[1, 0])
        plt.setp(ax[0,0].get_xticklabels(), visible=False)
        ax[0,0].annotate(
                "a",
                xy=(0.01, 1), xycoords='axes fraction',
                xytext=(1, -1), textcoords='offset fontsize',
                fontsize=fs_lab, verticalalignment='top',
                bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
        ax[0,0].annotate(
                "t = 3 kyr",
                xy=(0.73, 0.155), xycoords='axes fraction',
                xytext=(1, -1), textcoords='offset fontsize',
                fontsize=fs_lab, verticalalignment='top',
                bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
        ax[0,0].legend(bbox_to_anchor=(0.66, 0.325), loc='upper left', borderaxespad=0., fontsize=fs_lab, framealpha=1, facecolor='white', edgecolor='black', fancybox=False).get_frame().set_linewidth(lw)
        
        # tangential displacement
        ax[1,0].plot(theta_1d, disp_tangent_1d, color='r', linestyle='-', linewidth=lw)
        ax[1,0].plot(theta_1d, disp_tangent_3d, color='k', linestyle='-', linewidth=lw)
        ax[1,0].set_xlabel(r'Theta ($^\circ$)', fontsize=fs_lab)
        ax[1,0].set_ylabel('Tangential displacement (m)', fontsize=fs_lab)
        ax[1,0].grid(True, linestyle='dotted')
        ax[1,0].tick_params(axis='both', which='major', labelsize=fs)
        ax[1,0].set_ylim([-400, 400])
        ax[1,0].annotate(
                "c",
                xy=(0.01, 1), xycoords='axes fraction',
                xytext=(1, -1), textcoords='offset fontsize',
                fontsize=fs_lab, verticalalignment='top',
                bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
        ax[1,0].annotate(
                "t = 3 kyr",
                xy=(0.73, 0.155), xycoords='axes fraction',
                xytext=(1, -1), textcoords='offset fontsize',
                fontsize=fs_lab, verticalalignment='top',
                bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
        
        # normal velocity
        ax[0,1].plot(theta_1d, vel_normal_1d, color='r', linestyle='-', linewidth=lw)
        ax[0,1].plot(theta_1d, vel_normal_3d, color='k', linestyle='-', linewidth=lw)
#        ax[0,1].set_xlabel(r'Theta ($^\circ$)', fontsize=fs)
        ax[0,1].set_ylabel(r'Radial velocity (mm / yr)', fontsize=fs_lab)
        ax[0,1].grid(True, linestyle='dotted')
        ax[0,1].tick_params(axis='both', which='major', labelsize=fs)
        ax[0,1].set_ylim([-40, 15])
        ax[0,1].annotate(
                "b",
                xy=(0.87, 1), xycoords='axes fraction',
                xytext=(1, -1), textcoords='offset fontsize',
                fontsize=fs_lab, verticalalignment='top',
                bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
        ax[0,1].annotate(
                "t = 3 kyr",
                xy=(0.73, 0.155), xycoords='axes fraction',
                xytext=(1, -1), textcoords='offset fontsize',
                fontsize=fs_lab, verticalalignment='top',
                bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
        
        # tangential velocity
        ax[1,1].plot(theta_1d, vel_tangent_1d, color='r', linestyle='-', linewidth=lw)
        ax[1,1].plot(theta_1d, vel_tangent_3d, color='k', linestyle='-', linewidth=0.75)
        ax[1,1].set_xlabel(r'Theta ($^\circ$)', fontsize=fs_lab)
        ax[1,1].set_ylabel(r'Tangential velocity (mm / yr)', fontsize=fs_lab)
        ax[1,1].grid(True, linestyle='dotted')
        ax[1,1].set_ylim([-40, 40])
        ax[1,1].sharex(ax[0,1])
        plt.setp(ax[0,1].get_xticklabels(), visible=False)
        ax[1,1].tick_params(axis='both', which='major', labelsize=fs)
        ax[1,1].annotate(
                "d",
                xy=(0.87, 1), xycoords='axes fraction',
                xytext=(1, -1), textcoords='offset fontsize',
                fontsize=fs_lab, verticalalignment='top',
                bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
        ax[1,1].annotate(
                "t = 3 kyr",
                xy=(0.733, 0.155), xycoords='axes fraction',
                xytext=(1, -1), textcoords='offset fontsize',
                fontsize=fs_lab, verticalalignment='top',
                bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
        
    

# plotting misfits through time
time = np.linspace(50, 10000, 200)/1000


ax[2,0].plot(time, diff_time_rad, color='k', linestyle='-', marker='o', markevery=20, markersize=ms, linewidth=lw, label='Radial')
ax[2,0].plot(time, diff_time_tang, color='k', linestyle='-', marker='x', markevery=20, markersize=ms, linewidth=lw, label='Tangential')
ax[2,0].plot([3, 3], [0, 2], linestyle='dashed', color='k', linewidth=lw)
ax[2,0].set_ylim([0, 1.1])
ax[2,0].set_xlabel(r'Time (kyr)', fontsize=fs_lab)
ax[2,0].set_ylabel('RMS difference in displacement (m)', fontsize=fs_lab)
ax[2,0].tick_params(axis='both', which='major', labelsize=fs)
ax[2,0].grid(True, linestyle='dotted')
ax[2,0].annotate(
        "e",
        xy=(0.01, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
ax[2,0].annotate(
        "t = 3 kyr",
        xy=(0.325, 0.7), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
ax[2,0].legend(loc='lower right', fontsize=fs_lab, framealpha=1, facecolor='white', edgecolor='black', fancybox=False).get_frame().set_linewidth(lw)

ax[2,1].plot(time, diff_time_rad_vel, color='k', linestyle='-', linewidth=lw, marker='o', markevery=20, markersize=ms)
ax[2,1].plot(time, diff_time_tang_vel, color='k', linestyle='-', linewidth=lw, marker='x', markevery=20, markersize=ms)
ax[2,1].plot([3, 3], [0, 2], linestyle='dashed', color='k', linewidth=lw)
ax[2,1].set_ylim([0, 1.5])
ax[2,1].set_xlabel(r'Time (kyr)', fontsize=fs_lab)
ax[2,1].set_ylabel('RMS difference in velocity (mm / yr)', fontsize=fs_lab)
ax[2,1].tick_params(axis='both', which='major', labelsize=fs)
ax[2,1].grid(True, linestyle='dotted')
ax[2,1].annotate(
        "f",
        xy=(0.87, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))

ax[2,1].annotate(
        "t = 3 kyr",
        xy=(0.325, 0.7), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
#ax[1].set_ylim([-1, 1])
plt.savefig(f'21.08.25_1dvs3dvisc_dispvel_misfit_snapshot_units_swap.png')
plt.close()


