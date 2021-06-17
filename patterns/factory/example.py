class Person:
    _id = -1

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'id:{self.id} name:{self.name}'

    @classmethod
    def create_person(cls, name):
        cls._id += 1
        return Person(cls._id, name)

# class PersonFactory:
#     _id = -1

#     @classmethod
#     def create_person(cls, name):
#         cls._id += 1
#         return Person(cls._id, name)


if __name__ == '__main__':
    burak = Person.create_person('burak')
    ahmet = Person.create_person('ahmet')

    print(burak, ahmet)
