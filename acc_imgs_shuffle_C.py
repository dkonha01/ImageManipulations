import os
import glob
import time
import pygame
import adxl345
from SimpleCV import *
print __doc__

my_images_pathA = "/home/pi/imageA" #put your image path here if you want to override current directory
extension = "*.jpg"
my_images_pathB = "/home/pi/imageB"
my_images_pathC = "/home/pi/imageC"
accel = adxl345.ADXL345()
axes = accel.getAxes(True)


pathA = my_images_pathA
pathB = my_images_pathB
pathC = my_images_pathC

imgs = list() #load up an image list
directoryA = os.path.join(pathA, extension)
filesA = glob.glob(directoryA)

imgs = list()
directoryB = os.path.join(pathB, extension)
filesB = glob.glob(directoryB)

imgs = list()
directoryC = os.path.join(pathC, extension)
filesC = glob.glob(directoryC)

while True:

        axes = accel.getAxes(True)
        x = axes['x']
        y = axes['y']
        z = axes['z']

        random.shuffle(filesA)
        random.shuffle(filesB)
        random.shuffle(filesC)
        new_imgA = Image(filesA[1])
        disp = Display((800,800))
        pygame.mouse.set_visible(False)
        new_imgB = Image(filesB[1])
        new_imgC = Image(filesC[1])


        if x > .95:
             newer_img = new_imgA + new_imgB
             disp.writeFrame(newer_img)

        elif y < -.65:
             newer_img = new_imgB.invert() - new_imgA
             disp.writeFrame(newer_img)

        else:
             newer_img = new_imgC
             disp.writeFrame(newer_img)
