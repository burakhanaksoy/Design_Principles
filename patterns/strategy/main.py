from abc import ABC
from enum import Enum, auto


class ListStrategy(ABC):
    def start(self, buffer): pass
    def end(self, buffer): pass
    def add_list_item(self, buffer, item): pass


class MarkDownListStrategy(ListStrategy):
    def add_list_item(self, buffer, item):
        buffer.append(f' * {item}\n')


class HtmlListStrategy(ListStrategy):
    def start(self, buffer): buffer.append('<ul>\n')
    def end(self, buffer): buffer.append('</ul>\n')

    def add_list_item(self, buffer, item): buffer.append(
        f'  <li>{item}</li>\n')


class OutputFormat(Enum):
    HTML = auto()
    MARKDOWN = auto()


class TextProcessor:

    def __init__(self, list_strategy=HtmlListStrategy()):
        self.list_strategy = list_strategy
        self.buffer = []

    def append_list(self, items):
        ls = self.list_strategy
        ls.start(self.buffer)
        for item in items:
            ls.add_list_item(self.buffer, item)
        ls.end(self.buffer)

    def set_output_format(self, output_format):
        if output_format == OutputFormat.HTML:
            self.list_strategy = HtmlListStrategy()
        elif output_format == OutputFormat.MARKDOWN:
            self.list_strategy = MarkDownListStrategy()

    def display(self):
        print(''.join(self.buffer))

    def clear(self):
        self.buffer.clear()


if __name__ == '__main__':
    tp = TextProcessor()
    items = ['foo', 'bar', 'baz']
    tp.append_list(items)
    tp.display()

    tp.clear()

    tp.set_output_format(OutputFormat.MARKDOWN)
    tp.append_list(items)
    tp.display()
