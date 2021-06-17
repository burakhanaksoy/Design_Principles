from math import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x:{self.x} y:{self.y}'


class PointFactory:
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))


point = PointFactory.new_cartesian_point(2, 3)
point_two = PointFactory.new_polar_point(1, pi/2)
print(point)
print(point_two)
