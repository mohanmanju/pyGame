import pygame

clock = pygame.time.Clock()

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

snake_x = 200
snake_y = 200

x = pygame.init()
display = pygame.display.set_mode((400,400))

pygame.display.update()
exit = False
change_x = 0
change_y = 0
while not exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_LEFT):
                change_x = -10
            if(event.key == pygame.K_RIGHT):
                change_x = 10
            if(event.key == pygame.K_UP):
                change_y = -10
            if(event.key == pygame.K_DOWN):
                change_y = 10
        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                change_x = 0
            if(event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                change_y = 0

    snake_x += change_x
    snake_y += change_y
    display.fill(white)
    pygame.draw.rect(display,red,[snake_x,snake_y,50,50])
    pygame.display.update()
    clock.tick(30)
    pygame.time.wait(1)
pygame.quit()
quit()
