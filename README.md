# Curriedef

Currying facade for Python.

This package provides the `curried` class and the `curry` decorator to create curried functions.

## Installation

```console
pip install curriedef
```

## Examples

```py
from curriedef import curried

def add(a, b):
    return a + b

add_two = curried(add)(2)

print(add_two(1)) # prints "3"
print(add_two(2)) # prints "4"
print(add_two(10)) # prints "12"
```

That's great but having to type `curried` every single time you want to curry a function is a pain, isn't it?.
Because of that there is a `curry` decorator.

```py
from curriedef import curry

@curry
def add(a, b):
    return a + b

add_two = add(2)

print(add_two(1)) # prints "3"
print(add_two(2)) # prints "4"
print(add_two(10)) # prints "12"
```

