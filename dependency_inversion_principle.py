from enum import Enum
from abc import abstractmethod


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass


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


class Research(Relationships):
    def __init__(self, browser, name):
        for n in browser._find_all_children_of(name):
            print(f'{name} has a child named {n}')


ahmet = Person('Ahmet')
berke = Person('Berke')
nazli = Person('Nazli')

relationships = Relationships()
relationships.add_parent_and_child(ahmet, Relationship.PARENT, berke)
relationships.add_parent_and_child(ahmet, Relationship.PARENT, nazli)

research = Research(relationships, 'Ahmet')
