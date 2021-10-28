import pygame
pygame.init()

from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN, K_SPACE, K_ESCAPE)
from Explorer.constants import screen, Spaceship, FPS
from Explorer.object import Drawer

#screen = pygame.display.set_mode([WIDTH, HEIGHT])

#testing drawing
#def Spaceship_draw(positionx, positiony):
    #screen.blit(Spaceship, (positionx, positiony))

#def Spaceman_draw(positionx, positiony):
    #screen.blit(Spaceman, (positionx, positiony))

#caption And Icon
pygame.display.set_caption('Space Explorer')
pygame.display.set_icon(Spaceship)

def main():
    SpaceshipX, SpaceshipY = 370, 20
    SpacemanX, SpacemanY = 370, 480
    running = True
    clock = pygame.time.Clock()
    #draw = Drawer()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False          
            
                if event.key == K_RIGHT:
                    SpacemanX = SpacemanX + 30
            
                if event.key == K_LEFT:
                    SpacemanX = SpacemanY - 30

                if event.key == K_UP:
                    SpacemanY = SpacemanY - 30
            
                if event.key == K_SPACE:
                    pass
                    #SpacemanY = SpacemanY - 30

                if event.key == K_DOWN:
                    SpacemanY = SpacemanY + 30

            SpaceshipX = SpaceshipX + 1

        screen.fill((0,0,0))

        Drawer.Spaceship_draw(SpaceshipX, SpaceshipY)
        Drawer.Spaceman_draw(SpacemanX, SpacemanY)
        pygame.display.update()
        #pygame.display.flip()

    pygame.quit()

main()