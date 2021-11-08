import pygame
pygame.init()

from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN, K_SPACE, K_ESCAPE)
from Explorer.constants import AstroidX, AstroidY, screen, Spaceship, FPS, WIDTH, HEIGHT
from Explorer.object import Drawer, Star


#caption And Icon
pygame.display.set_caption('Space Explorer')
pygame.display.set_icon(Spaceship)

def main():
    SpaceshipX, SpaceshipY = 370, 20
    SpacemanX, SpacemanY = 370, 480
    star_list = [Star(WIDTH, HEIGHT) for _ in range(300)]
    Astroid_position = [100, 200, 300, 400, 500, 600, 700, 800, 900]
    gravity = 5 #For full game change back to 12
    #AstroidX, AstroidY = 370, 370

    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False          
        
            if event.key == K_RIGHT:
                SpacemanX += 12
        
            if event.key == K_LEFT:
                SpacemanX -= 12

            if event.key == K_UP:
                SpacemanY  -= 20
        
            if event.key == K_SPACE:
                SpacemanY  -= 20

            if event.key == K_DOWN and SpacemanY <= 490:
                SpacemanY += 12

        SpaceshipX = SpaceshipX + 1
        
        if SpacemanY >= 490:
            gravity = 0

        if SpacemanY <= 490:
            gravity = 5

        SpacemanY += gravity

        screen.fill((0,0,0))
        
        for s in star_list:
            s.show(screen)

        Drawer.Spaceship_draw(SpaceshipX, SpaceshipY)
        Drawer.Spaceman_draw(SpacemanX, SpacemanY)
        
        
        #AstroidX = random.choice(Astroid_position)
        #AstroidY = random.choice(Astroid_position)
        #Drawer.Astroid_draw(AstroidX, AstroidY)

        pygame.display.update()
        pygame.display.flip()

    pygame.quit()

main()

'''
1) Speed up character movements
2) Find images from game
3) Build functions to draw these images in game
4) Build randimizer for some of the drawings
'''