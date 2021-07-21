##Spaceship class##
import pygame
import math
import operator

from pygame import locals as const
pg = pygame

class Spaceship(pg.sprite.Sprite):
    images = {
        "idle" : None
        }
    def __init__(self, thrust_power_):
        pg.sprite.Sprite.__init__(self) #pygame sprit init
        self.image = self.images["idle"]
        self.rect = self.image.get_rect()
        self.angle = 0
        self.gravity = 10
        self.acc = (0,0)
        self.speed = (0,0)
        self.thrust_power = thrust_power_ 
    
    def rotate(self, howmuch):
        self.angle += howmuch
    
    def thrust_level_update(self, value):
        self.thrust_level += value
        if self.thrust_level <= 0:
            self.thrust_level = 0
        if self.thrust_level >= 3:
            self.thrust_level = 3
    
    def apply_forces(self):
        self.acc = (math.sin(self.angle)*self.thrust_power, self.gravity - math.cos(self.angle)*self.thrust_power)
        self.rect.center = (self.rect.center[0]+self.acc[0], self.rect.center[1]+self.rect.center[1])
        self.speed = (self.speed[0] + self.acc[0], self.speed[1] + self.acc[1])