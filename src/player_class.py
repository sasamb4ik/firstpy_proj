import pygame
import json
from globals import *

vec = pygame.math.Vector2
import shared


class Player:
    def __init__(self, app, pos):
        self.app = app
        self.starting_pos = [pos.x, pos.y]
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.direction = vec(1, 0)
        self.stored_direction = None
        self.able_to_move = True
        self.current_score = 0
        self.speed = 2
        self.lives = 2
        shared.bonusTimer = 0
        self.best_score = 0
        self.diff = 0

    def upload(self):
        with open("../data/best_score.json", 'r') as file:
            self.best_score = json.load(file)

    def update(self):
        if self.current_score > self.best_score:
            self.best_score = self.current_score
        if self.able_to_move:
            self.pix_pos += self.direction * self.speed
        if self.time_to_move():
            if self.stored_direction is not None:
                if self.can_move(self.stored_direction):
                    self.direction = self.stored_direction
                    self.stored_direction = None
            self.able_to_move = self.can_move(self.direction)

        self.grid_pos[0] = (self.pix_pos[0] - TOP_BOTTOM +
                            self.app.cell_width // 2) // self.app.cell_width + 1
        self.grid_pos[1] = (self.pix_pos[1] - TOP_BOTTOM +
                            self.app.cell_height // 2) // self.app.cell_height + 1
        shared.bonusTimer -= 0.01

        if self.on_coin():
            self.eat_coin()
        if self.on_bonus():
            self.eat_bonus()

    def can_move(self, direction):
        if direction is None:
            return False
        next_pos = vec(self.grid_pos) + direction
        for wall in self.app.walls:
            if next_pos == wall:
                return False
        return True

    def move(self, direction):
        if self.stored_direction is None:
            self.stored_direction = direction
        elif self.can_move(direction):
            self.direction = direction
            self.stored_direction = None
        else:
            self.stored_direction = direction

    def time_to_move(self):
        if int(self.pix_pos.x + TOP_BOTTOM // 2) % self.app.cell_width == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                return True
        if int(self.pix_pos.y + TOP_BOTTOM // 2) % self.app.cell_height == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                return True
        return False

    def draw(self):
        pygame.draw.circle(self.app.screen, PLAYER_COLOUR, (int(self.pix_pos.x),
                                                            int(self.pix_pos.y)), self.app.cell_width // 2 - 2)

        # Drawing player lives
        for x in range(self.lives):
            pygame.draw.circle(self.app.screen, PLAYER_COLOUR, (30 + 20 * x, HEIGHT - 15), 7)

    def on_coin(self):
        if self.grid_pos in self.app.coins:
            if int(self.pix_pos.x + TOP_BOTTOM // 2) % self.app.cell_width == 0:
                if self.direction == vec(1, 0) or self.direction == vec(-1, 0):
                    return True
            if int(self.pix_pos.y + TOP_BOTTOM // 2) % self.app.cell_height == 0:
                if self.direction == vec(0, 1) or self.direction == vec(0, -1):
                    return True
        return False

    def on_bonus(self):
        if self.grid_pos in self.app.bonus:
            if int(self.pix_pos.x + TOP_BOTTOM // 2) % self.app.cell_width == 0:
                if self.direction == vec(1, 0) or self.direction == vec(-1, 0):
                    shared.bonusTimer = 2
                    return True
            if int(self.pix_pos.y + TOP_BOTTOM // 2) % self.app.cell_height == 0:
                if self.direction == vec(0, 1) or self.direction == vec(0, -1):
                    shared.bonusTimer = 2
                    return True
        return False

    def eat_coin(self):
        self.app.coins.remove(self.grid_pos)
        self.current_score += 1
        if self.current_score > self.best_score:
            self.best_score = self.current_score

    def eat_bonus(self):
        self.app.bonus.remove(self.grid_pos)
        self.current_score += 100
        if self.current_score > self.best_score:
            self.best_score = self.current_score

    def get_pix_pos(self):
        x_pos = (self.grid_pos[0] * self.app.cell_width)
        y_pos = (self.grid_pos[1] * self.app.cell_height)
        return vec(x_pos + TOP_BOTTOM // 2 + self.app.cell_width // 2,
                   y_pos + TOP_BOTTOM // 2 + self.app.cell_height // 2)
