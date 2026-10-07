import pygame
import time
import math


def Now(seconds=None):
    now = time.localtime(seconds)
    return now.tm_hour, now.tm_min, now.tm_sec


def Deg2Rad(angle):
    return angle * math.pi / 180


def Lerp(a, b, t):
    return a + (b-a)*t


WIDTH = 640
HEIGHT = 480

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

RADIUS = min(WIDTH, HEIGHT) * 0.45
THICKNESS = RADIUS * 0.02

center = (WIDTH // 2, HEIGHT // 2)

black = (0, 0, 0)
white = (255, 255, 255)
gray = (150, 150, 150)

s_length = RADIUS * 0.9
m_length = RADIUS * 0.8
h_length = RADIUS * 0.7

t = None
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill(white)

    pygame.draw.circle(window, black, center, RADIUS)
    pygame.draw.circle(window, white, center, RADIUS-THICKNESS)
    pygame.draw.circle(window, black, center, THICKNESS * 2)

    for i in range(60):
        l = 5
        r = RADIUS - THICKNESS//2
        p1 = ((r - l) * math.cos(Deg2Rad(i * 6)) + center[0], (r - l) * math.sin(Deg2Rad(i * 6)) + center[1])
        p2 = ((r + l) * math.cos(Deg2Rad(i * 6)) + center[0], (r + l) * math.sin(Deg2Rad(i * 6)) + center[1])
        pygame.draw.line(window, black, p1, p2, 2)

    h, m, s = Now(t)
    # t += 1

    pygame.display.set_caption(f"{h:02}:{m:02}:{s:02}")

    s_angle = Deg2Rad(s * 6 - 90)
    m_angle = Deg2Rad(Lerp(m, m+1, s/60) * 6 - 90)
    h_angle = Deg2Rad(Lerp(h, h+1, m/60 + s/3600) * 30 - 90)

    s_point = (s_length * math.cos(s_angle) + center[0], s_length * math.sin(s_angle) + center[1])
    m_point = (m_length * math.cos(m_angle) + center[0], m_length * math.sin(m_angle) + center[1])
    h_point = (h_length * math.cos(h_angle) + center[0], h_length * math.sin(h_angle) + center[1])

    print(h_point)

    pygame.draw.line(window, black, center, h_point, 4)
    pygame.draw.line(window, gray, center, m_point, 2)
    pygame.draw.line(window, gray, center, s_point, 1)

    pygame.display.flip()
    clock.tick(60)