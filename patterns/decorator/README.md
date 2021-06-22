<h1>Decorator</h1>

>Adding behavior without altering the class itself.
>
<h2>Definition</h2>

<p>
  <i>"A decorator is a pattern that facilitates additional behaviors to individual objects without inheriting from them."</i>
</p>

<h2>Motivation</h2>

- Want to add augment an object with additional functionality
- Do not want to rewrite or alter existing code (OCP)
- Want to keep new functionality separate (SRP)

<h2>Python Functional Decorators</h2>

In Python, decorators are objects that <b>wraps</b> another object to add additional features to it.

Let's say that we have a function, called `some_op`

```python
import time

def some_op():
    print('do something')
    time.sleep(1)
    print('finish operation')
    return 123
```

Here, let's say that we want to measure the time elapsed when `some_op` is run..

Using SRP with Pythonic way, we can define a decorator object, called `time_taken`

```python
def time_taken(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f'Time taken: {(end-start):3f}s')
        return result
    return wrapper
```

Let's run 

```python
if __name__ == '__main__':
    time_taken(some_op)()
```

The output is:

```
do something
finish operation
Time taken: 1.004728s
```
One great way about Python is that we can actually use decorators with `@` symbol.

```python
@time_taken
def some_op():
    print('do something')
    time.sleep(1)
    print('finish operation')
    return 123

if __name__ == '__main__':
    some_op()
```

Outputs

```
do something
finish operation
Time taken: 1.004728s
```

In addition, we can also use multiple decorators to augment an object... (This is an awesome feature)

say that we have `disconnect` function which disconnects from server, session etc., after function is run..

```python
def disconnect(func):
    def wrapper():
        result = func()
        print(f'disconnected...')
        return result
    return wrapper
```

We can do something like as follows

```python
@disconnect
@time_taken
def some_op():
    print('do something')
    time.sleep(1)
    print('finish operation')
    return 123
```

Outputs:

```
do something
finish operation
Time taken: 1.002328s
disconnected...
```


<h2>Classic Decorator</h2>

<b>In typical object oriented programming, a decorator is simply a class which takes the decorated object as an argument. It takes some additional values and provides the extra functionality.</b>

Let's say that we want to decorate shapes.

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    '''Unit class for Shape'''

    @abstractmethod
    def __str__(self):
        raise NotImplementedError("You have to implement __str__")
```
Here, we have our abstract base class for `Shape`.

Then, create different shapes.

```python
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
```

Define our decorators.

```python
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
```

Test!

```python
if __name__ == "__main__":
    circle = Circle(2)
    print(circle)

    half_transparent_circle = AddTransparency(circle, 0.3)
    print(half_transparent_circle)

    green_half_transparent_circle = AddColor(half_transparent_circle, 'green')
    print(green_half_transparent_circle)
```

Outputs:

```
A circle with radius 6
A circle with radius 6 with %30 transparency
A circle with radius 6 with %30 transparency with color green
```

<img width="724" alt="Screen Shot 2021-06-22 at 9 43 10 PM" src="https://user-images.githubusercontent.com/31994778/122981842-df553c80-d3a2-11eb-848f-a8c13d5a7095.png">

