import pygame
from pygame.locals import *

SIZE = 640, 480
pygame.init()
screen = pygame.display.set_mode(SIZE)

done = False
screen.fill((255, 255, 255))
other1 = pygame.image.load("rocket.png").convert_alpha()
other2 = pygame.transform.rotate(other1, 270)
screen.blit(other2, (0, 0))
pygame.display.flip()

while not done:
    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            done = True
            break
