#Gets Points/Faces From Stored Model
def data(obj):
    lines = []
    f = open(obj,"r") 
    for line in f:
        lines.append(line.rstrip("\n"))

    points = []
    faces = []
    for line in lines:
        words = []
        words.append(line.split(" "))
        #stores vetex and faces in two different arrays
        if words[0][0] == "v":
            points.append([float(words[0][1]),float(words[0][2]),float(words[0][3])])

        elif words[0][0] == "f":
            faceVertex = []
            for i in range(len(words[0])-1):
                faceVertex.append(int(words[0][i+1]))
            faces.append(faceVertex)
            
    return[points,faces]
