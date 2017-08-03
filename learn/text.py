import pygame
import time

pygame.init()
display = pygame.display.set_mode((400,400))
display.fill((255,255,255))

font = pygame.font.SysFont(None,30)

text = font.render("hello there",True,(255,0,0))
display.blit(text,[200,200])


pygame.display.update()
time.sleep(5)
pygame.quit()
quit()
