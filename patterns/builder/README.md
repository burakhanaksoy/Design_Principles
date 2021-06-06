<h1>Builder</h1>

>When piecewise object construction is complicated, provide an API for doing it succinctly.

<b>Sometimes creation of objects are not as easy as just calling an initializer and passing a few arguments. 
  Sometimes we may have to have lots of arguments to pass on, however, it's not a great practice to define a single chunky initializer for creating objects like this. 
Instead, we can do initialization piecewise and use Builder pattern</b>

<h5>Motivation</h5>

- Some objects are simple and require a single initializer call
- However, other objects may require quite a ceremony to complete initialization
- For object like these, we opt for piecewise construction
- Builder provides an API for constructing an object step-by-step

```python

# # A very simple construction of an HTML element
# text = 'hello'
# parts = ['<h1>', text, '</h1>']
# print(''.join(parts))

words = ['hello', 'world']
parts = ['<ul>']
for w in words:
    parts.append(f'  <li>{w}</li>')

parts.append('</ul>')
print('\n'.join(parts))
```

<b>Here, the problem is we need to make this construction in a structured way so that it looks both pretty and error-free. (someone might forget to append </ul>, for example)</b>

We need to outsource the process of constructing different chunks of HTML.

```python
class HtmlElement:
    indent_size = 2

    def __init__(self, name='', text=''):
        self.text = text
        self.name = name
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)


class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(self.root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    def __str__(self):
        return str(self.__root)

builder = HtmlBuilder('ul')
builder.add_child('li','Hello')
builder.add_child('li','world')

print(builder)
```


