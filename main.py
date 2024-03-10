# gör så pygame används
import pygame

pygame.init()

# gör ett pygame fönster med 960x540 pixlar.
screen = pygame.display.set_mode((960, 540))

# Skriver texten Ninja game
pygame.display.set_caption('Ninja game')

# laddar in .jpg och skalar om den till 960x540
image = pygame.image.load('background.jpg')
image = pygame.transform.scale(image, (960, 540))

# skapar en rektangel i 960x540
imagerect = image.get_rect()
imagerect.center = (960, 540)

# stänger ned spelet
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


# Gör fönstret svart sedan centrerar den bilden.
    screen.fill('black')
    screen.blit(image, imagerect)
    screen.blit(image, (0, 0))


pygame.display.update()
