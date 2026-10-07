import pygame
import random


def CreatePoint(x, y):
    while 1:
        px = random.randint(0, SCREEN_WIDTH - WIDTH) // WIDTH * WIDTH
        py = random.randint(0, SCREEN_HEIGHT - HEIGHT) // HEIGHT * HEIGHT
        if not Intersects(x, y, px, py):
            return (px, py)


def Intersects(x, y, px, py):
    return px >= x and px + RADIUS <= x + WIDTH and py >= y and py + RADIUS <= y + HEIGHT


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

WIDTH = 50
HEIGHT = 50
RADIUS = 10
x = WIDTH
y = HEIGHT
speed = 50

points = set()
for i in range(1):
    points.add(CreatePoint(x, y))
creationSpeed = 10
creationAccel = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            mx = x
            my = y
            if (event.key == pygame.K_w) or (event.key == pygame.K_UP):
                my -= speed
            elif (event.key == pygame.K_a) or (event.key == pygame.K_LEFT):
                mx -= speed
            elif (event.key == pygame.K_s) or (event.key == pygame.K_DOWN):
                my += speed
            elif (event.key == pygame.K_d) or (event.key == pygame.K_RIGHT):
                mx += speed
            if (mx >= 0) and (mx + WIDTH <= SCREEN_WIDTH) and (my >= 0) and (my + HEIGHT <= SCREEN_HEIGHT):
                x = mx
                y = my

    eaten = []
    for point in points:
        if Intersects(x, y, point[0], point[1]):
            eaten.append(point)
    for point in eaten:
        points.remove(point)
        points.add(CreatePoint(x, y))

    screen.fill("white")
    pygame.draw.rect(screen, "red", (x, y, WIDTH, HEIGHT))
    for point in points:
        dx = point[0] + WIDTH // 2
        dy = point[1] + HEIGHT // 2
        pygame.draw.circle(screen, "blue", (dx, dy), RADIUS)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
