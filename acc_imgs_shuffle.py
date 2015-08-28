import os
import glob
import time
import pygame
import adxl345
from SimpleCV import *
print __doc__

#Settings
my_images_pathA = "/home/pi/imageA" #put your image path here if you want to override current directory
extension = "*.jpg"
my_images_pathB = "/home/pi/imageB"
accel = adxl345.ADXL345()
#axes = accel.getAxes(True)

pathA = my_images_pathA
pathB = my_images_pathB
  
imgs = list() #load up an image list
directoryA = os.path.join(pathA, extension)
filesA = glob.glob(directoryA)

imgs = list()
directoryB = os.path.join(pathB, extension)
filesB = glob.glob(directoryB)

while True:

        random.shuffle(filesA)
        random.shuffle(filesB)
        new_imgA = Image(filesA[1])
        disp = Display((800,800))
        pygame.mouse.set_visible(False)
        new_imgB = Image(filesB[1])
        newer_img = new_imgA + new_imgB
        disp.writeFrame(newer_img)





