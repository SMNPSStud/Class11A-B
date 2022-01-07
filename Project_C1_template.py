import pygame, sys

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((400,600))


face=pygame.Rect(100,200,200,200)

while True:    
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         
    pygame.draw.rect(screen,(120,120,120),face)  
    
    pygame.display.update()
    clock.tick(30)



