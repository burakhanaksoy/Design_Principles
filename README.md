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
  <h3> SRP / SOC<br><br>
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
  
