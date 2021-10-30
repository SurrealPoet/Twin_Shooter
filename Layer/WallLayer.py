import pygame as pg
from pygame.math import Vector2
from .Layer import Layer


class WallLayer(Layer):
    def __init__(self, cell_size, image_file):
        super().__init__(cell_size, image_file)

    def render(self, window):
        window.blit(self.texture, Vector2(200, 200))
        window.blit(self.texture, Vector2(200, 218))
        window.blit(self.texture, Vector2(200, 236))
        window.blit(self.texture, Vector2(400, 200))
        window.blit(self.texture, Vector2(600, 200))
