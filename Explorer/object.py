from .constants import Spaceman, Spaceship, screen

class Drawer:
    def __init__(self, positionx, positiony):
        self.positionx = positionx
        self.positiony = positiony
    
    def Spaceship_draw(positionx, positiony):
        screen.blit(Spaceship, (positionx, positiony))

    def Spaceman_draw(positionx, positiony):
        screen.blit(Spaceman, (positionx, positiony))