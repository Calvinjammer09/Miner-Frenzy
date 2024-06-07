import pygame
import random

from entity import BaseEntity

class Rock(BaseEntity):
    def __init__(self):
        super().__init__('../graphics/Boulder.png', 1, 32, 29, 3, 0, 0)
        self.image = self.frame_list[0]
        self.rock_amount = 50
        self.rect.x = random.randint(500, 2000)
        self.rect.y = random.randint(500, 2000)

rock_group = pygame.sprite.Group()#[Rock() for _ in range(50)])