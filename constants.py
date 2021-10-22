cuboVerticies = (
    (0,0,0),
    (1,0,0),
    (1,1,0),
    (0,1,0),

    (0,0,-1),
    (1,0,-1),
    (1,1,-1),
    (0,1,-1),
)

cuboFaces = (
    ((0.1,0.1,0.1),4,5,6,7),    #1
    ((0,1,1),3,2,6,7),          #2
    ((1,1,0),0,1,5,4),          #4
    ((0,1,0),0,1,2,3),          #3
)

cuboFacesbc= (
    ((1,0,0),0,1,2,3),          #3
    ((1,1,0),0,1,5,4),          #4
    ((1,1,1),0,4,7,3),          #5
    ((0,1,1),3,2,6,7),          #2
    ((0,0,1),1,2,6,5),          #6
    ((0.1,0.1,0.1),4,5,6,7),    #1
)

squadVerticies = (
    (0,0,0),
    (1,0,0),
    (1,0.707106781,-0.707106781),
    (0,0.707106781,-0.707106781),
)

triangleVerticies = (
    (0,0,0),
    (1,0,0),
    (0,1,0),
)

squadColor = (0,0,1)
triangleColor = (0,1,0)