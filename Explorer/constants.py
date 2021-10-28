import pygame

WIDTH, HEIGHT = 1200,800

FPS = 60

Spaceship = pygame.transform.scale(pygame.image.load('assets/tiny_ship.png'), (88, 50))
SpaceshipX, SpaceshipY = 370, 20

Spaceman = pygame.transform.scale(pygame.image.load('assets/Spaceman.png'), (88, 50))
SpacemanX, SpacemanY = 370, 480

screen = pygame.display.set_mode([WIDTH, HEIGHT])