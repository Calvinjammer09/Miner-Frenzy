import pygame
import time
import random

# initialize pygame for further use
pygame.init()

# set up the window
screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h
win = pygame.display.set_mode((screen_width, screen_height))

from map_state import Render
import player
import enemy

# set some tuples for easier use in pygame colors
BLACK = (0, 0, 0)

# initialize the rendering info (rocks, player, etc.)
render = Render()

mushroom = enemy.Mushroom()
mushroom.spawn(render.camera_x, render.camera_y)

def dead(win):
    run = True

    while run:
        win.blit(render.dead_screen, (0, 0))

        # code from game.py to check for quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                # check if the player wants to show fps or take a screenshot
                render.key_checks(event, win)

                # set the players health to max and start spawning enemies
                render.restart()
                main()
                return
        
        pygame.display.update()

def main():
    run = True

    wave = 1

    last_shot = 0

    mush_spawn_1 = 1
    mush_spawn_2 = 3

    mushspawnr = 1

    mush_spawn_time = random.randint(mush_spawn_1, mush_spawn_2)

    # run the game loop
    while run:
        
        if player.player.lives <= 0:
            dead(win)
            return
        
        mush_spawn_time -= mushspawnr / 60

        if pygame.mouse.get_pressed()[0] and time.time() - last_shot >= 0.2:
            last_shot = time.time()
            player.player.shoot(render.camera_x, render.camera_y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # check for key presses to toggle fps display or screenshot
            if event.type == pygame.KEYDOWN:
                render.key_checks(event, win)

                if event.key == pygame.K_ESCAPE:
                    run = False

        if mush_spawn_time <= 0:
            if wave == 5:
                mush_spawn_2 -= 1
            elif wave > 10 and wave < 13:
                mushspawnr += 1
            elif wave == 30:
                mushspawnr += 2
            elif wave == 50:
                mushspawnr += 2 

            mush_spawn_time = random.randint(mush_spawn_1, mush_spawn_2)

            new_mushroom = enemy.Mushroom()

            new_mushroom.spawn(render.camera_x, render.camera_y)

            wave += 1
            enemy.enemies.add(new_mushroom)

        # redraw the game with updated camera position and entity rendering
        render.redraw(win, BLACK)

    pygame.quit()

if __name__ == "__main__":
    main()
