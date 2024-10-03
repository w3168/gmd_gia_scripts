# 2d adjoint model based on Weerdesteijn et al 2023

from gadopt import *
from weerdesteijn_2d import Weerdesteijn2d


class InstantIceLoadWeerdesteijn2d(Weerdesteijn2d):
    name = "weerdesteijn-instant-ice"
    vertical_component = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def setup_ramp(self):
        # Seems like you need domain for constant but I thought this had
        # depreciated?
        self.ramp = Constant(1)

    def setup_ice_load(self):
        super().setup_ice_load()
        # Only update the ice load at initial times
        self.ice_load.interpolate(self.ramp * self.rho_ice * self.g * self.Hice * self.disc)

    def update_ramp(self):
        # already initialised with 1 for instantaneous loading
        pass

    def update_ice_load(self):
        # interpolating ice load at each timestep breaks adjoint (and is probably not 'adjointable')
        pass

    def checkpoint_filename(self):
        return f"{self.name}-dx{round(self.dx/1000)}km-nz{self.nz}-dt{self.dt_years}years-low-viscosity{self.low_viscosity_region}-chk.h5"

    def displacement_filename(self):
        return f"displacement-{self.name}-dx{round(self.dx/1000)}km-nz{self.nz}-dt{self.dt_years}years-low-viscosity{self.low_viscosity_region}.dat"


if __name__ == "__main__":
    simulation = InstantIceLoadWeerdesteijn2d(dx=5e3, nz=160, Tend_years=5000, dt_out_years=5000, do_write=True)
    simulation.run_simulation()
