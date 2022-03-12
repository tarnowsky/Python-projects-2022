from cmath import pi
from logging import setLogRecordFactory
from math import sin, cos
from tkinter import W
import pygame, sys

pygame.init()
clock = pygame.time.Clock()

screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), 0, 1)
bg_color = 255, 255, 255

x_offset = screen_width / 2
y_offset = 150

# Main variables
pendulum_color = pygame.Color(0, 0, 0)

canvas = pygame.display.set_mode((screen_width, screen_height))
canvas.fill((0, 0, 0))
pygame.draw.line(canvas, pendulum_color, (50, 80), (40, 140))

class FormulaImplicator():
    def __init__(self, m1, r1, a1, a1_v, 
                       m2, r2, a2, a2_v, g = 1):

        self.m1, self.m2 = m1, m2
        self.r1, self.r2 = r1, r2
        self.a1, self.a2 = a1, a2
        self.a1_v, self.a2_v = a1_v, a2_v
        self.g = g

    def acceleration(self):
        num1 = -self.g * (2 * self.m1 + self.m2) * sin(self.a1)
        num2 = -self.m2 * self.g * sin(self.a1 - 2 * self.a2)
        num3 = -2 * sin(self.a1 - self.a2) * self.m2
        num4 = (self.a2_v ** 2 * self.r2 + self.a1_v ** 2 * self.r1 * cos(self.a1 - self.a2))

        det = self.r1 * (2 * self.m1 + self.m2 - self.m2 * cos(2 * self.a1 - 2 * self.a2))

        a1_a = (num1 + num2 + num3 * num4) / det

        num1 = 2 * sin(self.a1 - self.a2)
        num2 = self.a1_v ** 2 * self.r1 * (self.m1 + self.m2)
        num3 = self.g * (self.m1 + self.m2) * cos(self.a1)
        num4 = self.a2_v ** 2 * self.r2 * self.m2 * cos(self.a1 - self.a2)
        
        a2_a = (num1 * (num2 + num3 + num4)) / det

        return a1_a, a2_a

class PendulumDrawing():
    def __init__(self, r, m, a, startPos=(x_offset, y_offset), x_offset=screen_width / 2, y_offset=150, first_pendulum = True):
        self.r = r
        self.m = m
        self.a = a
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.startPos = startPos
        if first_pendulum:
            self.is_first_pendulum = 1
        else: self.is_first_pendulum = 0

    def drawPendulum(self):
        x = self.r * sin(self.a) + self.x_offset * self.is_first_pendulum
        y = self.r * cos(self.a) + self.y_offset * self.is_first_pendulum

        


r1 = 150
r2 = 150
m1 = 10
m2 = 10

a1 = pi / 2
a2 = -pi / 2 
a1_v = 0
a2_v = 0
a1_a = 0
a2_a = 0

g = 0.1

x1 = r1 * sin(a1) + x_offset
y1 = r1 * cos(a1) + y_offset

x2 = r2 * sin(a2) + x1
y2 = r2 * cos(a2) + y1

path_coord_list = [(x2, y2)]

friction = 0.99999

startPos = (x_offset, y_offset) # Translate (0, 0)

acceleration_calc = FormulaImplicator(m1, r1, a1, a1_v, m2, r2, a2, a2_v, g)

if __name__ == '__main__':
    while True:
        pygame.display.set_caption('Double Pendulum')
        screen.fill(bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        x1 = r1 * sin(a1) + x_offset
        y1 = r1 * cos(a1) + y_offset

        x2 = r2 * sin(a2) + x1
        y2 = r2 * cos(a2) + y1

        path_coord_list.append((x2, y2))
        pygame.draw.lines(screen, (99, 99, 99), False, path_coord_list)

        pygame.draw.line(screen, pendulum_color, startPos, (x1, y1))
        pygame.draw.circle(screen, pendulum_color, (x1, y1), m1, m1)
        pygame.draw.line(screen, pendulum_color, (x1, y1), (x2, y2))
        pygame.draw.circle(screen, pendulum_color, (x2, y2), m2, m2)
        
        a1_a = acceleration_calc.acceleration()[0]
        a2_a = acceleration_calc.acceleration()[1]

        a1_v += a1_a
        a2_v += a2_a
        a1 += a1_v
        a2 += a2_v

        # a1 *= friction
        # a2 *= friction
        # a1 += 0.01
        # a2 -= 0.04

        acceleration_calc = FormulaImplicator(m1, r1, a1, a1_v, m2, r2, a2, a2_v, g)

        pygame.display.flip()
        clock.tick(120)