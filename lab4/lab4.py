def readplane(f):
    temp = f.readline().split()
    return [float(temp[0]), float(temp[1]), float(temp[2])], [float(temp[3]), float(temp[4]), float(temp[5])]

def sub(vec1, vec2):
    return [vec1[0]-vec2[0],vec1[1]-vec2[1],vec1[2]-vec2[2]]
def det(vec0, vec1, vec2):
    return vec0[0]*vec1[1]*vec2[2] - vec0[0]*vec1[2]*vec2[1] - vec0[1]*vec1[0]*vec2[2] + vec0[1]*vec1[2]*vec2[0] - vec0[2]*vec1[1]*vec2[0] + + vec0[2]*vec1[0]*vec2[1]
def factord(norm, p):
    return -norm[0]*p[0]-norm[1]*p[1]-norm[2]*p[2]
def skal(vec1, vec2):
    return vec1[0]*vec2[0]+vec1[1]*vec2[1]+vec1[2]*vec2[2];
def product(vec1, vec2):
    return [vec1[1]*vec2[2]-vec1[2]*vec2[1], vec1[2]*vec2[0]-vec1[0]*vec2[2], vec1[0]*vec2[1]-vec1[1]*vec2[0]]
def isunderplane(point, planenorm, planep):
    return skal(point,planenorm)<=-factord(planenorm, planep)+0.1
def intersect(n1, p1, n2, p2, n3, p3):
    delta = det(n1, n2, n3)
    if delta == 0:
        return -1
    d1 = factord(n1, p1)
    d2 = factord(n2, p2)
    d3 = factord(n3, p3)

    result = [0,0,0]
    result[0] = -(det([d1, n1[1], n1[2]],[d2, n2[1], n2[2]],[d3, n3[1], n3[2]]))/delta
    result[1] = -(det([n1[0], d1, n1[2]],[n2[0], d2, n2[2]],[n3[0], d3, n3[2]]))/delta
    result[2] = -(det([n1[0], n1[1], d1],[n2[0], n2[1], d2],[n3[0], n3[1], d3]))/delta
    return result;

f = open("input.txt", "r")

n = int(f.readline())

normals = []
points = []

i=0
while i < n:
    normal, point = readplane(f)
    normals.append(normal)
    points.append(point)
    i+=1
f.close()

vertices = []
vertplanes = []
v = 0

i=0
while i < n-2:
    j=i+1
    while j < n-1:
        k=j+1
        while k < n:
            tmp = intersect(normals[i],points[i],normals[j],points[j],normals[k],points[k])
            print(tmp)
            if tmp != -1:
                isunder = True
                l=0
                while l<n:
                    isunder = isunderplane(tmp,normals[l],points[l])
                    if not isunder:
                        break
                    l+=1
                l=0
                while l<v and isunder:
                    isunder = not(vertices[l]==tmp)
                    l+=1
                if isunder:
                    vertices.append(tmp)
                    vertplanes.append([i,j,k])
                    v+=1
            k+=1
        j+=1
    i+=1

edges = []
e = 0

i=0
while i < v-1:
    j=i+1
    while j < v:
        k = 0
        tmp=0
        while k < 3:
            if  vertplanes[i][k] == vertplanes[j][0] or vertplanes[i][k] == vertplanes[j][1] or vertplanes[i][k] == vertplanes[j][2]:
                tmp+=1
            k+=1
        if tmp == 2:
            exists = False
            k=0
            while k < e:
                if [vertices[i],vertices[j]] == edges[k]:
                    #exists = True
                    break
                k+=1
            if not exists:
                edges.append([vertices[i],vertices[j]])
                e+=1
        j+=1
    i+=1

isinoneplane = True
i=0
while i < v-3 and isinoneplane:
    j=i+1
    while j < v-2 and isinoneplane:
        k=j+1
        while k < v-1 and isinoneplane:
            l=k+1
            while l < v and isinoneplane:
                point1 = sub(vertices[j], vertices[i])
                point2 = sub(vertices[k], vertices[i])
                point3 = sub(vertices[l], vertices[i])
                isinoneplane = abs(det(point1,point2,point3)) < 0.00001
                l+=1
            k+=1
        j+=1
    i+=1



f = open("output.txt", "w")
if not isinoneplane:
    f.write(str(e)+"\n")
    i=0
    while i < e:
        j=0
        while j < 3:
            f.write(str(edges[i][0][j])+" ")
            j+=1
        j=0
        while j < 3:
            f.write(str(edges[i][1][j])+" ")
            j+=1
        f.write("\n")
        i+=1
else:
    f.write("0")
f.close()

