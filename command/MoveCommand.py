from command.Command import Command
import pygame


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

        # offset = self.unit.rect.topleft[0] - self.state.test.rect.topleft[0], \
        #          self.unit.rect.topleft[1] - self.state.test.rect.topleft[1]
        # mask_test = self.unit.mask.overlap(self.state.test.mask, offset)
        if self.unit.rect.collidelistall(self.state.walls):
            print("Colliding with:", self.unit.rect.collidelistall(self.state.walls))
            # print(mask_test)

        self.unit.position = self.unit.real_position

    def inside_world(self, position):
        return 0 <= position.x <= self.ui.world_width - 32 and 0 <= position.y <= self.ui.world_height - 32

    def reposition_unit_to_be_inside_world(self):
        if self.unit.real_position.x < 0:
            self.unit.real_position.x = 0
        if self.unit.real_position.x > self.ui.world_width - self.state.cell_size.x:
            self.unit.real_position.x = self.ui.world_width - self.state.cell_size.x
        if self.unit.real_position.y < 0:
            self.unit.real_position.y = 0
        if self.unit.real_position.y > self.ui.world_height - self.state.cell_size.y:
            self.unit.real_position.y = self.ui.world_height - self.state.cell_size.y
