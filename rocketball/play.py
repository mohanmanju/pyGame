import pygame
import rocket
import math
import random

pygame.init()
display = pygame.display.set_mode((400,400))

white = (255,255,255)
red = (255,0,0)

clock = pygame.time.Clock()

WIDTH,HEIGHT = pygame.display.get_surface().get_size()

display.fill(white)
#pygame.draw.rect(display,(255,0,0),[150,150,50,50])
pygame.display.update()

img = pygame.image.load("rocket.png").convert_alpha()
imgrect = img.get_rect()

#display.blit(img,[WIDTH/2,HEIGHT-40,10,40])
pygame.display.flip()

x = WIDTH/2
y = HEIGHT-40

rotate = 45



exit = False

while not exit:

    clock.tick(20)
    rotate = random.randrange(-90,90)
    img = pygame.image.load("rocket.png").convert_alpha()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                exit = True
    display.fill(white)
    img = pygame.transform.rotate(img,rotate)
    display.blit(img,(x+10,y+20))
    pygame.display.flip()
    y-=math.cos(rotate*math.pi/180)
    x-=math.sin(rotate*math.pi/180)

pygame.quit()
quit()
