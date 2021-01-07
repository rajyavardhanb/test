import pygame
import random
import time 
import os
import sys 



print ('Splash loaded') 
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.font.init()

#Splash screen

def loading():
	screen = pygame.display.set_mode((600,230),pygame.NOFRAME)
	background = pygame.Surface(screen.get_size()) 
	background.fill((16,24,32)) 
	screen.blit(background, (0,0)) 
	screen.blit(pygame.font.Font('resources//Font.ttf', 50).render('Snake Game', 10, (254,231,21)), (50,70)) 
	screen.blit(pygame.font.Font('resources//Font.ttf', 10).render('Created By', 10, (254,231,21)), (50,130))
	screen.blit(pygame.font.Font('resources//Font.ttf', 10).render('Rajyavardhan B.', 10, (254,231,21)), (70,150))
	screen.blit(pygame.font.Font('resources//Font.ttf', 7).render('Loading Matrix..', 10, (254,231,21)), (10,210))
	pygame.display.update() 
	time.sleep(0.5)

	#Matrix
	screen = pygame.display.set_mode((600,230),pygame.NOFRAME)
	background = pygame.Surface(screen.get_size()) 
	background.fill((16,24,32)) 
	screen.blit(background, (0,0)) 
	screen.blit(pygame.font.Font('resources//Font.ttf', 50).render('Snake Game', 10, (254,231,21)), (50,70)) 
	screen.blit(pygame.font.Font('resources//Font.ttf', 10).render('Created By', 10, (254,231,21)), (50,130))
	screen.blit(pygame.font.Font('resources//Font.ttf', 10).render('Rajyavardhan B.', 10, (254,231,21)), (70,150))
	screen.blit(pygame.font.Font('resources//Font.ttf', 7).render('Loading Matrix....', 10, (254,231,21)), (10,210))
	pygame.display.update() 
	time.sleep(0.5)

	#Prepraing Screen
	screen = pygame.display.set_mode((600,230),pygame.NOFRAME)
	background = pygame.Surface(screen.get_size()) 
	background.fill((16,24,32)) 
	screen.blit(background, (0,0)) 
	screen.blit(pygame.font.Font('resources//Font.ttf', 50).render('Snake Game', 10, (254,231,21)), (50,70)) 
	screen.blit(pygame.font.Font('resources//Font.ttf', 10).render('Created By', 10, (254,231,21)), (50,130))
	screen.blit(pygame.font.Font('resources//Font.ttf', 10).render('Rajyavardhan B.', 10, (254,231,21)), (70,150))
	screen.blit(pygame.font.Font('resources//Font.ttf', 7).render('Loading Screen', 10, (254,231,21)), (10,210))
	pygame.display.update() 
	time.sleep(0.5)

	screen = pygame.display.set_mode((600,230),pygame.NOFRAME)
	background = pygame.Surface(screen.get_size()) 
	background.fill((16,24,32)) 
	screen.blit(background, (0,0)) 
	screen.blit(pygame.font.Font('resources//Font.ttf', 50).render('Snake Game', 10, (254,231,21)), (50,70)) 
	screen.blit(pygame.font.Font('resources//Font.ttf', 10).render('Created By', 10, (254,231,21)), (50,130))
	screen.blit(pygame.font.Font('resources//Font.ttf', 10).render('Rajyavardhan B.', 10, (254,231,21)), (70,150))
	screen.blit(pygame.font.Font('resources//Font.ttf', 7).render('Loading Screen ..', 10, (254,231,21)), (10,210))
	pygame.display.update() 
	time.sleep(0.5)

	screen = pygame.display.set_mode((600,230),pygame.NOFRAME)
	background = pygame.Surface(screen.get_size()) 
	background.fill((16,24,32)) 
	screen.blit(background, (0,0)) 
	screen.blit(pygame.font.Font('resources//Font.ttf', 50).render('Snake Game', 10, (254,231,21)), (50,70)) 
	screen.blit(pygame.font.Font('resources//Font.ttf', 10).render('Created By', 10, (254,231,21)), (50,130))
	screen.blit(pygame.font.Font('resources//Font.ttf', 10).render('Rajyavardhan B.', 10, (254,231,21)), (70,150))
	screen.blit(pygame.font.Font('resources//Font.ttf', 7).render('Loading Screen ....', 10, (254,231,21)), (10,210))
	pygame.display.update() 
	time.sleep(0.5)

	#Starting
	screen = pygame.display.set_mode((600,230),pygame.NOFRAME)
	background = pygame.Surface(screen.get_size()) 
	background.fill((16,24,32)) 
	screen.blit(background, (0,0)) 
	screen.blit(pygame.font.Font('resources//Font.ttf', 50).render('Snake Game', 10, (254,231,21)), (50,70)) 
	screen.blit(pygame.font.Font('resources//Font.ttf', 10).render('Created By', 10, (254,231,21)), (50,130))
	screen.blit(pygame.font.Font('resources//Font.ttf', 10).render('Rajyavardhan B.', 10, (254,231,21)), (70,150))
	screen.blit(pygame.font.Font('resources//Font.ttf', 7).render('Starting..', 10, (254,231,21)), (10,210))
	pygame.display.update() 
	time.sleep(0.5)

	screen = pygame.display.set_mode((600,230),pygame.NOFRAME)
	background = pygame.Surface(screen.get_size()) 
	background.fill((16,24,32)) 
	screen.blit(background, (0,0)) 
	screen.blit(pygame.font.Font('resources//Font.ttf', 50).render('Snake Game', 10, (254,231,21)), (50,70)) 
	screen.blit(pygame.font.Font('resources//Font.ttf', 10).render('Created By', 10, (254,231,21)), (50,130))
	screen.blit(pygame.font.Font('resources//Font.ttf', 10).render('Rajyavardhan B.', 10, (254,231,21)), (70,150))
	screen.blit(pygame.font.Font('resources//Font.ttf', 7).render('Starting..', 10, (254,231,21)), (10,210))
	pygame.display.update() 
	time.sleep(0.5)

