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
background = pygame.image.load('Background.jpg')

# We add music
mixer.music.load('BackgroundMusic.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Player variables
img_player = pygame.image.load("rocket.png")
player_x = 368
player_y = 520
player_x_change = 0

# Enemy variables
img_enemy = pygame.image.load("enemy.png")
enemy_x = random.randint(0,736)
enemy_y = random.randint(50,200)
enemy_x_change = 0.3
enemy_y_change = 50

# bullet variables
img_bullet = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 500
bullet_x_change = 3
bullet_y_change = 1
bullet_visible = False

# score
score = 0
#font = pygame.font.Font('fastest.ttf', 32)
text_x = 10
text_y = 10

# Player Function
def player(x,y):
    screen.blit(img_player, (x,y))

# Enemy Function
def enemy(x,y):
    screen.blit(img_enemy, (x,y))

# Shoot Bullet function
def shoot_bullet(x,y):
    global bullet_visible
    bullet_visible = True
    screen.blit(img_bullet, (x + 16, y + 10))

# detect collisions
def there_collision(x_1,y_1,x_2, y_2):
    distance= math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1 ,2))
    if distance < 27:
        return True
    else:
        return False
# Game Loop
is_exec = True
while is_exec:
    # RGB
    #screen.fill((205, 144, 228))
    screen.blit(background,(0,0))
    #iterate event
    for event in pygame.event.get():

        # Close event
        if event.type == pygame.QUIT:
            is_exec = False
        # Keys event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -1
            if event.key == pygame.K_RIGHT:
                player_x_change = 1
            if event.key == pygame.K_SPACE:
                if not bullet_visible:
                    bullet_x= player_x
                    shoot_bullet(bullet_x, bullet_y)

        #KeyUp event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Modify Location  player
    player_x += player_x_change

    #Keep player inside
    if player_x <=0:
        player_x =0
    if player_x >= 736:
        player_x = 736

    # Modify Location enemy
    enemy_x += enemy_x_change

    # Keep enemy inside
    if enemy_x <= 0:
       enemy_x_change = 1
       enemy_y += enemy_y_change
    elif enemy_x >= 736:
       enemy_x_change = -1
       enemy_y += enemy_y_change

    # Move bullet
    if bullet_y <= -64:
        bala_y =500
        bullet_visible= False

    if bullet_visible:
        shoot_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    # collision
    collision = there_collision(enemy_x, enemy_y, bullet_x, bullet_y)
    if collision:
        bullet_y = 500
        bullet_visible =  False
        score +=1
        print (score)
        enemy_x = random.randint(0, 736)
        enemy_y = random.randint(50, 200)

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)

    #Update display
    pygame.display.update()