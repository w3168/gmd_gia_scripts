# 3d spherical model based on Spada et al 2011

from gadopt import *
from spada_cylindrical_2d import SpadaCylindrical2d


class SpadaSpherical3d(SpadaCylindrical2d):
    name = "spada-spherical-3d"
    vertical_component = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def initialise_background_field(self, field, background_values):
        r = sqrt(self.X[0]**2 + self.X[1]**2 + self.X[2]**2)-self.radius_values[0]
        for i in range(0, len(background_values)-1):
            field.interpolate(conditional(r >= self.radius_values[i+1] - self.radius_values[0],
                              conditional(r <= self.radius_values[i] - self.radius_values[0],
                              background_values[i], field), field))

        # Catches cases where mesh just sticking above z=0 surface by 1e-9 and below depth of mantle...
        field.interpolate(conditional(r > 0, background_values[0], field))
        field.interpolate(conditional(r < -self.D, background_values[-2], field))

    def setup_surface_mesh(self):
        reflevel = 6
        self.ncells = 8*2**(reflevel-1) #256 # 8*2**(3-1)
        self.surface_mesh = CubedSphereMesh(self.rmin, refinement_level=reflevel, degree=2, name='surface_mesh')

    def setup_nullspaces(self):
        # Nullspaces and near-nullspaces:
        self.Z_nullspace = create_stokes_nullspace(self.M, closed=False, rotational=True)
        self.Z_near_nullspace = create_stokes_nullspace(self.M, closed=False, rotational=True, translations=[0, 1, 2])

    def initialise_colatitude(self):
        # This gives 0 at the north pole and pi (-pi) near the South pole
        distance_from_rotation_axis = sqrt(self.X[0]**2 + self.X[1]**2)
        return atan2(distance_from_rotation_axis, self.X[2])


if __name__ == "__main__":
    simulation = SpadaSpherical3d(dx=500*1e3, nz=160, cartesian=False, do_write=True)
    simulation.run_simulation()

