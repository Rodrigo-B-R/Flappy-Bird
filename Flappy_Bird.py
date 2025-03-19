import pygame
import sys
import os
import random 

pygame.init()

pygame.display.set_caption('Flappy Bird')
clock=pygame.time.Clock()
size = width, height = 1000, 800

screen = pygame.display.set_mode(size)

font= pygame.font.Font(None, 50 )

bird_surface = pygame.transform.scale(pygame.image.load(os.path.join('images','bird.png')).convert_alpha(),(100,100))
background_surface= pygame.transform.scale(pygame.image.load(os.path.join('images','background.png')),(width,height))
text_surface =   font.render('Flappy Bird', True  , 'Green')


def pipes():
    gap= height/5

    min_height= height/6
    max_height= height-gap-min_height
    
    lower_tube_height= random.randint(int(min_height), int(max_height))
    upper_tube_height= int(height - lower_tube_height - gap)

    tube_width= int(width/8)

    lower_position= int(upper_tube_height+gap)

    upper_tube_surface= pygame.transform.scale(pygame.image.load(os.path.join('images','tube_image_rotated.png')),(tube_width, upper_tube_height))
    lower_tube_surface= pygame.transform.scale(pygame.image.load(os.path.join('images','tube_image.png')),(tube_width, lower_tube_height))  

    return [upper_tube_surface,lower_tube_surface,lower_position]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        # if event.type == pygame.K_SPACE:


    
    
    upper_tube, lower_tube, lower_position = pipes()
    # pygame.Surface.convert_alpha()
    screen.blit(background_surface,(0,0))

    screen.blit(upper_tube,(500,0)) #upper tube
    screen.blit(lower_tube,(500,lower_position)) #lower tube
    screen.blit(text_surface,(200,200))
    screen.blit(bird_surface, (200,350))
    
    pygame.display.update()
    clock.tick(1)



    


