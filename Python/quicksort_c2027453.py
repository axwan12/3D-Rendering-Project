from random import randint
from data_c2027453 import *

def quicksort(l):
    if len(l) < 2:
        return l
    else:
        smaller = []
        larger = [] # or equal to
        pivot = l.pop(randint(0,len(l)-1))
        for i in range(0,len(l)):
            item = l.pop(0)
            if item[1] < pivot[1]:
                smaller.append(item)
            else:
                larger.append(item)
        return_list = []
        smaller = quicksort(smaller)
        larger = quicksort(larger)
        for i in range(0,len(smaller)):
            return_list.append(smaller.pop(0))
        return_list.append(pivot)
        for i in range(0,len(larger)):
            return_list.append(larger.pop(0))
        return return_list

def orderedPoints(points,faces):
    zavg = []
    for i in range(len(faces)):
        z_count=0
        for r in range(len(faces[0])):
            z_count = z_count + points[faces[i][r]-1][2]
        zavg.append([i,z_count/len(faces[0])])

    face_pos = quicksort(zavg)

    displayFaces = []

    for i in range(len(faces)):
        displayFaces.append(faces[face_pos[i][0]-1])

    return displayFaces
