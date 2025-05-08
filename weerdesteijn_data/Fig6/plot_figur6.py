import matplotlib.pyplot as plt
import matplotlib
import numpy as np

short_folder = "short/"

vr0pt1_nz10_dx5_dt10 = np.loadtxt(f'{short_folder}07.05.25_weerdesteijn_burgers_internalvariable_200a_dt10yr_dtout10ka_work896cores_mem4000gb_dx5to200km_refinedsurface_DG0nzperlayer10_icetanh1km_bulktoshear1.94_symmmult_nondim_compbuoyVifix_gmres_viscratio0.1_includescompprestress_data_min_disp')
vr0pt1_nz10_dx5_dt5 = np.loadtxt(f'{short_folder}07.05.25_weerdesteijn_burgers_internalvariable_200a_dt5yr_dtout10ka_work896cores_mem4000gb_dx5to200km_refinedsurface_DG0nzperlayer10_icetanh1km_bulktoshear1.94_symmmult_nondim_compbuoyVifix_gmres_viscratio0.1_includescompprestress_data_min_disp')
vr0pt1_nz5_dx5_dt10 = np.loadtxt(f'{short_folder}07.05.25_weerdesteijn_burgers_internalvariable_200a_dt10yr_dtout10ka_work896cores_mem4000gb_dx5to200km_refinedsurface_DG0nzperlayer5_icetanh1km_bulktoshear1.94_symmmult_nondim_compbuoyVifix_gmres_viscratio0.1_includescompprestress_data_min_disp')
vr0pt1_nz10_dx10_dt10 = np.loadtxt(f'{short_folder}07.05.25_weerdesteijn_burgers_internalvariable_200a_dt10yr_dtout10ka_work896cores_mem4000gb_dx10to200km_refinedsurface_DG0nzperlayer10_icetanh1km_bulktoshear1.94_symmmult_nondim_compbuoyVifix_gmres_viscratio0.1_includescompprestress_data_min_disp')
vr0pt5_nz10_dx5_dt10 = np.loadtxt(f'{short_folder}07.05.25_weerdesteijn_burgers_internalvariable_200a_dt10yr_dtout10ka_work896cores_mem4000gb_dx5to200km_refinedsurface_DG0nzperlayer10_icetanh1km_bulktoshear1.94_symmmult_nondim_compbuoyVifix_gmres_viscratio0.5_includescompprestress_data_mindisp')
vr1_nz10_dx5_dt10 = np.loadtxt(f'{short_folder}07.05.25_weerdesteijn_burgers_internalvariable_200a_dt10yr_dtout10ka_work896cores_mem4000gb_dx5to200km_refinedsurface_DG0nzperlayer10_icetanh1km_bulktoshear1.94_symmmult_nondim_compbuoyVifix_gmres_viscratio1_includescompprestress_data_min_disp')

long_burgers = "long/"
gadopt_displacement_comp_burgers = np.loadtxt(f"{long_burgers}displacement-weerdesteijn-3d-internalvariable-burgers-symmult_nondim_gmres_Vifix_mu1mu2visc1visc2half_fixmu-refinedsurfaceTrue-dx5.0km-nz5perlayer-dt1000.0years-bulk1.94-compbuoyTrue-nondim.dat")
gadopt_displacement_comp_burgers_0pt5 = np.loadtxt(f"{long_burgers}displacement-weerdesteijn-3d-internalvariable-burgers--refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk1.94-compbuoyTrue-viscratio0.5-nondim.dat")
gadopt_displacement_comp_burgers_0pt1 = np.loadtxt(f"{long_burgers}displacement-weerdesteijn-3d-internalvariable-burgers--refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk1.94-compbuoyTrue-viscratio0.1-nondim.dat")

times_dt10 = np.arange(0, 210, 10)
times_dt5 = np.arange(5, 205, 5)

fig, ax = plt.subplots(1, 2, figsize=(7,3), dpi=300)

lw = 0.8
ax[0].plot(times_dt10, vr0pt1_nz10_dx5_dt10[:21], color='orange', linewidth=lw, linestyle='-', label=r'$\eta_1 / \eta_2 = 10$')
ax[0].plot(times_dt10, vr0pt5_nz10_dx5_dt10[:21], color='b', linewidth=lw,linestyle='-', label=r'$\eta_1 / \eta_2 = 2$')
ax[0].plot(times_dt10, vr1_nz10_dx5_dt10[:21], color='k', linewidth=lw, linestyle='-', label=r'$\eta_1 / \eta_2 = 1$')

fs = 6
fs_lab = 7
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
# Plot short, 1D burgers
ax[0].set_xlabel('Time (a)', fontsize=fs_lab)
ax[0].set_ylabel('Maximum vertical displacement (m)', fontsize=fs_lab)
ax[0].grid(True)
ax[0].tick_params(axis='both', which='major', labelsize=fs)
ax[0].legend(fontsize=fs)
ax[0].annotate('a)', (-9.1, 0.11), fontsize=fs_lab, annotation_clip=False)

# Plot long, 1D burgers
ax[1].plot(gadopt_displacement_comp_burgers_0pt1[:,0]/1e3, gadopt_displacement_comp_burgers_0pt1[:,1], color='orange', linewidth=lw, linestyle='-', label=r'$\eta_1 / \eta_2 = 10$')
ax[1].plot(gadopt_displacement_comp_burgers_0pt5[:,0]/1e3, gadopt_displacement_comp_burgers_0pt5[:,1], color='b', linewidth=lw, linestyle='-', label=r'$\eta_1 / \eta_2 = 2$')
ax[1].plot(gadopt_displacement_comp_burgers[:,0]/1e3, gadopt_displacement_comp_burgers[:,1], color='k', linewidth=lw, linestyle='-', label=r'$\eta_1 / \eta_2 = 1$')
ax[1].set_xlabel('Time (ka)', fontsize=fs_lab)
ax[1].set_ylabel('Maximum vertical displacement (m)', fontsize=fs_lab)
ax[1].grid(True)
ax[1].tick_params(axis='both', which='major', labelsize=fs)
ax[1].annotate('b)', (-5, 6), fontsize=fs_lab, annotation_clip=False)

figname = "Figure_6_compressible_burgers_08.05.25"
fig.savefig(f'{figname}.png')

