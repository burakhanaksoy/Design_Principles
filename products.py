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


class FilterProduct:
    def filter_by_color(self, products, color):
        for product in products:
            if product.color == color:
                yield product

    def filter_by_size(self, products, size):
        for product in products:
            if product.size == size:
                yield product


class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    # Combinator
    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':

    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.MEDIUM)
    house = Product('House', Color.BLUE, Size.LARGE)

    items = (apple, tree, house)

    # Old(bad) way of filtering
    print('(old)Green products:')
    fp = FilterProduct()
    for item in fp.filter_by_color(items, Color.GREEN):
        print(f'\t{item.name} is green.')

    # Better approach
    print('(new)Green products:')
    bf = BetterFilter()
    green = ColorSpecification(Color.GREEN)

    for item in bf.filter(items, green):
        print(f'\t{item.name} is green.')

    print('Large products:')

    large = SizeSpecification(Size.LARGE)
    for item in bf.filter(items, large):
        print(f'\t{item.name} is large.')

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
