# showPixelValue.py
import json

import cv2
import numpy as np

POINTS_NUM = 10 #需要多少个点
points_pointer = 0
arg1 = '../mission2/zhu_2.jpg'
json_file = 'corner_point2.json'
def getMousePos(img):
    points_set = []
    global points_pointer
    points_pointer = 0
    def onmouse(event, x, y, flags, param):
        cv2.imshow("img", img)
        global points_pointer
        # if event==cv2.EVENT_MOUSEMOVE:
        # print(img[y,x], " pos: ", x, " x ", y)
        # 双击左键，显示鼠标位置
        if event == cv2.EVENT_LBUTTONDOWN:
            strtext = str(points_pointer + 1)
            cv2.circle(img, (x, y), 4, (0, 0, 255), 6)
            cv2.putText(img, strtext, (x + 2, y + 15),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 200), 1)
            points_set.append((x,y))
            if len(points_set) == POINTS_NUM:
                 with open(json_file,'w') as f:
                     json.dump(points_set,f)
            return

    cv2.namedWindow("img", cv2.WINDOW_NORMAL)

    print(img.shape)

    cv2.setMouseCallback("img", onmouse)
    if (cv2.waitKey() & 0xFF == 27):  # 按下‘q'键，退出
        return points_set
        cv2.destroyAllWindows()


def showPixelValue(imgName):
    img = cv2.imread(imgName)

    def onmouse(event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE:
            print(img[y, x])

    cv2.namedWindow("img")
    cv2.setMouseCallback("img", onmouse)
    cv2.imshow("img", img)
    if cv2.waitKey() == ord('q'):  # 按下‘q'键，退出
        cv2.destroyAllWindows()


if __name__ == '__main__':
    img1 = cv2.imread(arg1,0)
    pts = getMousePos(img1)
    print(pts)