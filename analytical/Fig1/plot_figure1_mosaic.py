import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
folder = "./"


# a) analytical solutions comp/incomp across top
# b) and c) zoomed elastic panel next to viscoelastic panel showing timesteps
# d) and e) L2 elastic and viscoelastic errors
fig, axd = plt.subplot_mosaic(
            [["a", "a"],
             ["b", "c"],
             ["d", "e"],],
            figsize=(24,24))

# timestepping
rho0 = 4500  # density in kg/m^3
g = 10  # gravitational acceleration in m/s^2
viscosity = 1e21  # Viscosity Pa s
shear_modulus = 1e11  # Shear modulus in Pa
maxwell_time = viscosity / shear_modulus  # Maxwell time in s. This is nondimensional timescale.
bulk_modulus = 2e11
D = 3e6
lam_factor = 8
# Set up surface load
kk_dim = 2 * np.pi / (D/lam_factor)  # wavenumber in m^-1
F0 = 1000  # initial free surface amplitude in m

# Timestepping parameters
tau0 = 2 * kk_dim * viscosity / (rho0 * g)   # viscous relaxation time


bulk_shear_ratio = bulk_modulus/shear_modulus
lambda_lame = bulk_modulus - 2/3 * shear_modulus
f_e = (lambda_lame + 2*shear_modulus) / (lambda_lame + shear_modulus)

eta_analytical = [0.]
eta_analytical_incomp = [0.]
times = [0.]

dt = 0.0001
max_timesteps = round(160/dt)
for i in range(1, max_timesteps):
    time = dt * i * maxwell_time
    times.append(time)
    eta_analytical.append(F0 * (1 - 1 / (1 + f_e*maxwell_time/tau0) + (1-np.exp(-(time)/(tau0+f_e*maxwell_time)))/ (1 + f_e*maxwell_time/tau0)))
    eta_analytical_incomp.append(F0 * (1 - 1 / (1 + maxwell_time/tau0) + (1-np.exp(-(time)/(tau0+maxwell_time)))/ (1 + maxwell_time/tau0)))
    
times = np.array(times)

# Plot analytical solution for 1a and 1b
axd["a"].plot(times/maxwell_time, eta_analytical, color='orange', linestyle='solid', label='Compressible')
axd["a"].plot(times/maxwell_time, eta_analytical_incomp, color='b', linestyle='solid', label='Incompressible')
axd["b"].plot(times/maxwell_time, eta_analytical, color='orange', linestyle='solid', label='Analytical (compressible)')
axd["b"].plot(times/maxwell_time, eta_analytical_incomp, color='b', linestyle='solid', label='Analytical (incompressible)')
axd["c"].plot(times/maxwell_time, eta_analytical, color='orange', linestyle='solid', label='Analytical (compressible)')
axd["c"].plot(times/maxwell_time, eta_analytical_incomp, color='b', linestyle='solid', label='Analytical (incompressible)')

axd["a"].set_xlabel(r'Time ($\alpha$)', fontsize='25')
axd["a"].set_ylabel('Vertical displacement (m)', fontsize=25)
axd["a"].grid(True)
axd["a"].tick_params(axis='both', which='major', labelsize=20)
axd["a"].legend(fontsize='30')
axd["a"].annotate(
        "Analytical solution",
        xy=(0.0375, 1), xycoords='axes fraction',
        xytext=(+0.5, -0.5), textcoords='offset fontsize',
        fontsize=30, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', pad=5.0))
axd["a"].add_patch(plt.Rectangle((-1, -5), 2, 40, ls="--", lw=2, ec="black", fc="none"))
axd["a"].annotate(
        "b",
        xy=(-7, 110), 
        xytext=(+0.5, -0.5), textcoords='offset fontsize',
        fontsize=30, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', pad=5.0))
axd["a"].add_patch(plt.Rectangle((100, 700), 60, 190, ls="--", lw=2, ec="black", fc="none"))
axd["a"].annotate(
        "c",
        xy=(154, 850), 
        xytext=(+0.5, -0.5), textcoords='offset fontsize',
        fontsize=30, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', pad=5.0))


ls = [(0, (1, 10)), (0, (1, 5)), (0, (5, 10)), 
     (0, (5, 5)), (0, (3, 10, 1, 10)), (0, (3, 5, 1, 5)),
     ]
# plot figure 1a elastic disp through time

ms = 10
lw = 2

for j in range(3):
    disp_time_series = [0.]
    dt = 0.1*0.5**j
    times = [0., dt]
    print(f"surface_disp/surface_displacement_dt{dt}_nx320arrays_bulktoshear2.0.csv")
    disp_df = pd.read_csv(f"surface_disp/surface_displacement_dt{dt}_nx320arrays_bulktoshear2.0.csv")
    disp_max = disp_df[f"surface_disp_step1"].max()
    disp_time_series.append(disp_max)
    times = np.array(times)
    axd["b"].plot(times, disp_time_series, color='orange', linestyle='dashed', marker='o', markersize=ms,linewidth=lw, label=rf'dt = {dt} $\alpha$ (compressible)')
    # Incompressible
    disp_time_series = [0.]
    disp_df = pd.read_csv(f"surface_disp/surface_displacement_dt{dt}_nx320arrays_bulktoshear10000.0.csv")
    disp_max = disp_df[f"surface_disp_step1"].max()
    disp_time_series.append(disp_max)
    axd["b"].plot(times, disp_time_series, color='b', linestyle='dashed', marker='x',markersize=ms,linewidth=lw, label=rf'dt = {dt} $\alpha$ (incompressible, bulk/mu = 10000)')
    
axd["b"].set_xlabel(r'Time ($\alpha$)', fontsize='25')
axd["b"].set_ylabel('Vertical displacement (m)', fontsize=25)
axd["b"].grid(True)
axd["b"].tick_params(axis='both', which='major', labelsize=18)
#axd["b"].legend(fontsize='15')
axd["b"].set_xlim(0, 0.11)
axd["b"].set_ylim(0, 25)
axd["b"].annotate(
        r"T$_\mathrm{end}$ = $\Delta$t",
        xy=(0.075, 1), xycoords='axes fraction',
        xytext=(+0.5, -0.5), textcoords='offset fontsize',
        fontsize=30, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', pad=5.0))

# plot figure 1c viscoelastic disp through time
for j in range(3):
    disp_time_series = [0.]
    times = [0.]
    dt = 16*0.5**j
    max_timesteps = round(160/dt)
    disp_df = pd.read_csv(f"surface_disp/surface_displacement_dt{dt}_nx320arrays_bulktoshear2.0.csv")

    for i in range(1, max_timesteps+1):
        time = dt * i
        times.append(time)
        disp_max = disp_df[f"surface_disp_step{i}"].max()
        disp_time_series.append(disp_max)

    times = np.array(times)
    axd["c"].plot(times, disp_time_series, color='orange', linestyle='dashed', marker='o',markersize=ms,linewidth=lw, label=rf'dt = {dt} $\alpha$ (compressible)')
    
    # Plot incompressible
    disp_time_series = [0.]
    disp_df = pd.read_csv(f"surface_disp/surface_displacement_dt{dt}_nx640arrays_bulktoshear100.0.csv")
    surf_x = disp_df['surface_points']
    xunique, unique_i = np.unique(surf_x, return_index=True)

    for i in range(1, max_timesteps+1):
        disp_max = disp_df[f"surface_disp_step{i}"].max()
        disp_time_series.append(disp_max)
    axd["c"].plot(times, disp_time_series, color='blue', linestyle='dashed', marker='x',markersize=ms,linewidth=lw, label=rf'dt = {dt} $\alpha$ (incompressible)')

axd["c"].set_xlabel(r'Time ($\alpha$)', fontsize='25')
axd["c"].set_ylabel('Vertical displacement (m)', fontsize=25)
axd["c"].grid(True)
axd["c"].tick_params(axis='both', which='major', labelsize=18)
#axd["c"].legend(fontsize='15')
axd["c"].set_xlim(100, 160)
axd["c"].set_ylim(700, 890)
axd["c"].annotate(
        r"T$_\mathrm{end}$ = 160 $\alpha$",
        xy=(0.075, 1), xycoords='axes fraction',
        xytext=(+0.5, -0.5), textcoords='offset fontsize',
        fontsize=30, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', pad=5.0))


# Figure 1d and 1e
elastic_comp = np.loadtxt("error_convergence/errors-elastic-compressible-visc1e21-shear1e11-bulk2e11-lam8-compahpFalse-internalvariable-coupled-320cells_nondimensional_direct_T2tau-free-surface.dat")
elastic_incomp = np.loadtxt("error_convergence/errors-elastic-incompressible-visc1e21-shear1e11-bulk1e15-lam8-compahpFalse-internalvariable-coupled-320cells_nondimensional_direct_T2tau-free-surface.dat")
viscoelastic_comp = np.loadtxt("error_convergence/errors-viscoelastic-compressible-visc1e21-shear1e11-bulk2e11-lam8-dtfstart16alpha-compahpFalse_160alpha-internalvariable-coupled-320cells_nondimensional_direct_T2tau-free-surface.dat")
viscoelastic_incomp = np.loadtxt("error_convergence/errors-viscoelastic-incompressible-visc1e21-shear1e11-bulk1e13-lam8-dtfstart16alpha-compahpFalse_160alpha-internalvariable-coupled-640cells_nondimensional_direct_T2tau-free-surface.dat")


dt_elastic = [0.1*0.5**i for i in range(7)]
dt_viscoelastic = [16*0.5**i for i in range(6)]

print(dt_elastic)

for pos in np.linspace(-2, 1, 20):
    axd["d"].axline((pos, 0), slope=1, color='grey', transform=axd["d"].transAxes, alpha=0.8)
axd["d"].loglog(dt_elastic, elastic_comp, color='orange', linestyle='dashed', marker='o',markersize=ms,linewidth=lw, label='Compressible')
axd["d"].loglog(dt_elastic, elastic_incomp, color='b', linestyle='dashed', marker='x',markersize=ms, linewidth=lw, label='Incompressible')
axd["d"].set_xlabel(r'$\Delta t$ ($\alpha$)', fontsize='25')
axd["d"].set_ylabel('L2 error', fontsize=25)
axd["d"].tick_params(axis='both', which='both', labelsize=20)
#axd["d"].legend(fontsize='15')
axd["d"].grid(True)
axd["d"].annotate(
        r"T$_\mathrm{end}$ = $\Delta$t",
        xy=(0.075, 1), xycoords='axes fraction',
        xytext=(+0.5, -0.5), textcoords='offset fontsize',
        fontsize=30, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', pad=5.0))

# Viscoelastic error convergence
for pos in np.linspace(-2, 10, 60):
    axd["e"].axline((pos, 0), slope=1, color='grey', transform=axd["e"].transAxes, alpha=0.8)
axd["e"].loglog(dt_viscoelastic, viscoelastic_comp, color='orange', linestyle='dashed', marker='o',markersize=ms, linewidth=lw, label='Compressible')
axd["e"].loglog(dt_viscoelastic, viscoelastic_incomp, color='b', linestyle='dashed', linewidth=lw, marker='x',markersize=ms, label='Incompressible')
axd["e"].set_xlabel(r'$\Delta t$ ($\alpha$)', fontsize='25')
axd["e"].set_ylabel('L2 error', fontsize=25)
axd["e"].tick_params(axis='both', which='both', labelsize=20)
#axd["e"].legend(fontsize='15')
axd["e"].grid(True)
axd["e"].annotate(
        r"T$_\mathrm{end}$ = 160 $\alpha$",
        xy=(0.075, 1), xycoords='axes fraction',
        xytext=(+0.5, -0.5), textcoords='offset fontsize',
        fontsize=30, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', pad=5.0))

for label, ax in axd.items():
    # Use Axes.annotate to put the label
    # - at the top left corner (axes fraction (0, 1)),
    # - offset half-a-fontsize right and half-a-fontsize down
    #   (offset fontsize (+0.5, -0.5)),
    # i.e. just inside the axes.
    ax.annotate(
        label,
        xy=(0, 1), xycoords='axes fraction',
        xytext=(+0.5, -0.5), textcoords='offset fontsize',
        fontsize=30, verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', pad=5.0))



figname = "14.05.25_Figure1_analytical_compressibleincompressible_mosaic_bulkdiff_simplify"
fig.savefig(f'{figname}.png')

