from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print('This tea is delicious')


class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious')


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil water,'
              f'put {amount}ml of water, enjoy')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind beans, boil water',
              f'put {amount}ml of water, fresh coffee!')
        return Coffee()


class HotDrinkMachine:
    class AvailableDrinks(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrinks:
                name = d.name[0] + d.name[1:].lower()
                factory_instance = eval(name + 'Factory')()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        for pos, d in enumerate(self.factories):
            print(str(pos)+'.'+d[0])

        s = input(f'Please select a drink (0-{len(self.factories)-1}): ')
        idx = int(s)
        s = input(f'Please select the amount in ml: ')
        amount = int(s)

        return self.factories[idx][1].prepare(amount)


if __name__ == '__main__':
    hdm = HotDrinkMachine()
    hdm.make_drink()
