class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_a_cold(self):
        self.falls_ill(self.name, self.address)


def call_doctor(name, address):
    print(f'{name} needs doctor at {address}')


if __name__ == "__main__":
    person = Person('Burak', '221 B Baker Street')
    person.falls_ill.append(call_doctor)
    person.catch_a_cold()
