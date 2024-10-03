// Based off tutorial 10 from the Gmsh manual

// Let's create a simple rectangular geometry

km = 1e3;

lc = 200*km;
L = 1500*km;
D = 2891*km; 
Point(1) = {0.0,0.0,0,lc}; Point(2) = {L,0.0,0,lc};
Point(3) = {L,L,0,lc};     Point(4) = {0,L,0,lc};

Point(5) = {0.0,0.0,-D,lc}; Point(6) = {L,0.0,-D,lc};
Point(7) = {L,L,-D,lc};     Point(8) = {0,L,-D,lc};

// Choose boundary ids to match Firedrake's unit meshes... 
//    1: plane x == 0
//    2: plane x == L
//    3: plane y == 0
//    4: plane y == L
//    5: plane z == 0
//    6: plane z == D

// Top side
Line(1) = {1,2}; Line(2) = {2,3}; Line(3) = {3,4}; Line(4) = {4,1};

// Bottom Side
Line(5) = {5,6}; Line(6) = {6,7}; Line(7) = {7,8}; Line(8) = {8,5};

// Connecting lines y = 0 going up
Line(9) = {5,1}; Line(10) = {6,2};

// Connecting lines y = L going up
Line(11) = {8,4}; Line(12) = {7,3};

// Top side
Curve Loop(6) = {1,2,3,4}; Plane Surface(6) = {6};

// bottom side
Curve Loop(5) = {5,6,7,8}; Plane Surface(5) = {5};

// x = 0
Curve Loop(1) = {8,9,-4,-11}; Plane Surface(1) = {1};

// x = L
Curve Loop(2) = {6,12,-2,-10}; Plane Surface(2) = {2};

// y = 0
Curve Loop(3) = {5,10,-1,-9}; Plane Surface(3) = {3};

// y = L
Curve Loop(4) = {7,11,-3,-12}; Plane Surface(4) = {4};

Surface Loop(1) = {1, 2, 3, 4, 5, -6};

Volume(1) = {1};

Physical Surface(1) = 1;
Physical Surface(2) = 2;
Physical Surface(3) = 3;
Physical Surface(4) = 4;
Physical Surface(5) = 5;
Physical Surface(6) = 6;

Physical Volume(1) = {1};


// Set up a distance field from point 1 i.e. (0,0) where the iceloading will be 
Field[1] = Distance;
Field[1].PointsList = {1};


// We then define a `Threshold' field, which uses the return value of the
// `Distance' field 1 in order to define a simple change in element size
// depending on the computed distances. This will make the mesh 40x finer 
// near point 1 i.e. dx = dy = 5 km.
//
// SizeMax -                     /------------------
//                              /
//                             /
//                            /
// SizeMin -o----------------/
//          |                |    |
//        Point         DistMin  DistMax
Field[2] = Threshold;
Field[2].InField = 1;
Field[2].SizeMin = lc / 20;
Field[2].SizeMax = lc;
Field[2].DistMin = 450*km;
Field[2].DistMax = 900*km;

Background Field = 2;
// below is from the tutorial 
// To determine the size of mesh elements, Gmsh locally computes the minimum of
//
// 1) the size of the model bounding box;
// 2) if `Mesh.MeshSizeFromPoints' is set, the mesh size specified at
//    geometrical points;
// 3) if `Mesh.MeshSizeFromCurvature' is positive, the mesh size based on
//    curvature (the value specifying the number of elements per 2 * pi rad);
// 4) the background mesh size field;
// 5) any per-entity mesh size constraint.
//
// This value is then constrained in the interval [`Mesh.MeshSizeMin',
// `Mesh.MeshSizeMax'] and multiplied by `Mesh.MeshSizeFactor'. In addition,
// boundary mesh sizes are interpolated inside surfaces and/or volumes depending
// on the value of `Mesh.MeshSizeExtendFromBoundary' (which is set by default).
//
// When the element size is fully specified by a mesh size field (as it is in
// this example), it is thus often desirable to set

Mesh.MeshSizeExtendFromBoundary = 0;
Mesh.MeshSizeFromPoints = 0;
Mesh.MeshSizeFromCurvature = 0;

// This will prevent over-refinement due to small mesh sizes on the boundary.

// Finally, while the default "Frontal-Delaunay" 2D meshing algorithm
// (Mesh.Algorithm = 6) usually leads to the highest quality meshes, the
// "Delaunay" algorithm (Mesh.Algorithm = 5) will handle complex mesh size
// fields better - in particular size fields with large element size gradients:

Mesh.Algorithm = 5;
