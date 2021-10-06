import math

def skal(x1, y1, z1, x2, y2, z2):
  return x1*x2+y1*y2+z1*z2;
def leng(x, y, z):
  return math.sqrt(x*x+y*y+z*z)
def angle(x1, y1, z1, x2, y2, z2):
  return math.acos(skal(x1, y1, z1, x2, y2, z2)/leng(x1,y1,z1)/leng(x2,y2,z2))/math.pi*180
def product(x1, y1, z1, x2, y2, z2):
  return y1*z2-z1*y2, z1*x2-x1*z2, x1*y2-y1*x2

f = open('input.txt', 'r')

vx, vy = f.readline().split(' ')
vx, vy = int(vx), int(vy)

ax, ay = f.readline().split(' ')
ax, ay = int(ax), int(ay)

mx, my = f.readline().split(' ')
mx, my = int(mx), int(my)

wx, wy = f.readline().split(' ')
wx, wy = int(wx), int(wy)

f.close()

wx -= vx;
wy -= vy;

cx, cy, cz = product(mx,my,1,ax,ay,0)

ang = angle(cx,cy,0,wx,wy,0)
dir = angle(ax,ay,0,wx,wy,0)
side = 1
if ang>90:
    ang = 180 - ang
    side = -1
if ang>60:
    side = 0
if dir>90:
    ang = -ang
mat = angle(mx,my,1,0,0,1);
if cz>0:
    mat=-mat
f = open('output.txt', 'w')
f.write(str(side)+"\n")
f.write(str(ang)+"\n")
f.write(str(mat)+"\n")
f.write("Arrivederci\n")
f.close()
