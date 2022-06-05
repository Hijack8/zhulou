import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import json
import get_point
img1 = cv.imread('zhu_1.jpg',0)  #queryimage # left image
img2 = cv.imread('zhu_2.jpg',0) #trainimage # right image
k = np.array(([3026.5,0,0],
             [0,3048.6,0],
             [2009.4,1611,1]),dtype='float64')
k = k.T
pts1 = []
pts2 = []
with open('point1.json','r') as f:
    pts1 = json.load(f)
with open('point2.json','r') as f:
    pts2 = json.load(f)
#pts1 = get_point.getMousePos(img1)
#pts2 = get_point.getMousePos(img2)
pts1 = np.int32(pts1)
pts2 = np.int32(pts2)
F, mask = cv.findFundamentalMat(pts1,pts2,cv.FM_LMEDS)
l1 = np.linalg.norm(F,1)
F = F/l1
u,d,v = np.linalg.svd(F)
'''d[2] = 0
F = u.dot(d).dot(v)'''
E = k.T.dot(F).dot(k)
u,d,v = np.linalg.svd(E)
W = np.array(([0,-1,0],
             [1,0,0],
             [0,0,1]))
t1 = u[:][2]
R1 = u.dot(W).dot(v.T)
if np.linalg.det(R1) <0:
    t1 = -t1
    R1 = -R1
print("t1:"+str(t1))
print("R1:"+str(R1))
