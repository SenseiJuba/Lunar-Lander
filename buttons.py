import pygame as pg

class Button(pg.sprite.Sprite): 
    
    def __init__(self, screen, images, pos=(0,0), hovering=0):
         pg.sprite.Sprite.__init__(self) #pygame sprit init 
         
         self.screen = screen
         self.images = images
         self.hovering = hovering
         self.image = self.images[self.hovering]
         self.rect = (self.image.get_rect()) #Note that the image does not subscribe auto in the rect 
         self.pos = pos #position of the scribble
         self.rect.center = pos
         
    def change_state(self):
        self.hovering = 0 if self.state == 1 else 1
        self.image = self.images[self.hovering]
        
    def clone(self,x,y):
        return Button(x,y,self.state,self.images)
    
    def update(self):
        self.image = self.images[self.hovering]
        self.screen.blit(self.image, self.rect)
        
    def is_over(self,pos):
        return self.rect.collidepoint(pos)