import pygame
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))
# screen.fill((250, 250, 200))
pygame.display.set_caption('Invader Game')

# player 
playerImg = pygame.image.load('player.png')
playerX, playerY = 370, 480
playerX_change = 0

# mixer.Sound('laser.wav').play()

running = True


def player(x, y):
    screen.blit(playerImg, (x, y))


while running:
    screen.fill((0, 0, 0))
    # font = pygame.font.SysFont(None, 80)
    # message = font.render('this is test text', False, (255, 255, 255))
    # screen.blit(message, (20, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    playerX += 1
    player(playerX, playerY)
    pygame.display.update()
