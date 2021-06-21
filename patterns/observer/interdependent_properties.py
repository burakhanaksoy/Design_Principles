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

        old_can_vote = self.can_vote

        self._age = value
        self.property_changed('age', value)

        if old_can_vote != self.can_vote:
            self.property_changed('can_vote', self.can_vote)

    @property
    def can_vote(self):
        return self.age >= 18


class TrafficAuthority:
    """ Unit class for TrafficAuthority """

    def __init__(self, person):
        self.person = person
        self.person.property_changed.append(self.person_changed)

    def person_changed(self, name, value):
        if name == 'can_vote':
            print(f'Voting ability changed to {self.person.can_vote}')
        if name == 'age':
            if self.person.age < 16:
                print('You can\'t drive')
            else:
                print('You can drive')


def main():
    person = Person()
    trf = TrafficAuthority(person)

    for age in range(15,20):
        person.age = age


if __name__ == '__main__':
    main()
