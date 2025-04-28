import matplotlib.pyplot as plt
import matplotlib
import numpy as np

folder = "./"
folder_gadopt = "./"

gadopt_displacement = np.loadtxt(f"{folder_gadopt}displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk100.0-nondim.dat")
gadopt_displacement_short = np.loadtxt("displacement-weerdesteijn-3d-internalvariable-prestressadv-short-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt10.0years-bulk1000.0-compbuoyFalse-nondim.dat")
gadopt_displacement_short_lowvisc = np.loadtxt("displacement-weerdesteijn-3d-internalvariable-prestressadv-short_lateralvisc-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt10.0years-bulk100.0-compbuoyFalse-nondim.dat")

aspect_displacement_short_old = np.loadtxt(f"{folder}aspect_fig_3b.csv", delimiter=',')
aspect_displacement_short = np.loadtxt(f"{folder}aspect_short_picks_fig3b.csv", delimiter=',')
aspect_displacement_long = np.loadtxt(f"{folder}aspect_fig_4b_file.csv", delimiter=',')
aspect_displacement_short_lowvisc = np.loadtxt(f"{folder}aspect_short_lowvisc_picks_fig7c.csv", delimiter=',')

abaqus_displacement_short = np.loadtxt(f"{folder}abaqus_short_picks_fig3b.csv", delimiter=',')
abaqus_displacement_long = np.loadtxt(f"{folder}abaqus_picks_fig4b.csv", delimiter=',')

taboo_displacement_short = np.loadtxt(f"{folder}taboo_short_picks_fig3b.csv", delimiter=',')
taboo_displacement_long = np.loadtxt(f"{folder}taboo_picks_fig4b.csv", delimiter=',')


fig, ax = plt.subplots(2, 2, figsize=(20, 15))
#plt.rcParams.update({'font.size': 30})

# Plot short, 1D
ax[0, 0].plot(abaqus_displacement_short[:,0],abaqus_displacement_short[:,1], color='k', linestyle='dotted', label='Abaqus')
ax[0, 0].plot(aspect_displacement_short[:,0],aspect_displacement_short[:,1], color='k', linestyle='dashdot', label='Aspect')
ax[0, 0].plot(taboo_displacement_short[:,0],taboo_displacement_short[:,1], color='k', linestyle='dashed', label='Taboo')
ax[0, 0].plot(gadopt_displacement_short[:,0], gadopt_displacement_short[:,1], 'b-', label='G-ADOPT')
ax[0, 0].set_xlabel('Time (a)', fontsize='30')
ax[0, 0].set_ylabel('Maximum vertical displacement (m)', fontsize=20)
ax[0, 0].grid(True)
ax[0, 0].legend()


# Plot long, 1D
ax[0, 1].plot(abaqus_displacement_long[:,0],abaqus_displacement_long[:,1], color='k',linestyle='dotted', label='Abaqus')
ax[0, 1].plot(aspect_displacement_long[:,0]/1e3,aspect_displacement_long[:,1], color='k', linestyle='dashdot', label='Aspect')
ax[0, 1].plot(taboo_displacement_long[:,0],taboo_displacement_long[:,1], color='k', linestyle='dashed', label='Taboo')
ax[0, 1].plot(gadopt_displacement[:,0]/1e3, gadopt_displacement[:,1], 'b-', label='G-ADOPT')
ax[0, 1].set_xlabel('Time (ka)', fontsize='30')
ax[0, 1].set_ylabel('Maximum vertical displacement (m)', fontsize='20')
ax[0, 1].grid(True)
ax[0, 1].legend()

# Plot short, 3D
ax[1, 0].plot(aspect_displacement_short_lowvisc[:,0],aspect_displacement_short_lowvisc[:,1], color='k', linestyle='dashdot', label='Aspect')
ax[1, 0].plot(gadopt_displacement_short_lowvisc[:,0], gadopt_displacement_short_lowvisc[:,1], 'b-', label='G-ADOPT')
ax[1, 0].set_xlabel('Time (a)', fontsize='30')
ax[1, 0].set_ylabel('Maximum vertical displacement (m)', fontsize=20)
ax[1, 0].grid(True)
ax[1, 0].legend()


figname = "Figure_3_incompressible_weerdesteijn_28.04.25"
fig.savefig(f'{figname}.png')

exit()
font = {'size': 20}
# using rc function
plt.rc('font', **font)
plt.xticks(fontsize=40)
plt.yticks(fontsize=40)




#plt.show()
ax.set_xlim([70e3, 110e3])
ax.set_ylim([-80, -45])
fig.savefig(f'{figname}_zoom_peak.png')

ax.set_xlim([85e3, 110e3])
ax.set_ylim([-70, -5])
fig.savefig(f'{figname}_zoom_end.png')

ax.set_xlim([-5e2, 20e3])
ax.set_ylim([-20, 1])
fig.savefig(f'{figname}_zoom_start.png')


# Plot compressible vs incompressible (and burgers)
gadopt_displacement_bulk2x = np.loadtxt(f"{folder_gadopt}displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk2.0-nondim.dat")


fig, ax = plt.subplots(1, 1, figsize=(20, 15))

ax.plot(gadopt_displacement[:,0], gadopt_displacement[:,1], 'b-', label='G-ADOPT, incompressible')
ax.plot(gadopt_displacement_bulk2x[:,0], gadopt_displacement_bulk2x[:,1], 'k-', label='G-ADOPT, compressible')

plt.rcParams.update({'font.size': 30})

font = {'size': 20}
 
# using rc function
plt.rc('font', **font)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#ax.set_xlim([0, 1000])
#ax.set_ylim([-0.5, 0])
ax.set_xlabel('Time (years)', fontsize='30')
ax.set_ylabel('Maximum vertical displacement (m)', fontsize='30')
ax.grid(True)
ax.legend()

figname = "25.03.25_gadopt_3d_weerdesteijn_internalvariable_nondim_dx5_nz10_dt1ka_bulkcomparison"
fig.savefig(f'{figname}.png')
#plt.show()
ax.set_xlim([70e3, 110e3])
ax.set_ylim([-80, -45])
fig.savefig(f'{figname}_zoom_peak.png')

ax.set_xlim([85e3, 110e3])
ax.set_ylim([-70, -5])
fig.savefig(f'{figname}_zoom_end.png')

ax.set_xlim([-5e2, 20e3])
ax.set_ylim([-20, 1])
fig.savefig(f'{figname}_zoom_start.png')

