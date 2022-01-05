#William M A Pearson
#FindingAnAngleInbetweenTwoPlanes
import numpy as np
import math

def CreateAPlane(point1, point2, point3):
    #This functions Creates a Plane from three points
    #Create Numpy Points
    pointA = np.array(point1)
    pointB = np.array(point2)
    pointC = np.array(point3)

    #Create Vectors
    V1 = pointB - pointA
    V2 = pointC - pointA

    #Create Plane
    plane = np.cross(V1, V2)

    return plane

def FindAngleBetweenTwoPlanes(plane1, plane2):
    #This functions finds the angle between two plane normals
    #angle between the two normals
    #dot product
    angle = np.dot(plane1,plane2)
    
    #divide by magnitude of vectors
    angle = ang = np.arccos(np.dot(plane1, plane2) / (np.linalg.norm(plane1) * np.linalg.norm(plane2)))

    return angle


Plane1 = CreateAPlane([-1,1,0], [1,1,0], [1,1,1])
Plane2 = CreateAPlane([0,0,0], [1,1,0], [1,1,1])
Angle = FindAngleBetweenTwoPlanes(Plane1, Plane2)

print(f"Angle || Radians - {Angle} || Degrees - {math.degrees(Angle)}")
