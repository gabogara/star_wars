import pygame
from pygame import mixer


pygame.init()
size=(800,600)
screen = pygame.display.set_mode(size)

# Title and Icon
pygame.display.set_caption("Star wars")
icon = pygame.image.load("ovni.png")
pygame.display.set_icon(icon)
background = pygame.image.load('Fondo.jpg')

# We add music
mixer.music.load('BackgroundMusic.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Player variables
img_player = pygame.image.load("rocket.png")
player_x = 368
player_y = 500
player_x_change = 0




