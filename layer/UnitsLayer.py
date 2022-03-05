from math import atan2, pi

from layer.Layer import Layer


class UnitsLayer(Layer):
    def __init__(self, cell_size, image_file, units):
        super().__init__(cell_size, image_file)
        self.units = units

    def render(self, window):
        for unit in self.units:
            distance_to_target = (unit.position + self.cell_size // 2) - unit.weapon_target
            angle = atan2(distance_to_target.x, distance_to_target.y) * 180 / pi
            unit.rect = self.render_tile(window, unit.position, unit.tile, angle)
