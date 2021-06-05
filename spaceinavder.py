# Importing and Intilizing Pygame , Importing Random , Import Maths
import pygame
import random
import math

pygame.init()

# Creating The Screen For Our Game
screen = pygame.display.set_mode((800, 600))

# Title
pygame.display.set_caption('Space Invander Game')

# Icon
icon = pygame.image.load('launch.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('ufo.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(0, 100)
enemyX_change = 0.3
enemyY_change = 40

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"

score = 0


def player():
    screen.blit(playerImg, (playerX, playerY))


def enemy():
    screen.blit(enemyImg, (enemyX, enemyY))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x,y))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX, 2) + math.pow(enemyY-bulletY, 2))
    if distance < 27:
        return True
    else:
        return False 


# Game Loop
running = True
while running:

    screen.fill(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.4
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.4
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerX_change = 0
            if event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Adding Boundries So that our player cannot go outside
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    # Enemy Movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    if enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    # Bullet Movement
    if bulletY < 0 :
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 800)
        enemyY = random.randint(0, 100)
        

    # Calling The Functions
    enemy()
    player()
    pygame.display.update()
