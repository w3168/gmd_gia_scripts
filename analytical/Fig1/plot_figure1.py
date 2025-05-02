import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
folder = "./"




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


h_elastic2 = F0/(1 + f_e*maxwell_time/tau0)
h_elastic = F0 - h_elastic2  # Constant(F0/(1 + maxwell_time/tau0))
h_elastic2_incomp = F0/(1 + maxwell_time/tau0)
h_elastic_incomp = F0 - h_elastic2_incomp  # Constant(F0/(1 + maxwell_time/tau0))

eta_analytical = [0.]
eta_analytical_incomp = [0.]
times = [0.]

dt_factor = 0.00001
dt = dt_factor * tau0
max_timesteps = round(2*tau0/dt)
for i in range(1, max_timesteps):
    time = dt * i
    times.append(time)
    eta_analytical.append(((F0 - h_elastic) * (1-np.exp(-(time)/(tau0+f_e*maxwell_time)))+h_elastic) )
    eta_analytical_incomp.append(((F0 - h_elastic_incomp) * (1-np.exp(-(time)/(tau0+maxwell_time)))+h_elastic_incomp) )
    print(time)
    
times = np.array(times)

fig, ax = plt.subplots(2, 2, figsize=(30, 20))
# Plot analytical solution for 1a and 1b
ax[0,0].plot(times/maxwell_time, eta_analytical, color='k', linestyle='solid', label='Analytical (compressible)')
ax[0,0].plot(times/maxwell_time, eta_analytical_incomp, color='b', linestyle='solid', label='Analytical (incompressible)')
ax[1,0].plot(times/maxwell_time, eta_analytical, color='k', linestyle='solid', label='Analytical (compressible)')
#ax[1,0].plot(times/maxwell_time, eta_analytical_incomp, color='b', linestyle='solid', label='Analytical (incompressible)')

ls = ['dashed', 'dotted', 'dashdot']
# plot figure 1a elastic disp through time

for j in range(3):
    disp_time_series = [0.]
    dt_factor = 0.001*0.5**j
    dt = dt_factor * tau0
    times = [0., dt]
    disp_df = pd.read_csv(f"surface_displacement_dt{dt/maxwell_time}_nx320arrays.csv")
    surf_x = disp_df['surface_points']
    xunique, unique_i = np.unique(surf_x, return_index=True)
    disp_unique = disp_df[f"surface_disp_step1"][unique_i]
    disp_time_series.append(disp_unique[0])
    times = np.array(times)
    ax[0, 0].plot(times/maxwell_time, disp_time_series, color='k', linestyle=ls[j], marker='x', label=rf'dt = {dt/maxwell_time:1f} $\alpha$ (compressible)')
    # Incompressible
    disp_time_series = [0.]
    disp_df = pd.read_csv(f"surface_displacement_dt{dt/maxwell_time}_nx320arrays_incompressible.csv")
    surf_x = disp_df['surface_points']
    xunique, unique_i = np.unique(surf_x, return_index=True)
    disp_unique = disp_df[f"surface_disp_step1"][unique_i]
    disp_time_series.append(disp_unique[0])
    ax[0, 0].plot(times/maxwell_time, disp_time_series, color='b', linestyle=ls[j], marker='x', label=rf'dt = {dt/maxwell_time:1f} $\alpha$ (incompressible)')

ax[0, 0].set_xlabel(r'Time ($\alpha$)', fontsize='25')
ax[0, 0].set_ylabel('Maximum vertical displacement (m)', fontsize=25)
ax[0, 0].grid(True)
ax[0, 0].tick_params(axis='both', which='major', labelsize=15)
ax[0, 0].legend(fontsize='15')
ax[0, 0].set_xlim(0, 0.1)
ax[0, 0].set_ylim(0, 25)

# plot figure 1b elastic disp through time
for j in range(3):
    disp_time_series = [0.]
    times = [0.]
    dt_factor = 0.1*0.5**j
    dt = dt_factor * tau0
    max_timesteps = round(2*tau0/dt)
    disp_df = pd.read_csv(f"surface_displacement_dt{dt/maxwell_time}_nx320arrays.csv")
    surf_x = disp_df['surface_points']
    xunique, unique_i = np.unique(surf_x, return_index=True)

    for i in range(1, max_timesteps):
        time = dt * i
        times.append(time)
        disp_unique = disp_df[f"surface_disp_step{i}"][unique_i]
        disp_time_series.append(disp_unique[0])

    times = np.array(times)
    ax[1, 0].plot(times/maxwell_time, disp_time_series, color='k', linestyle=ls[j], label=rf'dt = {dt/maxwell_time:1f} $\alpha$')

ax[1, 0].set_xlabel(r'Time ($\alpha$)', fontsize='25')
ax[1, 0].set_ylabel('Maximum vertical displacement (m)', fontsize=25)
ax[1, 0].grid(True)
ax[1, 0].tick_params(axis='both', which='major', labelsize=15)
ax[1, 0].legend(fontsize='15')
ax[1, 0].set_xlim(45, 150)
ax[1, 0].set_ylim(400, 900)

#ax[0,0].annotate('a)', (-9.1, 0.07), fontsize='25', annotation_clip=False)


# Figure 1b
elastic_comp = np.loadtxt("error_convergence/errors-elastic-compressible-visc1e21-shear1e11-bulk2e11-lam8-compahpFalse-internalvariable-coupled-320cells_nondimensional_direct_T2tau-free-surface.dat")
elastic_incomp = np.loadtxt("error_convergence/errors-elastic-incompressible-visc1e21-shear1e11-bulk1e15-lam8-compahpFalse-internalvariable-coupled-320cells_nondimensional_direct_T2tau-free-surface.dat")
viscoelastic_comp = np.loadtxt("error_convergence/errors-viscoelastic-compressible-visc1e21-shear1e11-bulk2e11-lam8-compahpFalse-internalvariable-coupled-320cells_nondimensional_direct_T2tau-free-surface.dat")
viscoelastic_incomp = np.loadtxt("error_convergence/errors-viscoelastic-incompressible-visc1e21-shear1e11-bulk1e15-lam8-compahpFalse-internalvariable-coupled-640cells_nondimensional_direct_T2tau-free-surface.dat")


dt_elastic = [(0.001*tau0/maxwell_time)*0.5**i for i in range(4)]
dt_viscoelastic = [(0.1*tau0/maxwell_time)*0.5**i for i in range(4)]

print(dt_elastic)

for pos in np.linspace(-2, 1, 20):
    ax[0, 1].axline((pos, 0), slope=1, color='grey', transform=ax[0,1].transAxes, alpha=0.8)
ax[0, 1].loglog(dt_elastic, elastic_comp, color='k', linestyle='dashed', marker='x', label='Compressible')
ax[0, 1].loglog(dt_elastic, elastic_incomp, color='b', linestyle='dashed', marker='+', label='Incompressible')
ax[0, 1].set_xlabel(r'$\Delta t$ ($\alpha$)', fontsize='25')
ax[0, 1].set_ylabel('L2 error', fontsize=25)
ax[0, 1].tick_params(axis='both', which='both', labelsize=15)
ax[0, 1].legend(fontsize='15')
ax[0, 1].grid(True)

# Viscoelastic error convergence
for pos in np.linspace(-2, 10, 60):
    ax[1, 1].axline((pos, 0), slope=2, color='grey', transform=ax[0,1].transAxes, alpha=0.8)
ax[1, 1].loglog(dt_viscoelastic, viscoelastic_comp, color='k', linestyle='dotted', marker='x', label='Compressible')
ax[1, 1].loglog(dt_viscoelastic, viscoelastic_incomp, color='b', linestyle='dotted', marker='+', label='Incompressible')
ax[1, 1].set_xlabel(r'$\Delta t$ ($\alpha$)', fontsize='25')
ax[1, 1].set_ylabel('L2 error', fontsize=25)
ax[1, 1].tick_params(axis='both', which='both', labelsize=15)
ax[1, 1].legend(fontsize='15')
ax[1, 1].grid(True)




figname = "Figure_1_analytical_compressibleincompressible_woutincomplong_1.05.25"
fig.savefig(f'{figname}.png')

