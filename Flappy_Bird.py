import pygame
import sys
import os
import random 
 

pygame.init()

pygame.display.set_caption('Flappy Bird')
clock=pygame.time.Clock()
size = width, height = 1200, 800

screen = pygame.display.set_mode(size)

font= pygame.font.Font(None, 50 )

seconds=0  
g= 1.5
flap_strength = -7
bird_velocity_y = 0
bird_position_y= 350


bird_surface = pygame.transform.scale(pygame.image.load(os.path.join('images','bird.png')).convert_alpha(),(30,30))
bird_rect= bird_surface.get_rect(center=(200, bird_position_y))

background_surface= pygame.transform.scale(pygame.image.load(os.path.join('images','background.png')),(width,height))


font = pygame.font.Font(None,50)
lose_surface= font.render('YOU LOST', True, (255, 0, 0))



tube_list= []

SPAWN_PIPE= pygame.USEREVENT+1 #create a pygame event and call it every x seconds
pygame.time.set_timer(SPAWN_PIPE,2500)


def pipes():
    gap= int(height/4)

    min_height= int(height/8)
    max_height= int(height-gap-min_height)
    
    lower_tube_height= random.randint(int(min_height), int(max_height))
    upper_tube_height= int(height - lower_tube_height - gap)

    tube_width= int(width/10)

    lower_position= int(upper_tube_height+gap)

    upper_tube_surface= pygame.transform.scale(pygame.image.load(os.path.join('images','tube_image_rotated.png')).convert_alpha(),(tube_width, upper_tube_height))
    lower_tube_surface= pygame.transform.scale(pygame.image.load(os.path.join('images','tube_image.png')).convert_alpha(),(tube_width, lower_tube_height))  

    upper_tube_rect= upper_tube_surface.get_rect(topleft= (width,0))
    lower_tube_rect= lower_tube_surface.get_rect(topleft= (width,lower_position))

    tube_list.append({"Top Tube":upper_tube_surface,"Bottom Tube": lower_tube_surface,
                      'upper_rect':upper_tube_rect,'lower_rect': lower_tube_rect})
    #create a list containing a dictionary with the values and add each new tube to the list



lost=False

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type ==  SPAWN_PIPE: #the pygame event calls the pipe function wich will add a new pipe to the list
            pipes()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: 
                bird_velocity_y = flap_strength
                seconds=0

    
    dt = clock.tick(60) / 1000  

    screen.blit(background_surface,(0,0))


    for tube in tube_list: 

        if not lost:

            tube['upper_rect'].x -=5 
            tube['lower_rect'].x -=5 

            tube['upper_rect'].topleft =(tube['upper_rect'].x,tube['upper_rect'].y) #update the position of the rectangle
            tube['lower_rect'].topleft =(tube['lower_rect'].x,tube['lower_rect'].y)

        screen.blit(tube['Top Tube'],tube['upper_rect']) #(surface, rectangle)
        screen.blit(tube['Bottom Tube'], tube['lower_rect'])

      
    

    tube_list = [tube for tube in tube_list if tube["upper_rect"].x > - int(width/8)] #delete tubes after they have passed the screen

    seconds += dt
    bird_velocity_y += g * seconds
    bird_position_y += bird_velocity_y 

    if bird_position_y > height: sys.exit()

    
    
    bird_rect.center=(200,bird_position_y)
    screen.blit(bird_surface, bird_rect)

    for i, tube in enumerate(tube_list):
        if bird_rect.colliderect(tube['upper_rect']) or bird_rect.colliderect(tube['lower_rect']):
            screen.blit(lose_surface,(int(width/2.5),int(height/4)))
            lost= True
            break

    pygame.display.update()
    clock.tick(60)



    


