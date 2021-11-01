import pygame

WIDTH, HEIGHT = 1200,800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
FPS = 60

#spaceship
Spaceship = pygame.transform.scale(pygame.image.load('assets/tiny_ship.png'), (88, 50))
SpaceshipX, SpaceshipY = 370, 20

#spaceman
Spaceman = pygame.transform.scale(pygame.image.load('assets/Spaceman.png'), (88, 50))
SpacemanX, SpacemanY = 370, 480

#astroid Note: Using planet as place holder
Astroid = pygame.transform.scale(pygame.image.load('assets/Ice_planet.png'), (50, 50))
AstroidX, AstroidY = 370, 370
