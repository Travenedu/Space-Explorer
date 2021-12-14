import pygame
pygame.init()

from Explorer.constants import screen, Spaceship, FPS, WIDTH, HEIGHT, planet1, planet2, planet3, planet4
from Explorer.object import Drawer, Star, Spaceman,  Bullet, Enemy, bullet_group, alien_group


#caption And Icon
pygame.display.set_caption('Space Fighter')
pygame.display.set_icon(Spaceship)

def main():
    running = True
    clock = pygame.time.Clock()
    move_left = False
    game_over = False
    move_right = False
    crouch = False
    shoot = False
    score = 0
    high_score = 0

    Max_ememies = 10
    enemy_timer = 1000
    last_enemy = pygame.time.get_ticks()
    enemies_live = 0

    SpaceshipX, SpaceshipY = 370, 20
    star_list = [Star(WIDTH, HEIGHT) for _ in range(300)]
    #bullet = bullet()
    Spaceman_soldier = Spaceman(318, 200, 3, 7)
    Alien_Enemy = Enemy(1200, 250, 1.5, 3)

    while running:
        clock.tick(FPS)
        if game_over == False:
            screen.fill((0,0,0))
            pygame.draw.line(screen, (255,0,0), (0, 300), (WIDTH, 300))

            for s in star_list:
                s.stars(screen)
            
            #Spaceship
            Drawer.Spaceship_draw(SpaceshipX, SpaceshipY)
            #Draws planets in specific areas
            Drawer.planet_draw(planet1, 350, 100)
            Drawer.planet_draw(planet2, 650, 700)
            Drawer.planet_draw(planet3, 850, 300)
            Drawer.planet_draw(planet4, 550, 400)
            #Spaceman
            Spaceman_soldier.update_animation()
            Spaceman_soldier.Spaceman_draw()
            
            if len(alien_group) < Max_ememies:
                if pygame.time.get_ticks() - last_enemy > enemy_timer:
                    Alien_Enemy = Enemy(1200, 250, 1.5, 3)
                    alien_group.add(Alien_Enemy)
                    last_enemy = pygame.time.get_ticks()

            #bullets
            bullet_group.draw(screen)


            if Spaceman_soldier.alive:
                if shoot:
                    if Spaceman_soldier.shoot_cooldown == 0:
                        Spaceman_soldier.shoot_cooldown = 24
                        bullet = Bullet((Spaceman_soldier.rect.centerx - 20)+ (((Spaceman_soldier.rect.size[0]) -10) * Spaceman_soldier.direction), Spaceman_soldier.rect.centery, Spaceman_soldier.direction)
                        bullet_group.add(bullet)
                    if Spaceman_soldier.shoot_cooldown != 0:
                        Spaceman_soldier.shoot_cooldown -= 4

            if Alien_Enemy.alive:
                alien_group.update(Spaceman_soldier)
                bullet_group.update(Alien_Enemy)    
                if Spaceman_soldier.in_air:
                    Spaceman_soldier.update_action(3)#jump
                elif move_left or move_right:
                    Spaceman_soldier.update_action(0)#run
                elif crouch:
                    Spaceman_soldier.update_action(2)#crouch
                else:
                    Spaceman_soldier.update_action(1)#idle
                Spaceman_soldier.moving(move_left, move_right)

            score += 0.10
            if game_over == False:
                Drawer.score_display('main_game', score, high_score)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        move_left = True
                    if event.key == pygame.K_d:
                        move_right = True
                    if event.key == pygame.K_w and Spaceman_soldier.alive:
                        Spaceman_soldier.jump = True    
                    if event.key == pygame.K_s:
                        crouch = True
                    if event.key == pygame.K_ESCAPE:
                        running = False   
                    if event.key == pygame.K_m:
                        shoot = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        move_left = False
                    if event.key == pygame.K_d:
                        move_right = False
                    if event.key == pygame.K_s:
                        crouch = False
                    if event.key == pygame.K_m:
                        shoot = False   
            
            if Spaceman_soldier.health == 0:
                game_over = True

            if game_over == True:
                high_score = Drawer.update_score(score, high_score)
                Drawer.score_display('game_over', score, high_score)            
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        game_over = False
                        alien_group.empty()
                        Spaceman_soldier = Spaceman(318, 200, 3, 7)
                        score = 0.5
                        Spaceman_soldier.health = 100
        pygame.display.update()
        pygame.display.flip()

    pygame.quit()

main()