from enum import Enum, verify, CONTINUOUS, Flag, CONFORM, auto

color = Enum('color', ['red', 'blue', 'green'])
print(color.__len__())


@verify(CONTINUOUS)
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class ConformFlag(Flag, boundary=CONFORM):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

