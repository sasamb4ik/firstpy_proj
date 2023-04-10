import copy
import pygame
import math
import sys
sys.path.insert(0, "level")
from level1 import boards

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
for i in range(1, 5):
    player_images.append(pygame.transform.scale(pygame.image.load(f'players_icons/{i}.png'), (45, 45)))
blinky_img = pygame.transform.scale(pygame.image.load(f'ghosts_icons/red.png'), (45, 45))
pinky_img = pygame.transform.scale(pygame.image.load(f'ghosts_icons/pink.png'), (45, 45))
inky_img = pygame.transform.scale(pygame.image.load(f'ghosts_icons/blue.png'), (45, 45))
clyde_img = pygame.transform.scale(pygame.image.load(f'ghosts_icons/orange.png'), (45, 45))
spooked_img = pygame.transform.scale(pygame.image.load(f'ghosts_icons/powerup.png'), (45, 45))
dead_img = pygame.transform.scale(pygame.image.load(f'ghosts_icons/dead.png'), (45, 45))
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