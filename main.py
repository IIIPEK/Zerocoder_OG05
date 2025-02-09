import pygame
from random import randint as ra

from pygame.gfxdraw import pixel
from requests.packages import target

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
target_image = pygame.transform.scale(target_image, (target_width, target_height))
target_x =ra(0, SCREEN_WIDTH - target_width)
target_y = ra(0, SCREEN_HEIGHT - target_height)

color =(ra(0, 255), ra(0, 255), ra(0, 255))


running = True

while running:
    screen.fill(color=color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                img_x, img_y = mouse_x - target_x, mouse_y - target_y
                pixel = target_image.get_at((img_x, img_y))
                if pixel.a > 0:
                    target_x = ra(0, SCREEN_WIDTH - target_width)
                    target_y = ra(0, SCREEN_HEIGHT - target_height)
                    color = (ra(0, 255), ra(0, 255), ra(0, 255))


    screen.blit(target_image, (target_x, target_y))
    pygame.display.update()

pygame.quit()
