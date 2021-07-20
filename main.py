import pygame
from pygame import locals as const
import time
import buttons
import game

def main():

    pygame.init()

    screen = pygame.display.set_mode((1000, 1000))
    
    # Import des images du menu
    
    fond = pygame.image.load("images/fond.png").convert_alpha()
    #icon = pygame.image.load("images/icon.png").convert_alpha()
    title = pygame.image.load("images/title.png").convert_alpha()
    play_button_images = [pygame.image.load("images/play_button.png").convert_alpha(),pygame.image.load("images/play_button2.png").convert_alpha()]
    options_button_images = [pygame.image.load("images/options_button.png").convert_alpha(),pygame.image.load("images/options_button2.png").convert_alpha()]
    
    # Déclaration des variables 
    count = 0
    pos_title = (screen.get_width()/2, 200)
    pos_play_button = (screen.get_width()/2,400)
    pos_options_button = (screen.get_width()/2,600)
    w, h = title.get_size()
    title_time = time.time()
    continuer = True
    
    # Création des buttons
    
    play_button = buttons.Button(screen, play_button_images, pos_play_button)
    options_button = buttons.Button(screen, options_button_images, pos_options_button)
    
    # Création du jeu
    
    jeu = game.Game(screen)

    while continuer:
        for event in pygame.event.get():
            if event.type == const.QUIT or (event.type == const.KEYDOWN and event.key == const.K_ESCAPE):
                # de manière à pouvoir quitter le menu avec echap ou la croix
                continuer = 0
            if event.type == const.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if play_button.is_over(pos):
                    jeu.start()
                
            else:
                pos = pygame.mouse.get_pos()
                if play_button.is_over(pos):
                    play_button.hovering = True
                else:
                    play_button.hovering = False
                    
                if options_button.is_over(pos):
                    options_button.hovering = True
                else:
                    options_button.hovering = False
                
        
        screen.blit(fond, (0,0))
        
        play_button.update()
        options_button.update()
        
        
        x,y=pos_title
        blitRotate(screen, title, (x,y+real_pos(count)), (w//2,h//2), real_angle(count))
        
        if time.time() - title_time > 0.04:
            count += 1 
            title_time = time.time()

        pygame.display.flip()

    pygame.quit()

def real_pos(count):
    return 0
    if (count//33)%4 == 0:
        return count%33
    elif (count//33)%4 == 1:
        return 33-(count%33)
    elif (count//33)%4 == 2:
        return -(count%33)
    else:
        return -33+(count%33)

def real_angle(angle):
    if (angle//22)%4 == 0:
        return angle%22
    elif (angle//22)%4 == 1:
        return 22-(angle%22)
    elif (angle//22)%4 == 2:
        return -(angle%22)
    else:
        return -22+(angle%22)
    

def blitRotate(surf, image, pos, originPos, angle):

    # calcaulate the axis aligned bounding box of the rotated image
    w, h       = image.get_size()
    box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    # calculate the translation of the pivot 
    pivot        = pygame.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move   = pivot_rotate - pivot

    # calculate the upper left origin of the rotated image
    origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)

    # rotate and blit the image
    surf.blit(rotated_image, origin)


if __name__ == '__main__':
    main()