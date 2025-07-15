from data_c2027453 import *
def facing(points,face):
    direction = 0
    for i in range(len(face)):
        #determenant for the line vector, sums up for the length of face lis.
        direction += points[(face[(i+1)%len(face)]-1)][0]*points[face[i]-1][1]-points[face[i]-1][0]*points[(face[(i+1)%len(face)]-1)][1]
    return direction

def renderingList(points,faces,reflection):
    renderlist = []
    for i in range(len(faces)):
        #checks for desired direction to add to the rendering queue
        direction = facing(points,faces[i])
        if reflection == False:
            if direction > 0:
                renderlist.append(faces[i])
        elif reflection == True:
            if direction < 0:
                renderlist.append(faces[i])
    return renderlist
