import tifffile
import math
import numpy as np
import cv2
from PIL import Image


mask1 = Image.open('/home/lambdaworkstation/infected.tif')
mask2 = Image.open('/home/lambdaworkstation/Holelessmask.tif')

buffer1 = np.asarray(mask1)
buffer2 = np.asarray(mask2)
buffer3 = buffer2 - buffer1

newimage = Image.fromarray(buffer3)

newimage.show()
newimage.save("difference.png")
