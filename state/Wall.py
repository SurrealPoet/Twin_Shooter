from state.Entity import Entity


class Wall(Entity):
    def __init__(self, state, position, tile):
        super().__init__(state, position, tile)
        self.is_solid = True
