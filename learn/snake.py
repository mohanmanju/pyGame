import pygame
import time
import random

clock = pygame.time.Clock()

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

x = pygame.init()
display = pygame.display.set_mode((800,500))
WIDTH, HEIGHT = pygame.display.get_surface().get_size()

pygame.display.update()

block_size = 10

def disp_message(mes):
    font = pygame.font.SysFont(None,30) #size 30
    text = font.render(mes,True,red)  #true for antiallising
    display.blit(text,[200,200]) #putting font onto the game display with position
    pygame.display.update()

def getApplePos():
    apple_x = round(random.randrange(0,WIDTH)/block_size)*block_size
    apple_y = round(random.randrange(0,HEIGHT)/block_size)*block_size
    return apple_x,apple_y

def draw_snake(snakeList):
    i = len(snakeList)
    while i >0:
        pos = snakeList[i-1]
        pygame.draw.rect(display,green,[pos[0],pos[1],block_size,block_size])
        i-=1
    #for pos in snakeList:
        #pygame.draw.rect(display,green,[pos[0],pos[1],block_size,block_size])

def gameLoop():

    snake_x = 200
    snake_y = 200

    exit = False
    gameOver = False
    change_x = 0
    change_y = 0
    snakelength = 1

    while not exit:
        apple_x,apple_y = getApplePos()
        snakeList = []
        nextMove = [True,True,True,True]
        while not gameOver:

            #apple_x = random.randrange(0,WIDTH)
            #apple_y = random.randrange(0,HEIGHT)

            clock.tick(15)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True
                elif event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_LEFT and nextMove[0]):
                        change_x = -10
                        change_y = 0
                        nextMove =[True,False,True,True]
                    elif(event.key == pygame.K_RIGHT and nextMove[1]):
                        change_x = 10
                        change_y = 0
                        nextMove =[False,True,True,True]
                    elif(event.key == pygame.K_UP and nextMove[2]):
                        change_y = -10
                        change_x = 0
                        nextMove =[True,True,True,False]
                    elif(event.key == pygame.K_DOWN and nextMove[3]):
                        change_y = 10
                        change_x = 0
                        nextMove =[True,True,False,True]
                '''elif(event.type == pygame.KEYUP):
                    if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                        change_x = 0
                    elif(event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                        change_y = 0'''
            #for ends here

            snake_x += change_x
            snake_y += change_y
            display.fill(white)
            pygame.draw.rect(display,red,[apple_x,apple_y,block_size,block_size])

            snake = []
            snake.append(snake_x)
            snake.append(snake_y)
            snakeList.append(snake)
            if(len(snakeList)>snakelength):
                snakeList = snakeList[1:]

            for snakeblocks in snakeList[:-1]:
                if snakeblocks == snake:
                    display.fill(white)
                    disp_message("Crashed!!... You loose")
                    gameOver = True

            draw_snake(snakeList)
            pygame.display.update()

            if(snake_x >= WIDTH or snake_x < 0 or snake_y >= HEIGHT or snake_y <0 ):
                display.fill(white)
                disp_message("Crashed!!... You loose")
                #time.sleep(5)
                gameOver = True

            if snake_x == apple_x and snake_y == apple_y:
                apple_x,apple_y = getApplePos()
                '''snake[0] = snake_x + change_x
                snake[1] = snake_y + change_y
                snakeList.append(snake)'''
                snakelength+=1
        #gameOver while ends here

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit = True
                    break
                if event.key == pygame.K_p:
                    snake_x = 200
                    snake_y = 200
                    change_x = 0
                    change_y = 0
                    gameOver = False
                    break
    pygame.quit()
    quit()

gameLoop()
