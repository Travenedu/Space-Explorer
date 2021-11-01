import random
from .constants import Spaceman, Spaceship, screen, Astroid

class Drawer:
    def __init__(self, positionx, positiony):
        self.positionx = positionx
        self.positiony = positiony
    
    def Spaceship_draw(positionx, positiony):
        screen.blit(Spaceship, (positionx, positiony))

    def Spaceman_draw(positionx, positiony):
        screen.blit(Spaceman, (positionx, positiony))

    def Astroid_draw(positionx, positiony):
        screen.blit(Astroid, (positionx, positiony))

    def Boss_draw():
        pass
    
    def Treasure_draw():
        pass

    def Arrows_draw():
        pass

    def Background_planet_draw():
        pass

    def Stars_draw():
        pass
