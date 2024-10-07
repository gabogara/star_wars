import pygame
import random
from pygame import mixer


pygame.init()
size=(800,600)
screen = pygame.display.set_mode(size)

# Title and Icon
pygame.display.set_caption("Star wars")
icon = pygame.image.load("ovni.png")
pygame.display.set_icon(icon)
background = pygame.image.load('Background.jpg')

# We add music
mixer.music.load('BackgroundMusic.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Player variables
img_player = pygame.image.load("rocket.png")
player_x = 368
player_y = 500
player_x_change = 0

# Enemy variables
img_enemy = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
enemy_amount = 8

for e in range(enemy_amount):
    img_enemy.append(pygame.image.load("enemy.png"))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 200))
    enemy_x_change.append(0.5)
    enemy_y_change.append(50)



