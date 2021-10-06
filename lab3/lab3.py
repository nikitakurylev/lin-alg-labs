def readvector(f):
    temp = f.readline().split()
    return float(temp[0]), float(temp[1]), float(temp[2])

import math

def sum(vec1, vec2):
    return [vec1[0]+vec2[0],vec1[1]+vec2[1],vec1[2]+vec2[2]];
def sub(vec1, vec2):
    return [vec1[0]-vec2[0],vec1[1]-vec2[1],vec1[2]-vec2[2]];
def multi(vec, k):
    return [vec[0]*k,vec[1]*k,vec[2]*k];
def skal(vec1, vec2):
    return vec1[0]*vec2[0]+vec1[1]*vec2[1]+vec1[2]*vec2[2];
def leng(vec):
    return math.sqrt(vec[0]*vec[0]+vec[1]*vec[1]+vec[2]*vec[2])
def leng(vec):
    return math.sqrt(vec[0]*vec[0]+vec[1]*vec[1]+vec[2]*vec[2])
def angle(vec1, vec2):
    return math.acos(skal(vec1, vec2)/leng(vec1)/leng(vec2))/math.pi*180
def product(vec1, vec2):
    return [vec1[1]*vec2[2]-vec1[2]*vec2[1], vec1[2]*vec2[0]-vec1[0]*vec2[2], vec1[0]*vec2[1]-vec1[1]*vec2[0]]
def norm(vec):
    len = leng(vec)
    return [vec[0]/len,vec[1]/len,vec[2]/len]
def point(r, s, n, p):
    d = -n[0]*p[0]-n[1]*p[1]-n[2]*p[2]
    d += skal(r,n)
    temp = skal(s,n)
    if temp == 0:
        return -1
    d /= temp
    return sub(r, multi(s,d))
def reflect(v,n):
    n=norm(n)
    return sub(v, multi(n,2*skal(v,n)))

a,b,c,d,v,o=[],[],[],[],[],[]

f = open('input.txt', 'r')

cuben = []
cubep = []

a = readvector(f)
b = readvector(f)
c = readvector(f)
d = readvector(f)
cuben.append(sub(b,a))
cubep.append(a)
cuben.append(sub(a,b))
cubep.append(b)
cuben.append(sub(c,b))
cubep.append(b)
cuben.append(sub(b,c))
cubep.append(c)
cuben.append(sub(d,c))
cubep.append(c)
cuben.append(sub(c,d))
cubep.append(d)

v = readvector(f)#ориентация входа
o = readvector(f)#точка входа

e = int(f.readline())
n = int(f.readline())

normals = []
points = []

i=0
while i < n:
    p = readvector(f)
    q = readvector(f)
    r = readvector(f)
    points.append(p)
    vec1 = sub(q,p) # q[0]-p[0],q[1]-p[1],q[2]-p[2]
    vec2 = sub(r,p) # r[0]-p[0],r[1]-p[1],r[2]-p[2]
    normals.append(product(vec1,vec2))
    l = leng(normals[i])
    i+=1
f.close()

mini = -1
result = 0
while e>0:
    i=0
    mindist=float("inf")
    minp = 0
    while i<n:
        p = point(o,v,normals[i],points[i])
        if p == -1:
            i+=1
            continue
        dist = leng(sub(p,o))
        if dist<mindist and skal(v,sub(p,o))>0:
            mindist=dist
            minp=p
            mini=i
        i+=1
    i=0
    while i<6:
        p = point(o,v,cuben[i],cubep[i])
        if p == -1:
            i+=1
            continue
        dist = leng(sub(p,o))
        if dist<mindist and skal(v,sub(p,o))>0:
            mindist=dist
            minp=p
            result = 1
        i+=1
    o = minp
    if result == 1:
        break
    v = reflect(v, normals[mini])
    e-=1
f = open('output.txt', 'w')
f.write(str(result)+"\n")
if result == 0:
    f.write(str(o[0])+" "+str(o[1])+" "+str(o[2])+"\n")
else:
    f.write(str(e)+"\n")
    f.write(str(o[0])+" "+str(o[1])+" "+str(o[2])+"\n")
    f.write(str(v[0])+" "+str(v[1])+" "+str(v[2])+"\n")
f.close();