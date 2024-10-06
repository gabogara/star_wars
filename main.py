import pygame

pygame.init()
size=(800,600)
screen = pygame.display.set_mode(size)

# Title and Icon
pygame.display.set_caption("Star wars")
icon = pygame.image.load("ovni.png")
pygame.display.set_icon(icon)
background = pygame.image.load('Fondo.jpg')
