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
  <h5>Yani aslinda OCP'yi kullanmamizin temel sebebi degisikliklerin surekli olacagini dusunup yeni requirementlarin(mesela yeni bir filtreleme isleminin) cok daha rahat bir sekilde implemente edilmesini saglamak.Dizayni en basta bu sekilde tutmamiz, buyuyen ve karmasiklasan yapinin daha rahat kontrol edilebilmesini sagliyor.Bunu soyle dusunebiliriz.</h5>
 
mesela eski tip ile devam etseydik ve color, size, ve baska bir spesifikasyon icin kontrol saglamamiz gerekseydi bu sefer ```def check_size_color_other_function(self)``` gibi bir kod yazacaktik bu da en az 10-15 satir bir kod olacakti. Halbuki OCP ile bunu ```AndSpecification``` class'ina args ile tanitarak yapabilir ve tek satirda bu isi cozebiliriz... 

  ```python
  # Implementing AndSpecification, [both Blue and Large object]
    print('Blue and Large products:')
    blue = ColorSpecification(Color.BLUE)
    and_spec = AndSpecification(blue, large)

    for item in bf.filter(items, and_spec):
        print(f'\t{item.name} is blue and large.')

    # We can even do like this
    large_blue = large & blue
    for item in bf.filter(items, large_blue):
        print(f'\t{item.name} is blue and large.')
```
  
  <h3> 3 - LSP / Liskov Substitution Principle</h3>
  
  >Substitutability is a principle in object-oriented programming stating that, in a computer program, if S is a subtype of T, then objects of type T may be replaced with objects of type S without altering any of the desirable properties of the program
  
  <h5>Liskov Substitution Principle states that if you are inheriting from a base class, the base class cannot have anything that will break the functioning of the child class..</h5>

  - ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) `derived classes should be able to extend their base classes without changing their behavior.`
  
  <img width="701" alt="Screen Shot 2021-06-05 at 7 01 04 PM" src="https://user-images.githubusercontent.com/31994778/120897742-67f87c80-c630-11eb-92f5-c89d805e2996.png">
 
Credits to -> [Maysara Alhindi](https://stackoverflow.com/users/5503714/maysara-alhindi "Maysara Alhindi") on [Answer](https://stackoverflow.com/questions/56860/what-is-an-example-of-the-liskov-substitution-principle 'Answer')

  <h3> 4 - ISP / Interface Segragation Principle</h3>
  
  >Don't  put too many elements in an interface!
  
  <h5>Say that we have an interface for a machine that defines methods for what a modern-day printer does</h5>
  
```python
  class Machine:
    def print(self):
        raise NotImplementedError

    def fax(self):
        raise NotImplementedError

    def scan(self):
        raise NotImplementedError
```
  
And then, we want to create our ModernPrinter class and implement Machine interface.
  
```python
  class ModernPrinter(Machine):
    def print(self):
        # does something
        pass

    def fax(self):
        # does something
        pass

    def scan(self):
        # does something
        pass
```
However, if we have an old-fashioned printer, we won't be using ```fax``` and ```scan``` methods, which in turn may be problematic.

```python
  class OldPrinter(Machine):
    def print(self):
        # does something
        pass

    def fax(self):
        # no op
        pass

    def scan(self):
        # no op
        pass
```
  
  <h5>Here, we are not using these methods and one way is to pass the method and not do anything, another method is to raise some error</h5>
  
  * passing the method directly won't be very good since we will not be doing anything with that method and if we don't do anything with it why did we implement it in the first place?
  * raising error won't be a good practice since someone may use the method in their code and if the code contains many thousand lines of code it will be hard to debug the problem and find the exception raised.
  
  
In a situation like this, we should split our methods into different interfaces. In this way, an old printer can only implement ```print()``` method, and a modern printer can implement ```print()```, ```scan()```, and ```fax()``` methods. This is what <b>Interface Segregation</b> suggests.
  
```python
  class Printer:
    @abstractmethod
    def print(self):
        raise NotImplementedError


class Faxer:
    @abstractmethod
    def fax(self):
        raise NotImplementedError


class Scanner:
    @abstractmethod
    def scan(self):
        raise NotImplementedError
```
  
```python
  class ModernPrinter(Printer, Faxer, Scanner):
    def print(self):
        # does something
        pass

    def fax(self):
        # does something
        pass

    def scan(self):
        # does something
        pass
```
  
```python
  class OldPrinter(Printer):
    def print(self):
        # does something
        pass
```
  
```python
printer = ModernPrinter()
printer.fax()
printer.scan()
printer.print()

old_printer = OldPrinter()
old_printer.print()
```
  
<h3> 5 - DIP / Dependency Inversion Principle</h3>

>DIP states that high level classes or high level modules in your code should not directly depend on low level modules. Instead, they should depend on abstractions.
  
Imagine that we want to create a geneology application that finds out the children of a parent. We can come up with a code like this:
  ```python
  from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class Relationships:
    def __init__(self):
        self.relationship_list = []

    def add_parent_and_child(self, parent, relationship_type, child):
        self.relationship_list.append(
            (parent, relationship_type, child)
        )
  ```
  <h5>Here, we have an enum for relationship classification, a class called Person, and a class called Relationships that is used for adding a parent-child to a list </h5>
  
  Let's say that I want to implement a class called ```Research``` to reach to ```relationship_list``` and print out parents and children.
  
  ```python
  class Research:
    def __init__(self, relationships):
        self.relationships = relationships.relationship_list

        for r in self.relationships:
            if r[0].name == 'Ahmet' and r[1] == Relationship.PARENT:
                print(f'Ahmet has a child named {r[2].name}')
  ```
  
Good? <b>No</b>:confused:
  
<h5>Because</h5>
  
- ```Research class relies heavily on the relationshi_list list of Relationships class```
- ```If we change the list data structure to a dictionary one day, our Research class would crash, since it's using indexing r[0], r[2] as such...```
- ```Imagine we use a mongodb instead of a list here and we want to switch to a relational, like SQL, db. This means our Research class will crash again...```
  
<b>How to fix it?</b>
  
>We should use an interface for the low level module. The idea is that Research should not depend on the concrete implementation, it should depend on some sort of an abstraction that can subsequently change.
 
 So, let's define a class ```RelationshipBrowser``` with an abstractmethod ```find_all_children_of```
 
  ```python
  class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass
  ```
  <b>This method needs to be implemented in whoever inherits from ```RelationshipBrowser``` class.</b>
  
  Let's make ```Relationship``` class inherit from ```RelationshipBrowser```.
  
  ```python
  class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relationship_list = []

    def add_parent_and_child(self, parent, relationship_type, child):
        self.relationship_list.append(
            (parent, relationship_type, child)
        )

    def _find_all_children_of(self, name):
        for r in self.relationship_list:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name
```

>As you can see, we also implemented ```_find_all_children_of(self, name)``` method in our class in order to handle everything about relationships within this class. In this way, we eliminate the dependency of a high-level module (Research) from a low-level module (Relationships).
  
<b>Now we can get rid of everything inside the ```Research``` class and re-implement it as follows</b>

  ```python
  class Research(Relationships):
    def __init__(self, browser, name):
        for n in browser._find_all_children_of(name):
            print(f'{name} has a child named {n}')
```

This has the following advantages:
 - if, in the future, we have to use another data structure, e.g., dict, we don't have to change ```Research``` class at all. 
 - The only change would be is to create a new class, i.e., ```RelationshipsDict``` and implement ```def find_all_children_of(self, name):``` method accordingly.
 - This is very convenient since we won't have to tinker with high-level modules and, if needed, only extend on the low-level ones. (such as creating new classes and having ```Research``` inherit from classes that implement them.)

  
<h2>Summary
  
  <img width="1136" alt="Screen Shot 2021-06-06 at 3 36 24 PM" src="https://user-images.githubusercontent.com/31994778/120924574-122dde00-c6dd-11eb-8331-be21a406538c.png">
