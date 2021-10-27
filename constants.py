import pygame

WIDTH, HEIGHT = 1200,800

FPS = 60

first_object = pygame.transform.scale(pygame.image.load('assets/tiny_ship.png'), (88, 50))
first_objectX, first_objectY = 370, 20

second_object = pygame.transform.scale(pygame.image.load('assets/Spaceman.png'), (88, 50))
second_objectX, second_objectY = 370, 480