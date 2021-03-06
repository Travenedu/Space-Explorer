import random
import pygame

from .constants import Spaceship, screen, Astroid, Gravity, game_font, bullet, WIDTH

class Drawer:
    def __init__(self, positionx, positiony):
        self.positionx = positionx
        self.positiony = positiony
    
    def Spaceship_draw(positionx, positiony):
        screen.blit(Spaceship, (positionx, positiony))
    
    def planet_draw(planet, positionx, positiony):
        screen.blit(planet, (positionx, positiony))
    
    def score_display(game_state, score, high_score):
        if game_state == 'main_game':
            score_surface = game_font.render(str(int(score)),True,(255,255,255))
            score_rect = score_surface.get_rect(center = (970, 50))
            screen.blit(score_surface, score_rect)
        if game_state == 'game_over':
            score_surface = game_font.render(f'Score: {int(score)}',True,(255,255,255))
            score_rect = score_surface.get_rect(center = (900, 50))
            screen.blit(score_surface, score_rect)

            high_score_surface = game_font.render(f'High score: {int(high_score)}',True,(255,255,255))
            high_score_rect = high_score_surface.get_rect(center = (300, 50))
            Again_score_surface = game_font.render('Press A to Restart', True, (255,255,255))
            Again_score_rect = high_score_surface.get_rect(center = (550, 100))
            
            screen.blit(high_score_surface, high_score_rect)
            screen.blit(Again_score_surface, Again_score_rect)

    def update_score(score, high_score):
        if score > high_score:
            high_score = score
        return high_score 
    

class Spaceman(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.health = 100
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
        self.rect = pygame.Rect(0,0,40,100)
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

        if self.rect.bottom + changeinY > 300:
            changeinY = 300 - self.rect.bottom
            self.in_air = False

        self.rect.x += changeinX
        self.rect.y += changeinY    

    def check_if_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            

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
        screen.blit(pygame.transform.flip(self.Spaceman_image, self.flip, False), (self.rect.x - 50, self.rect.y - 38))

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = bullet
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self, enemy):
        self.rect.x += (self.direction * self.speed)
        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

        if pygame.sprite.spritecollide(enemy, bullet_group, False):
            if enemy.alive:
               enemy.health -= 5
               enemy.kill()
        screen.blit(self.image, self.rect)

bullet_group = pygame.sprite.Group()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.health = 25
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        animation_types = ['Alien_walk', 'Alien_Attack', 'Alien_Death']
        animation_file_numbers = {'Alien_walk': 7,'Alien_Attack': 6, 'Alien_Death': 6}

        for animation in animation_types:
            temp_animation_list = []

            number_of_frames = animation_file_numbers[animation]

            for i in range(number_of_frames):
                enemy = pygame.image.load(f'assets/Alien_Enemy/{animation}/{i}.png')#enemy image 
                enemy = pygame.transform.scale(enemy, (int(enemy.get_width() * scale), int(enemy.get_height() * scale)))
                temp_animation_list.append(enemy)
            self.animation_list.append(temp_animation_list)

        self.Enemy_image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect(0, 0, 70, 100)
        self.rect.center = (x, y)

    def moving(self, target):
        changeinX = 0
        changeinY = 0
        if self.rect.left > target.rect.right:
            #move left
            changeinX = -self.speed
            self.flip = True
            self.direction = -1
        if self.rect.right < target.rect.left:
            #move right
            changeinX = self.speed
            self.flip = False
            self.direction = 1

        if self.rect.bottom + changeinY > 350:
            changeinY = 350 - self.rect.bottom
            self.in_air = False

        if self.rect.right < 200 or self.rect.left > WIDTH:
            self.kill()

        self.rect.x += changeinX
        self.rect.y += changeinY    

    def attack(self, target):
        if target.rect.right - 10 < self.rect.left <= target.rect.right + 10 or target.rect.left - 10 < self.rect.right <= target.rect.left + 10:
            target.health -= 5

    def check_if_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            
    def update_animation(self):
        ANIMATION_COOLDOWN = 100
        self.Enemy_image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1

        if self.frame_index  >= len(self.animation_list[self.action]):
            if self.action == 2:
                self.frame_index  = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def update_bullet(self, bullet):
        if pygame.sprite.spritecollide(bullet, alien_group, False):
            if self.alive:
                self.health = 0
                bullet.kill()

    def update(self, target):
        if self.health <= 0:
            self.update_action(2)
        elif target.rect.right - 10 < self.rect.left <= target.rect.right + 10 or target.rect.left - 10 < self.rect.right <= target.rect.left + 10:
            self.attack(target)
            self.update_action(1)

        else:
            self.moving(target)
            self.update_action(0)

        
        self.update_animation()
        screen.blit(pygame.transform.flip(self.Enemy_image, self.flip, False), (self.rect.x - 40, self.rect.y - 10))

alien_group = pygame.sprite.Group()

    
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


