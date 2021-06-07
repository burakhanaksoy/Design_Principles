><h1>Singleton</h1>

In software engineering, the singleton pattern is a software design pattern that restricts the instantiation of a class to one "single" instance.
This is useful when exactly one object is needed to coordinate actions across the system. The term comes from the mathematical concept of a singleton.

>Critics consider the singleton to be an anti-pattern in that it is frequently used in scenarios where it's not beneficial, introduces unnecessary restrictions in situations where a sole instance of a class is not actually required, and introduces global state into an application..

<h5>Long story short. A singleton is a component(class) that is instantiated only once.</h5>

<h2>Example</h2>

```python
class Database:
    _instance = None

    def __init__(self):
        print('Creating database...')

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)

        return cls._instance
```

<h5>Althoug this code may seem innocent at first, it is not :confused:</h5> It uses __init__ method for each object..

```python
if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 is d2)
```

Outputs 

```
Creating database...
Creating database...
True
```
<h5>So, this should not be used as a singleton creating mechanism since singletons are meant to be initialized only once in our applications</h5>

In this case, one, although cannot have different instance, can initialize different singletons from the same singleton class. Not good..

One way to prevent this is to use a class level decorator

```python
def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)

        return instances[class_]

    return get_instance
```

```python
@singleton
class Database:
    def __init__(self):
        print('Creating database...')
```

```python
if __name__ == '__main__':
    db1 = Database()
    db2 = Database()
    print(db1 is db2)
```

Outputs

```
Creating database...
True
```
<h2>Alternative to Using Decorator</h2>

<h5>One alternative to using a decorator is to use a metaclass implementation</h5>

```python
class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)

        return cls._instance[cls]
```

```python
class Database(metaclass=Singleton):
    def __init__(self):
        print('Creating database...')
```

```python
if __name__ == '__main__':
    db1 = Database()
    db2 = Database()
    print(db1 == db2)
```

Outputs

```
Creating database...
True
```
<h2>Shared State Implementation</h2>

```python
class CEO:

    _shared_state = {
        'name': 'Burak',
        'age': 25
    }

    def __init__(self):
        self.__dict__ = self._shared_state

    def __str__(self):
        return f'name: {self.name} age: {self.age}'
```

```python
if __name__ == '__main__':
    ceo1 = CEO()
    ceo2 = CEO()

    print(ceo1 == ceo2)
```

```
False
```

<h4>However, ceo1 and ceo2 are not the same objects</h4>

So, we can do something like this..

```python
class Monostate:
    _shared_state = {
        'name': 'Burak',
        'age': 25
    }

    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Monostate, cls).__new__(
                cls, *args, **kwargs)
            cls._instances[cls].__dict__ = cls._shared_state

        return cls._instances[cls]
```

```python
class CEO(Monostate):

    def __str__(self):
        return f'name: {self.name} age: {self.age}'
```

```python
if __name__ == '__main__':
    ceo1 = CEO()
    ceo2 = CEO()
    print(ceo1)
    print(ceo1 == ceo2)
```

Outputs

```
name: Burak age: 25
True
```

<h3>Opinion</h3>

Probably the best approach is ```decorator implementation```...
