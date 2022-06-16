import cv2
import numpy as np
import json
import scipy.io
pMatrix_file = 'projMatrix2.json'
point1_file = 'corner_point1.json'
point2_file = 'corner_point2.json'
matlab_file = 'point.mat'
with open(pMatrix_file,'r') as f:
    pMatrix_list = json.load(f)
pMatrix2 = np.float64(pMatrix_list)
with open(point1_file,'r') as f:
    point1 = json.load(f)
with open(point2_file,'r') as f:
    point2 = json.load(f)

def calculate_location(point1=point1,point2=point2):
    point2 = np.float64(point2).T
    point1 = np.float64(point1).T

    pMatrix1 = np.array(([1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]),
                        dtype='float64')
    coordinates_location = cv2.triangulatePoints(pMatrix1, pMatrix2, point1,
                                                 point2)
    coordinates_location = np.float64(coordinates_location)
    coordinates_location = coordinates_location / coordinates_location[3]
    return coordinates_location


coordinates_location = calculate_location()

print(coordinates_location)
for i in range(coordinates_location.shape[1]):
        print("p" + str(i + 1) + " " + str(coordinates_location[0][i]) + "," + str(coordinates_location[1][i]) + "," + str(coordinates_location[2][i]))

location_dict = scipy.io.loadmat(matlab_file)
location_dict['x'] = coordinates_location[0]
location_dict['y'] = coordinates_location[1]
location_dict['z'] = coordinates_location[2]
scipy.io.savemat(matlab_file,location_dict)
