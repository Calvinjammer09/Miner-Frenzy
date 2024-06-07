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

            # create a surface with an alpha channel
            image = pygame.Surface((16, 16), pygame.SRCALPHA).convert_alpha()
            source_rect = pygame.Rect(frame * 16, 0, 16, 16)
            image.blit(self.tileset, (0, 0), source_rect)
            image = pygame.transform.scale(image, (16 * 5, 16 * 5))
            self.tiles.append(image)

    def load_tile(self):
        image = random.choice(self.tiles)

        return image

    def update(self, cx, cy):
        pass