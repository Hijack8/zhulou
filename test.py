from PIL import Image
from pylab import *

f1 = open('zuo.txt',"w")
im1 = array(Image.open('zhu_p_1.jpg'))
imshow(im1)

for i in range(14):

    x = ginput(1)
    f1.write(str(x))
    f1.write("\n")
    print('you clicked1:', x)

f1.close()

