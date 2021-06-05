# Design_Principles
I will be studying design patterns and principles in this repository

> <h1> The Patterns

Creational | Structural | Behavioral
------------ | ------------- | -------------
Builder | Adapter | Chain of responsibility
Factories [Abstract Factory, Factory Method] | Bridge | Command
Prototype | Composite | Interpreter
Singleton | Decorator | Iterator
$ | Facade | Mediator
$ | Flyweight | Memento
$ | Proxy | Observer
$ | $ | State
$ | $ | Strategy
$ | $ | Template method
$ | $ | Visitor
  

> <h2> SOLID Principles
  <h3> 1 - SRP / SOC<br><br>
    SRP : Single Responsibility Principle<br><br>
    SOC : Separation of Concerns principle<br>
  </h3>

>  SRP and SOC are pretty much the same thing in that they mean "If you have a class, that class should have its primary responsibility, whatever it's meant to be doing, and it shouldn't take on other responsibilities."

  Let's say that we have a Journal class, and it's responsibility is to hold our journals with methods ``` add_entry ``` and ```remove_entry```
  
  ```python
   class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count} : {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)
  ```
  <h5> So far so good, our class is doing what it's supposed to be doing, which are adding entry and removing entry..</h5>

  Let's break the ```Single Responsibility Principle```

  We are going to add new methods that are not meant to be implemented in this class...
  
  ```python
  def save(self, filename):
        with open(f'{filename}', 'w') as f:
            f.write(str(self))

    def load(self, filename):
        with open(f'{filename}', 'r') as f:
            return f.read()
```
  Implementing these methods inside Journal class will add <b>Persistence responsibility</b> to the Journal class, which in turn is bad for the following reasons:
  * 1- If we want to hold diaries and other types of journals later on, we would have to write their own ```save``` and ```load``` methods.
  * 2- If we want to change these methods in the future, we'd have to change each of them individually, which is tedious.
  
    <h5> So, let's delegate Persistence Responsibility to a class named PersistenceManager</h5>
  ```python
  class PersistenceManager:
    @staticmethod
    def save(journal, filename):
        ''' Persists data to filename '''
        with open(f'{filename}', 'w') as f:
            f.write(str(journal))

    @staticmethod
    def load(filename):
        ''' Loads data from filename '''
        with open(f'{filename}', 'r') as f:
            return f.read()
```
  <h5>Then, I can use this in my Journal class as follows</h5>
  
  ```python
  PersistenceManager.save(my_journal, 'My First Journal.txt')
j = PersistenceManager.load('My First Journal.txt')
print(j)
```
  > <h3> Main Takeaway</h3>
  <h5>The main takeaway of this example is to show that we don't want to overload our classes with too many "responsibilities"</br>
  In computing, the opposite is called ~God Object.. God Object is an antipattern which is probably written by a newbie developer, like me :),<br> that has all of the responsibilities in a single class. This is bad programming...</h5>

  <h3> 2 - OPC / Open Closed Principle</h3>
  
  <h5>Open Closed Principle suggests that when you add a new functionality, you add it via extension, not modification...<br>
  "OCP = Open for extension, closed for modification"</h5>
  
  <h5>This can be understood as after you've written a class and tested it, you should not ```modify``` it. Instead, you should ```extend``` it</h5>
  
  Imagine that we have the following class named Product for products in our website.
  
  ```python
  from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
```
Now, imagine that we have a requirement in our project where we should add filtering functionality to our products by color..
  So in this case, we might implement something like this.
  ```python
  class FilterProduct:
    def filter_by_color(self, products, color):
        for product in products:
            if product.color == color:
                yield product
```
  So you implemented this, and tested it, and take it to production.. Then you have a new requirement where you<br> should add a new filter for size..
  You probably modify the class with the following code
  ```python
  def filter_by_size(self, products, size):
        for product in products:
            if product.size == size:
                yield product
  ```
  <h5> However, This is not a good idea! Because if, later on, we want to add different filtering requirements, we have to add new functions,
  and this goes on forever! Instead, let us define base classes for Specification and Filter</h5>
  
  ```python
  class Specification:
    def is_satisfied(self, item):
        pass


class Filter:
    def filter(self, items, spec):
        pass
```
  
  <h5> We are going to be extending from these classes when we want to extend on our specifications and filters. </h5>
  
Note that we use ```pass``` operator since we will merely use these classes for ```inheritance and overloading```. 
  
```python
  class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color
  ```
  In the same way, if I want to implement a size specification, I'd do:
  ```python
  class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size
  ```
  <h5>Test it!</h5>
  
  ```python
  if __name__ == '__main__':

    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.MEDIUM)
    house = Product('House', Color.BLUE, Size.LARGE)

    items = (apple, tree, house)

    # Old(bad) way of filtering
    fp = FilterProduct()
    for item in fp.filter_by_color(items, Color.GREEN):
        print(f'{item.name} is green.')

    # Better approach
    bf = BetterFilter()
    spec = ColorSpecification(Color.GREEN)

    for item in bf.filter(items, spec):
        print(f'{item.name} is green.')
  ```
  
