import pygame
pygame.init() 

GREEN=(0,255,0)
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
size = (400, 400)

#Create a variable "playery" and set its value to 1
playery=1

player=pygame.Rect(190,350,20,20)
path=pygame.Rect(170,0,60,400)
border1=pygame.Rect(160,0,10,400)
border2=pygame.Rect(230,0,10,400)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Project C2")

carryOn = True
name = pygame.font.SysFont(None,24).render("Danny", True, WHITE)
name.get_rect(center=player.center)

while carryOn:
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
      carryOn = False    
          screen.fill(GREEN)

  #increment the y-coordinate of "player" rectangle by "playery"
  player.y=player.y+playery

  #Check if the y-coordinate of "player" rectangle is greater than or equal to 390
  if player.y>=390:

    #Change direction within the if statement
    playery=-playery

  #Check if the y-coordinate of "player" rectangle is lesser than or equal to 0
  if player.y<=0:

    #Change direction within the if statement
    playery=-playery

  screen.blit(name,player)
  pygame.draw.rect(screen,(0,0,0),path)
  pygame.draw.rect(screen,WHITE,border1)
  pygame.draw.rect(screen,WHITE,border2)
  pygame.draw.rect(screen,YELLOW,player)
  pygame.time.wait(5)
  pygame.display.flip()
pygame.quit()
