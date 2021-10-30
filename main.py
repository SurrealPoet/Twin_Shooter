import math
import sys

import pygame as pg

from Mode import PlayGameMode


class UserInterface:
    def __init__(self):
        # Window
        pg.init()
        self.width = 1280
        self.height = int(self.width * 9 / 16)  # 720
        self.window = pg.display.set_mode((self.width, self.height))
        self.window_caption = "Twin Shooter"

        self.running = True
        self.play_game_mode = PlayGameMode(self)

        # Clock
        self.clock = pg.time.Clock()
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

        pg.quit()
        sys.exit()


if __name__ == "__main__":
    UserInterface().run()
