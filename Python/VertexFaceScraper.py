lines = []
g = open("TeapotData.txt","w")

f = open("Teapot.txt","r")
for line in f:
    words = []
    words.append(line.split(" "))
    #if first letter of the line is v, write to new text doc "g"
    if words[0][0]=="v":
        g.write(line)
    #if first letter is f, remove normals and shader data and the write to "g"
    if words[0][0]=="f":
        writeFaces = "\n"
        faces = line.replace("/"," ")
        splitFaces = []
        splitFaces.append(faces.split(" "))
        for i in range(len(words[0])-1):
            writeFaces = " {}{}".format(splitFaces[0][((i+1)*3)-2],writeFaces)
        writeFaces = "f{}".format(writeFaces)
        g.write(writeFaces)
g.close()
f.close()


