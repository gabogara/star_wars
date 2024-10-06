import pygame

pygame.init()
size=(800,600)
screen = pygame.display.set_mode(size)
is_run = True
while is_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             is_run = False