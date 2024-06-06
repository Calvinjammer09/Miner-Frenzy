import pygame

class BaseEntity(pygame.sprite.Sprite):
    def __init__(self, sprite, frames, width, height, scale, x, y):
        super().__init__()
        
        # load the sprite for use in make_sprite
        self.sprite = pygame.image.load(sprite)
        self.size = int((width + height) * scale / 2)

        # create frames of animations if needed
        self.frame_list = []
        for frame in range(frames):
            self.temp_frame = self.make_sprite(frame, width, height, scale)
            self.frame_list.append(self.temp_frame)

        self.rect = self.frame_list[0].get_rect()
        self.rect.x = x
        self.rect.y = y

        self.image = self.frame_list[0]

    def make_sprite(self, frame, width, height, scale):

        # create a surface with an alpha channel
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        source_rect = pygame.Rect(frame * width, 0, width, height)
        image.blit(self.sprite, (0, 0), source_rect)
        image = pygame.transform.scale(image, (width * scale, height * scale))
        return image
