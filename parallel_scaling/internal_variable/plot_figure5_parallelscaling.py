import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


weak_structured = np.loadtxt("structured_weak_scaling.dat", delimiter=',')
strong_structured = np.loadtxt("structured_strong_scaling.dat", delimiter=',')

weak_unstructured = np.loadtxt("unstructured_weak_scaling.dat", delimiter=',')
strong_unstructured = np.loadtxt("unstructured_strong_scaling.dat", delimiter=',')

fig, ax = plt.subplots(1, 2, figsize=(7,3), dpi=300)





lw = 0.8
ax[0].semilogx(weak_structured[:, 0], weak_structured[:, -1]/20,  color='orange', linestyle="", marker='o', label=r'Isotropic structured mesh')
ax[0].semilogx(weak_unstructured[:, 0], weak_unstructured[:, -1]/20, color='blue', linestyle="", marker='x', label=r'Anisotropic unstructured mesh')

fs = 6
fs_lab = 7
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
# Plot weak scaling
ax[0].set_xlabel('No. of CPUs', fontsize=fs_lab)
ax[0].set_ylabel('Solve time per timestep (s)', fontsize=fs_lab)
ax[0].set_xlim((50,10000))
ax[0].set_ylim((0,220))
ax[0].grid(True, axis='y', linestyle='dotted', linewidth=1)
ax[0].tick_params(axis='both', which='major', labelsize=fs)
ax[0].legend(fontsize=fs)
ax[0].annotate('a)', (50, 230), fontsize=fs_lab, annotation_clip=False)


# Calculate total simulation time. therefore perfect scaling should be flat.
total_cpu_time_structured = strong_structured[:, -1]*strong_structured[:, 0]
total_cpu_time_structured_norm = total_cpu_time_structured / total_cpu_time_structured[-1]

total_cpu_time_unstructured = strong_unstructured[:, -1]*strong_unstructured[:, 0]
total_cpu_time_unstructured_norm = total_cpu_time_unstructured / total_cpu_time_unstructured[-1]

# Plot strong scaling
ax[1].semilogx(strong_structured[:, 0], total_cpu_time_structured_norm, color='orange', linestyle="", marker='o', label=r'Isotropic structured mesh')
ax[1].semilogx(strong_unstructured[:, 0], total_cpu_time_unstructured_norm, color='blue', linestyle="", marker='x', label=r'Anisotropic unstructured mesh')
ax[1].set_xlabel('No. of CPUs', fontsize=fs_lab)
ax[1].set_ylabel('Normalised total CPU time', fontsize=fs_lab)
ax[1].set_xlim((500,10000))
ax[1].set_ylim((0,1.05))
ax[1].yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax[1].grid(True, axis='y', which='both', linestyle='dotted', linewidth=1)
ax[1].tick_params(axis='both', which='both', labelsize=fs)
ax[1].annotate('b)', (500, 1.1), fontsize=fs_lab, annotation_clip=False)

figname = "Figure_5_parallelscaling_12.05.25"
fig.savefig(f'{figname}.png')

