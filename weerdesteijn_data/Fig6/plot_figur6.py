import matplotlib.pyplot as plt
import matplotlib
from matplotlib import colormaps
import numpy as np

short_folder = "short/"
cmap = colormaps['Set1']
colours = cmap.colors

colour_comp = colours[0]
colour_incomp = colours[1]
colour_burgers_2 = colours[3]
colour_burgers_10 = colours[4]

# incompressible
incomp_short = np.loadtxt(f"{short_folder}displacement-weerdesteijn-3d-internalvariable-prestressadv-short-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt10.0years-bulk1000.0-compbuoyFalse-nondim.dat")

# Burgers
vr0pt1_nz10_dx5_dt10 = np.loadtxt(f'{short_folder}07.05.25_weerdesteijn_burgers_internalvariable_200a_dt10yr_dtout10ka_work896cores_mem4000gb_dx5to200km_refinedsurface_DG0nzperlayer10_icetanh1km_bulktoshear1.94_symmmult_nondim_compbuoyVifix_gmres_viscratio0.1_includescompprestress_data_min_disp')
vr0pt1_nz10_dx5_dt5 = np.loadtxt(f'{short_folder}07.05.25_weerdesteijn_burgers_internalvariable_200a_dt5yr_dtout10ka_work896cores_mem4000gb_dx5to200km_refinedsurface_DG0nzperlayer10_icetanh1km_bulktoshear1.94_symmmult_nondim_compbuoyVifix_gmres_viscratio0.1_includescompprestress_data_min_disp')
vr0pt1_nz5_dx5_dt10 = np.loadtxt(f'{short_folder}07.05.25_weerdesteijn_burgers_internalvariable_200a_dt10yr_dtout10ka_work896cores_mem4000gb_dx5to200km_refinedsurface_DG0nzperlayer5_icetanh1km_bulktoshear1.94_symmmult_nondim_compbuoyVifix_gmres_viscratio0.1_includescompprestress_data_min_disp')
vr0pt1_nz10_dx10_dt10 = np.loadtxt(f'{short_folder}07.05.25_weerdesteijn_burgers_internalvariable_200a_dt10yr_dtout10ka_work896cores_mem4000gb_dx10to200km_refinedsurface_DG0nzperlayer10_icetanh1km_bulktoshear1.94_symmmult_nondim_compbuoyVifix_gmres_viscratio0.1_includescompprestress_data_min_disp')
vr0pt5_nz10_dx5_dt10 = np.loadtxt(f'{short_folder}07.05.25_weerdesteijn_burgers_internalvariable_200a_dt10yr_dtout10ka_work896cores_mem4000gb_dx5to200km_refinedsurface_DG0nzperlayer10_icetanh1km_bulktoshear1.94_symmmult_nondim_compbuoyVifix_gmres_viscratio0.5_includescompprestress_data_mindisp')
vr1_nz10_dx5_dt10 = np.loadtxt(f'{short_folder}07.05.25_weerdesteijn_burgers_internalvariable_200a_dt10yr_dtout10ka_work896cores_mem4000gb_dx5to200km_refinedsurface_DG0nzperlayer10_icetanh1km_bulktoshear1.94_symmmult_nondim_compbuoyVifix_gmres_viscratio1_includescompprestress_data_min_disp')

long_burgers = "long/"
incomp = np.loadtxt(f"{long_burgers}displacement-weerdesteijn-3d-internalvariable-rerun_outer1e-2-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk1000.0-compbuoyFalse-nondim.dat")
comp = np.loadtxt(f"{long_burgers}displacement-weerdesteijn-3d-internalvariable-rerun_outer1e-2-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk1.94-compbuoyTrue-nondim.dat")
comp_burgers_viscratio1 = np.loadtxt(f"{long_burgers}displacement-weerdesteijn-3d-internalvariable-burgers-rerun_comphydpre-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk1.94-compbuoyTrue-viscratio1.0-nondim.dat")
comp_burgers_viscratio0pt5 = np.loadtxt(f"{long_burgers}displacement-weerdesteijn-3d-internalvariable-burgers-rerun_comphydpre-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk1.94-compbuoyTrue-viscratio0.5-nondim.dat")
comp_burgers_viscratio0pt1 = np.loadtxt(f"{long_burgers}displacement-weerdesteijn-3d-internalvariable-burgers-rerun_comphydpre-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk1.94-compbuoyTrue-viscratio0.1-nondim.dat")

gadopt_displacement_comp_burgers = np.loadtxt(f"{long_burgers}displacement-weerdesteijn-3d-internalvariable-burgers-symmult_nondim_gmres_Vifix_mu1mu2visc1visc2half_fixmu-refinedsurfaceTrue-dx5.0km-nz5perlayer-dt1000.0years-bulk1.94-compbuoyTrue-nondim.dat")
gadopt_displacement_comp_burgers_0pt5 = np.loadtxt(f"{long_burgers}displacement-weerdesteijn-3d-internalvariable-burgers--refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk1.94-compbuoyTrue-viscratio0.5-nondim.dat")
gadopt_displacement_comp_burgers_0pt1 = np.loadtxt(f"{long_burgers}displacement-weerdesteijn-3d-internalvariable-burgers--refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk1.94-compbuoyTrue-viscratio0.1-nondim.dat")

times_dt10 = np.arange(0, 210, 10)
times_dt5 = np.arange(5, 205, 5)

fig, ax = plt.subplots(1, 2, figsize=(8,3.5), dpi=300, layout="constrained")

# fonts and linewidths etc
fs = 9
fs_lab = 10
ms = 5
lw = 0.75
ax[0].plot(incomp_short[:,0], incomp_short[:,1], color=colour_incomp, linewidth=lw, linestyle='-', label=r'Incompressible')
ax[0].plot(times_dt10, vr1_nz10_dx5_dt10[:21], color=colour_comp, linewidth=lw, linestyle='-', label=r'Compressible')
ax[0].plot(times_dt10, vr0pt5_nz10_dx5_dt10[:21], color=colour_burgers_2, linewidth=lw,linestyle='-', label=r'Burgers ($\eta_1 / \eta_2 = 2$)')
ax[0].plot(times_dt10, vr0pt1_nz10_dx5_dt10[:21], color=colour_burgers_10, linewidth=lw, linestyle='-', label=r'Burgers ($\eta_1 / \eta_2 = 10$)')

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
# Plot short, 1D burgers
ax[0].set_xlabel('Time (a)', fontsize=fs_lab)
ax[0].set_ylabel('Maximum vertical displacement (m)', fontsize=fs_lab)
ax[0].grid(True, linestyle='dotted')
ax[0].tick_params(axis='both', which='major', labelsize=fs)
ax[0].annotate(
        "a",
        xy=(0.465, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
ax[0].annotate(
        r"Short, 1D viscosity",
        xy=(0.54, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))

# Plot long, 1D burgers
ax[1].plot(incomp[:,0]/1e3, incomp[:,1], color=colour_incomp, linewidth=lw, linestyle='-', label=r'Maxwell (incompressible)')
ax[1].plot(comp[:,0]/1e3, comp[:,1], color=colour_comp, linewidth=lw, linestyle='-', label=r'Maxwell (compressible)')
ax[1].plot(comp_burgers_viscratio0pt5[:,0]/1e3, comp_burgers_viscratio0pt5[:,1], color=colour_burgers_2, linewidth=lw, linestyle='-', label=r'Burgers ($\eta_1 / \eta_2 = 2$)')
ax[1].plot(comp_burgers_viscratio0pt1[:,0]/1e3, comp_burgers_viscratio0pt1[:,1], color=colour_burgers_10, linewidth=lw, linestyle='-', label=r'Burgers ($\eta_1 / \eta_2 = 10$)')
ax[1].set_xlabel('Time (ka)', fontsize=fs_lab)
#ax[1].set_ylabel('Maximum vertical displacement (m)', fontsize=fs_lab)
ax[1].grid(True, linestyle='dotted')
ax[1].tick_params(axis='both', which='major', labelsize=fs)
ax[1].legend(loc='lower left', fontsize=fs-0.5, framealpha=1, facecolor='white', edgecolor='black', fancybox=False).get_frame().set_linewidth(lw)
ax[1].annotate(
        "b",
        xy=(0.425, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
ax[1].annotate(
        r"Long, 1D viscosity",
        xy=(0.5, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
#plt.show()
figname = "Figure_6_compressible_burgers_26.05.25"
fig.savefig(f'{figname}.png')

