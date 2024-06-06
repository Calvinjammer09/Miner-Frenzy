import pygame
import math

tiles = pygame.sprite.Group()

chunk_size_x = 100
chunk_size_y = 100

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def update(self, cx, cy):
        