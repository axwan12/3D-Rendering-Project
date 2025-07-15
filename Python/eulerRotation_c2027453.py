from math import *

def pointDot(eulerMatrix,point):
    rotatedPoint=[]
    for i in range(3):
        rotatedPoint.append(eulerMatrix[i][0]*point[0]+eulerMatrix[i][1]*point[1]+eulerMatrix[i][2]*point[2])
    return rotatedPoint

def eulerRotate(points,eulerAngle):
    RotatedX = [[1,0,0],[0,cos(eulerAngle[0]),-sin(eulerAngle[0])],[0,sin(eulerAngle[0]),cos(eulerAngle[0])]]

    RotatedY = [[cos(eulerAngle[1]),0,sin(eulerAngle[1])],[0,1,0],[-sin(eulerAngle[1]),0,cos(eulerAngle[1])]]

    RotatedZ = [[cos(eulerAngle[2]),-sin(eulerAngle[2]),0],[sin(eulerAngle[2]),cos(eulerAngle[2]),0],[0,0,1]]

    rotated = []
    
    for i in range(len(points)):
        rotate = pointDot(RotatedX ,points[i])
        rotate = pointDot(RotatedY ,rotate)
        rotate = pointDot(RotatedZ ,rotate)
        rotated.append(rotate)
    return rotated
