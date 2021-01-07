import pygame
import random
import time 
import os
import sys
import loading 



pygame.init()
loading.loading()

white = (255, 255, 255)
yellow = (254,231,21)
red = (213, 50, 80)
green = (43,174,102)
blue = (50, 153, 213)
whiteblack = (16,24,32)
orange = (242,170,76)
lblue=(139,190,232)

width = 700
height = 500

dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

font_style = pygame.font.Font("resources//Font.ttf", 16)
score_font = pygame.font.Font("resources//Font.ttf", 25)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, lblue)
    dis.blit(value, [5, 5])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, orange, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width / 30, height / 2])


def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Snake_Length = 1

    foodx1 = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody1 = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(whiteblack)
            message("You Lost! Press R To Restart or Q To Quit", white)
			
            Your_score(Snake_Length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(whiteblack)
        pygame.draw.rect(dis, green, [foodx1, foody1, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Snake_Length:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Snake_Length - 1)

        pygame.display.update()

        if x1 == foodx1 and y1 == foody1:
            foodx1 = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody1 = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Snake_Length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()
	
gameLoop()
