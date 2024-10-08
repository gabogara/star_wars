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

# I add music
mixer.music.load('BackgroundMusic.mp3')
mixer.music.set_volume(0.2)
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

# bullet variables
img_bullet = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 500
bullet_x_change = 0
bullet_y_change = 3
bullet_visible = False

# score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10

# end of game text
final_font = pygame.font.Font('freesansbold.ttf', 40)

def final_text():
    my_final_font = final_font.render("Game over", True, (255, 255, 255))
    screen.blit(my_final_font, (60, 200))

# Show score function
def show_score(x, y):
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (x, y))

# Player Function
def player(x,y):
    screen.blit(img_player, (x,y))

# Enemy Function
def enemy(x,y, ene):
    screen.blit(img_enemy[ene], (x,y))

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

    # Image background
    screen.blit(background,(0,0))

    #iterate event
    for event in pygame.event.get():

        # event close
        if event.type == pygame.QUIT:
            is_exec = False

        # event press keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -1
            if event.key == pygame.K_RIGHT:
                player_x_change = 1
            if event.key == pygame.K_SPACE:
                sound_bullet = mixer.Sound('blast.mp3')
                sound_bullet.play()
                if not bullet_visible:
                    bullet_x = player_x
                    shoot_bullet(bullet_x, bullet_y)

        # key release event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

   # modify player location
    player_x += player_x_change

    # keep player inside edges
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # modify enemy location
    for e in range(enemy_amount):

        # End game
        if enemy_y[e] > 500:
            for k in range(enemy_amount):
                enemy_y[k] = 1000
            final_text()
            break

        enemy_x[e] += enemy_x_change[e]

        # keep enemy inside borders
        if enemy_x[e] <= 0:
            enemy_x_change[e] = 1
            enemy_y[e] += enemy_y_change[e]
        elif enemy_x[e] >= 736:
            enemy_x_change[e] = -1
            enemy_y[e] += enemy_y_change[e]

        # collision
        collision = there_collision(enemy_x[e], enemy_y[e], bullet_x, bullet_y)
        if collision:
            sound_collision = mixer.Sound('explosion.mp3')
            sound_collision.play()
            bullet_y = 500
            bullet_visible = False
            score += 1
            enemy_x[e] = random.randint(0, 736)
            enemy_y[e] = random.randint(50, 200)

        enemy(enemy_x[e], enemy_y[e], e)

    # bullet trajectory
    if bullet_y <= -64:
        bullet_y = 500
        bullet_visible = False

    if bullet_visible:
        shoot_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x, player_y)

    show_score(text_x, text_y)

    # Update
    pygame.display.update()