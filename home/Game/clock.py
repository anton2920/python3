import pygame
import time
import math


def Now():
    now = time.localtime()
    return now.tm_hour, now.tm_min, now.tm_sec


# 13, 14, [0;1] == m / 60
def Lerp(a, b, t):
    return a + (b - a) * t


def Deg2Rad(angle):
    return angle * math.pi / 180


WIDTH = 640
HEIGHT = 480

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

h = 0
m = 0
s = 0

black = (0, 0, 0)
gray = (100, 100, 100)

percent = 0.45
radius = min(WIDTH * percent, HEIGHT * percent)
thickness = 5

font = pygame.font.SysFont("Arial", 30)
print(font.get_height())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((255, 255, 255))

    center = (WIDTH // 2, HEIGHT // 2)
    pygame.draw.circle(window, (0, 0, 0), center, radius)
    pygame.draw.circle(window, (255, 255, 255), center, radius - thickness)
    pygame.draw.circle(window, (0, 0, 0), center, 10)

    for i in range(0, 360, 6):
        angle = Deg2Rad(i)
        dr = 5
        r = radius - thickness / 2
        x1 = (r - dr) * math.cos(angle) + center[0]
        y1 = (r - dr) * math.sin(angle) + center[1]
        x2 = (r + dr) * math.cos(angle) + center[0]
        y2 = (r + dr) * math.sin(angle) + center[1]
        pygame.draw.line(window, (0, 0, 0), (x1, y1), (x2, y2), 2)

    for i in range(12):
        angle = Deg2Rad(30 * i - 90)
        r = radius - font.get_height() + 5
        x = r * math.cos(angle) + center[0]
        y = r * math.sin(angle) + center[1]
        i = 12 if not i else i
        text = font.render(str(i), True, (0, 0, 0))
        window.blit(text, (x - text.get_width()//2, y-text.get_height()//2))

    h, m, s = Now()
    pygame.display.set_caption(f"{h:02}:{m:02}:{s:02}")

    s_length = radius - radius * 0.1
    m_length = radius - radius * 0.2
    h_length = radius - radius * 0.3
    s_angle = (s * 6 - 90) * math.pi / 180
    m_angle = (Lerp(m, m + 1, s / 60) * 6 - 90) * math.pi / 180
    h_angle = (Lerp(h, h + 1, m / 60 + s / 3600) * 30 - 90) * math.pi / 180

    pygame.draw.line(window, black, center, (h_length * math.cos(h_angle) + center[0], h_length * math.sin(h_angle) + center[1]), 4)  # Hour hand.
    pygame.draw.line(window, gray, center, (m_length * math.cos(m_angle) + center[0], m_length * math.sin(m_angle) + center[1]), 2)  # Minute hand.
    pygame.draw.line(window, gray, center, (s_length * math.cos(s_angle) + center[0], s_length * math.sin(s_angle) + center[1]), 1)  # Second hand.

    pygame.display.flip()
    clock.tick(60)
