from .Command import Command


class TargetCommand(Command):
    def __init__(self, state, unit, target):
        self.state = state
        self.unit = unit
        self.target = target

    def execute(self):
        self.unit.weapon_target = self.target
