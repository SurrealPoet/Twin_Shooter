from .Command import Command


class MoveCommand(Command):
    def __init__(self, state, unit, move_vector):
        self.state = state
        self.unit = unit
        self.move_vector = move_vector

    def execute(self):
        self.unit.velocity = self.move_vector * self.unit.move_speed * self.state.ui.delta_time
        self.unit.real_position += self.unit.velocity
        # Check if within map and correct if not
        if self.unit.real_position.x < 0:
            self.unit.real_position.x = 0
        if self.unit.real_position.x > self.state.ui.width - self.state.cell_size.x:
            self.unit.real_position.x = self.state.ui.width - self.state.cell_size.x
        if self.unit.real_position.y < 0:
            self.unit.real_position.y = 0
        if self.unit.real_position.y > self.state.ui.height - self.state.cell_size.y:
            self.unit.real_position.y = self.state.ui.height - self.state.cell_size.y

        self.unit.position = self.unit.real_position
