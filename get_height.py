import ast
import numpy as np
f1 = open("zuo.txt", "r")

def p2qi(p):
    return np.array([p[0] , p[1] , 1])

def getline_2p(p1, p2):
    return np.cross(p1, p2)


def normalization(p):
    p[0] /= p[2]
    p[1] /= p[2]
    p[2] = 1
    return p


def getp_2l(line1, line2):
    return normalization(np.cross(line1, line2))

def get_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

line = f1.readline()
line = ast.literal_eval(line)
p1 = p2qi(line[0])
line = ast.literal_eval(f1.readline())
p2 = p2qi(line[0])
line = ast.literal_eval(f1.readline())
p11 = p2qi(line[0])
line = ast.literal_eval(f1.readline())
p22 = p2qi(line[0])
line = ast.literal_eval(f1.readline())
p3 = p2qi(line[0])
line = ast.literal_eval(f1.readline())
p4 = p2qi(line[0])
line = ast.literal_eval(f1.readline())
p33 = p2qi(line[0])
line = ast.literal_eval(f1.readline())
p44 = p2qi(line[0])
line = ast.literal_eval(f1.readline())
H = p2qi(line[0])
line = ast.literal_eval(f1.readline())
D = p2qi(line[0])
line = ast.literal_eval(f1.readline())
Hp = p2qi(line[0])
line = ast.literal_eval(f1.readline())
Dp = p2qi(line[0])

line = ast.literal_eval(f1.readline())
H2 = p2qi(line[0])
line = ast.literal_eval(f1.readline())
D2 = p2qi(line[0])


f1.close()


print(p1)
print(p2)
line12 = getline_2p(p1, p2)
line1122 = getline_2p(p11, p22)

die1 = getp_2l(line12, line1122)

line34 = getline_2p(p3, p4)
line3344 = getline_2p(p33, p44)

die2 = getp_2l(line34, line3344)

print(getline_2p(p1, p2))

die_line = getline_2p(die1, die2)

groud_line = getline_2p(Dp, D)

die0 = getp_2l(groud_line, die_line)

head_line = getline_2p(die0, Hp)

building = getline_2p(H, D)

building2 = getline_2p(H2, D2)

sky = getp_2l(building, building2)

building_top = H

head_on_building = getp_2l(building, head_line)

building_down = D

ratio = (get_distance(building_top, building_down) / get_distance(head_on_building, building_down))   *    (get_distance(sky, head_on_building) / get_distance(sky, building_top))

Hr = ratio * 1.85

print("测量出来主楼高度为：")
print(Hr)
