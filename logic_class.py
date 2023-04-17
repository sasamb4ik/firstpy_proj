import pygame
import sys
from player_class import *
from enemy_class import *


pygame.init()
vec = pygame.math.Vector2

<<<<<<< HEAD
# музыка
pygame.mixer.init()
pygame.mixer.music.load('pacman.mp3')
pygame.mixer.music.play(-1, 0.0)
=======
>>>>>>> 5531239 (1st attempt)

class Logic:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.cell_width = MAP_WIDTH // COLS
        self.cell_height = MAP_HEIGHT // ROWS
        self.walls = []
        self.coins = []
        self.bonus = []
        self.enemies = []
        self.e_pos = []
        self.p_pos = None
        self.load()
        self.player = Player(self, vec(self.p_pos))
        self.make_enemies()
<<<<<<< HEAD
        self.to_win = 0
=======
>>>>>>> 5531239 (1st attempt)

    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            elif self.state == 'game over':
<<<<<<< HEAD
                self.game_end_events()
                self.game_over_update()
                self.game_over_draw()
            elif self.state == 'game won':
                self.game_end_events()
                self.game_won_update()
                self.game_won_draw()
=======
                self.game_over_events()
                self.game_over_update()
                self.game_over_draw()
>>>>>>> 5531239 (1st attempt)
            else:
                self.running = False
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

<<<<<<< HEAD
=======

>>>>>>> 5531239 (1st attempt)
    def draw_text(self, words, screen, pos, size, colour, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)

    def load(self):
        self.background = pygame.image.load('map.png')
        self.background = pygame.transform.scale(self.background, (MAP_WIDTH, MAP_HEIGHT))


        with open("map.txt", 'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == "1":
                        self.walls.append(vec(xidx, yidx))
                    elif char == "C":
                        self.coins.append(vec(xidx, yidx))
                    elif char == "L":
                        self.bonus.append(vec(xidx, yidx))
                    elif char == "P":
                        self.p_pos = [xidx, yidx]
                    elif char in ["2", "3", "4", "5"]:
                        self.e_pos.append([xidx, yidx])
                    elif char == "B":
                        pygame.draw.rect(self.background, BLACK, (xidx*self.cell_width, yidx*self.cell_height,
                                                                  self.cell_width, self.cell_height))
<<<<<<< HEAD
        buf = self.coins
        self.to_win = len(buf)
=======
>>>>>>> 5531239 (1st attempt)

    def make_enemies(self):
        for idx, pos in enumerate(self.e_pos):
            self.enemies.append(Enemy(self, vec(pos), idx))

    def draw_grid(self):
        for x in range(WIDTH//self.cell_width):
            pygame.draw.line(self.background, PINK, (x*self.cell_width, 0),
                             (x*self.cell_width, HEIGHT))
        for x in range(HEIGHT//self.cell_height):
            pygame.draw.line(self.background, PINK, (0, x*self.cell_height),
                             (WIDTH, x*self.cell_height))

    def reset(self):
        self.player.lives = 3
        self.player.current_score = 0
        self.player.grid_pos = vec(self.player.starting_pos)
        self.player.pix_pos = self.player.get_pix_pos()
        self.player.direction *= 0
        for enemy in self.enemies:
            enemy.grid_pos = vec(enemy.starting_pos)
            enemy.pix_pos = enemy.get_pix_pos()
            enemy.direction *= 0

        self.coins = []
        self.bonus = []
        with open("map.txt", 'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == 'C':
                        self.coins.append(vec(xidx, yidx))
                    if char == 'L':
                        self.bonus.append(vec(xidx, yidx))
        self.state = "playing"

    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'

    def start_update(self):
        pass

    def start_draw(self):
        self.screen.fill(BLACK)
        self.draw_text('Нажмите пробел', self.screen, [
                       WIDTH//2, HEIGHT//2-50], START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
        self.draw_text('Лучший счёт', self.screen, [4, 0],
                       START_TEXT_SIZE, (255, 255, 255), START_FONT)
        pygame.display.update()


    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(vec(-1, 0))
                if event.key == pygame.K_RIGHT:
                    self.player.move(vec(1, 0))
                if event.key == pygame.K_UP:
                    self.player.move(vec(0, -1))
                if event.key == pygame.K_DOWN:
                    self.player.move(vec(0, 1))

    def playing_update(self):
        # Обновить состояние игроков и врагов
<<<<<<< HEAD
        buf = self.coins
        if self.to_win == len(buf):
            self.state = 'game won'
=======
>>>>>>> 5531239 (1st attempt)
        self.player.update()
        for enemy in self.enemies:
            enemy.update()

        # Проверить на столкновение с врагами
        for enemy in self.enemies:
            if enemy.grid_pos == self.player.grid_pos:
                if self.player.bonusTimer < 0:
                    self.remove_life()
                else:
                    idx = enemy.number
                    self.enemies.remove(enemy)
                    self.enemies.append(Enemy(self, vec(14, 15), idx))

        target_focus = vec(14, 15) if self.player.bonusTimer > 0 else self.player.grid_pos
        for enemy in self.enemies:
            enemy.targetFocus = target_focus

    def playing_draw(self):
        self.screen.fill(BLACK)

        self.screen.blit(self.background, (TOP_BOTTOM // 2, TOP_BOTTOM // 2))

        #  Рисуем монетки и жирные монетки
        self.draw_coins()
        self.draw_bonus()

        score_text = f"Счёт сейчас: {self.player.current_score}"
        best_score_text = "Лучший счёт: 0"
        self.draw_text(score_text, self.screen, [60, 0], 18, WHITE, START_FONT)
        self.draw_text(best_score_text, self.screen, [WIDTH // 2 + 60, 0], 18, WHITE, START_FONT)

        self.player.draw()
        for enemy in self.enemies:
            enemy.draw()

        pygame.display.update()

    def remove_life(self):
        self.player.lives -= 1
        if self.player.lives == 0:
            self.state = "game over"
        else:
            self.player.grid_pos = vec(self.player.starting_pos)
            self.player.pix_pos = self.player.get_pix_pos()
            self.player.direction *= 0
            for enemy in self.enemies:
                enemy.grid_pos = vec(enemy.starting_pos)
                enemy.pix_pos = enemy.get_pix_pos()
                enemy.direction *= 0

    def draw_coins(self):
        for coin in self.coins:
            pygame.draw.circle(self.screen, (255, 255, 204),
                               (int(coin.x * self.cell_width) + self.cell_width // 2 + TOP_BOTTOM // 2,
                                int(coin.y * self.cell_height) + self.cell_height // 2 + TOP_BOTTOM // 2), 5)

    def draw_bonus(self):
        for bonus in self.bonus:
            pygame.draw.circle(self.screen, (255, 0, 127),
                               (int(bonus.x*self.cell_width) + self.cell_width // 2 + TOP_BOTTOM // 2,
                                int(bonus.y*self.cell_height) + self.cell_height // 2 + TOP_BOTTOM // 2), 7)

<<<<<<< HEAD
    def game_end_events(self):
=======
    def game_over_events(self):
>>>>>>> 5531239 (1st attempt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.reset()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

    def game_over_update(self):
        pass

<<<<<<< HEAD
    def game_won_update(self):
        pass

=======
>>>>>>> 5531239 (1st attempt)
    def game_over_draw(self):
        self.screen.fill(BLACK)
        quit_text = "Нажмите ESC чтобы выйти"
        again_text = "Нажмите SPACE чтобы играть снова"
        self.draw_text("GAME OVER", self.screen, [WIDTH//2, 100],  52, RED, "arial", centered=True)
        self.draw_text(again_text, self.screen, [
                       WIDTH//2, HEIGHT//2],  36, (190, 190, 190), "arial", centered=True)
        self.draw_text(quit_text, self.screen, [
                       WIDTH//2, HEIGHT//1.5],  36, (190, 190, 190), "arial", centered=True)
        pygame.display.update()
<<<<<<< HEAD

    def game_won_draw(self):
        self.screen.fill(BLACK)
        quit_text = "Нажмите ESC чтобы выйти"
        again_text = "Нажмите SPACE чтобы играть снова"
        self.draw_text("GAME WON", self.screen, [WIDTH//2, 100],  52, GREEN, "arial", centered=True)
        self.draw_text(again_text, self.screen, [
                       WIDTH//2, HEIGHT//2],  36, (190, 190, 190), "arial", centered=True)
        self.draw_text(quit_text, self.screen, [
                       WIDTH//2, HEIGHT//1.5],  36, (190, 190, 190), "arial", centered=True)
        pygame.display.update()
=======
>>>>>>> 5531239 (1st attempt)
