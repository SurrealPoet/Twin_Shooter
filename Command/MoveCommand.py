from .Command import Command


class MoveCommand(Command):
    def __init__(self, state, ui, unit, move_vector):
        self.state = state
        self.ui = ui
        self.unit = unit
        self.move_vector = move_vector

    def execute(self):
        self.unit.velocity = self.move_vector * self.unit.move_speed * self.ui.delta_time
        self.unit.real_position += self.unit.velocity

        if not self.inside_world(self.unit.real_position):
            self.reposition_unit_to_be_inside_world()

        # Check for unit collisions and reposition

        self.unit.position = self.unit.real_position

    def inside_world(self, position):
        return 0 <= position.x <= self.ui.width - 32 and 0 <= position.y <= self.ui.height - 32

    def reposition_unit_to_be_inside_world(self):
        if self.unit.real_position.x < 0:
            self.unit.real_position.x = 0
        if self.unit.real_position.x > self.ui.width - self.state.cell_size.x:
            self.unit.real_position.x = self.ui.width - self.state.cell_size.x
        if self.unit.real_position.y < 0:
            self.unit.real_position.y = 0
        if self.unit.real_position.y > self.ui.height - self.state.cell_size.y:
            self.unit.real_position.y = self.ui.height - self.state.cell_size.y
