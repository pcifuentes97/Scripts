import slideio
import cv2
import numpy as np

imagefile = '/home/lambdaworkstation/Documents/Pathogen_slides/Cancer/Korea/Training/Training_phase_1_001/01_01_0083.svs'
maskFile =  '/home/lambdaworkstation/Documents/Pathogen_slides/Cancer/Korea/Training/Training_phase_1_001/01_01_0083_whole.tif'
slide = slideio.open_slide(imagefile, driver_id="SVS")
scene = slide.get_scene(0)
img = cv2.imread(scene, 0)
maskimg = cv2.imread(maskFile,0)
