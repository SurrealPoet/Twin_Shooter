from pygame.math import Vector2

from .GameItem import GameItem


class Unit(GameItem):
    def __init__(self, state, position, tile):
        super().__init__(state, position, tile)
        self.move_speed = 360
        self.weapon_target = Vector2(0, 0)
