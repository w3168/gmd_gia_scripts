import matplotlib.pyplot as plt
import matplotlib
import numpy as np

folder = "./"
folder_gadopt = "./"


# dx
gadopt_displacement_dx5 = np.loadtxt(f"{folder_gadopt}displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk100.0-nondim.dat")
gadopt_displacement_dx10 = np.loadtxt(f"{folder_gadopt}displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx10.0km-nz10perlayer-dt1000.0years-bulk100.0-nondim.dat")
gadopt_displacement_dx20 = np.loadtxt(f"{folder_gadopt}displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx20.0km-nz10perlayer-dt1000.0years-bulk100.0-nondim.dat")

# nz
gadopt_displacement_nz10 = np.loadtxt(f"{folder_gadopt}displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk100.0-nondim.dat")
gadopt_displacement_nz5 = np.loadtxt(f"{folder_gadopt}displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz5perlayer-dt1000.0years-bulk100.0-nondim.dat")
gadopt_displacement_nz2 = np.loadtxt(f"{folder_gadopt}displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz2perlayer-dt1000.0years-bulk100.0-nondim.dat")
gadopt_displacement_nz1 = np.loadtxt(f"{folder_gadopt}displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz1perlayer-dt1000.0years-bulk100.0-nondim.dat")

# dt
gadopt_displacement_dt1000 = np.loadtxt(f"{folder_gadopt}displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk100.0-nondim.dat")
gadopt_displacement_dt2000 = np.loadtxt(f"{folder_gadopt}displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt2000.0years-bulk100.0-nondim.dat")
gadopt_displacement_dt5000 = np.loadtxt(f"{folder_gadopt}displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt5000.0years-bulk100.0-nondim.dat")
gadopt_displacement_dt10000 = np.loadtxt(f"{folder_gadopt}displacement-weerdesteijn-3d-internalvariable-symmult-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt10000.0years-bulk10000000000000.0.dat")

# compressibility
gadopt_displacement_bulk100 = np.loadtxt(f"{folder_gadopt}displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk100.0-nondim.dat")
gadopt_displacement_bulk1000 = np.loadtxt(f"{folder_gadopt}displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk1000.0-nondim.dat")
gadopt_displacement_bulk2 = np.loadtxt(f"{folder_gadopt}displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk2.0-nondim.dat")

fig, ax = plt.subplots(2, 2, figsize=(20, 15))
#plt.rcParams.update({'font.size': 30})

# Plot dx sensitivity
ax[0, 0].plot(gadopt_displacement_dx5[:,0]/1e3, gadopt_displacement_dx5[:,1], 'b-', label='dx = 5 km (default)')
ax[0, 0].plot(gadopt_displacement_dx10[:,0]/1e3, gadopt_displacement_dx10[:,1], color='k', linestyle='--',marker='x',markevery=10, label='dx = 10 km',alpha=0.5)
ax[0, 0].plot(gadopt_displacement_dx20[:,0]/1e3, gadopt_displacement_dx20[:,1], color='k', linestyle='--', marker='o', markevery=10, label='dx = 20 km',alpha=0.5)
ax[0, 0].set_xlabel('Time (ka)', fontsize='20')
ax[0, 0].set_ylabel('Maximum vertical displacement (m)', fontsize=20)
ax[0, 0].grid(True)
ax[0, 0].tick_params(axis='both', which='major', labelsize=12)
ax[0, 0].legend(fontsize=12)
ax[0, 0].annotate('a)', (-5, 6), fontsize='25', annotation_clip=False)

# Plot nz sensitivity
ax[0, 1].plot(gadopt_displacement_nz10[:,0]/1e3, gadopt_displacement_nz10[:,1], 'b-', label='10 cells per layer (default)')
ax[0, 1].plot(gadopt_displacement_nz5[:,0]/1e3, gadopt_displacement_nz5[:,1], color='k', linestyle='--',marker='x',markevery=10, label='5 cells per layer',alpha=0.5)
ax[0, 1].plot(gadopt_displacement_nz2[:,0]/1e3, gadopt_displacement_nz2[:,1], color='k', linestyle='--', marker='o', markevery=10, label='2 cells per layer',alpha=0.5)
ax[0, 1].plot(gadopt_displacement_nz1[:,0]/1e3, gadopt_displacement_nz1[:,1], color='k', linestyle='--', marker='^', markevery=10, label='1 cell per layer',alpha=0.5)
ax[0, 1].set_xlabel('Time (ka)', fontsize='20')
ax[0, 1].set_ylabel('Maximum vertical displacement (m)', fontsize=20)
ax[0, 1].grid(True)
ax[0, 1].tick_params(axis='both', which='major', labelsize=12)
ax[0, 1].legend(fontsize=12)
ax[0, 1].annotate('b)', (-5, 6), fontsize='25', annotation_clip=False)

# Plot dt sensitivity
ax[1, 0].plot(gadopt_displacement_dt1000[:,0]/1e3, gadopt_displacement_dt1000[:,1], 'b-', label='dt = 1 ka (default)')
ax[1, 0].plot(gadopt_displacement_dt2000[:,0]/1e3, gadopt_displacement_dt2000[:,1], color='k', linestyle='--',marker='x',markevery=5, label='dt = 2 ka',alpha=0.5)
ax[1, 0].plot(gadopt_displacement_dt5000[:,0]/1e3, gadopt_displacement_dt5000[:,1], color='k', linestyle='--', marker='o', markevery=2, label='dt = 5 ka',alpha=0.5)
ax[1, 0].plot(gadopt_displacement_dt10000[:,0]/1e3, gadopt_displacement_dt10000[:,1], color='k', linestyle='--', marker='^', markevery=1, label='dt = 10 ka',alpha=0.5)
ax[1, 0].set_xlabel('Time (ka)', fontsize='20')
ax[1, 0].set_ylabel('Maximum vertical displacement (m)', fontsize=20)
ax[1, 0].grid(True)
ax[1, 0].legend()
ax[1, 0].tick_params(axis='both', which='major', labelsize=12)
ax[1, 0].legend(fontsize=12)
ax[1, 0].annotate('c)', (-5, 6), fontsize='25', annotation_clip=False)

# Plot bulk
ax[1, 1].plot(gadopt_displacement_bulk2[:,0]/1e3, gadopt_displacement_bulk2[:,1], color='k', linestyle='--',marker='x',markevery=10, label=r'$\kappa / \mu$ = 2',alpha=1)
ax[1, 1].plot(gadopt_displacement_bulk100[:,0]/1e3, gadopt_displacement_bulk100[:,1], 'b-', label=r'$\kappa / \mu$ = 100 (default)')
ax[1, 1].plot(gadopt_displacement_bulk1000[:,0]/1e3, gadopt_displacement_bulk1000[:,1], color='k', linestyle='--', marker='o', markevery=10, label=r'$\kappa / \mu$ = 1000',alpha=0.5)
ax[1, 1].set_xlabel('Time (ka)', fontsize='20')
ax[1, 1].set_ylabel('Maximum vertical displacement (m)', fontsize=20)
ax[1, 1].grid(True)
ax[1, 1].tick_params(axis='both', which='major', labelsize=12)
ax[1, 1].legend(fontsize=12)
ax[1, 1].annotate('d)', (-5, 7), fontsize='25', annotation_clip=False)


figname = "Figure_4_incompressible_weerdesteijn_long_res_30.04.25"
fig.savefig(f'{figname}.png')

