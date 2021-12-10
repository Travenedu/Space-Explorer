import pygame

WIDTH, HEIGHT = 1200,800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
FPS = 60
Gravity = 0.75

#spaceship
Spaceship = pygame.transform.scale(pygame.image.load('assets/Game Utilities/tiny_ship.png'), (88, 50))
SpaceshipX, SpaceshipY = 370, 20

# bullet
bullet = pygame.image.load('assets/Game Utilities/Bullet.png')
#aim cursor
aim_cursor_image = pygame.image.load('assets/Game Utilities/aim_cursor.png')

#astroid Note: Using planet as place holder
Astroid = pygame.transform.scale(pygame.image.load('assets/Planets/Ice_planet.png'), (50, 50))
AstroidX, AstroidY = 370, 370

#planets
planet1 = pygame.transform.scale(pygame.image.load('assets/Planets/Ice_planet.png'), (50, 50))
planet2 = pygame.transform.scale(pygame.image.load('assets/Planets/sun.png'), (50, 50))
planet3 = pygame.transform.scale(pygame.image.load('assets/Planets/mars.png'), (50, 50))
planet4 = pygame.transform.scale(pygame.image.load('assets/Planets/Emeraldar/emeraldar_norings.png'), (50, 50))

