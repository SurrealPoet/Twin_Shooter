import sys

import pygame

from mode import PlayGameMode


class UserInterface:
    def __init__(self):
        # Window
        pygame.init()
        self.world_width = 1280
        self.world_height = 736
        self.window = pygame.display.set_mode((self.world_width, self.world_height))
        self.window_caption = "Twin Shooter"

        self.running = True
        self.play_game_mode = PlayGameMode(self)

        # Clock
        self.clock = pygame.time.Clock()
        self.delta_time = 0

    def quit_game(self):
        self.running = False

    def run(self):
        while self.running:
            self.play_game_mode.process_input()
            self.play_game_mode.update()
            self.play_game_mode.render(self.window)

            # Set frame rate and store time passage in seconds
            self.delta_time = self.clock.tick(60) / 1000

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    UserInterface().run()
