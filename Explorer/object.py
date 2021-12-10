import random
import pygame

from .constants import Spaceship, screen, Astroid, Gravity, aim_cursor_image, bullet, WIDTH

class Drawer:
    def __init__(self, positionx, positiony):
        self.positionx = positionx
        self.positiony = positiony
    
    def Spaceship_draw(positionx, positiony):
        screen.blit(Spaceship, (positionx, positiony))

    def Astroid_draw(positionx, positiony):
        screen.blit(Astroid, (positionx, positiony))
    
    def planet_draw(planet, positionx, positiony):
        screen.blit(planet, (positionx, positiony))
    
    def Boss_draw():
        pass
    
    def Treasure_draw():
        pass

    def Arrows_draw():
        pass

    def Background_planet_draw():
        pass

class Spaceman(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.speed = speed
        self.direction = 1
        self.velocity_y = 0
        self.shoot_cooldown = 0
        self.jump = False
        self.in_air = False
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        animation_types = ['RunGunForward', 'Idle_Stand_Forward', 'Crouch_Forward', 'Jump']
        
        animation_file_numbers = {'RunGunForward': 3, 'Idle_Stand_Forward':1, 'Crouch_Forward': 1, 'Jump': 1}

        for animation in animation_types:
            temp_animation_list = []

            number_of_frames = animation_file_numbers[animation]

            for i in range(number_of_frames):
                spaceman = pygame.image.load(f'assets/Spacesoldier/{animation}/{i}.png')
                spaceman = pygame.transform.scale(spaceman, (int(spaceman.get_width() * scale), int(spaceman.get_height() * scale)))
                temp_animation_list.append(spaceman)
            self.animation_list.append(temp_animation_list)

        self.Spaceman_image = self.animation_list[self.action][self.frame_index]
        self.rect = self.Spaceman_image.get_rect()
        self.rect.center = (x, y)

    def moving(self, move_left, move_right):
        changeinX = 0
        changeinY = 0
        if move_left:
            changeinX = -self.speed
            self.flip = True
            self.direction = -1
        if move_right:
            changeinX = self.speed
            self.flip = False
            self.direction = 1

        if self.jump == True and self.in_air == False:
            self.velocity_y = -11
            self.jump = False
            self.in_air = True

        self.velocity_y += Gravity
        if self.velocity_y > 10:
            self.velocity_y

        changeinY  += self.velocity_y

        if self.rect.bottom + changeinY > 318:
            changeinY = 318 - self.rect.bottom
            self.in_air = False


        self.rect.x += changeinX
        self.rect.y += changeinY    

    def update_animation(self):
        ANIMATION_COOLDOWN = 100
        self.Spaceman_image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1

        if self.frame_index  >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def Spaceman_draw(self):
        screen.blit(pygame.transform.flip(self.Spaceman_image, self.flip, False), self.rect)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = bullet
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        self.rect.x += (self.direction * self.speed)
        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()


bullet_group = pygame.sprite.Group()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        animation_types = ['RunGunForward', 'Idle_Stand_Forward', 'Crouch_Forward', 'Jump']
        
        animation_file_numbers = {'RunGunForward': 3, 'Idle_Stand_Forward':1, 'Crouch_Forward': 1, 'Jump': 1}

        for animation in animation_types:
            temp_animation_list = []

            number_of_frames = animation_file_numbers[animation]

            for i in range(number_of_frames):
                enemy = pygame.image.load(f'assets/Spacesoldier/{animation}/{i}.png')#enemy image 
                enemy = pygame.transform.scale(enemy, (int(enemy.get_width() * scale), int(enemy.get_height() * scale)))
                temp_animation_list.append(enemy)
            self.animation_list.append(temp_animation_list)

        self.Enemy_image = self.animation_list[self.action][self.frame_index]
        self.rect = self.Enemy_image.get_rect()
        self.rect.center = (x, y)

    def moving(self, move_left, move_right):
        changeinX = 0
        changeinY = 0
        if move_left:
            changeinX = -self.speed
            self.flip = True
            self.direction = -1
        if move_right:
            changeinX = self.speed
            self.flip = False
            self.direction = 1


        if self.rect.bottom + changeinY > 318:
            changeinY = 318 - self.rect.bottom
            self.in_air = False


        self.rect.x += changeinX
        self.rect.y += changeinY    

    def update_animation(self):
        ANIMATION_COOLDOWN = 100
        self.Enemy_image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1

        if self.frame_index  >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def Spaceman_draw(self):
        screen.blit(pygame.transform.flip(self.enemy_image, self.flip, False), self.rect)



    



class Star:
  def __init__(self, screen_width, screen_height):
    self.radius = random.randint(1,2)
    self.color = (255,255,255)
    self.pos_x = random.randint(0, screen_width)
    self.pos_y = random.randint(0, screen_height)
    self.decrease = True
    self.done = True
    self.planet_tracker = []

  def stars(self, screen):
    t = random.randint(0,100)

    if t == 1 or t == 0:
      if self.decrease and self.radius > 1:
        self.radius -= 1
        self.decrease = False
      else:
        self.radius += 1
        self.decrease = True
    
    pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.radius)


