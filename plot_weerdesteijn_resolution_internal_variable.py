import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# resolution/dt testing 14.03.24 on gadi
folder = "./weerdesteijn_data/"
folder_gadopt = "./weerdesteijn_data/internal_variable/nondimensional/"

# Aspect displacement taken from log file in supplementary information from Weerdesteijn et al 2023
aspect_displacement_long = np.loadtxt(folder+"aspect_fig_4b_file.csv", delimiter=',')
# abaqus and taboo data picked from Figure 4b Weerdesteijn et al 2023 using WebPlotDigitizer
abaqus_displacement_long = np.loadtxt(folder+"abaqus_picks_fig4b.csv", delimiter=',')
taboo_displacement_long = np.loadtxt(folder+"taboo_picks_fig4b.csv", delimiter=',')

# Indexes for time = 90 ka (Maximum load)
abaqus_taboo_index = 45
aspect_index = 1800
disp_abaqus = abaqus_displacement_long[abaqus_taboo_index, 1]
disp_taboo = taboo_displacement_long[abaqus_taboo_index, 1]
disp_aspect = aspect_displacement_long[aspect_index, 1]

# Hack to redefine xticks for horiztonal resolution plots to include structured and unstructured resolution 
all_horizontal_res = [5, 10, 12.5, 20, 25, 50]

# Dictionary containing information about resolution/timestep sensitivity experiments
    # resolution - list of grid or timestep resolution (in m or years) for each experiment
    # dt - list of timestep in years for each simulation
    # files - filepaths of experiments
    # matplotlib arguments - axes (which axes to plot on), xlabel,ylabel, marker, legend (label for legend), 
    # default index - specify which experiment was the default (i.e. horizontally unstructured 5 km, 80 layers, dt = 50 a

experiments = {
        'refined_dx': {
            'resolution': [5, 10, 20],
            'dt': [1000, 1000, 1000],
            'files': ["displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk100.0-nondim.dat",
                "displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk100.0-nondim.dat",
                "displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx10.0km-nz10perlayer-dt1000.0years-bulk100.0-nondim.dat",
                "displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx20.0km-nz10perlayer-dt1000.0years-bulk100.0-nondim.dat",
                ],
            'axes': [0,0],
            'x_label': 'Horizontal resolution (km)',
            'y_label': 'Peak displacement at 90 ka (m)',
            'y_lims': [-66, -58],
            'marker': 'x',
            'legend': 'G-ADOPT: unstructured horizontal',
            'default_index': 0
            },
        'structured_dx': {
            'resolution': [12.5, 25, 50],
            'dt': [1000, 1000, 1000],
            'files': ["displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceFalse-dx12.5km-nz10perlayer-dt1000.0years-bulk100.0-nondim.dat",
                      "displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceFalse-dx25.0km-nz10perlayer-dt1000.0years-bulk100.0-nondim.dat",
                      "displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceFalse-dx50.0km-nz10perlayer-dt1000.0years-bulk100.0-nondim.dat",
                ],
            'axes': [0,0],
            'x_label': 'Horizontal resolution (km)',
            'y_label': 'Peak displacement at 90 ka (m)',
            'y_lims': [-66, -58],
            'marker': 'o',
            'legend': 'G-ADOPT: structured horizontal'
            },
        'nz': {
            'resolution': [10, 5, 2, 1],
            'dt': [1000, 1000, 1000, 1000],
            'files': ["displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk100.0-nondim.dat",
                      "displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz5perlayer-dt1000.0years-bulk100.0-nondim.dat",
                      "displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz2perlayer-dt1000.0years-bulk100.0-nondim.dat",
                      "displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz1perlayer-dt1000.0years-bulk100.0-nondim.dat",
                ],
            'axes': [0,1],
            'x_label': 'Number of vertical cells per layer',
            'y_label': 'Peak displacement at 90 ka (m)',
            'y_lims': [-66, -58],
            'marker': 'x',
            'legend': 'G-ADOPT',
            'default_index': 0
            },
        'dt': {
            'resolution': [1000, 2000, 5000, 10000],
            'dt': [1000, 2000, 5000, 10000],
            'files': ["displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk100.0-nondim.dat",
                "displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt2000.0years-bulk100.0-nondim.dat",
                "displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt5000.0years-bulk100.0-nondim.dat",
                "displacement-weerdesteijn-3d-internalvariable-symmult-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt10000.0years-bulk10000000000000.0.dat", # forgot to run nondimension for dt = 10ka. this is dimensional but should be identical...!
                ],
            'axes': [1,0],
            'x_label': 'Timestep (a)',
            'y_label': 'Peak displacement at 90 ka (m)',
            'y_lims': [-66, -58],
            'marker': 'x',
            'legend': 'G-ADOPT',
            'default_index': 0
            },
        'compressibility': {
            'resolution': [2, 100, 1000],
            'dt': [1000, 1000, 1000],
            'files': ["displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk2.0-nondim.dat",
                "displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk100.0-nondim.dat",
                "displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk1000.0-nondim.dat"
               ],
            'axes': [1,1],
            'x_label': 'Ratio of Bulk / Shear modulus',
            'y_label': 'Peak displacement at 90 ka (m)',
            'y_lims': [-80, -58],
            'marker': 'x',
            'legend': 'G-ADOPT',
            'default_index': 1
            },
        }


def get_plot_data(plot_data):
    # helper function to get peak displacement for set of sensitivity experiments
    res = plot_data['resolution']
    files = plot_data['files']
    dts = plot_data['dt']
    disp = []
    # loop over sensitivity tests
    for dt, f in zip(dts, files):
        disp_array = np.loadtxt(folder_gadopt+f)

        timestep = round(90e3 / dt)  # this is time 90000 years
        disp.append(disp_array[timestep, 1])
    return res, disp

# Weerdesteijn resolution/timestep sensitivity figure
fig, axs = plt.subplots(2, 2, figsize=(20, 15))

for key, plot_data in experiments.items():
    # get correct axes
    ax_row, ax_col = plot_data['axes']
    axes = axs[ax_row, ax_col]
    
    # get grid resolution/timestep and corresponding peak displacement at 90 ka
    res, disp = get_plot_data(plot_data)

    # plot peak displacement sensitivity experiments
    label = plot_data['legend']
    marker = plot_data['marker']
    axes.scatter(res, disp, s=75, marker=marker, color='k', label=label)

    # highlight default simulation by overplotting with different colour
    if 'default_index' in plot_data:
        index = plot_data['default_index']
        axes.scatter(res[index], disp[index], s=200, marker=marker, color='b')

    # Set axis labels and limits
    x_label = plot_data['x_label']
    y_label = plot_data['y_label']
    fs = 18
    axes.set_xlabel(x_label, fontsize=fs)
    axes.set_ylabel(y_label, fontsize=fs)
    y_lims = plot_data['y_lims']
    axes.set_ylim(y_lims)
    
    # Change tick label text size
    axes.tick_params(axis='both', which='major', labelsize=16)
    # Change xaxis to log base 2 because we refine by a factor of 2
    axes.set_xscale('log', base=2)
    # Change output from 2^x back to usual numbers
    axes.xaxis.set_major_formatter(ScalarFormatter())
    
    # Change xaxis ticks to actual resolution/timestep used for experiment (bit hacky)
    if plot_data['axes'] == [0,0]:
        res = all_horizontal_res  # Hack to reset horizontal res to include structured and unstructured tests
    axes.xaxis.set_ticks(res)
    
    # Add abaqus, aspect and taboo values from Weerdesteijn et al 2023
    if key == 'refined_dx':
        # Going to add weerdesteijn reference values later when plottig structured_dx
        pass
    else:
        axes.plot([res[0], res[-1]],[disp_abaqus, disp_abaqus], color='k', linestyle='dotted', label='Abaqus')
        axes.plot([res[0], res[-1]],[disp_aspect, disp_aspect], color='k', linestyle='dashed', label='Aspect')
        axes.plot([res[0], res[-1]],[disp_taboo, disp_taboo], color='k', linestyle='dashdot', label='Taboo')
    
    axes.legend(fontsize=fs)

plt.savefig('25.03.24_weerdesteijn_grid_dt_sensitivity_peakdisplacement_internal_variable_nondim.png')


experiments_bulk2x = {
        'refined_dx': {
            'resolution': [5, 10, 20],
            'dt': [1000, 1000, 1000],
            'files': ["displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk2.0-nondim.dat",
                "displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk2.0-nondim.dat",
                "displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx10.0km-nz10perlayer-dt1000.0years-bulk2.0-nondim.dat",
                "displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx20.0km-nz10perlayer-dt1000.0years-bulk2.0-nondim.dat",
                ],
            'axes': [0,0],
            'x_label': 'Horizontal resolution (km)',
            'y_label': 'Peak displacement at 90 ka (m)',
            'y_lims': [-80, -58],
            'marker': 'x',
            'legend': 'G-ADOPT: unstructured horizontal',
            'default_index': 0
            },
#        'structured_dx': {
#            'resolution': [12.5, 25, 50],
#            'dt': [1000, 1000, 1000],
#            'files': ["displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceFalse-dx12.5km-nz10perlayer-dt1000.0years-bulk2.0-nondim.dat",
#                      "displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceFalse-dx25.0km-nz10perlayer-dt1000.0years-bulk2.0-nondim.dat",
#                      "displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceFalse-dx50.0km-nz10perlayer-dt1000.0years-bulk2.0-nondim.dat",
#                ],
#            'axes': [0,0],
#            'x_label': 'Horizontal resolution (km)',
#            'y_label': 'Peak displacement at 90 ka (m)',
#            'y_lims': [-66, -58],
#            'marker': 'o',
#            'legend': 'G-ADOPT: structured horizontal'
#            },
        'nz': {
            'resolution': [10, 5, 2, 1],
            'dt': [1000, 1000, 1000, 1000],
            'files': ["displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk2.0-nondim.dat",
                      "displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz5perlayer-dt1000.0years-bulk2.0-nondim.dat",
                      "displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz2perlayer-dt1000.0years-bulk2.0-nondim.dat",
                      "displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz1perlayer-dt1000.0years-bulk2.0-nondim.dat",
                ],
            'axes': [0,1],
            'x_label': 'Number of vertical cells per layer',
            'y_label': 'Peak displacement at 90 ka (m)',
            'y_lims': [-80, -58],
            'marker': 'x',
            'legend': 'G-ADOPT',
            'default_index': 0
            },
        'dt': {
            'resolution': [1000, 2000, 5000, 10000],
            'dt': [1000, 2000, 5000, 10000],
            'files': ["displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt1000.0years-bulk2.0-nondim.dat",
                "displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt2000.0years-bulk2.0-nondim.dat",
                "displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt5000.0years-bulk2.0-nondim.dat",
                "displacement-weerdesteijn-3d-internalvariable-symmult_nondim-refinedsurfaceTrue-dx5.0km-nz10perlayer-dt10000.0years-bulk2.0-nondim.dat",
                ],
            'axes': [1,0],
            'x_label': 'Timestep (a)',
            'y_label': 'Peak displacement at 90 ka (m)',
            'y_lims': [-80, -58],
            'marker': 'x',
            'legend': 'G-ADOPT',
            'default_index': 0
            },
        }

# Weerdesteijn resolution/timestep sensitivity figure
fig, axs = plt.subplots(2, 2, figsize=(20, 15))

for key, plot_data in experiments_bulk2x.items():
    # get correct axes
    ax_row, ax_col = plot_data['axes']
    axes = axs[ax_row, ax_col]
    
    # get grid resolution/timestep and corresponding peak displacement at 90 ka
    res, disp = get_plot_data(plot_data)

    # plot peak displacement sensitivity experiments
    label = plot_data['legend']
    marker = plot_data['marker']
    axes.scatter(res, disp, s=75, marker=marker, color='k', label=label)

    # highlight default simulation by overplotting with different colour
    if 'default_index' in plot_data:
        index = plot_data['default_index']
        axes.scatter(res[index], disp[index], s=200, marker=marker, color='b')

    # Set axis labels and limits
    x_label = plot_data['x_label']
    y_label = plot_data['y_label']
    fs = 18
    axes.set_xlabel(x_label, fontsize=fs)
    axes.set_ylabel(y_label, fontsize=fs)
    y_lims = plot_data['y_lims']
    axes.set_ylim(y_lims)
    
    # Change tick label text size
    axes.tick_params(axis='both', which='major', labelsize=16)
    # Change xaxis to log base 2 because we refine by a factor of 2
    axes.set_xscale('log', base=2)
    # Change output from 2^x back to usual numbers
    axes.xaxis.set_major_formatter(ScalarFormatter())
    
    # Change xaxis ticks to actual resolution/timestep used for experiment (bit hacky)
    if plot_data['axes'] == [0,0]:
        res = all_horizontal_res  # Hack to reset horizontal res to include structured and unstructured tests
    axes.xaxis.set_ticks(res)
    
#    # Add abaqus, aspect and taboo values from Weerdesteijn et al 2023
#    if key == 'refined_dx':
#        # Going to add weerdesteijn reference values later when plottig structured_dx
#        pass
#    else:
#        axes.plot([res[0], res[-1]],[disp_abaqus, disp_abaqus], color='k', linestyle='dotted', label='Abaqus')
#        axes.plot([res[0], res[-1]],[disp_aspect, disp_aspect], color='k', linestyle='dashed', label='Aspect')
#        axes.plot([res[0], res[-1]],[disp_taboo, disp_taboo], color='k', linestyle='dashdot', label='Taboo')
    
    axes.legend(fontsize=fs)

plt.savefig('25.03.24_weerdesteijn_grid_dt_sensitivity_peakdisplacement_internal_variable_nondim_bulk2x.png')
