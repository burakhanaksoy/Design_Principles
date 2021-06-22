from abc import ABC, abstractmethod


class Shape(ABC):
    '''Unit class for Shape'''

    @abstractmethod
    def __str__(self):
        raise NotImplementedError("You have to implement __str__")


class Circle(Shape):
    '''Unit class for Circle'''

    def __init__(self, radius):
        self.radius = radius

    def resize(self, number):
        self.radius *= number

    def __str__(self):
        return f'A circle with radius {self.radius}'


class Square(Shape):
    '''Unit class for Square'''

    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'A square with side {self.side}'


class AddColor:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def __str__(self):
        return f'{self.shape} with color {self.color}'


class AddTransparency:
    def __init__(self, shape, transparency):
        self.shape = shape
        self.transparency = transparency

    def __str__(self):
        return f'{self.shape} with %{int(self.transparency * 100)} transparency'


if __name__ == "__main__":
    circle = Circle(2)
    print(circle)

    half_transparent_circle = AddTransparency(circle, 0.3)
    print(half_transparent_circle)

    green_half_transparent_circle = AddColor(half_transparent_circle, 'green')
    print(green_half_transparent_circle)
