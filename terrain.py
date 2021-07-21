import pygame
import random as rd
pg = pygame

class Terrain(pg.sprite.Sprite): 
    
    def __init__(self, screen, nb_points=0):
         pg.sprite.Sprite.__init__(self) #pygame sprit init 
         
         self.screen = screen
         self.nb_points = nb_points
         self.points = []
         
    def generate_terrain(self,mode="default"):
        self.points = []
        if mode == "default":
            x = 0
            prev_y = rd.randint(0, self.screen.get_width()/2)
            pente = 0
            for i in range(self.nb_points):
                self.points.append((x,1000-prev_y))
                x += rd.randint(self.screen.get_width()/(self.nb_points), 3*self.screen.get_width()//(2*self.nb_points))
                if rd.random()>0.1:
                    y = rd.randint(self.screen.get_height()//3, self.screen.get_height())
                    while abs(y-prev_y)>100:
                        if True or pente<20 or pente*(y-prev_y)>=0:
                            y = rd.randint(0, self.screen.get_height())
                    pente = y-prev_y
                    prev_y = y
    
    def update(self):
        pos_prev = self.points[0]
        for pos in self.points[1:]:
            pygame.draw.line(self.screen,(255,255,255),pos_prev,pos)
            pos_prev = pos
