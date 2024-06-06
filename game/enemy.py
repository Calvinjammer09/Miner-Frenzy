import pygame
import random

enemies = pygame.sprite.Group()

from entity import BaseEntity
import player

class BaseEnemy(BaseEntity):
    def __init__(self, sprite, frames, width, height, scale, speed, health):
        super().__init__(sprite, frames, width, height, scale, 0, 0)
        self.frame = 0
        self.health = health

        # self.hit_time = 0
        # self.alpha = 255
        # self.alpha_bool = False

        # setting movement speed
        self.speed = speed

    def spawn(self, x, y):

        # using tuples to set some rectangles of where enemies can spawn and then randomizing which rectangle is picked
        left = (-250 + x, -125 + x)
        right = (pygame.display.Info().current_w + 125 + x, pygame.display.Info().current_w + 250 + x)
        top = (-250 - y, -125 - y)
        bottom = (pygame.display.Info().current_h + 125 + y, pygame.display.Info().current_w + 250 + y)

        # a bunch of intermediate variables that i should really fix later
        list_x = [left, right]
        list_y = [top, bottom]

        # choose a random side for the enemy to be on
        side_x = random.choice(list_x)
        side_y = random.choice(list_y)

        # using the tuples pick a random value in the random
        self.rect.x = random.randint(side_x[0], side_x[1])
        self.rect.y = random.randint(side_y[0], side_y[1])

        print(self.rect.y, self.rect.x)

        enemies.add(self)

    def remove_from_group(self):
        enemies.remove(self)

    def update(self):
        self.frame += 0.013

        distance_x = player.player.rect.x - self.rect.x
        distance_y = player.player.rect.y - self.rect.y
        distance = (distance_x ** 2 + distance_y ** 2) ** 0.5

        # move the enemy toward the player if the player is close
        if distance != 0:
            self.rect.x += self.speed * distance_x / distance
            self.rect.y += self.speed * distance_y / distance
            self.frame = (self.frame + 0.05) % 2

        if self.health <= 0:
            enemies.remove(self)

class Mushroom(BaseEnemy):
    def __init__(self):
        super().__init__('../graphics/mushroom_man.png', 4, 21, 23, 3, 3, 9)
        self.frame_list_R = [self.frame_list[0], self.frame_list[1]]
        self.frame_list_L = [self.frame_list[3], self.frame_list[2]]

    def update(self):

        distance_x = player.player.rect.x - self.rect.x
        distance_y = player.player.rect.y - self.rect.y
        distance = (distance_x ** 2 + distance_y ** 2) ** 0.5

        # move the enemy toward the player if the player is close
        if distance != 0:
            self.rect.x += self.speed * distance_x / distance
            self.rect.y += self.speed * distance_y / distance
            self.frame = (self.frame + 0.08) % 2
        else:
            self.frame = 0

        if self.health <= 0:
            enemies.remove(self)

        self.image = self.frame_list_L[int(self.frame)] if distance_x < 0 else self.frame_list_R[int(self.frame)]
