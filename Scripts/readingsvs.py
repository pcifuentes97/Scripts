import openslide
from openslide import open_slide
import numpy as np
import math
import os
import PIL
import cv2

SCALE_FACTOR = 64

scan = openslide.OpenSlide('/home/lambdaworkstation/Documents/Pathogen_slides/Cancer/Korea/Training/Training_phase_1_001/01_01_0083.svs')
orig_w = np.int(scan.properties.get('aperio.OriginalWidth'))
orig_h = np.int(scan.properties.get('aperio.OriginalHeight'))
print(orig_w)
print(orig_h)
print(scan.level_dimensions[0])
print(scan.level_dimensions[1])
print(scan.level_dimensions[2])

large_w, large_h = scan.dimensions
new_w = math.floor(large_w / SCALE_FACTOR)
new_h = math.floor(large_h / SCALE_FACTOR)
level = scan.get_best_level_for_downsample(SCALE_FACTOR)
whole_scan_image = scan.read_region((0, 0), level, scan.level_dimensions[level])
whole_scan_image = whole_scan_image.convert("RGB")
#img = cv2.cv.CreateImageHeader(whole_scan_image.size, cv.IPL_DEPTH_8U, 3)
img = whole_scan_image.resize((new_w, new_h), PIL.Image.BILINEAR)
# img.show()

opencvImage = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)


cv2.imshow("img", opencvImage)
cv2.waitKey(0)

k = cv2.waitKey(0)
# if k == 27:         # wait for ESC key to exit
#     cv2.destroyAllWindows()
# elif k == ord('s'): # wait for 's' key to save and exit
#     cv2.destroyAllWindows()



import tifffile
import math
SCALE_FACTOR = 64

mask = tifffile.imread('/home/lambdaworkstation/Documents/Pathogen_slides/Cancer/Korea/Training/Training_phase_1_001/01_01_0083_whole.tif')
mask = mask * 255
large_w, large_h = mask.shape
new_w = math.floor(large_w / SCALE_FACTOR)
new_h = math.floor(large_h / SCALE_FACTOR)
res = cv2.resize(mask, dsize=(new_h, new_w), interpolation=cv2.INTER_CUBIC)
cv2.imshow("image", res)
cv2.imwrite("mask.png",res)
cv2.waitKey(0)
k = cv2.waitKey(0)
# if k == 27:         # wait for ESC key to exit
#     cv2.destroyAllWindows()
# elif k == ord('s'): # wait for 's' key to save and exit
#     cv2.destroyAllWindows()
mask3ch = np.zeros_like(opencvImage)
mask3ch [:,:,0] = res
mask3ch [:,:,1] = res
mask3ch [:,:,2] = res
mask3ch[:,:,2] = np.where(mask3ch[:,:,2] > 1, 0 ,mask3ch[:,:,2])
blend = cv2.addWeighted(opencvImage, 0.9, mask3ch, 0.1, 0.0)
cv2.imshow("blend2", blend)
cv2.waitKey(0)
# cv2.destroyAllWindows()
cv2.destroyAllWindows()
