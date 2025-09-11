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

# Power law, n=3, transition stress 0.2MPa and 1 MPa.
long_power = "power_law/long/"
power_pt2_dt50 = np.loadtxt(f"{long_power}displacement-weerdesteijn-3d-internalvariable-power_n3_transstress0.2_snes_dt50_dev_thresh1e-16_lag_updm-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt50.0years-bulk1.94-compbuoyTrue-powerlawTrue-nondim.dat")
power_pt2_dt125 = np.loadtxt(f"{long_power}displacement-weerdesteijn-3d-internalvariable-power_n3_transstress0.2_snes_dt125_dev_thresh1e-16_lag_updm-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt125.0years-bulk1.94-compbuoyTrue-powerlawTrue-nondim.dat")
power_pt2_dt125_nz20 = np.loadtxt(f"{long_power}displacement-weerdesteijn-3d-internalvariable-power_n3_transstress0.2_snes_dt125_dev_thresh1e-16_lag_updm-refinedsurfaceTrue-dx5.0km-nz20perlayer-dt125.0years-bulk1.94-compbuoyTrue-powerlawTrue-nondim.dat")
power_pt2_dt250 = np.loadtxt(f"{long_power}displacement-weerdesteijn-3d-internalvariable-power_n3_transstress0.2_snes_dt250_dev_thresh1e-16_lag_updm-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt250.0years-bulk1.94-compbuoyTrue-powerlawTrue-nondim.dat")
power_pt2_dt500 = np.loadtxt(f"{long_power}displacement-weerdesteijn-3d-internalvariable-power_n3_transstress0.2_snes_dt500_dev_thresh1e-16_lag_updm-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt500.0years-bulk1.94-compbuoyTrue-powerlawTrue-nondim.dat")
power_pt2_dt1000 = np.loadtxt(f"{long_power}displacement-weerdesteijn-3d-internalvariable-power_n3_transstress0.2_snes_dt1000_dev_thresh1e-16_lag_updm-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk1.94-compbuoyTrue-powerlawTrue-nondim.dat")
power_pt2_dt2000 = np.loadtxt(f"{long_power}displacement-weerdesteijn-3d-internalvariable-power_n3_transstress0.2_snes_dt2000_dev_thresh1e-16_lag_updm-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt2000.0years-bulk1.94-compbuoyTrue-powerlawTrue-nondim.dat")

# power law coupled
power_pt2_dt125_coupled = np.loadtxt(f"{long_power}displacement-weerdesteijn-3d-internalvariable-power_n3_transstress0.2_dt125_coupled_scale1e6_fix-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt125.0years-bulk1.94-compbuoyTrue-nondim.dat")
power_pt2_dt250_coupled = np.loadtxt(f"{long_power}displacement-weerdesteijn-3d-internalvariable-power_n3_transstress0.2_dt250_coupled_scale1e6_fix-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt250.0years-bulk1.94-compbuoyTrue-nondim.dat")
power_pt2_dt500_coupled = np.loadtxt(f"{long_power}displacement-weerdesteijn-3d-internalvariable-power_n3_transstress0.2_dt500_coupled_scale1e6_fix-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt500.0years-bulk1.94-compbuoyTrue-nondim.dat")
power_pt2_dt1000_coupled = np.loadtxt(f"{long_power}displacement-weerdesteijn-3d-internalvariable-power_n3_transstress0.2_dt1000_coupled_scale1e6_fix-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk1.94-compbuoyTrue-nondim.dat")
power_pt2_dt2000_coupled = np.loadtxt(f"{long_power}displacement-weerdesteijn-3d-internalvariable-power_n3_transstress0.2_dt2000_coupled_scale1e6_fix-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt2000.0years-bulk1.94-compbuoyTrue-nondim.dat")

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
ax[0].plot(times_dt10, vr0pt5_nz10_dx5_dt10[:21], color=colour_burgers_2, linewidth=lw,linestyle='dashed', label=r'Burgers ($\eta_1 / \eta_2 = 2$)')
ax[0].plot(times_dt10, vr0pt1_nz10_dx5_dt10[:21], color=colour_burgers_10, linewidth=lw, linestyle='dashdot', label=r'Burgers ($\eta_1 / \eta_2 = 10$)')

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
# Plot short, 1D burgers
ax[0].set_xlabel('Time (yr)', fontsize=fs_lab)
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
ax[1].plot(comp_burgers_viscratio0pt5[:,0]/1e3, comp_burgers_viscratio0pt5[:,1], color=colour_burgers_2, linewidth=lw, linestyle='dashed', label=r'Burgers (comp., $\eta_1 / \eta_2 = 2$)')
ax[1].plot(comp_burgers_viscratio0pt1[:,0]/1e3, comp_burgers_viscratio0pt1[:,1], color=colour_burgers_10, linewidth=lw, linestyle='dashdot', label=r'Burgers (comp., $\eta_1 / \eta_2 = 10$)')

# long, power law
#ax[1].plot(power_pt2_dt50[:,0]/1e3, power_pt2_dt50[:,1], linewidth=lw, linestyle='--', label=r'power dt 50 yr')
#ax[1].plot(power_pt2_dt125_nz20[:,0]/1e3, power_pt2_dt125_nz20[:,1], linewidth=lw, linestyle='--', label=r'power dt 125 yr, nz =20')
#ax[1].plot(power_pt2_dt125[:,0]/1e3, power_pt2_dt125[:,1], linewidth=lw, linestyle='--', label=r'power dt 125 yr')
#ax[1].plot(power_pt2_dt250[:,0]/1e3, power_pt2_dt250[:,1], linewidth=lw, linestyle='--', label=r'power dt 250 yr')
#ax[1].plot(power_pt2_dt500[:,0]/1e3, power_pt2_dt500[:,1], linewidth=lw, linestyle='--', label=r'power dt 500 yr')
#ax[1].plot(power_pt2_dt1000[:,0]/1e3, power_pt2_dt1000[:,1], linewidth=lw, linestyle='--', label=r'power dt 1000 yr')
#ax[1].plot(power_pt2_dt2000[:,0]/1e3, power_pt2_dt2000[:,1], linewidth=lw, linestyle='--', label=r'power dt 2000 yr')

#long power law coupled
#ax[1].plot(power_pt2_dt125_coupled[:,0]/1e3, power_pt2_dt125_coupled[:,1], linewidth=lw, linestyle=':', label=r'power dt 125 yr, coupled')
#ax[1].plot(power_pt2_dt250_coupled[:,0]/1e3, power_pt2_dt250_coupled[:,1], linewidth=lw, linestyle=':', label=r'power dt 250 yr, coupled')
#ax[1].plot(power_pt2_dt500_coupled[:,0]/1e3, power_pt2_dt500_coupled[:,1], linewidth=lw, linestyle=':', label=r'power dt 500 yr, coupled')
#ax[1].plot(power_pt2_dt1000_coupled[:,0]/1e3, power_pt2_dt1000_coupled[:,1], linewidth=lw, linestyle=':', label=r'power dt 1000 yr, coupled')
#ax[1].plot(power_pt2_dt2000_coupled[:,0]/1e3, power_pt2_dt2000_coupled[:,1], linewidth=lw, linestyle=':', label=r'power dt 2000 yr, coupled')

ax[1].set_xlabel('Time (kyr)', fontsize=fs_lab)
#ax[1].set_ylabel('Maximum vertical displacement (m)', fontsize=fs_lab)
ax[1].grid(True, linestyle='dotted')
ax[1].tick_params(axis='both', which='major', labelsize=fs)
ax[1].legend(loc='lower left', fontsize=fs-0.75, framealpha=1, facecolor='white', edgecolor='black', fancybox=False).get_frame().set_linewidth(lw)
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
figname = "Figure_5_compressible_burgers_11.09.25_linestyle"
fig.savefig(f'{figname}.png')

