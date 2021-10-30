import pygame as pg

from pygame.math import Vector2

from Command import MoveCommand, TargetCommand
from Layer import UnitsLayer, WallLayer
from State import GameState


class PlayGameMode:
    def __init__(self, ui):
        self.ui = ui
        self.game_state = GameState()
        self.cell_size = Vector2(32, 32)
        self.actions = {"left": False, "right": False, "up": False, "down": False}
        self.commands = []
        self.layers = [WallLayer(self.cell_size, pg.image.load("Assets/Wall.png")),
                       UnitsLayer(self.cell_size, pg.image.load("Assets/Player_Circle.png"),
                                  self.game_state, self.game_state.unit)]

    def process_input(self):
        move_vector = Vector2()
        # Set flags
        self.controls_handler()

        # Check movement flags
        if self.actions["left"]:
            move_vector.x += -1
        if self.actions["right"]:
            move_vector.x += 1
        if self.actions["up"]:
            move_vector.y += -1
        if self.actions["down"]:
            move_vector.y += 1
        if ((self.actions["left"] and self.actions["up"]) or
                (self.actions["left"] and self.actions["down"]) or
                (self.actions["right"] and self.actions["up"]) or
                (self.actions["right"] and self.actions["down"])):
            move_vector *= .7071  # 1 / sqrt 2 to normalize vector
        self.commands.append(MoveCommand(self, self.game_state.player_unit, move_vector))

        mouse_position = pg.mouse.get_pos()
        target = Vector2()
        target.x = mouse_position[0]
        target.y = mouse_position[1]
        self.commands.append(TargetCommand(self.game_state, self.game_state.player_unit, target))

    def update(self):
        for command in self.commands:
            command.execute()
        self.commands.clear()

    def render(self, window):
        self.ui.window.fill((0, 0, 0))
        for layer in self.layers:
            layer.render(window)

        pg.display.update()

        pg.display.set_caption(self.ui.window_caption + "       " + str(int(self.ui.clock.get_fps())) + " FPS")

    def controls_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.ui.quit_game()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.ui.quit_game()
                if event.key == pg.K_a:
                    self.actions["left"] = True
                if event.key == pg.K_d:
                    self.actions["right"] = True
                if event.key == pg.K_w:
                    self.actions["up"] = True
                if event.key == pg.K_s:
                    self.actions["down"] = True
            if event.type == pg.KEYUP:
                if event.key == pg.K_a:
                    self.actions["left"] = False
                if event.key == pg.K_d:
                    self.actions["right"] = False
                if event.key == pg.K_w:
                    self.actions["up"] = False
                if event.key == pg.K_s:
                    self.actions["down"] = False
