from enum import Enum
from math import *


class Coordinates(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, a, b, coordinate_system):
        if coordinate_system == Coordinates.CARTESIAN:
            self.x = a
            self.y = b
            print('Initialized in cartesian')
        elif coordinate_system == Coordinates.POLAR:
            self.x = a * cos(a)
            self.y = b * sin(b)
            print('Initialized in polar')
        else:
            pass

    def __str__(self):
        return f'x:{self.x} y:{self.y}'


point = Point(2, 3, Coordinates.CARTESIAN)
print(point)

point_two = Point(2, 3, Coordinates.POLAR)
print(point_two)
