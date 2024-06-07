import pygame
import random

from entity import BaseEntity

tiles = pygame.sprite.Group()

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image

        self.rect = image.get_rect()

        self.size = 16

        self.rect.x = x
        self.rect.y = y

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # self.tiles_loaded = set()
        # self.tiles_to_load = set()

        self.x_tiles = 1000
        self.y_tiles = 1000

        self.tileset = pygame.image.load('../graphics/background.png')

        # self.cx = -941
        # self.cy = -510

        self.tiles = []

        for frame in range(4):

            # create a surface with an alpha channel
            image = pygame.Surface((16, 16), pygame.SRCALPHA).convert_alpha()
            source_rect = pygame.Rect(frame * 16, 0, 16, 16)
            image.blit(self.tileset, (0, 0), source_rect)
            #image = pygame.transform.scale(image, (16 * 5, 16 * 5))

            self.tiles.append(image)

        for x_tile in range(self.x_tiles):
            for y_tile in range(self.y_tiles):
                tile = Tile(self.load_tile(), x_tile * 16 - self.x_tiles // 2 * 16, y_tile * 16 - self.y_tiles // 2 * 16)

                tiles.add(tile)

    def load_tile(self):
        image = random.choice(self.tiles)

        return image
    
    # currently unused update function, itll take a long time but ill make some sort of chunk loading function later
    def update(self, cx, cy):
        pass
