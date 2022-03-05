from pygame.math import Vector2
import pygame


class Entity:
    def __init__(self, state, position, tile):
        self.state = state
        self.status = "alive"
        self.position = position
        self.real_position = Vector2()
        self.velocity = Vector2()
        self.move_speed = 0
        self.tile = tile
        self.is_solid = False
        self.rect = self.tile.get_rect(topleft=self.position)
        self.mask = pygame.mask.from_surface(self.tile)
