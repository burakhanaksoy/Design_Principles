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
