from turtle import Vec2D
from PIL import Image
import pygame 
from time import sleep
from pygame.locals import *


class NFT:
   
    def __init__(self):
        pygame.init()
        self.WIDTH = 360
        self.HEIGHT = 360
        self.image_path="image.jpg"
        self.image_path1="image1.jpg"
        self.img =None
        self.offset=(180,240)
        self.offset1=(240,240)
    
    def display(self):
        print(self.image_path,self.WIDTH,self.HEIGHT)
        windowSurface = pygame.display.set_mode((self.WIDTH, self.HEIGHT), 0, 0)
        self.img = pygame.image.load(self.image_path)
        shadow = pygame.image.load(self.image_path1)
        # print(windowSurface.get_rect().center)
        # print(type(windowSurface.get_rect().center))
        
        logo_rect =self.img.get_rect(center=self.offset)
        logo_rect1 =shadow.get_rect(center=self.offset1)
        # windowSurface.blit(self.img, (0, 0))
        windowSurface.fill((0,0,0))
        windowSurface.blit(self.img, logo_rect)
        windowSurface.blit(shadow, logo_rect1)
        pygame.display.update()

