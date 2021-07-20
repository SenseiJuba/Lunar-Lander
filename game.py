import pygame
from pygame import locals as const
import random as rd

class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.continuer = True
        self.terrain = []
    
    def prepare(self):
        pygame.key.set_repeat(200, 50)
        self.continuer = True
        self.terrain = []
        y = rd.randint(400, 1000)
        for x in range(0,1001,20):
            y = self.heigth_y(y) 
            self.terrain.append((x,y))
        self.update_screen()
    
    def heigth_y(self,prev_y):
        if rd.random()<0.1:
            return prev_y
        y = rd.randint(0, 1000)
        while abs(y-prev_y)>100 or y<400:
            y = rd.randint(0, 1000)
        return y
    
    def update_screen(self):
        pygame.draw.rect(self.screen, (0,0,0), (0, 0) + self.screen.get_size())
        pos_prev = self.terrain[0]
        for pos in self.terrain[1:]:
            pygame.draw.line(self.screen,(255,255,255),pos_prev,pos)
            pos_prev = pos
        
    def process_event(self, event: pygame.event):
        if event.type == const.MOUSEBUTTONDOWN:
            print(event.pos)
        if event.type == const.KEYDOWN and event.key == const.K_RIGHT:
            print("truc")
        if event.type == const.QUIT:
            self.continuer = False
                
    
    def start(self):
        self.prepare()
        
        while self.continuer:
            for event in pygame.event.get():
                self.process_event(event)
            
            self.update_screen()
            
            pygame.display.flip()