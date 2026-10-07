import pygame
import math

WIDTH = 640
HEIGHT = 480
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
velocity_x = 1
velocity_y = 1
x = 150
y = 150
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    window.fill((0, 0, 0))
    pygame.draw.circle(window, "cyan", (x, y), 25)
    y += velocity_y
    x += velocity_x
    if y-25 <= 0:
        velocity_y = -velocity_y
    if x-25 <= 0:
        velocity_x = -velocity_x
    if x + 25 >= WIDTH:
        velocity_x = -velocity_x
    if y + 25 >= HEIGHT:
        velocity_y = -velocity_y
    pygame.display.flip()

    clock.tick(60)