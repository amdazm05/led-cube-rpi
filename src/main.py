import time
from PIL import Image
img = Image.open("image.jpg")
img.show()
 
#  

import pygame 
from time import sleep
from pygame.locals import *
pygame.init()
WIDTH = 480
HEIGHT = 480
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)
img = pygame.image.load("image.jpg")
windowSurface.blit(img, (0, 0))
pygame.display.flip()

while(True):
    sleep(1)