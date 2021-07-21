import pygame
from pygame import locals as const
import random as rd
import terrain
pg = pygame

class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.continuer = True
        self.terrain = terrain.Terrain(screen,100)
        self.h = screen.get_height()
        self.w = screen.get_width()
    
    def prepare(self):
        pygame.key.set_repeat(200, 50)
        self.continuer = True
        self.terrain.generate_terrain()
        self.update_screen()

    
    def update_screen(self):
        pygame.draw.rect(self.screen, (0,0,0), (0, 0) + self.screen.get_size())
        self.terrain.update()
        
    def process_event(self, event: pygame.event):
        if event.type == const.MOUSEBUTTONDOWN:
            print(event.pos)
        if event.type == const.KEYDOWN and event.key == const.K_RIGHT:
            print("truc")
        if event.type == const.KEYDOWN and event.key == const.K_ESCAPE:
            self.continuer = False
        if event.type == const.QUIT:
            pg.quit()
        
                
    
    def start(self):
        self.prepare()
        
        while self.continuer:
            for event in pygame.event.get():
                self.process_event(event)
            
            self.update_screen()
            
            pygame.display.flip()