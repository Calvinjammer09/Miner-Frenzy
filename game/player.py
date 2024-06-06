import pygame
import time
import math

from rock import rock_group
from entity import BaseEntity
from enemy import enemies

bullet_fun = False

def collision(entity, group):
    return pygame.sprite.spritecollide(entity, group, False)

projectiles = pygame.sprite.Group()

class Bullet(BaseEntity):
    def __init__(self, sprite, frames, width, height, scale, speed, damage, start_pos, vel_x, vel_y):
        super().__init__(sprite, frames, width, height, scale, start_pos[0], start_pos[1])

        self.damage = damage

        self.vel_x = vel_x * speed
        self.vel_y = vel_y * speed

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        for enemy in enemies.sprites():
            if pygame.sprite.spritecollide(enemy, projectiles, True):
                enemy.health -= self.damage

        if self.rect.x >= player.rect.x + pygame.display.Info().current_w + 1000 or self.rect.x <= player.rect.x - pygame.display.Info().current_w - 1000 or self.rect.y >= player.rect.y + pygame.display.Info().current_h + 1000 or self.rect.y <= player.rect.y - pygame.display.Info().current_h - 1000:
            projectiles.remove(self)

class Pickaxe(Bullet):
    def __init__(self, start_pos, vel_x, vel_y, broken):
        if not broken:
            super().__init__('../graphics/Pickaxe.png', 1, 11, 11, 3, 20, 3, start_pos, vel_x, vel_y)
        else:
            super().__init__( '../graphics/broken_pick.png', 1, 11, 11, 3, 20, 3, start_pos, 0, 0)
            
        self.broken = broken

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        for enemy in enemies.sprites():
            if pygame.sprite.spritecollide(enemy, projectiles, not bullet_fun):
                enemy.health -= self.damage

                if not self.broken:
                    fallen_pick = Pickaxe((self.rect.x, self.rect.y), 0, 0, True)
                    
                    projectiles.add(fallen_pick)

        if self.rect.x >= player.rect.x + pygame.display.Info().current_w + 1000 or self.rect.x <= player.rect.x - pygame.display.Info().current_w - 1000 or self.rect.y >= player.rect.y + pygame.display.Info().current_h + 1000 or self.rect.y <= player.rect.y - pygame.display.Info().current_h - 1000:
            projectiles.remove(self)

class Player(BaseEntity):
    def __init__(self):
        super().__init__('../graphics/miner_walk_cycle.png', 4, 13, 20, 3, 0, 0)

        self.frame_list_R = [self.frame_list[1], self.frame_list[0]]
        self.frame_list_L = [self.frame_list[2], self.frame_list[3]]
        self.frame = 0

        self.hit_time = 0
        self.hit = False
        self.alpha = 255
        self.alpha_bool = False
        self.lives = 5
        self.movement = 7
        
        self.right = True
        self.left = False
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        keys = pygame.key.get_pressed()

        rock_collisions = collision(self, rock_group)
        enemy_collision = collision(self, enemies)

        if enemy_collision and self.hit_time - time.time() <= -1:
            self.hit_time = time.time()
            self.lives -= 1

        self.vel_x = 0
        self.vel_y = 0

        if keys[pygame.K_w]:
            self.vel_y -= self.movement
        if keys[pygame.K_s]:
            self.vel_y += self.movement
        if keys[pygame.K_a]:
            self.vel_x -= self.movement
            self.left = True
            self.right = False
        if keys[pygame.K_d]:
            self.vel_x += self.movement
            self.right = True
            self.left = False

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.vel_x or self.vel_y:
            self.frame = (self.frame + 0.05) % 2
        else:
            self.frame = 0

        self.image = self.frame_list_L[int(self.frame)] if self.left else self.frame_list_R[int(self.frame)]
        if self.hit_time - time.time() >= -0.4:
            if self.alpha_bool:
                self.alpha = 255
                self.alpha_bool = False
            else:
                self.alpha = int(255 / 3)
                self.alpha_bool = True
        else:
            self.alpha = 255
            self.alpha_bool = False

        self.image.set_alpha(self.alpha)

    def shoot(self, screen_w, screen_h):

        mouse_x, mouse_y = pygame.mouse.get_pos()

        mouse_x -= (self.rect.centerx - screen_w)
        mouse_y -= (self.rect.centery - screen_h)
    
        if not mouse_x:
            mouse_x = 90
        if not mouse_y:
            mouse_y = 90

        hyp = math.sqrt((mouse_y ** 2) + (mouse_x ** 2))

        cos = mouse_x/hyp
        sin = mouse_y/hyp

        bullet = Pickaxe((self.rect.center), cos, sin, False)

        projectiles.add(bullet)

player = Player()
player_group = pygame.sprite.Group(player)
