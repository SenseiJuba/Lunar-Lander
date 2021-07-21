##Spaceship class##
import pygame
from pygame import locals as const
pg = pygame

class Spaceship(pg.sprite.Sprite):
    images = {
        "idle" : None
        }
    def __init__(self):
        pg.sprite.Sprite.__init__(self) #pygame sprit init
        self.image = self.images["idle"]
        self.rect = self.image.get_rect()
        self.angle = 0
        self.weight = 