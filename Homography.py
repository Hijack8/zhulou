'''
取得4个相对应的点 计算Homography矩阵
'''
import ast
import numpy as np
from numpy.linalg import svd
from PIL import Image
from pylab import *


def getline_2p(p1, p2):
    return np.cross(p1, p2)


def normalization(p):
    p[0] /= p[2]
    p[1] /= p[2]
    p[2] = 1
    return p


def getp_2l(line1, line2):
    return normalization(np.cross(line1, line2))


def nullspace(A, atol=1e-13, rtol=0):
    A = np.atleast_2d(A)
    u, s, vh = svd(A)
    tol = max(atol, rtol * s[0])
    nnz = (s >= tol).sum()
    ns = vh[nnz:].conj().T
    return ns

f1 = open("homo.txt", 'r')

def p2qi(p):
    return np.array([p[0] , p[1] , 1])

v = []
line = ast.literal_eval(f1.readline())
v.append(p2qi(line[0]))
line = ast.literal_eval(f1.readline())
v.append(p2qi(line[0]))
line = ast.literal_eval(f1.readline())
v.append(p2qi(line[0]))
line = ast.literal_eval(f1.readline())
v.append(p2qi(line[0]))

u = []
q1 = np.array([0, 0, 1])
q2 = np.array([535, 0, 1])
q3 = np.array([0, 730, 1])
q4 = np.array([536, 730, 1])
u.append(q1)
u.append(q2)
u.append(q3)
u.append(q4)

A = np.array([])

for i in range(4):
    A0 = np.array([[v[i][0] , v[i][1], 1, 0, 0, 0, -v[i][0] * u[i][0], -u[i][0] * v[i][1], -u[i][0]] , [0, 0, 0, v[i][0], v[i][1], 1, -v[i][0] * u[i][1], -u[i][1] * v[i][1], -u[i][1]]])
    if(i == 0):
        A = A0
    else :
        A = np.vstack((A, A0))

H = nullspace(A).reshape(3,3)

print("right + head")
print(normalization(H.dot(v[1])))

# 已经求出了H矩阵
# 下面只需要进行一下后向变换即可

p_list = []
max_x = 0
max_y = 0
min_x = 1e10
min_y = 1e10
for i in range(4):
    if v[i][0] < min_x:
        min_x = v[i][0]
    if v[i][0] > max_x:
        max_x = v[i][0]
    if v[i][1] > max_y:
        max_y = v[i][1]
    if v[i][1] < min_y:
        min_y = v[i][1]

line12 = getline_2p(v[0], v[1])
line13 = getline_2p(v[0], v[2])
line34 = getline_2p(v[2], v[3])
line42 = getline_2p(v[3], v[1])

for i in range(int(min_x), int(max_x)):
    for j in range(int(min_y), int(max_y)):
        p = np.array([i, j, 1])
        if(p.dot(line12.T) * v[2].dot(line12.T) > 0):
            pass
        else:
            continue
        if(p.dot(line13.T) * v[1].dot(line13.T) > 0):
            pass
        else:
            continue
        if(p.dot(line42.T) * v[0].dot(line42.T) > 0):
            pass
        else:
            continue
        if(p.dot(line34.T) * v[0].dot(line34.T) > 0):
            pass
        else:
            continue
        p_list.append(p)


# 得到所有需要修改的点的坐标 p_list
# 接下来对每个点进行变换即可：

im_zhu = array(Image.open('zhu_6.jpg'))
im_liv = array(Image.open('liv.jpg'))
imshow(im_liv)
error = 0
right = 0

for i in p_list:
    p = normalization(H.dot(i.T))
    p[0] = int(p[0])
    p[1] = int(p[1])
    try:
        im_zhu[i[1]][i[0]] = im_liv[int(p[1])][int(p[0])]
        right += 1
    except:
        error += 1
        pass

'''
for i in range(int(min_x), int(max_x)):
    for j in range(int(min_y), int(max_y)):
        p = np.array([i,j,1])
        p = normalization(H.dot(p.T))
        try:
            im_zhu[j][i] = im_liv[int(p[1])][int(p[0])]
        except:
            pass
'''



print(right)

plt.imshow(im_zhu)
plt.show()