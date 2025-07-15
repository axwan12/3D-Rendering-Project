import pygame

White = (255,255,255)
Black = (0,0,0)
Blue = (0,0,255)

def reflect(array,x,y,z):
    reflected=[]
    for i in range(len(array)):
        reflected.append([array[i][0]*x,array[i][1]*y,array[i][2]*z])
    return reflected

def render(points,faces,scene,scale,offset):
    nfaces = len(faces)
    for i in range(nfaces):
        linePoints = []
        for r in range(len(faces[i])):
            linePoints.append([(points[faces[i][r]-1][0])*scale +offset[0],(points[faces[i][r]-1][1])*scale +offset[1]])
        pygame.draw.polygon(scene, Blue , linePoints)

        for r in range(len(faces[i])):
            pygame.draw.line(scene, Black,(linePoints[(r+1)%len(faces[i])][0],linePoints[(r+1)%len(faces[i])][1]),(linePoints[r%len(faces[i])][0],linePoints[r%len(faces[i])][1]),2)

def perspective(array,viewDistance,pos,zoffset):
    perspective = []
    for i in range(len(array)):
        perspective.append([(array[i][0]+pos[0])*viewDistance/(array[i][2]+pos[2]+zoffset),(array[i][1]+pos[1])*viewDistance/(array[i][2]+pos[2]+zoffset),-array[i][2]+pos[2]+zoffset])
    return perspective
        
    
