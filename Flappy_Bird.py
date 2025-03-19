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


tube_list= []

SPAWN_PIPE= pygame.USEREVENT+1 #create a pygame event and call it every 5 seconds
pygame.time.set_timer(SPAWN_PIPE,1000)


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

    tube_list.append({"Top Tube":upper_tube_surface,"Bottom Tube": lower_tube_surface,"x": width , 'y': lower_position })
    #create a list containing a dictionary with the values and add each new tube to the list
   


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type ==  SPAWN_PIPE: #the pygame event calls the pipe function wich will add a new pipe to the list
            pipes()


    screen.blit(background_surface,(0,0))

    for tube in tube_list: 
        screen.blit(tube['Top Tube'],(tube['x'], 0))
        screen.blit(tube['Bottom Tube'],(tube['x'], tube['y']))
        tube['x'] -= 5
        

    tube_list = [tube for tube in tube_list if tube["x"] > - int(width/8)]

    screen.blit(text_surface,(200,200))
    screen.blit(bird_surface, (200,350))
    
    pygame.display.update()
    clock.tick(60)



    


