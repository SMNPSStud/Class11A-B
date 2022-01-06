import pygame
pygame.init() 
screen = pygame.display.set_mode((600, 600))

box1= pygame.Rect(300, 500, 60, 10)
box2= pygame.Rect(200, 320, 60, 10)
box3= pygame.Rect(120, 300, 60, 10)
box4= pygame.Rect(200, 500, 60, 10)
box5= pygame.Rect(320, 325, 60, 10)

carryOn = True
while carryOn:
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                  carryOn = False           
    screen.fill((36,90,190))
    
pygame.draw.rect(screen,(255,192,203),box1)
pygame.draw.rect(screen,(255,192,203),box2)
pygame.draw.rect(screen,(255,192,203),box3)
pygame.draw.rect(screen,(255,192,203),box4)
pygame.draw.rect(screen,(255,192,203),box5)
    
    
pygame.display.flip()
pygame.quit()
