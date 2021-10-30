from math import atan2, pi

from .Layer import Layer


class UnitsLayer(Layer):
    def __init__(self, cell_size, image_file, game_state, units):
        super().__init__(cell_size, image_file)
        self.game_state = game_state
        self.units = units

    def render(self, window):
        for unit in self.units:
            distance_to_target = (unit.position + self.cell_size // 2) - unit.weapon_target
            angle = atan2(distance_to_target.x, distance_to_target.y) * 180 / pi
            self.render_tile(window, unit.position, unit.tile, angle)
