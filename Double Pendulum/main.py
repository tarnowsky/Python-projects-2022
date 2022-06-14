from cmath import pi
from math import sin, cos
import pygame, sys

pygame.init()
clock = pygame.time.Clock()

screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
bg_color = 227, 218, 201

x_offset = screen_width / 2
y_offset = 200

pendulum_color = pygame.Color(255, 0, 0)
pendulum_color2 = pygame.Color(51, 29, 222)
# pendulum_color3 = pygame.Color(72, 156, 30)

path_color = 230, 55, 99
path_color2 = 94, 77, 232
# path_color3 = 83, 201, 24

class FormulaImplicator():
    def __init__(self, m1, r1,
                       m2, r2, g = 1.0):

        self.m1, self.m2 = m1, m2
        self.r1, self.r2 = r1, r2
        self.g = g

    def acceleration(self, a1, a1_v, a2, a2_v):
        num1 = -self.g * (2 * self.m1 + self.m2) * sin(a1)
        num2 = -self.m2 * self.g * sin(a1 - 2 * a2)
        num3 = -2 * sin(a1 - a2) * self.m2
        num4 = (a2_v ** 2 * self.r2 + a1_v ** 2 * self.r1 * cos(a1 - a2))

        det = self.r1 * (2 * self.m1 + self.m2 - self.m2 * cos(2 * a1 - 2 * a2))

        a1_a = (num1 + num2 + num3 * num4) / det

        num1 = 2 * sin(a1 - a2)
        num2 = a1_v ** 2 * self.r1 * (self.m1 + self.m2)
        num3 = self.g * (self.m1 + self.m2) * cos(a1)
        num4 = a2_v ** 2 * self.r2 * self.m2 * cos(a1 - a2)
        
        a2_a = (num1 * (num2 + num3 + num4)) / det

        return a1_a, a2_a

    def angle(self, a, a_v):
        a += a_v
        return a

    def velocity(self, a_v, a_a):
        a_v += a_a
        return a_v

class PendulumDrawing():
    def __init__(self, r, m, start_angle, is_first_pendulum=True, start_angle_main=0,
                 path_len=1, x_offset=screen_width / 2, y_offset=200):

        self.r = r
        self.m = m
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.path_len = path_len
        self.start_angle = start_angle
        self.is_first_pendulum = is_first_pendulum

        self.startPos_2 = 0, 0 # start position for second pendulum relative to the first

        self.path_coords = [self.coords_calc(self.start_angle, self.is_first_pendulum, start_angle_main)]

    def drawPendulum(self, a, a_mainPen=0, startPos=(x_offset, y_offset), pendulum_color=pendulum_color):

        x, y = self.coords_calc(a, self.is_first_pendulum, a_mainPen)

        self.startPos_2 = x, y # forming coords for the second pendulum to start drawing

        pygame.draw.line(screen, pendulum_color, startPos, (x, y))
        pygame.draw.circle(screen, pendulum_color, (x, y), self.m - 5, self.m - 5)

    def coords_calc(self, a, is_first_pendulum=True, a_mainPen=0):
        if is_first_pendulum:
            is_first_pendulum = 1
        else: is_first_pendulum = 0

        x = self.r * sin(a) + self.x_offset * is_first_pendulum
        y = self.r * cos(a) + self.y_offset * is_first_pendulum

        if not is_first_pendulum: # offseting the second pendulum for the coords of the first one
            x += first_pendulum.coords_calc(a_mainPen)[0]
            y += first_pendulum.coords_calc(a_mainPen)[1]

        return x, y

    def get_coords(self):
        return self.startPos_2
    #
    # def append_coord_list_value(self, x, y):
    #     self.path_coords.append((x, y))

    def drawPath(self, color=path_color):
        # print(self.path_coords)
        # sys.exit()
        self.path_coords.append(self.startPos_2)


        self.path_len += 1

        if self.path_len == 1000:
            del self.path_coords[0]
            self.path_len -= 1

        pygame.draw.lines(screen, color, False, self.path_coords)

r1 = 150
r2 = 150
m1 = 10
m2 = 10
a1 = pi / 2
a2 = pi / 2

r3 = 150
r4 = 150
m3 = 10
m4 = 10
a3 = pi / 2
a4 = pi / 2.0001

# r5 = 150
# r6 = 150
# m5 = 10
# m6 = 10
# a5 = -pi / 2
# a6 = pi / 2.001

a1_v = a2_v = a1_a = a2_a = a3_v = a4_v = a3_a = a4_a = 0
# a5_v = a6_v = a5_a = a6_a = 0

g = 0.1

friction = 0.99999

startPos = (x_offset, y_offset) # Translate (0, 0)

acceleration_calc = FormulaImplicator(m1, r1, m2, r2, g)
acceleration_calc2 = FormulaImplicator(m3, r3, m4, r4, g)
# acceleration_calc3 = FormulaImplicator(m5, r5, m6, r6, g)

first_pendulum = PendulumDrawing(r1, m1, a1)
second_pendulum = PendulumDrawing(r2, m2, a2, False, a1)

third_pendulum = PendulumDrawing(r3, m3, a3)
fourth_pendulum = PendulumDrawing(r4, m4, a4, False, a3)

# fifth_pendulum = PendulumDrawing(r5, m5, a5)
# sixth_pendulum = PendulumDrawing(r6, m6, a6, False, a5)


if __name__ == '__main__':
    while True:
        pygame.display.set_caption('Double Pendulum')
        screen.fill(bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        first_pendulum.drawPendulum(a1)
        second_pendulum.drawPendulum(a2, a1, first_pendulum.coords_calc(a1))
        second_pendulum.drawPath()

        third_pendulum.drawPendulum(a3, 0, startPos, pendulum_color2)
        fourth_pendulum.drawPendulum(a4, a3, third_pendulum.coords_calc(a3), pendulum_color2)
        fourth_pendulum.drawPath(path_color2)

        # fifth_pendulum.drawPendulum(a5, 0, startPos, pendulum_color3)
        # sixth_pendulum.drawPendulum(a6, a5, third_pendulum.coords_calc(a5), pendulum_color3)
        # sixth_pendulum.drawPath(path_color3)
        
        a1_a = acceleration_calc.acceleration(a1, a1_v, a2, a2_v)[0]
        a2_a = acceleration_calc.acceleration(a1, a1_v, a2, a2_v)[1]

        a1_v = acceleration_calc.velocity(a1_v, a1_a)
        a2_v = acceleration_calc.velocity(a2_v, a2_a)

        a1 = acceleration_calc.angle(a1, a1_v)
        a2 = acceleration_calc.angle(a2, a2_v)

        a1 *= friction
        a2 *= friction

        a3_a = acceleration_calc2.acceleration(a3, a3_v, a4, a4_v)[0]
        a4_a = acceleration_calc2.acceleration(a3, a3_v, a4, a4_v)[1]

        a3_v = acceleration_calc2.velocity(a3_v, a3_a)
        a4_v = acceleration_calc2.velocity(a4_v, a4_a)

        a3 = acceleration_calc2.angle(a3, a3_v)
        a4 = acceleration_calc2.angle(a4, a4_v)

        a3 *= friction
        a4 *= friction

        # a5_a = acceleration_calc2.acceleration(a5, a5_v, a6, a6_v)[0]
        # a6_a = acceleration_calc2.acceleration(a5, a5_v, a6, a6_v)[1]
        #
        # a5_v = acceleration_calc2.velocity(a5_v, a5_a)
        # a6_v = acceleration_calc2.velocity(a6_v, a6_a)
        #
        # a5 = acceleration_calc2.angle(a5, a5_v)
        # a6 = acceleration_calc2.angle(a6, a6_v)
        #
        # a5 *= friction
        # a6 *= friction

        acceleration_calc = FormulaImplicator(m1, r1, m2, r2, g)
        acceleration_calc2 = FormulaImplicator(m3, r3, m4, r4, g)
        # acceleration_calc3 = FormulaImplicator(m5, r5, m6, r6, g)

        pygame.display.flip()
        clock.tick(120)