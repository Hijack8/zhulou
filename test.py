from PIL import Image
from pylab import *

f1 = open('homo.txt',"w")
im1 = array(Image.open('zhu_6.jpg'))
imshow(im1)

for i in range(4):
    x = ginput(1)
    f1.write(str(x))
    f1.write("\n")
    print('you clicked1:', x)

f1.close()
