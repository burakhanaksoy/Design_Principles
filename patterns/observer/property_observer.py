class Event(list):
    """ Unit class for Observer Design Pattern """

    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class PropertyObservable:
    """ Unit class for PropertyObservable """

    def __init__(self):
        self.property_changed = Event()


class Person(PropertyObservable):
    """ Unit class for Person """

    def __init__(self, age=0):
        super().__init__()
        self._age = age

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


def main():
    person = Person()
    trf = TrafficAuthority(person)

    person.age = 15
    person.age = 16


if __name__ == '__main__':
    main()
