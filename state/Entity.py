from pygame.math import Vector2


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
