import pygame as pg

from pygame.math import Vector2

from State import Unit


class GameState:
    def __init__(self):
        self.player_image = pg.image.load("Assets/Player_Circle.png")
        self.unit = [Unit(self, Vector2(0, 0), self.player_image)]
        self.player_unit = self.unit[0]
        self.cell_size = Vector2(32, 32)
