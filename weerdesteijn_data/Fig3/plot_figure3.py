import matplotlib.pyplot as plt
import matplotlib
import numpy as np

folder = "./"
folder_gadopt = "./"

gadopt_displacement = np.loadtxt(f"{folder_gadopt}displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk100.0-nondim.dat")
gadopt_displacement_short = np.loadtxt("displacement-weerdesteijn-3d-internalvariable-prestressadv-short-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt10.0years-bulk1000.0-compbuoyFalse-nondim.dat")

gadopt_displacement_short_lowvisc = np.loadtxt("displacement-weerdesteijn-3d-internalvariable-prestressadv-short_lateralvisc-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt10.0years-bulk1000.0-compbuoyFalse-nondim.dat")
gadopt_displacement_short_lowvisc_dt5 = np.loadtxt("displacement-weerdesteijn-3d-internalvariable-prestressadv-short_lateralvisc-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt5.0years-bulk1000.0-compbuoyFalse-nondim.dat")


gadopt_displacement_long_lowvisc_nz5 = np.loadtxt("displacement-weerdesteijn-3d-internalvariable-prestressadv-long_lateralvisc-refinedsurfaceTrue-dx5.0km-nz5perlayer-dt1000.0years-bulk100.0-compbuoyFalse-nondim.dat")
gadopt_displacement_long_lowvisc = np.loadtxt("displacement-weerdesteijn-3d-internalvariable-prestressadv-long_lateralvisc-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk100.0-compbuoyFalse-nondim.dat")

aspect_displacement_short_old = np.loadtxt(f"{folder}aspect_fig_3b.csv", delimiter=',')
aspect_displacement_short = np.loadtxt(f"{folder}aspect_short_picks_fig3b.csv", delimiter=',')
aspect_displacement_long = np.loadtxt(f"{folder}aspect_fig_4b_file.csv", delimiter=',')
aspect_displacement_short_lowvisc = np.loadtxt(f"{folder}aspect_short_lowvisc_picks_fig7c.csv", delimiter=',')

abaqus_displacement_short = np.loadtxt(f"{folder}abaqus_short_picks_fig3b.csv", delimiter=',')
abaqus_displacement_long = np.loadtxt(f"{folder}abaqus_picks_fig4b.csv", delimiter=',')
abaqus_displacement_short_lowvisc = np.loadtxt(f"{folder}abaqus_short_lowvisc_picks_fig7c.csv", delimiter=',')

taboo_displacement_short = np.loadtxt(f"{folder}taboo_short_picks_fig3b.csv", delimiter=',')
taboo_displacement_long = np.loadtxt(f"{folder}taboo_picks_fig4b.csv", delimiter=',')


fig, ax = plt.subplots(2, 2, figsize=(20, 15))

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# Plot short, 1D
ax[0, 0].plot(abaqus_displacement_short[:,0],abaqus_displacement_short[:,1], color='k', linestyle='dotted', label='Abaqus')
ax[0, 0].plot(aspect_displacement_short[:,0],aspect_displacement_short[:,1], color='k', linestyle='dashdot', label='Aspect')
ax[0, 0].plot(taboo_displacement_short[:,0],taboo_displacement_short[:,1], color='k', linestyle='dashed', label='Taboo')
ax[0, 0].plot(gadopt_displacement_short[:,0], gadopt_displacement_short[:,1], 'b-', label='G-ADOPT')
ax[0, 0].set_xlabel('Time (a)', fontsize='20')
ax[0, 0].set_ylabel('Maximum vertical displacement (m)', fontsize=20)
ax[0, 0].grid(True)
ax[0, 0].tick_params(axis='both', which='major', labelsize=12)
ax[0, 0].legend(fontsize='12')
ax[0, 0].annotate('a)', (-9.1, 0.07), fontsize='25', annotation_clip=False)

# Plot long, 1D
ax[0, 1].plot(abaqus_displacement_long[:,0],abaqus_displacement_long[:,1], color='k',linestyle='dotted', label='Abaqus')
ax[0, 1].plot(aspect_displacement_long[:,0]/1e3,aspect_displacement_long[:,1], color='k', linestyle='dashdot', label='Aspect')
ax[0, 1].plot(taboo_displacement_long[:,0],taboo_displacement_long[:,1], color='k', linestyle='dashed', label='Taboo')
ax[0, 1].plot(gadopt_displacement[:,0]/1e3, gadopt_displacement[:,1], 'b-', label='G-ADOPT')
ax[0, 1].set_xlabel('Time (ka)', fontsize='20')
ax[0, 1].set_ylabel('Maximum vertical displacement (m)', fontsize='20')
ax[0, 1].grid(True)
ax[0, 1].tick_params(axis='both', which='major', labelsize=12)
ax[0, 1].legend(fontsize='12')
ax[0, 1].annotate('b)', (-5, 6), fontsize='25', annotation_clip=False)

# Plot short, 3D
short3d_nz20 = [0, -0.07989565708296328, -0.17144317885944316, -0.27035517135079257, -0.37417535030035554, -0.48146908522353593, -0.591382854527602, -0.7033991488098003]
short3d_dx2pt5 = [0,-0.07982142709476364, -0.1711987954206557, -0.2698370476160385, -0.37328344534564184, -0.4801128213997595, -0.5894836911647034, -0.700889866936529, -0.8140196710373107, -0.9286717498082858]
print(short3d_nz20)
ax[1, 0].plot(abaqus_displacement_short_lowvisc[:,0],abaqus_displacement_short_lowvisc[:,1], color='k', linestyle='dotted', label='Abaqus')
ax[1, 0].plot(aspect_displacement_short_lowvisc[:,0],aspect_displacement_short_lowvisc[:,1], color='k', linestyle='dashdot', label='Aspect')
ax[1, 0].plot(gadopt_displacement_short_lowvisc[:,0], gadopt_displacement_short_lowvisc[:,1], 'b-', label='G-ADOPT')
ax[1, 0].plot(gadopt_displacement_short_lowvisc_dt5[:,0], gadopt_displacement_short_lowvisc_dt5[:,1], '-', label='G-ADOPT dt 5')
ax[1, 0].plot(gadopt_displacement_short_lowvisc[:8,0], short3d_nz20, '-', label='G-ADOPT 20 layers')
ax[1, 0].plot(gadopt_displacement_short_lowvisc[:10,0], short3d_dx2pt5, '-', label='G-ADOPT dx 2.5 km ')
ax[1, 0].set_xlabel('Time (a)', fontsize='20')
ax[1, 0].set_ylabel('Maximum vertical displacement (m)', fontsize=20)
ax[1, 0].grid(True)
ax[1, 0].tick_params(axis='both', which='major', labelsize=12)
ax[1, 0].legend(fontsize='12')
ax[1, 0].annotate('c)', (-9.1, 0.12), fontsize='25', annotation_clip=False)

# Plot long, 3d
ax[1, 1].plot(gadopt_displacement_long_lowvisc_nz5[:,0]/1e3, gadopt_displacement_long_lowvisc_nz5[:,1], 'b-', label='G-ADOPT')
ax[1, 1].set_xlabel('Time (ka)', fontsize='20')
ax[1, 1].set_ylabel('Maximum vertical displacement (m)', fontsize='20')
ax[1, 1].grid(True)
ax[1, 1].tick_params(axis='both', which='major', labelsize=12)
ax[1, 1].legend(fontsize='12')
ax[1, 1].annotate('d)', (-5, 6), fontsize='25', annotation_clip=False)


figname = "Figure_3_incompressible_weerdesteijn_1.05.25_checkshort20layers_dx2.5_dt5"
fig.savefig(f'{figname}.png')

