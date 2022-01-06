import pygame
pygame.init() 
screen = pygame.display.set_mode((600, 600))

#Create the box here
box=pygame.Rect(300,500,60,10)
box1=pygame.Rect(250,450,40,10)
box2=pygame.Rect(200,300,60,10)


carryOn = True
while carryOn:
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                  carryOn = False           
    screen.fill((36,90,190))
    
    pygame.draw.rect(screen,(255,192,203),box)
    pygame.draw.rect(screen,(254,193,204),box1)
    screen=pygame.display.set_mode(600,600)
    pygame.display.flip()
pygame.quit()
    