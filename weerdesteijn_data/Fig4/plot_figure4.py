import matplotlib.pyplot as plt
import matplotlib
from matplotlib import colormaps
import numpy as np

folder = "./"
folder_gadopt = "./"

cmap = colormaps['Set1']
colours = cmap.colors
default_colour = colours[1]

# fonts and linewidths etc
fs = 9
fs_ticks_zoom = 7
fs_lab = 10
ms = 5
lw = 0.75
lw_zoom = 1

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

fig, ax = plt.subplots(2, 2, figsize=(8, 7), dpi=300, sharex='col', sharey='row', layout='constrained')
fig.get_layout_engine().set(w_pad=1 / 72, h_pad=1 / 72, hspace=1/144, wspace=1/144)
#plt.rcParams.update({'font.size': 30})

# Plot dx sensitivity
ax[0, 0].plot(gadopt_displacement_dx5[:,0]/1e3, gadopt_displacement_dx5[:,1], color=default_colour, linestyle='-', label='5 km', lw=lw)
ax[0, 0].plot(gadopt_displacement_dx10[:,0]/1e3, gadopt_displacement_dx10[:,1], color='k', linestyle='--',marker='x',markevery=10, label='10 km',alpha=0.5, lw=lw)
ax[0, 0].plot(gadopt_displacement_dx20[:,0]/1e3, gadopt_displacement_dx20[:,1], color='k', linestyle='--', marker='o', markevery=10, label='20 km',alpha=0.5, lw=lw)
#ax[0, 0].set_xlabel('Time (ka)', fontsize=fs_lab)
ax[0, 0].set_ylabel('Maximum vertical displacement (m)', fontsize=fs_lab)
ax[0, 0].grid(True, linestyle='dotted')
ax[0, 0].tick_params(axis='both', which='major', labelsize=fs)
ax[0, 0].xaxis.tick_top()
ax[0,0].legend(loc='upper left', bbox_to_anchor=(-0.005, 0.75), fontsize=fs, framealpha=1, facecolor='white', edgecolor='black', fancybox=False).get_frame().set_linewidth(lw)
ax[0, 0].set_ylim((-77, 5))  # sharing y axis so need to account for k/mu = 2
ax[0,0].annotate(
        "a",
        xy=(0.46, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
ax[0,0].annotate(
        r"Horizontal resolution",
        xy=(0.535, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
#ax[0, 0].annotate('a)', (-5, 6), fontsize='25', annotation_clip=False)
# Add inset
x1, x2, y1, y2 = 87, 93, -64.75, -62  # subregion of the original image
axins = ax[0,0].inset_axes(
    [0.14, 0.11, 0.325, 0.325],
    xlim=(x1, x2), ylim=(y1, y2)) #, xticklabels=[], yticklabels=[])
axins.plot(gadopt_displacement_dx5[:,0]/1e3, gadopt_displacement_dx5[:,1], color=default_colour, linestyle='-', label='dx = 5 km', lw=lw_zoom)
axins.plot(gadopt_displacement_dx10[:,0]/1e3, gadopt_displacement_dx10[:,1], color='k', linestyle='--',marker='x',markevery=10, label='dx = 10 km',alpha=0.5, lw=lw_zoom)
axins.plot(gadopt_displacement_dx20[:,0]/1e3, gadopt_displacement_dx20[:,1], color='k', linestyle='--', marker='o', markevery=10, label='dx = 20 km',alpha=0.5, lw=lw_zoom)

axins.grid(True, linestyle='dotted')
for pos in ['bottom', 'left']:
    axins.spines[pos].set_edgecolor('grey')
for pos in ['right', 'top']:
    axins.spines[pos].set_alpha(0)
axins.tick_params(axis='both', which='major', labelsize=fs_ticks_zoom, color='grey')
#ax[0,0].indicate_inset_zoom(axins, edgecolor="black", lw=lw, linestyle='dotted', alpha=0.5)
coords = ax[0,0].transAxes.inverted().transform(axins.get_tightbbox())
border = 0.02
w, h = coords[1] - coords[0] + 2*border
ax[0,0].add_patch(plt.Rectangle(coords[0]-border, w, h, lw=lw, linestyle='solid', ec='grey', fc="white",
                           transform=ax[0,0].transAxes, zorder=2))

w2 = x2-x1
h2 = y2-y1
ax[0,0].add_patch(plt.Rectangle((x1, y1), w2, h2, lw=lw, linestyle='dashed', ec='grey', fill=False))

# Plot nz sensitivity
ax[0, 1].plot(gadopt_displacement_nz10[:,0]/1e3, gadopt_displacement_nz10[:,1], color=default_colour, linestyle='-', label='40 cells', lw=lw)
ax[0, 1].plot(gadopt_displacement_nz5[:,0]/1e3, gadopt_displacement_nz5[:,1], color='k', linestyle='--',marker='x',markevery=10, label='20 cells',alpha=0.5, lw=lw)
ax[0, 1].plot(gadopt_displacement_nz2[:,0]/1e3, gadopt_displacement_nz2[:,1], color='k', linestyle='--', marker='o', markevery=10, label='8 cells',alpha=0.5, lw=lw)
ax[0, 1].plot(gadopt_displacement_nz1[:,0]/1e3, gadopt_displacement_nz1[:,1], color='k', linestyle='--', marker='^', markevery=10, label='4 cells',alpha=0.5, lw=lw)
#ax[0, 1].set_xlabel('Time (ka)', fontsize=fs_lab)
#ax[0, 1].set_ylabel('Maximum vertical displacement (m)', fontsize=fs_lab)
ax[0, 1].grid(True, linestyle='dotted')
ax[0, 1].tick_params(axis='both', which='major', labelsize=fs)
ax[0, 1].xaxis.tick_top()
ax[0, 1].yaxis.tick_right()
ax[0,1].legend(loc='upper left', bbox_to_anchor=(-0.005, 0.75), fontsize=fs, framealpha=1, facecolor='white', edgecolor='black', fancybox=False).get_frame().set_linewidth(lw)
ax[0,1].annotate(
        "b",
        xy=(0.51, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
ax[0,1].annotate(
        r"Vertical resolution",
        xy=(0.585, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
#ax[0, 1].annotate('b)', (-5, 6), fontsize='25', annotation_clip=False)
# Add inset
x1, x2, y1, y2 = 86, 94, -66, -58  # subregion of the original image
axins = ax[0,1].inset_axes(
    [0.14, 0.11, 0.325, 0.325],
    xlim=(x1, x2), ylim=(y1, y2)) #, xticklabels=[], yticklabels=[])
axins.plot(gadopt_displacement_nz10[:,0]/1e3, gadopt_displacement_nz10[:,1], color=default_colour, linestyle='-', label='10 cells per layer', lw=lw)
axins.plot(gadopt_displacement_nz5[:,0]/1e3, gadopt_displacement_nz5[:,1], color='k', linestyle='--',marker='x',markevery=10, label='5 cells per layer',alpha=0.5, lw=lw_zoom)
axins.plot(gadopt_displacement_nz2[:,0]/1e3, gadopt_displacement_nz2[:,1], color='k', linestyle='--', marker='o', markevery=10, label='2 cells per layer',alpha=0.5, lw=lw_zoom)
axins.plot(gadopt_displacement_nz1[:,0]/1e3, gadopt_displacement_nz1[:,1], color='k', linestyle='--', marker='^', markevery=10, label='1 cell per layer',alpha=0.5, lw=lw_zoom)

axins.grid(True, linestyle='dotted')
for pos in ['bottom', 'left']:
    axins.spines[pos].set_edgecolor('grey')
for pos in ['right', 'top']:
    axins.spines[pos].set_alpha(0)
axins.tick_params(axis='both', which='major', labelsize=fs_ticks_zoom, color='grey')
#ax[0,0].indicate_inset_zoom(axins, edgecolor="black", lw=lw, linestyle='dotted', alpha=0.5)
coords = ax[0,1].transAxes.inverted().transform(axins.get_tightbbox())
w, h = coords[1] - coords[0] + 2*border
ax[0,1].add_patch(plt.Rectangle(coords[0]-border, w, h, lw=lw, linestyle='solid', ec='grey', fc="white",
                           transform=ax[0,1].transAxes, zorder=2))

w2 = x2-x1
h2 = y2-y1
ax[0,1].add_patch(plt.Rectangle((x1, y1), w2, h2, lw=lw, linestyle='dashed', ec='grey', fill=False))

# Plot dt sensitivity
ax[1, 0].plot(gadopt_displacement_dt1000[:,0]/1e3, gadopt_displacement_dt1000[:,1], color=default_colour, linestyle='-', label='1 ka', lw=lw)
ax[1, 0].plot(gadopt_displacement_dt2000[:,0]/1e3, gadopt_displacement_dt2000[:,1], color='k', linestyle='--',marker='x',markevery=5, label='2 ka',alpha=0.5, lw=lw)
ax[1, 0].plot(gadopt_displacement_dt5000[:,0]/1e3, gadopt_displacement_dt5000[:,1], color='k', linestyle='--', marker='o', markevery=2, label=r'5 ka',alpha=0.5, lw=lw)
ax[1, 0].plot(gadopt_displacement_dt10000[:,0]/1e3, gadopt_displacement_dt10000[:,1], color='k', linestyle='--', marker='^', markevery=1, label='10 ka',alpha=0.5, lw=lw)
ax[1, 0].set_xlabel('Time (ka)', fontsize=fs_lab)
ax[1, 0].set_ylabel('Maximum vertical displacement (m)', fontsize=fs_lab)
ax[1, 0].grid(True, linestyle='dotted')
ax[1, 0].legend(loc='upper left', bbox_to_anchor=(-0.005, 0.75), fontsize=fs, framealpha=1, facecolor='white', edgecolor='black', fancybox=False).get_frame().set_linewidth(lw)
ax[1, 0].tick_params(axis='both', which='major', labelsize=fs)
ax[1,0].annotate(
        "c",
        xy=(0.55, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
ax[1,0].annotate(
        r"Timestep length",
        xy=(0.62, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
#ax[1, 0].annotate('c)', (-5, 6), fontsize='25', annotation_clip=False)
# Add inset
x1, x2, y1, y2 = 87, 93, -64.75, -62  # subregion of the original image
axins = ax[1,0].inset_axes(
    [0.14, 0.11, 0.325, 0.325],
    xlim=(x1, x2), ylim=(y1, y2)) #, xticklabels=[], yticklabels=[])
axins.plot(gadopt_displacement_dt1000[:,0]/1e3, gadopt_displacement_dt1000[:,1], color=default_colour, linestyle='-', label='dt = 1 ka', lw=lw)
axins.plot(gadopt_displacement_dt2000[:,0]/1e3, gadopt_displacement_dt2000[:,1], color='k', linestyle='--',marker='x',markevery=5, label='dt = 2 ka',alpha=0.5, lw=lw_zoom)
axins.plot(gadopt_displacement_dt5000[:,0]/1e3, gadopt_displacement_dt5000[:,1], color='k', linestyle='--', marker='o', markevery=2, label='dt = 5 ka',alpha=0.5, lw=lw_zoom)
axins.plot(gadopt_displacement_dt10000[:,0]/1e3, gadopt_displacement_dt10000[:,1], color='k', linestyle='--', marker='^', markevery=1, label='dt = 10 ka',alpha=0.5, lw=lw_zoom)

axins.grid(True, linestyle='dotted')
for pos in ['bottom', 'left']:
    axins.spines[pos].set_edgecolor('grey')
for pos in ['right', 'top']:
    axins.spines[pos].set_alpha(0)
axins.tick_params(axis='both', which='major', labelsize=fs_ticks_zoom, color='grey')
#ax[0,0].indicate_inset_zoom(axins, edgecolor="black", lw=lw, linestyle='dotted', alpha=0.5)
coords = ax[1,0].transAxes.inverted().transform(axins.get_tightbbox())
w, h = coords[1] - coords[0] + 2*border
ax[1,0].add_patch(plt.Rectangle(coords[0]-border, w, h, lw=lw, linestyle='solid', ec='grey', fc="white",
                           transform=ax[1,0].transAxes, zorder=2))

w2 = x2-x1
h2 = y2-y1
ax[1,0].add_patch(plt.Rectangle((x1, y1), w2, h2, lw=lw, linestyle='dashed', ec='grey', fill=False))

# Plot bulk
ax[1, 1].plot(gadopt_displacement_bulk2[:,0]/1e3, gadopt_displacement_bulk2[:,1], color='k', linestyle='--',marker='x',markevery=10, label='2',alpha=1, lw=lw)
ax[1, 1].plot(gadopt_displacement_bulk100[:,0]/1e3, gadopt_displacement_bulk100[:,1], color=default_colour, linestyle='-', label='100', lw=lw)
ax[1, 1].plot(gadopt_displacement_bulk1000[:,0]/1e3, gadopt_displacement_bulk1000[:,1], color='k', linestyle='--', marker='o', markevery=10, label='1000',alpha=0.5, lw=lw)
ax[1, 1].set_xlabel('Time (ka)', fontsize=fs_lab)
#ax[1, 1].set_ylabel('Maximum vertical displacement (m)', fontsize=fs_lab)
ax[1, 1].grid(True, linestyle='dotted')
ax[1, 1].tick_params(axis='both', which='major', labelsize=fs)
ax[1, 1].yaxis.tick_right()
ax[1, 1].set_ylim((-77, 5))  # sharing y axis so need to account for k/mu = 2
ax[1, 1].legend(loc='upper left', bbox_to_anchor=(-0.005, 0.75), fontsize=fs, framealpha=1, facecolor='white', edgecolor='black', fancybox=False).get_frame().set_linewidth(lw)
ax[1,1].annotate(
        "d",
        xy=(0.265, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
ax[1,1].annotate(
        r"Ratio of Bulk to Shear modulus",
        xy=(0.34, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
#ax[1, 1].annotate('d)', (-5, 7), fontsize='25', annotation_clip=False)
# Add inset
x1, x2, y1, y2 = 87, 93, -76, -62  # subregion of the original image
axins = ax[1,1].inset_axes(
    [0.14, 0.11, 0.3, 0.3],
    xlim=(x1, x2), ylim=(y1, y2)) #, xticklabels=[], yticklabels=[])
axins.plot(gadopt_displacement_bulk2[:,0]/1e3, gadopt_displacement_bulk2[:,1], color='k', linestyle='--',marker='x',markevery=10, label=r'$\kappa / \mu$ = 2',alpha=1, lw=lw_zoom)
axins.plot(gadopt_displacement_bulk100[:,0]/1e3, gadopt_displacement_bulk100[:,1], color=default_colour, linestyle='-', label=r'$\kappa / \mu$ = 100', lw=lw_zoom)
axins.plot(gadopt_displacement_bulk1000[:,0]/1e3, gadopt_displacement_bulk1000[:,1], color='k', linestyle='--', marker='o', markevery=10, label=r'$\kappa / \mu$ = 1000',alpha=0.5, lw=lw_zoom)

axins.grid(True, linestyle='dotted')
for pos in ['bottom', 'left']:
    axins.spines[pos].set_edgecolor('grey')
for pos in ['right', 'top']:
    axins.spines[pos].set_alpha(0)
axins.tick_params(axis='both', which='major', labelsize=fs_ticks_zoom, color='grey')
#ax[0,0].indicate_inset_zoom(axins, edgecolor="black", lw=lw, linestyle='dotted', alpha=0.5)
coords = ax[1,1].transAxes.inverted().transform(axins.get_tightbbox())
w, h = coords[1] - coords[0] + 2*border
ax[1,1].add_patch(plt.Rectangle(coords[0]-border, w, h, lw=lw, linestyle='solid', ec='grey', fc="white",
                           transform=ax[1,1].transAxes, zorder=2))

w2 = x2-x1
h2 = y2-y1
ax[1,1].add_patch(plt.Rectangle((x1, y1), w2, h2, lw=lw, linestyle='dashed', ec='grey', fill=False))


figname = "Figure_4_incompressible_weerdesteijn_long_res_22.05.25"
fig.savefig(f'{figname}.png')

