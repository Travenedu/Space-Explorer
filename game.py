import pygame
pygame.init()

from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN, K_SPACE, K_ESCAPE)
from constants import WIDTH, HEIGHT, first_object, second_object, FPS

screen = pygame.display.set_mode([WIDTH, HEIGHT])

#testing drawing
def first_object_draw(positionx, positiony):
    screen.blit(first_object, (positionx, positiony))

def second_object_draw(positionx, positiony):
    screen.blit(second_object, (positionx, positiony))

#caption And Icon
pygame.display.set_caption('Not decided')
pygame.display.set_icon(first_object)



def main():
    first_objectX, first_objectY = 370, 20
    second_objectX, second_objectY = 370, 480
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
                    second_objectX = second_objectX + 30
            
                if event.key == K_LEFT:
                    second_objectX = second_objectY - 30

                if event.key == K_UP:
                    second_objectY = second_objectY - 30
            
                if event.key == K_SPACE:
                    pass
                    #second_objectY = second_objectY - 30

                if event.key == K_DOWN:
                    second_objectY = second_objectY + 30

            first_objectX = first_objectX + 1


        screen.fill((0,0,0))

        first_object_draw(first_objectX, first_objectY)
        second_object_draw(second_objectX, second_objectY)
        pygame.display.update()
        #pygame.display.flip()

    pygame.quit()

main()