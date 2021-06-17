<h3>Strategy</h3>

>"Enables the exact behavior of system to be selected at run-time.The strategy pattern allows grouping related algorithms under an abstraction, which allows switching out one algorithm or policy for another without modifying the client. Instead of directly implementing a single algorithm, the code receives runtime instructions specifying which of the group of algorithms to run."

Strategy pattern is about having a blueprint, e.g., `ListStrategy`, and extending different strategies, e.g., `MarkDownListStrategy` and `HtmlListStrategy`, and subsequently use these strategies in our code.

Here's an example:
```python
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
```

Here, we can change our strategy at runtime dynamically. The important thing is that bot strategies come from a shared base class, i.e., `ListStrategy`, so that they implement same functions differently, which doesn't constitute a problem when we make a change in runtime.

```python
if __name__ == '__main__':
    tp = TextProcessor()
    items = ['foo', 'bar', 'baz']
    tp.append_list(items)
    tp.display()

    tp.clear()

    tp.set_output_format(OutputFormat.MARKDOWN)
    tp.append_list(items)
    tp.display()
```

Here, with `tp.set_output_format()` method, we can change the strategy of choice in runtime.🥳

This outputs

```
<ul>
  <li>foo</li>
  <li>bar</li>
  <li>baz</li>
</ul>

 * foo
 * bar
 * baz
```
