import pygame

from pygame.math import Vector2


class Layer:
    def __init__(self, cell_size, image_file):
        self.cell_size = cell_size
        self.texture = image_file

    def render_tile(self, window, position, tile, angle=None):
        if angle is None:
            return window.blit(tile, position)
        else:
            texture_tile = pygame.Surface(self.cell_size, pygame.SRCALPHA)
            texture_tile.blit(tile, (0, 0))
            rotated_tile = pygame.transform.rotate(texture_tile, angle)
            rotated_tile_left_corner = Vector2(0, 0)
            rotated_tile_left_corner.x = position.x - (rotated_tile.get_width() - texture_tile.get_width()) // 2
            rotated_tile_left_corner.y = position.y - (rotated_tile.get_height() - texture_tile.get_height()) // 2

            return window.blit(rotated_tile, rotated_tile_left_corner)

    def render(self, window):
        raise NotImplementedError
