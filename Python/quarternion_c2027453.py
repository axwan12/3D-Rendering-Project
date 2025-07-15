from math import *

'''
Quarternion Calculations
'''

#Ivert Quartenion
def QInv(q):
    return [q[0],-q[1],-q[2],-q[3]]

#Quartenion Multiplication (q * p)
def Q(q,p):
    return [q[0]*p[0]-(q[1]*p[1]+q[2]*p[2]+q[3]*p[3]),
              q[0]*p[1]+q[1]*p[0]+q[2]*p[3]-q[3]*p[2],
              q[0]*p[2]+q[2]*p[0]+q[3]*p[1]-q[1]*p[3],
              q[0]*p[3]+q[3]*p[0]+q[1]*p[2]-q[2]*p[1]]

#Computes The Rotation
def Rotate(q,p):
    return Q(Q(q,p),QInv(q))

def sine(i):
    if i < 0:
        return(-1)
    else:
        return(1)

#Gets The Normalised Quarternion After Angle Applied
def axisRotate(point, axis, angle):
    SS=axis[0]**2+axis[1]**2+axis[2]**2
    if SS == 0:
        Quarternion=[1,0,0,0]
    else:
        Quarternion=[cos(angle),sine(axis[0])*sin(angle)*sqrt((axis[0]**2)/SS),sine(axis[1])*sin(angle)*sqrt((axis[1]**2)/SS),sine(axis[2])*sin(angle)*sqrt((axis[2]**2)/SS)]

    points=([0,point[0],point[1],point[2]])
    
    return Rotate(Quarternion, points)[1:]

#Rotates A Full Array
def pointsRotate(array, axis, angle):
    rotated = []
    for i in range(len(array)):
        rotated.append(axisRotate(array[i], axis, angle))
    return rotated
        
