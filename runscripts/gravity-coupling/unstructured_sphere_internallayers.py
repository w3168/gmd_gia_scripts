# modified from gmsh tutorial t5.py

import gmsh


def generate_mesh():
    # Before using any functions in the Python API, Gmsh must be initialized:
    gmsh.initialize()

    gmsh.model.add("t1")

    lc = 100e3
    lcg = 5000e3
    
    radius_values = [6371e3, 6301e3, 5951e3, 5701e3, 3480e3]
    res_values = [lcg, 100e3, 1e3, 5701e3, 3480e3]
    Rg = 31855e3
    Re = 6371e3
    Rl = 6301e3
    Rum = 5951e3
    Rlm = 5701e3
    Rc = 3480e3
    grav_mesh_depth = Rg-Re
    D = Re-Rc

    Rg_tilde = Rg/D
    Re_tilde = Re/D
    Rc_tilde = Rc/D
    Rl_tilde = Rl/D
    Rum_tilde = Rum/D
    Rlm_tilde = Rlm/D
    lc_tilde = lc/D
    lcg_tilde = lcg/D
    grav_mesh_depth_tilde = grav_mesh_depth/D

    def cheeseHole(x, y, z, r, lc):
        # This function will create a spherical hole in a volume. We don't specify
        # tags manually, and let the functions return them automatically:

        p1 = gmsh.model.geo.addPoint(x, y, z, lc)
        p2 = gmsh.model.geo.addPoint(x + r, y, z, lc)
        p3 = gmsh.model.geo.addPoint(x, y + r, z, lc)
        p4 = gmsh.model.geo.addPoint(x, y, z + r, lc)
        p5 = gmsh.model.geo.addPoint(x - r, y, z, lc)
        p6 = gmsh.model.geo.addPoint(x, y - r, z, lc)
        p7 = gmsh.model.geo.addPoint(x, y, z - r, lc)

        c1 = gmsh.model.geo.addCircleArc(p2, p1, p7)
        c2 = gmsh.model.geo.addCircleArc(p7, p1, p5)
        c3 = gmsh.model.geo.addCircleArc(p5, p1, p4)
        c4 = gmsh.model.geo.addCircleArc(p4, p1, p2)
        c5 = gmsh.model.geo.addCircleArc(p2, p1, p3)
        c6 = gmsh.model.geo.addCircleArc(p3, p1, p5)
        c7 = gmsh.model.geo.addCircleArc(p5, p1, p6)
        c8 = gmsh.model.geo.addCircleArc(p6, p1, p2)
        c9 = gmsh.model.geo.addCircleArc(p7, p1, p3)
        c10 = gmsh.model.geo.addCircleArc(p3, p1, p4)
        c11 = gmsh.model.geo.addCircleArc(p4, p1, p6)
        c12 = gmsh.model.geo.addCircleArc(p6, p1, p7)

        l1 = gmsh.model.geo.addCurveLoop([c5, c10, c4])
        l2 = gmsh.model.geo.addCurveLoop([c9, -c5, c1])
        l3 = gmsh.model.geo.addCurveLoop([c12, -c8, -c1])
        l4 = gmsh.model.geo.addCurveLoop([c8, -c4, c11])
        l5 = gmsh.model.geo.addCurveLoop([-c10, c6, c3])
        l6 = gmsh.model.geo.addCurveLoop([-c11, -c3, c7])
        l7 = gmsh.model.geo.addCurveLoop([-c2, -c7, -c12])
        l8 = gmsh.model.geo.addCurveLoop([-c6, -c9, c2])

        # We need non-plane surfaces to define the spherical holes. Here we use the
        # `gmsh.model.geo.addSurfaceFilling()' function, which can be used for
        # surfaces with 3 or 4 curves on their boundary. If the curves are circle
        # arcs with the same center, a spherical patch is created; otherwise
        # transfinite interpolation is used. With the OpenCASCADE kernel,
        # `gmsh.model.occ.addSurfaceFilling()' can be used with an arbitrary number
        # of boundary curves, and will fit a BSpline patch through them.

        s1 = gmsh.model.geo.addSurfaceFilling([l1])
        s2 = gmsh.model.geo.addSurfaceFilling([l2])
        s3 = gmsh.model.geo.addSurfaceFilling([l3])
        s4 = gmsh.model.geo.addSurfaceFilling([l4])
        s5 = gmsh.model.geo.addSurfaceFilling([l5])
        s6 = gmsh.model.geo.addSurfaceFilling([l6])
        s7 = gmsh.model.geo.addSurfaceFilling([l7])
        s8 = gmsh.model.geo.addSurfaceFilling([l8])

        sl = gmsh.model.geo.addSurfaceLoop([s1, s2, s3, s4, s5, s6, s7, s8])

        ids = [s1, s2, s3, s4, s5, s6, s7, s8]
        return sl, ids

    sg, idg = cheeseHole(0, 0, 0, Rg_tilde, 0.25*(Rg_tilde-Re_tilde))
    se, ide = cheeseHole(0, 0, 0, Re_tilde, 0.25*(Re_tilde-Rl_tilde))
    sl, idl = cheeseHole(0, 0, 0, Rl_tilde, 0.5*(Rl_tilde-Rum_tilde))
    s_um, idum = cheeseHole(0, 0, 0, Rum_tilde, 0.5*(Rum_tilde-Rlm_tilde))
    slm, idlm = cheeseHole(0, 0, 0, Rlm_tilde, 0.5*(Rlm_tilde-Rc_tilde))
    sc, idc = cheeseHole(0, 0, 0, Rc_tilde, 0.5*(Rlm_tilde-Rc_tilde))
    vg = gmsh.model.geo.addVolume([sg, se])
    ve = gmsh.model.geo.addVolume([se, sl])
    vl = gmsh.model.geo.addVolume([sl, s_um])
    vum = gmsh.model.geo.addVolume([s_um, slm])
    vlm = gmsh.model.geo.addVolume([slm, sc])
    gmsh.model.geo.synchronize()
    # Set physical groups for boundary tags
    # Bottom id: 1, Top id: 2
    gmsh.model.addPhysicalGroup(2, idg, 3)
    gmsh.model.addPhysicalGroup(2, ide, 2)
    gmsh.model.addPhysicalGroup(2, idc, 1)

    # boundary ids for lithosphere, upper mantle and lower mantle
    gmsh.model.addPhysicalGroup(2, idl, 13)
    gmsh.model.addPhysicalGroup(2, idum, 12)
    gmsh.model.addPhysicalGroup(2, idlm, 11)

    # set physical groups for surfaces mantle then exterior grav
    print(vg)
    gmsh.model.addPhysicalGroup(3, [ve, vl, vum, vlm], 101)
    gmsh.model.addPhysicalGroup(3, [vg], 102)

    
    
    refinement=False
    if not refinement:
        gmsh.model.mesh.generate(3)
        # ... and save it to disk
        gmsh.write("unstructured_sphere_internal_test.msh")

        gmsh.finalize()
        exit()

    

    # Refine near the Earth surface
    gmsh.model.mesh.field.add("Distance", 1)
    gmsh.model.mesh.field.setNumbers(1, "SurfacesList", ide)
    gmsh.model.mesh.field.setNumber(1, "Sampling", 100)

    # We then define a `Threshold' field, which uses the return value of the
    # `Distance' field 1 in order to define a simple change in element size
    # depending on the computed distances
    #
    # SizeMax -                     /------------------
    #                              /
    #                             /
    #                            /
    # SizeMin -o----------------/
    #          |                |    |
    #        Point         DistMin  DistMax
    gmsh.model.mesh.field.add("Threshold", 2)
    gmsh.model.mesh.field.setNumber(2, "InField", 1)
    gmsh.model.mesh.field.setNumber(2, "SizeMin", lc_tilde / 2.5)
    gmsh.model.mesh.field.setNumber(2, "SizeMax", 20*lc_tilde)
    gmsh.model.mesh.field.setNumber(2, "DistMin", 0.3*Rc_tilde)
    gmsh.model.mesh.field.setNumber(2, "DistMax", 0.5*Rc_tilde)

    # Coarsen near the edge of gravity mesh surface
    gmsh.model.mesh.field.add("Distance", 3)
    gmsh.model.mesh.field.setNumbers(3, "SurfacesList", idg)
    gmsh.model.mesh.field.setNumber(3, "Sampling", 100)

    # We then define a `Threshold' field, which uses the return value of the
    # `Distance' field 1 in order to define a simple change in element size
    # depending on the computed distances
    #
    # SizeMax -                     /------------------
    #                              /
    #                             /
    #                            /
    # SizeMin -o----------------/
    #          |                |    |
    #        Point         DistMin  DistMax
    gmsh.model.mesh.field.add("Threshold", 4)
    gmsh.model.mesh.field.setNumber(4, "InField", 3)
    gmsh.model.mesh.field.setNumber(4, "SizeMin", lcg_tilde)
    gmsh.model.mesh.field.setNumber(4, "SizeMax", lc_tilde)
    gmsh.model.mesh.field.setNumber(4, "DistMin", 0.8*Re_tilde)
    gmsh.model.mesh.field.setNumber(4, "DistMax", grav_mesh_depth_tilde-0.5*Re_tilde)

    gmsh.model.mesh.field.add("Min", 5)
    gmsh.model.mesh.field.setNumbers(5, "FieldsList", [2, 4])
    gmsh.model.mesh.field.setAsBackgroundMesh(5)



    # When the element size is fully specified by a mesh size field (as it is in
    # this example), it is thus often desirable to set

    gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 0)
    gmsh.option.setNumber("Mesh.MeshSizeFromPoints", 0)
    gmsh.option.setNumber("Mesh.MeshSizeFromCurvature", 0)

    # This will prevent over-refinement due to small mesh sizes on the boundary.

    # Finally, while the default "Frontal-Delaunay" 2D meshing algorithm
    # (Mesh.Algorithm = 6) usually leads to the highest quality meshes, the
    # "Delaunay" algorithm (Mesh.Algorithm = 5) will handle complex mesh size fields
    # better - in particular size fields with large element size gradients:

    gmsh.option.setNumber("Mesh.Algorithm", 5)

    gmsh.model.mesh.generate(3)

    # ... and save it to disk
    gmsh.write("unstructured_sphere_refined_surface_gravity.msh")

    gmsh.finalize()


if __name__ == "__main__":
    generate_mesh()
