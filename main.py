import pygame
import random
from pygame.locals import *
import time

def changeBackground(img):
    background = pygame.image.load(img)
    bg = pygame.transform.scale(background, (screen_width, screen_height))
    screen.blit(bg,(0,0))

pygame.init()
pygame.display.set_caption("Recycle Marathon")
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bin.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,60))
        self.rect = self.image.get_rect()

class Recyclable(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()

class Non_recyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("plastic.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()

images = ["item1.png", "item2.png", "item3.png"]

item_list = pygame.sprite.Group()
allsprites = pygame.sprite.Group()
plastic_list = pygame.sprite.Group()