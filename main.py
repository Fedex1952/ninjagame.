import time
from colorama import Fore
import pygame

pygame.init()
# skapar en klocka kopplat till spelet som är satt till 24
clock = pygame.time.Clock()
ticks_per_second = 24

# Skriver texten Ninja game
pygame.display.set_caption("Ninja game")
# gör ett pygame fönster med 800x600 pixlar.
screen_width = 800
screen_height = 600

# Skapar bakgrund.
screen = pygame.display.set_mode((screen_width, screen_height))
# laddar in .jpg och skalar om den till 800x600
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, [800, 600])
# skapar en rektangel i 800x600
imagerect = background.get_rect()
imagerect.center = (800, 600)
# Centrerar bilden.
screen.blit(background, imagerect)
screen.blit(background, (0, 0))

# definerar variablar.
x = 100
y = 375
change_x = 0
change_y = 0
is_grounded = True
CanMoveRight = True
CanMoveLeft = True
gravity = 1
speed = 12
JumpHeight = -20
LeftBorder = -10
RightBorder = 740
GroundLevel = 370
Timer = 0

# Laddar sprite 80x80
sprite_image = pygame.transform.scale(pygame.image.load("Eninja.png"), (80, 80))
screen.blit(sprite_image, (x, y))
# Huvudloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


# sprite kan gå vänster
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        change_x = -speed
# sprite kan gå höger
    if keys[pygame.K_RIGHT]:
        change_x = speed
# sprite kan hoppa
    if keys[pygame.K_UP] and is_grounded:
        change_y = JumpHeight
    if not keys[pygame.K_UP] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        change_x = 0


# gör så sprite endast kan hoppa när den är på ground nivå.
    if y == GroundLevel:
        is_grounded = True
    else:
        is_grounded = False
# sprite kan inte gå ut ur bilden vänster eller höger.
    if LeftBorder > x:
        CanMoveLeft = False
    else:
        CanMoveLeft = True

    if RightBorder < x:
        CanMoveRight = False
    else:
        CanMoveRight = True

    if change_x == -speed and CanMoveLeft == False:
        change_x = 0
    if change_x == speed and CanMoveRight == False:
        change_x = 0

# uppdaterar x and y så sprite faktiskt kan röra på sig.
    x += change_x
    y += change_y
    change_y += gravity

    # gör så att sprite inte går igenom marken.
    if y >= GroundLevel:
        y = GroundLevel

# renderar background och sprite igen.
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    screen.blit(sprite_image, (x, y))
    pygame.display.update()

# visar spriten för varje tick som definerats till 24.
    clock.tick(ticks_per_second)
