from pygame.math import Vector2

from state.Entity import Entity


class Unit(Entity):
    def __init__(self, state, position, tile):
        super().__init__(state, position, tile)
        self.move_speed = 360
        self.weapon_target = Vector2(0, 0)
