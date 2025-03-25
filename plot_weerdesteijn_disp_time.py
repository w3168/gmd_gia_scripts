import matplotlib.pyplot as plt
import matplotlib
import numpy as np

folder = "./weerdesteijn_data/"
folder_gadopt = "./weerdesteijn_data/internal_variable/nondimensional/"

gadopt_displacement = np.loadtxt(f"{folder_gadopt}displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk100.0-nondim.dat")

aspect_displacement_long = np.loadtxt(f"{folder}aspect_fig_4b_file.csv", delimiter=',')
abaqus_displacement_long = np.loadtxt(f"{folder}abaqus_picks_fig4b.csv", delimiter=',')
taboo_displacement_long = np.loadtxt(f"{folder}taboo_picks_fig4b.csv", delimiter=',')


fig, ax = plt.subplots(1, 1, figsize=(20, 15))

ax.plot(abaqus_displacement_long[:,0]*1e3,abaqus_displacement_long[:,1], color='k',linestyle='dotted', label='Abaqus')
ax.plot(taboo_displacement_long[:,0]*1e3,taboo_displacement_long[:,1], color='k', linestyle='dashed', label='Taboo')
ax.plot(aspect_displacement_long[:,0],aspect_displacement_long[:,1], color='k', linestyle='dashdot', label='Aspect')
ax.plot(gadopt_displacement[:,0], gadopt_displacement[:,1], 'b-', label='G-ADOPT')

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

figname = "25.03.25_gadopt_3d_weerdesteijn_internalvariable_nondim_bulk100x_dx5_nz10_dt1ka"
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

