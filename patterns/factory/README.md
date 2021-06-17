<h1>Factory</h1>

> A component responsible solely for the wholesale (not piecewise) creation of objects.

<h2>Motivation</h2>

- Object creation logic becomes too convoluted
- Initializer is not descriptive
- Wholesale object creation (non-piecewise, unlike Builder) can be outsourced to
  - A separate method (Factory method)
  - That may exist in a separate class (Factory)
  - Can create a hierarchy of factories with Abstract Factory

<h3>Factory Method</h3>

Imagine that you have a Point class for points in cartesian coordinate system. Your initializer would probably look like this.
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
```

This is all fine and dandy for cartesian coordinate system. The main question though, is:</br>
<b>What happens when you want to initialize your points in Polar coordinates</b>

Let's say that you want to initialize your points in Polar Coordinates.
One possible idea might be adding an if-check to __init__ method and initialize as follows:

```python
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

        elif coordinate_system == Coordinates.POLAR:
            self.x = a * cos(a)
            self.y = b * sin(b)
            
        else:
          pass
```

However, this is not a good idea because what happens when you want to initialize your points in a different coordinate system. 😖
Also, it breaks the open-closed principle...

Instead of this, then, we can use the following
```python
from math import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))

    def __str__(self):
        return f'x:{self.x} y:{self.y}'

```

As you can see, this is a much better approach in that
- We don't have to make an if check
- We have a single initializer
- @staticmethod usage is understandable and coherent
- Open-closed principle stays intact

<b>Here, @staticmethod is a factory method. In other words, a factory method is a method that creates objects</b>
![success_kid](https://user-images.githubusercontent.com/31994778/122351937-516af300-cf57-11eb-976d-57ed6c5c603e.jpeg)


<h3>Factory</h3>

Factories are used there are lots of factory methods and they need to be `classified` (a class of factory methods). This is good because it follows `separation of concerns` a.k.a `Single responsibility`

```python
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
```

In this case, we are kind of breaking ```dependency inversion principle``` in which modules should be loosely coupled to one another. However, there's nothing much we can do about this.

<b>All in all, factory methods and factory classes are very good  because they alleviate complex initialization processes, writing lots of lines inside __init__ method, and help building scalable applications.</b>
