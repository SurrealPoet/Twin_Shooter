from layer.Layer import Layer


class WallLayer(Layer):
    def __init__(self, cell_size, image_file, walls):
        super().__init__(cell_size, image_file)
        self.walls = walls

    def render(self, window):
        for wall in self.walls:
            wall.rect = self.render_tile(window, wall.position, wall.tile)
