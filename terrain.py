import pygame
import random as rd
pg = pygame

class Terrain(pg.sprite.Sprite): 
    
    def __init__(self, screen, nb_points=0):
         pg.sprite.Sprite.__init__(self) #pygame sprit init 
         
         self.screen = screen
         self.nb_points = nb_points
         self.points = []
         self.landing_pos = []
         
    def generate_terrain(self,mode="default"):
        self.points = []
        self.landing_pos = []
        if mode == "default":
            x = 0
            prev_y = rd.randint(self.screen.get_height()//2, self.screen.get_height())
            pente = 0
            for i in range(self.nb_points):
                self.points.append((x,prev_y))
                
                if rd.random()>0.1:
                    y = rd.randint(prev_y-50,prev_y+50)
                    count = 0
                    while (y>self.screen.get_height() or y<self.screen.get_height()*1/5 or not (abs(pente)<20 or pente*(y-prev_y)>0)) and count<1000:
                        y = rd.randint(prev_y-50,prev_y+50)
                        count+=1
                    pente = y-prev_y
                    prev_y = y
                    x += rd.randint(self.screen.get_width()/(self.nb_points), 3*self.screen.get_width()//(2*self.nb_points))
                else:
                    prev_x = x
                    x += rd.randint(self.screen.get_width()/(self.nb_points), 3*self.screen.get_width()//(2*self.nb_points))
                    self.landing_pos.append(((prev_x,prev_y),(x,prev_y)))
    
    def update(self):
        pos_prev = self.points[0]
        for pos in self.points[1:]:
            pygame.draw.line(self.screen,(255,255,255),pos_prev,pos)
            pos_prev = pos
        for land_pos in self.landing_pos:
            pos1, pos2 = land_pos
            pygame.draw.line(self.screen,(0,0,255),pos1,pos2)
