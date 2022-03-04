import pygame

from pygame.math import Vector2

from state import Unit, Wall


class GameState:
    def __init__(self):
        self.player_image = pygame.image.load("assets/Player_Circle.png")
        self.unit = [Unit(self, Vector2(0, 0), self.player_image)]
        self.player_unit = self.unit[0]
        self.cell_size = Vector2(32, 32)

        self.walls = [Wall(self, Vector2(200, 200), pygame.image.load("assets/Wall.png")),
                      Wall(self, Vector2(200, 218), pygame.image.load("assets/Wall.png")),
                      Wall(self, Vector2(200, 236), pygame.image.load("assets/Wall.png")),
                      Wall(self, Vector2(400, 200), pygame.image.load("assets/Wall.png")),
                      Wall(self, Vector2(600, 200), pygame.image.load("assets/Wall.png")),
                      Wall(self, Vector2(500, 500), pygame.image.load("assets/Wall.png")),
                      Wall(self, Vector2(800, 500), pygame.image.load("assets/Wall.png")),
                      Wall(self, Vector2(800, 518), pygame.image.load("assets/Wall.png")),
                      Wall(self, Vector2(800, 536), pygame.image.load("assets/Wall.png")), ]
