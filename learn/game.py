import pygame


x = pygame.init()
display = pygame.display.set_mode((400,400))

pygame.display.update()
exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    display.fill((255,255,255))
    pygame.display.update()

pygame.quit()
quit()
