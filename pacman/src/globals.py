import copy
import pygame
import math
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname("level1.py"), "..")))
from level.level1 import boards

pygame.init()

WIDTH = 900
HEIGHT = 950
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)
level = copy.deepcopy(boards)
color = 'blue'
PI = math.pi
player_images = []

players_icons_dir = os.path.join(os.path.dirname(__file__), '..', 'players_icons')
for i in range(1, 5):
    image_path = os.path.join(players_icons_dir, f'{i}.png')
    image = pygame.image.load(image_path)
    player_images.append(pygame.transform.scale(image, (45, 45)))

ghosts_icons_dir = os.path.join(os.path.dirname(__file__), '..', 'ghosts_icons')

blinky_path = os.path.join(ghosts_icons_dir, 'red.png')
blinky_img = pygame.transform.scale(pygame.image.load(blinky_path), (45, 45))

pinky_path = os.path.join(ghosts_icons_dir, 'pink.png')
pinky_img = pygame.transform.scale(pygame.image.load(pinky_path), (45, 45))

inky_path = os.path.join(ghosts_icons_dir, 'blue.png')
inky_img = pygame.transform.scale(pygame.image.load(inky_path), (45, 45))

clyde_path = os.path.join(ghosts_icons_dir, 'orange.png')
clyde_img = pygame.transform.scale(pygame.image.load(clyde_path), (45, 45))

powerup_path = os.path.join(ghosts_icons_dir, 'powerup.png')
spooked_img = pygame.transform.scale(pygame.image.load(powerup_path), (45, 45))

dead_path = os.path.join(ghosts_icons_dir, 'dead.png')
dead_img = pygame.transform.scale(pygame.image.load(dead_path), (45, 45))

player_x = 450
player_y = 663
direction = 0
blinky_x = 56
blinky_y = 58
blinky_direction = 0
inky_x = 440
inky_y = 388
inky_direction = 2
pinky_x = 440
pinky_y = 438
pinky_direction = 2
clyde_x = 440
clyde_y = 438
clyde_direction = 2
counter = 0
flicker = False
# ПРАВО, ЛЕВО, ВЕРХ, НИЗ
turns_allowed = [False, False, False, False]
direction_command = 0
player_speed = 2
score = 0
powerup = False
power_counter = 0
eaten_ghost = [False, False, False, False]
targets = [(player_x, player_y), (player_x, player_y), (player_x, player_y), (player_x, player_y)]
blinky_dead = False
inky_dead = False
clyde_dead = False
pinky_dead = False
blinky_box = False
inky_box = False
clyde_box = False
pinky_box = False
moving = False
ghost_speeds = [2, 2, 2, 2]
startup_counter = 0
lives = 3
game_over = False
game_won = False