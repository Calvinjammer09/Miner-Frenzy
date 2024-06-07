import pygame
import os
import time

pygame.display.init()

from player import player_group, player, projectiles
from enemy import enemies, Mushroom
from background import Background, tiles
from rock import rock_group

class Render:
    def __init__(self):
        
        # initialize pygame clock and stuff for fps display
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 100)
        self.show_fps = False

        # initialize camera variables
        self.camera_x = 0
        self.camera_y = 0
        self.camera_width = pygame.display.Info().current_w
        self.camera_height = pygame.display.Info().current_h

        # set up the heart sprite to show player HP
        self.heart_sprite = pygame.image.load('../graphics/Heart.png').convert_alpha()
        self.heart_sprite = pygame.transform.scale(self.heart_sprite, (16 * 3, 16 * 3))

        # set up the win screen and death screen for further use
        self.dead_screen = pygame.image.load('../graphics/you lost.png').convert_alpha()
        self.dead_screen = pygame.transform.scale(self.dead_screen, (368 * (self.camera_width / 368), 208 * (self.camera_height / 208)))

        self.win_screen = pygame.image.load('../graphics/end_screen.png').convert_alpha()
        self.win_screen = pygame.transform.scale(self.win_screen, (368 * (self.camera_width / 368), 208 * (self.camera_height / 208)))

        # setting up a number of screenshots taken by finding the amount of screenshots in the Screenshots folder
        self.ss_number = 0
        for file in os.listdir('../Screenshots'):
            if file.endswith('.png'):
                if os.path.isfile(os.path.join('../Screenshots', file)):
                    self.ss_number += 1

        self.background = Background()

        self.last_loaded_tile = 0
        self.loaded_tiles = self.background.tiles

    def update_camera(self, player):
        # update camera position based on player position
        self.camera_x = player.rect.centerx - self.camera_width // 2
        self.camera_y = player.rect.centery - self.camera_height // 2

    def key_checks(self, event, win):
        if event.key == pygame.K_f:
            self.show_fps = not self.show_fps
        if event.key == pygame.K_F2:

            # checking for if the player wants to take a screenshot and change the number in screenshots.txt accordingly
            self.ss_number += 1
            pygame.image.save(win, '../Screenshots/' + 'Screenshot ' + str(self.ss_number) + '.png')

    def restart(self):
        player_group.sprites()[0].lives = 5

        enemies.empty()
        projectiles.empty()

        new_mush = Mushroom()
        new_mush.spawn(self.camera_x, self.camera_y)
        enemies.add(new_mush)
        
    def redraw(self, window, color):

        # run the player and enemy move method to update the positions of the entities
        player_group.update()
        enemies.update()
        projectiles.update()
        tiles.update()
        
        # update camera position and set fps to 60
        self.clock.tick(60)
        self.update_camera(player_group.sprites()[0])

        # fill screen with background color
        window.fill(color)

        # render all sprites
        for sprite in player_group.sprites() + rock_group.sprites() + enemies.sprites() + projectiles.sprites():
            if sprite.rect.x - self.camera_x > self.camera_width or sprite.rect.x - self.camera_x < -sprite.size or sprite.rect.y - self.camera_y > self.camera_height or sprite.rect.y - self.camera_y < -sprite.size:
                pass
            else:
                window.blit(sprite.image, (sprite.rect.x - self.camera_x, sprite.rect.y - self.camera_y))

        lives_offset = 0
        for hearts in range(player_group.sprites()[0].lives):
            window.blit(self.heart_sprite, (lives_offset, 0))
            lives_offset += 48

        # render fps if enabled
        if self.show_fps:
            rounded_fps = str(round(self.clock.get_fps(), 2))
            fps_text = self.font.render(rounded_fps, True, (255, 255, 255))
            window.blit(fps_text, (0, 0))

        # if time.time() - self.last_loaded_tile >= 2:
        #     self.last_loaded_tile = time.time()
        #     self.loaded_tile = self.background.load_tile()

        #tile_offset = 0
        #for frame in self.loaded_tiles:
        #    window.blit(frame, (player.rect.centerx - self.camera_x + tile_offset, player.rect.centery - self.camera_y))
        #    tile_offset += 16 * 5
        
        pygame.display.update()
