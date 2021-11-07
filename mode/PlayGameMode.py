import pygame

from pygame.math import Vector2

from command import MoveCommand, TargetCommand
from layer import UnitsLayer, WallLayer
from state import GameState


class PlayGameMode:
    def __init__(self, ui):
        self.ui = ui
        self.game_state = GameState()
        self.actions = {"left": False, "right": False, "up": False, "down": False}
        self.commands = []
        self.layers = [WallLayer(self.game_state.cell_size, pygame.image.load("assets/Wall.png")),
                       UnitsLayer(self.game_state.cell_size, pygame.image.load("assets/Player_Circle.png"),
                                  self.game_state.unit)]

    def process_input(self):
        move_vector = Vector2()
        self.set_action_flags()
        self.check_action_flags(move_vector)
        self.commands.append(MoveCommand(self.game_state, self.ui, self.game_state.player_unit, move_vector))

        mouse_position = pygame.mouse.get_pos()
        target = Vector2()
        target.x = mouse_position[0]
        target.y = mouse_position[1]
        self.commands.append(TargetCommand(self.game_state.player_unit, target))

    def update(self):
        for command in self.commands:
            command.execute()
        self.commands.clear()

    def render(self, window):
        window.fill((0, 0, 0))
        for layer in self.layers:
            layer.render(window)

        pygame.display.update()

        pygame.display.set_caption(self.ui.window_caption + "       " + str(int(self.ui.clock.get_fps())) + " FPS")

    def set_action_flags(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.ui.quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.ui.quit_game()
                if event.key == pygame.K_a:
                    self.actions["left"] = True
                if event.key == pygame.K_d:
                    self.actions["right"] = True
                if event.key == pygame.K_w:
                    self.actions["up"] = True
                if event.key == pygame.K_s:
                    self.actions["down"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.actions["left"] = False
                if event.key == pygame.K_d:
                    self.actions["right"] = False
                if event.key == pygame.K_w:
                    self.actions["up"] = False
                if event.key == pygame.K_s:
                    self.actions["down"] = False

    def check_action_flags(self, move_vector):
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
