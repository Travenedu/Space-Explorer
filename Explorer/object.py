import random
import pygame

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

class Star:
  def __init__(self, screen_width, screen_height):
    self.radius = random.randint(1,2)
    self.color = (255,255,255)
    self.pos_x = random.randint(0, screen_width)
    self.pos_y = random.randint(0, screen_height)
    self.decrease = True

  def show(self, screen):
    t = random.randint(0,100)

    if t == 1 or t == 0:
      if self.decrease and self.radius > 1:
        self.radius -= 1
        self.decrease = False
      else:
        self.radius += 1
        self.decrease = True
    
    pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.radius)