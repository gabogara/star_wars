import pygame
import random
import math
from pygame import mixer

# Run pygame
pygame.init()

# create screen
size=(800,600)
screen = pygame.display.set_mode(size)

# Title and Icon
pygame.display.set_caption("Star wars")
icon = pygame.image.load("ovni.png")
pygame.display.set_icon(icon)
#background = pygame.image.load('Background.jpg')

# We add music
mixer.music.load('BackgroundMusic.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Player variables
img_player = pygame.image.load("rocket.png")
player_x = 368
player_y = 536
player_x_change = 0
def player(x,y):
    screen.blit(img_player, (x,y))

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

# bullet variables
img_bullet = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 536
bullet_x_change = 0
bullet_y_change = 3
bullet_visible = False

# score
score = 0
#font = pygame.font.Font('fastest.ttf', 32)
text_x = 10
text_y = 10

# Game Loop
is_exec = True
while is_exec:
    # RGB
    screen.fill((205, 144, 228))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_exec = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    player_x += player_x_change
    player(player_x,player_y)


    pygame.display.update()