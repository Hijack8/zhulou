import cv2
import numpy as np
import json
pMatrix_file = 'projMatrix2.json'
point1_file = 'corner_point1.json'
point2_file = 'corner_point2.json'

with open(pMatrix_file,'r') as f:
    pMatrix_list = json.load(f)
pMatrix2 = np.float64(pMatrix_list)
with open(point1_file,'r') as f:
    point1 = json.load(f)
with open(point2_file,'r') as f:
    point2 = json.load(f)
point2 = np.float64(point2)
point1 = np.float64(point1)
pMatrix1 = np.array(([1,0,0,0],[0,1,0,0],[0,0,1,0]),dtype='float64')
coordinates_location = cv2.triangulatePoints(pMatrix1,pMatrix2,point1,point2)
coordinates_location = np.float64(coordinates_location)
coordinates_location = coordinates_location/coordinates_location[3]


print(coordinates_location)