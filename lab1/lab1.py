def ReadMatrix(M):
    n, m = f.readline().split()
    n, m = [int(n), int(m)]
    data = f.readline().split()
    i = 0
    M = []
    for i in range (0, n):
        temp = []
        for j in range (0, m):
            temp.append(float(data[i*m+j]))
        M.append(temp)
    return M

def WriteMatrix(M):
    m, n = MatrixLength(M)
    s = ""
    for j in range (0, m):
        for i in range (0, n):
                s += str(M[j][i])+" "
    f.write(s+"\n")

def SumMatrices(M1, M2):
    m, n = MatrixLength(M1)
    p, o = MatrixLength(M2)
    if n != o or m != p :
        return []
    for i in range (0, n):
        for j in range (0, m):
            M1[j][i] += M2[j][i]
    return M1

def MultiplyMatrix(M1, a):
    m, n = MatrixLength(M1)
    for i in range (0, n):
        for j in range (0, m):
            M1[j][i] *= a
    return M1

def MultiplyMatrices(M1, M2):
    n, m = MatrixLength(M1)
    o, p = MatrixLength(M2)
    M = []
    if o != m :
        return M
    for i in range (0, n):
        temp = []
        for j in range (0, p):
            temp.append(0)
            for k in range (0, m):
                temp[j] += M1[i][k]*M2[k][j]
        M.append(temp)
    return M

def TransposeMatrix(M1):
    n, m = MatrixLength(M1)
    M = []
    for i in range (0, m):
        temp = []
        for j in range (0, n):
            temp.append(M1[j][i])
        M.append(temp)
    return M

def MatrixLength(M):
    n = len(M)
    if n > 0 :
        return n, len(M[0])
    else :
        return 0, 0


A=[]
B=[]
C=[]
D=[]
F=[]
f = open('input.txt', 'r')
a, b = f.readline().split()
a, b = [float(a), float(b)]
A = ReadMatrix(A)
B = ReadMatrix(B)
C = ReadMatrix(C)
D = ReadMatrix(D)
F = ReadMatrix(F)
f.close()

X = MultiplyMatrix(B,b)
X = TransposeMatrix(X)
X = SumMatrices(MultiplyMatrix(A, a), X)
X = TransposeMatrix(X)
X = MultiplyMatrices(C, X)
X = MultiplyMatrices(X, D)
X = SumMatrices(X, MultiplyMatrix(F, -1))

f = open('output.txt', 'w')
if X == [] :
    f.write("0\n")
else :
    f.write("1\n")
    f.write(str(len(X)) + " " + str(len(X[0])) + "\n")
    WriteMatrix(X)
f.close();
