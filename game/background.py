import pygame
import math

tiles = pygame.sprite.Group()

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.tiles_loaded = set()

        self.tileset = '../graphics/'

    def update(self, cx, cy):
        