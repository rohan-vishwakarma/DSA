from enum import Enum


class Color(Enum):
    Red = 1
    Blue = 2
    Green = 3
    Yellow = 4


for elements in Color:
    print(elements.name, " = > ", elements.value)


