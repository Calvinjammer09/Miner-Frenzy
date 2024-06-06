import pygame
import random

tiles = pygame.sprite.Group()

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.tiles_loaded = set()
        self.tileset = pygame.image.load('../graphics/background.png')

        self.tiles = []

        for frame in range(4):
            image = pygame.Surface((16 * frame + 1, 16), pygame.SRCALPHA).convert_alpha()
            image.blit(self.tileset, (0, 0))
            image = pygame.transform.scale(image, (16 * 5, 16 * 5))
            self.tiles.append(image)

    def load_tile(self):
        image = random.choice(self.tiles)

        return image

    def update(self, cx, cy):
        pass