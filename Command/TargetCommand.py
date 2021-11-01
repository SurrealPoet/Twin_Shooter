from .Command import Command


class TargetCommand(Command):
    def __init__(self, unit, target):
        self.unit = unit
        self.target = target

    def execute(self):
        self.unit.weapon_target = self.target
