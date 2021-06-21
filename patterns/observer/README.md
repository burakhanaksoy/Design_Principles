<h1>Observer</h1>

<p align="center">
  <img width="250" height="150" src="https://miro.medium.com/max/462/1*lA4IDccstYKHvd3aC3YjKA.png">
</p>

>An Observer is an object that wishes to be notified when a change occurs in the system. The entity generating the change(event) is called observable or subject.

<h2>Motivation</h2>

- <b>We need to be informed when certain things happen</b>

  - Object's property changes
  
  - Object does something
  
  - Some external event occurs
  
- <b>We want to listen to events and be notified when they occur</b>
  - Notifications should include useful data
  
- <b>Unsubscribe from events when we are no longer interested</b>

<h2>Implementation</h2>

Firstly, we start off by creating an `Event` class. 

```python
class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)
```

This snippet is very general and can be used for almost all cases.

Then,
```python
class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_a_cold(self):
        self.falls_ill(self.name, self.address)


def call_doctor(name, address):
    print(f'{name} needs doctor at {address}')
```

Here, we have an `Event` instance, `falls_ill`, which will be triggered when `catch_a_cold` method is called.

Let's take a closer look at the following function
```python
def call_doctor(name, address):
    print(f'{name} needs doctor at {address}')
```

This function is the <b>Observer</b>. We are going to make it so that whenever `catch_a_cold` method is called, this function will be called(notified) as well.

Let's write the `main()` function.

```python
def main():
    person = Person('Burak', '221 B Baker Street')
    person.falls_ill.append(call_doctor)
    person.catch_a_cold()
```

When we run this under `if __name__ == "__main__": main()`, we will get the following output.
```
Burak needs doctor at 221 B Baker Street
```

Here, the important points are:

- `call_doctor` function is called everytime we call `catch_a_cold()` method on a person object.
- This is achieved by appending `call_doctor` function to `falls_ill` instance through `person.falls_ill.append(call_doctor)`
- This, in other words, can be translated as " `call_doctor` function is subscribed to `falls_ill` event.
- We can have as many functions as we want that is subscribed to `falls_ill` event. 
- Here, `falls_ill` is called `Observable` and `call_doctor` is called `Observer`.
- We can also remove `call_doctor`'s subscription to `falls_ill` by `falls_ill.remove(call_doctor)`.

To emphasize once again, we can add as many observers to `falls_ill` as we can.

```python
def main():
    person = Person('Burak', '221 B Baker Street')
    person.falls_ill.append(lambda name, address: print(f'{name} falls ill.'))
    person.falls_ill.append(call_doctor)
    person.catch_a_cold()
```

Here, we added `person.falls_ill.append(lambda name, address: print(f'{name} falls ill.'))` function as an observer to `falls_ill`.

When we run `main()`, we get 
```
Burak falls ill.
Burak needs doctor at 221 B Baker Street
```
<h2>Property Observer</h2>

Since Python has `@property` that we can use as decorators, and also since we just set up the <b>"Observer Design Pattern"</b>, we can merge these two ideas together and set up the so called `Property Observers`.

>Basically, a <b>Property Observer</b> tells us whenever a certain property is changed.

<h3>Implementation Steps</h3>

1- First, we stick to our observer design pattern implementation.

```python
class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)
```

2- Second, we create `PropertyObservable` class

```python
class PropertyObservable:
    def __init__(self):
        self.property_changed = Event()
```

This class only have `property_changed` attribute, which is an `Event` instance.
The idea is to inherit from this class and use `property_changed` instance that it offers.

3- Third, set up the class whose property you want to observe.

```python
class Person(PropertyObservable):
    """ Unit class for Person """

    def __init__(self, age=0):
        super().__init__()
        self._age = age
```

Note that we have `_age` property since we want it to be a private attribute.

4- Now, let's write down getter and setter for `_age` attribute.

```python
@property
    def age(self):
        """ Getter for _age """
        return self._age

    @age.setter
    def age(self, value):
        """ Setter for _age """
        if self._age == value:
            return
        self._age = value
        self.property_changed('age', value)
```

Here, `Age setter` checks if the new age is the same as the old one. If not, do nothing, if is, set the new age and call `self.property_changed('age', value)`

5- Create `TrafficAuthority` class

```python
class TrafficAuthority:
    """ Unit class for TrafficAuthority """

    def __init__(self, person):
        self.person = person
        self.person.property_changed.append(self.person_changed)

    def person_changed(self, name, value):
        if name == 'age':
            if self.person.age < 16:
                print('Sorry, you cannot drive.')
            else:
                print('You can drive now.')
                self.person.property_changed.remove(self.person_changed)
```

6- Test!

```python
def main():
    person = Person()
    trf = TrafficAuthority(person)

    person.age = 15
    person.age = 17


if __name__ == '__main__':
    main()
```

This outputs 

```
Sorry, you cannot drive.
You can drive now.
```

<b>As you can see, `person_changed` method unsubscribed from `property_changed` event as soon as person's age hits 16.</b>


>This is very powerful since we let one class to notify another class as soon as some change in an attribute occurs. We did this with high cohesion and loose coupling. 

<h3>Caveat: Property Dependency</h3>

Trying to observe a change in a property that is dependent on another property can be problematic!
  
Assume that we have the following getter
  
```python
@property
def can_vote(self):
    return self.age >= 18
```
  
  Here, where do we call `self.property_changed()`? Since `can_vote` is actually dependent on `self.age`, it would be best to call `self.property_changed()` inside `self.age`.
  
  So, we can implement something like this
  
  ```python
  @age.setter
    def age(self, value):
        """ Setter for _age """
        if self._age == value:
            return

        old_can_vote = self.can_vote

        self._age = value
        self.property_changed('age', value)

        if old_can_vote != self.can_vote:
            self.property_changed('can_vote', self.can_vote)
```

Here, we are caching `can_vote` by `old_can_vote`.

Then, we can change `person_changed` method as

```python
def person_changed(self, name, value):
        if name == 'can_vote':
            print(f'Voting ability changed to {self.person.can_vote}')
        if name == 'age':
            if self.person.age < 16:
                print('You can\'t drive')
            else:
                print('You can drive')
```

So, when we run

```python
def main():
    person = Person()
    trf = TrafficAuthority(person)

    for age in range(15,20):
        person.age = age


if __name__ == '__main__':
    main()
```

we get

```
You can't drive
You can drive
You can drive
You can drive
Voting ability changed to True
You can drive
```
