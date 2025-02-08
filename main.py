import pygame
from random import randint as ra

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Shoot Game")
icon = pygame.image.load("images/target.png")
pygame.display.set_icon(icon)
target_image = pygame.image.load("images/apple.png")
target_width = 80
target_height = 80
target_x =ra(0 SCREEN_WIDTH - target_width)
target_y = ra(0, SCREEN_HEIGHT - target_height)

color =(ra(0, 255), ra(0, 255), ra(0, 255))


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



pygame.quit()
