import matplotlib.pyplot as plt
import matplotlib
from matplotlib import colormaps
import numpy as np

folder = "./"
folder_gadopt = "./"

cmap = colormaps['Set1']
colours = cmap.colors
gadopt_colour = colours[1]
abaqus_colour = colours[2]
aspect_colour = colours[3]
taboo_colour = colours[4]

# fonts and linewidths etc
fs = 9
fs_ticks_zoom = 7
fs_lab = 10
ms = 5
lw = 0.75
lw_zoom = 1

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


fig, ax = plt.subplots(2, 2, figsize=(8, 7), dpi=300, sharex='col', layout='constrained')
fig.get_layout_engine().set(w_pad=4 / 72, h_pad=1 / 72, hspace=1/144,
                            wspace=0)
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
# Plot short, 1D
ax[0, 0].plot(abaqus_displacement_short[:,0],abaqus_displacement_short[:,1], color=abaqus_colour, linestyle='dotted', label='Abaqus', lw=lw)
ax[0, 0].plot(aspect_displacement_short[:,0],aspect_displacement_short[:,1], color=aspect_colour, linestyle='dashdot', label='Aspect', lw=lw)
ax[0, 0].plot(taboo_displacement_short[:,0],taboo_displacement_short[:,1], color=taboo_colour, linestyle='dashed', label='Taboo', lw=lw)
ax[0, 0].plot(gadopt_displacement_short[:,0], gadopt_displacement_short[:,1], color=gadopt_colour, label='G-ADOPT', lw=lw)
#ax[0, 0].set_xlabel('Time (a)', fontsize=fs_lab)
ax[0, 0].set_ylabel('Maximum vertical displacement (m)', fontsize=fs_lab)
ax[0, 0].grid(True, linestyle='dotted')
ax[0, 0].tick_params(axis='both', which='major', labelsize=fs)
ax[0, 0].xaxis.tick_top()
ax[0,0].legend(fontsize=fs_lab, framealpha=1, facecolor='white', edgecolor='black', fancybox=False).get_frame().set_linewidth(lw)
ax[0,0].annotate(
        "a",
        xy=(0.43, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
ax[0,0].annotate(
        "Short, 1D viscosity",
        xy=(0.515, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))

# Add inset
x1, x2, y1, y2 = 95, 105, -0.67, -0.61  # subregion of the original image
axins = ax[0,0].inset_axes(
    [0.575, 0.45, 0.34, 0.355],
    xlim=(x1, x2), ylim=(y1, y2),) #yticklabels=[])

axins.plot(abaqus_displacement_short[:,0],abaqus_displacement_short[:,1], color=abaqus_colour, linestyle='dotted', label='Abaqus', lw=lw_zoom)
axins.plot(aspect_displacement_short[:,0],aspect_displacement_short[:,1], color=aspect_colour, linestyle='dashdot', label='Aspect', lw=lw_zoom)
axins.plot(taboo_displacement_short[:,0],taboo_displacement_short[:,1], color=taboo_colour, linestyle='dashed', label='Taboo', lw=lw_zoom)
axins.plot(gadopt_displacement_short[:,0], gadopt_displacement_short[:,1], color=gadopt_colour, label='G-ADOPT', lw=lw_zoom)
axins.grid(True, linestyle='dotted')
for pos in ['bottom', 'left']:
    axins.spines[pos].set_edgecolor('grey')
for pos in ['right', 'top']:
    axins.spines[pos].set_alpha(0)
axins.tick_params(axis='both', which='major', labelsize=fs_ticks_zoom, color='grey')
#ax[0,0].indicate_inset_zoom(axins, edgecolor="black", lw=lw, linestyle='dotted', alpha=0.5)
coords = ax[0,0].transAxes.inverted().transform(axins.get_tightbbox())
border = 0.005
w, h = coords[1] - coords[0] + 2*border
ax[0,0].add_patch(plt.Rectangle(coords[0]-border, w, h, lw=lw, linestyle='solid', ec='grey', fc="white",
                           transform=ax[0,0].transAxes, zorder=2))

w2 = x2-x1
h2 = y2-y1
ax[0,0].add_patch(plt.Rectangle((x1, y1), w2, h2, lw=lw, linestyle='dashed', ec='grey', fill=False))


# Plot long, 1D
ax[0, 1].plot(abaqus_displacement_long[:,0],abaqus_displacement_long[:,1], color=abaqus_colour,linestyle='dotted', label='Abaqus', lw=lw)
ax[0, 1].plot(aspect_displacement_long[:,0]/1e3,aspect_displacement_long[:,1], color=aspect_colour, linestyle='dashdot', label='Aspect', lw=lw)
ax[0, 1].plot(taboo_displacement_long[:,0],taboo_displacement_long[:,1], color=taboo_colour, linestyle='dashed', label='Taboo', lw=lw)
ax[0, 1].plot(gadopt_displacement[:,0]/1e3, gadopt_displacement[:,1], color=gadopt_colour, label='G-ADOPT', lw=lw)
#ax[0, 1].set_xlabel('Time (ka)', fontsize=fs_lab)
#ax[0, 1].set_ylabel('Maximum vertical displacement (m)', fontsize=fs_lab)
ax[0, 1].grid(True, linestyle='dotted')
ax[0, 1].tick_params(axis='both', which='major', labelsize=fs)
ax[0, 1].xaxis.tick_top()
#ax[0, 1].legend(fontsize)
ax[0,1].annotate(
        "b",
        xy=(0.44, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
ax[0,1].annotate(
        "Long, 1D viscosity",
        xy=(0.525, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))


# Add inset
x1, x2, y1, y2 = 86, 94, -65, -57  # subregion of the original image
axins = ax[0,1].inset_axes(
    [0.14, 0.11, 0.325, 0.325],
    xlim=(x1, x2), ylim=(y1, y2)) #, xticklabels=[], yticklabels=[])
axins.plot(abaqus_displacement_long[:,0],abaqus_displacement_long[:,1], color=abaqus_colour, linestyle='dotted', label='Abaqus', lw=lw_zoom)
axins.plot(aspect_displacement_long[:,0]/1e3,aspect_displacement_long[:,1], color=aspect_colour, linestyle='dashdot', label='Aspect', lw=lw_zoom)
axins.plot(taboo_displacement_long[:,0],taboo_displacement_long[:,1], color=taboo_colour, linestyle='dashed', label='Taboo', lw=lw_zoom)
axins.plot(gadopt_displacement[:,0]/1e3, gadopt_displacement[:,1], color=gadopt_colour, label='G-ADOPT', lw=lw_zoom)

axins.grid(True, linestyle='dotted')
for pos in ['bottom', 'left']:
    axins.spines[pos].set_edgecolor('grey')
for pos in ['right', 'top']:
    axins.spines[pos].set_alpha(0)
axins.tick_params(axis='both', which='major', labelsize=fs_ticks_zoom, color='grey')
#ax[0,0].indicate_inset_zoom(axins, edgecolor="black", lw=lw, linestyle='dotted', alpha=0.5)
coords = ax[0,1].transAxes.inverted().transform(axins.get_tightbbox())
border = 0.005
w, h = coords[1] - coords[0] + 2*border
ax[0,1].add_patch(plt.Rectangle(coords[0]-border, w, h, lw=lw, linestyle='solid', ec='grey', fc="white",
                           transform=ax[0,1].transAxes, zorder=2))

w2 = x2-x1
h2 = y2-y1
ax[0,1].add_patch(plt.Rectangle((x1, y1), w2, h2, lw=lw, linestyle='dashed', ec='grey', fill=False))


# plot short low visc
ax[1, 0].plot(abaqus_displacement_short_lowvisc[:,0],abaqus_displacement_short_lowvisc[:,1], color=abaqus_colour, linestyle='dotted', label='Abaqus', lw=lw)
ax[1, 0].plot(aspect_displacement_short_lowvisc[:,0],aspect_displacement_short_lowvisc[:,1], color=aspect_colour, linestyle='dashdot', label='Aspect', lw=lw)
ax[1, 0].plot(gadopt_displacement_short_lowvisc[:,0], gadopt_displacement_short_lowvisc[:,1], color=gadopt_colour, label='G-ADOPT', lw=lw)
ax[1, 0].set_xlabel('Time (a)', fontsize=fs_lab)
ax[1, 0].set_ylabel('Maximum vertical displacement (m)', fontsize=fs_lab)
ax[1, 0].grid(True, linestyle='dotted')
ax[1, 0].tick_params(axis='both', which='major', labelsize=fs)
#ax[1, 0].legend(fontsize=fs_lab)
#ax[1, 0].annotate('c)', (-9.1, 0.12), fontsize=fs_lab, annotation_clip=False)
ax[1,0].annotate(
        "c",
        xy=(0.43, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
ax[1,0].annotate(
        "Short, 3D viscosity",
        xy=(0.515, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))

# Add inset
x1, x2, y1, y2 = 95, 105, -1.08, -0.935  # subregion of the original image
axins = ax[1,0].inset_axes(
    [0.575, 0.45, 0.34, 0.355],
    xlim=(x1, x2), ylim=(y1, y2)) #, xticklabels=[], yticklabels=[])

axins.plot(abaqus_displacement_short_lowvisc[:,0],abaqus_displacement_short_lowvisc[:,1], color=abaqus_colour, linestyle='dotted', label='Abaqus', lw=lw_zoom)
axins.plot(aspect_displacement_short_lowvisc[:,0],aspect_displacement_short_lowvisc[:,1], color=aspect_colour, linestyle='dashdot', label='Aspect', lw=lw_zoom)
axins.plot(gadopt_displacement_short_lowvisc[:,0], gadopt_displacement_short_lowvisc[:,1], color=gadopt_colour, label='G-ADOPT', lw=lw_zoom)
axins.grid(True, linestyle='dotted')
for pos in ['bottom', 'left']:
    axins.spines[pos].set_edgecolor('grey')
for pos in ['right', 'top']:
    axins.spines[pos].set_alpha(0)
axins.tick_params(axis='both', which='major', labelsize=fs_ticks_zoom, color='grey')
#ax[0,0].indicate_inset_zoom(axins, edgecolor="black", lw=lw, linestyle='dotted', alpha=0.5)
coords = ax[1,0].transAxes.inverted().transform(axins.get_tightbbox())
border = 0.005
w, h = coords[1] - coords[0] + 2*border
ax[1,0].add_patch(plt.Rectangle(coords[0]-border, w, h, lw=lw, linestyle='solid', ec='grey', fc="white",
                           transform=ax[1,0].transAxes, zorder=2))

w2 = x2-x1
h2 = y2-y1
ax[1,0].add_patch(plt.Rectangle((x1, y1), w2, h2, lw=lw, linestyle='dashed', ec='grey', fill=False))

# Plot long, 3d
ax[1, 1].plot(gadopt_displacement_long_lowvisc_nz5[:,0]/1e3, gadopt_displacement_long_lowvisc_nz5[:,1], color=gadopt_colour, label='G-ADOPT', lw=lw)
ax[1, 1].set_xlabel('Time (ka)', fontsize=fs_lab)
#ax[1, 1].set_ylabel('Maximum vertical displacement (m)', fontsize=fs_lab)
ax[1, 1].grid(True, linestyle='dotted')
ax[1, 1].tick_params(axis='both', which='major', labelsize=fs)
#ax[1, 1].annotate('d)', (-5, 6), fontsize=fs_lab, annotation_clip=False)
ax[1,1].annotate(
        "d",
        xy=(0.44, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))
ax[1,1].annotate(
        "Long, 3D viscosity",
        xy=(0.525, 1), xycoords='axes fraction',
        xytext=(1, -1), textcoords='offset fontsize',
        fontsize=fs_lab, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', lw=lw, pad=5))

# Add inset
x1, x2, y1, y2 = 86, 94, -65, -57  # subregion of the original image
axins = ax[1,1].inset_axes(
    [0.14, 0.11, 0.325, 0.325],
    xlim=(x1, x2), ylim=(y1, y2)) #, xticklabels=[], yticklabels=[])
axins.plot(gadopt_displacement_long_lowvisc_nz5[:,0]/1e3, gadopt_displacement_long_lowvisc_nz5[:,1], color=gadopt_colour, label='G-ADOPT', lw=lw_zoom)

axins.grid(True, linestyle='dotted')
for pos in ['bottom', 'left']:
    axins.spines[pos].set_edgecolor('grey')
for pos in ['right', 'top']:
    axins.spines[pos].set_alpha(0)
axins.tick_params(axis='both', which='major', labelsize=fs_ticks_zoom, color='grey')
#ax[0,0].indicate_inset_zoom(axins, edgecolor="black", lw=lw, linestyle='dotted', alpha=0.5)
coords = ax[1,1].transAxes.inverted().transform(axins.get_tightbbox())
border = 0.01
w, h = coords[1] - coords[0] + 2*border
ax[1,1].add_patch(plt.Rectangle(coords[0]-border, w, h, lw=lw, linestyle='solid', ec='grey', fc="white",
                           transform=ax[1,1].transAxes, zorder=2))

w2 = x2-x1
h2 = y2-y1
ax[1,1].add_patch(plt.Rectangle((x1, y1), w2, h2, lw=lw, linestyle='dashed', ec='grey', fill=False))

figname = "Figure_3_incompressible_weerdesteijn_21.05.25"
fig.savefig(f'{figname}.png')

