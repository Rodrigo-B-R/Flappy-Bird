import pygame
import sys
import os
import random 
 

pygame.init()

pygame.display.set_caption('Flappy Bird')
clock=pygame.time.Clock()
size = width, height = 1500, 800

screen = pygame.display.set_mode(size)

font= pygame.font.Font(None, 50 )


bird_surface = pygame.transform.scale(pygame.image.load(os.path.join('images','bird.png')).convert_alpha(),(100,100))
background_surface= pygame.transform.scale(pygame.image.load(os.path.join('images','background.png')),(width,height))



tube_list= []

SPAWN_PIPE= pygame.USEREVENT+1 #create a pygame event and call it every x seconds
pygame.time.set_timer(SPAWN_PIPE,2500)


def pipes():
    gap= int(height/4)

    min_height= int(height/6)
    max_height= int(height-gap-min_height)
    
    lower_tube_height= random.randint(int(min_height), int(max_height))
    upper_tube_height= int(height - lower_tube_height - gap)

    tube_width= int(width/8)

    lower_position= int(upper_tube_height+gap)

    upper_tube_surface= pygame.transform.scale(pygame.image.load(os.path.join('images','tube_image_rotated.png')),(tube_width, upper_tube_height))
    lower_tube_surface= pygame.transform.scale(pygame.image.load(os.path.join('images','tube_image.png')),(tube_width, lower_tube_height))  

    tube_list.append({"Top Tube":upper_tube_surface,"Bottom Tube": lower_tube_surface,"x": width , 'y': lower_position })
    #create a list containing a dictionary with the values and add each new tube to the list

seconds=0  
g= 1.5
flap_strength = -7
bird_velocity_y = 0
bird_position_y= 350



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
        screen.blit(tube['Top Tube'],(tube['x'], 0))
        screen.blit(tube['Bottom Tube'],(tube['x'], tube['y']))
        tube['x'] -= 5 #displacement left
        

    tube_list = [tube for tube in tube_list if tube["x"] > - int(width/8)] #delete tubes after they have passed the screen

    seconds += dt
    bird_velocity_y += g * seconds
    bird_position_y += bird_velocity_y 

    if bird_position_y > height: sys.exit()

    screen.blit(bird_surface, (200,bird_position_y))

    
    pygame.display.update()
    clock.tick(60)



    


