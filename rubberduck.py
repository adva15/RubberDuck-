from typing import override

'''''''''
+---------------------------------------------------------------+
|                        RubberDuck                             |
+---------------------------------------------------------------+
| - __color: str = "yellow"               @class-variable       |
| - __quack_volume: int                                         |
+---------------------------------------------------------------+
| + __init__(quack_volume=5)                                    |
| + squeak(): None                         [@static-method]     |
| + get_color(): str                       [@class-method]      |
| + boost_volume(): None                   [@instance-method]   |
| + quack_volume: int                      [@property]          |
| + quack_volume(value: int): None         [@setter]            |
| + __str__(): str                         [@instance-method]   |
+---------------------------------------------------------------+
'''''''''

class RubberDuck:
    __color: str = "yellow"

    def __init__(self, quack_volume=5):
        self.quack_volume: int = quack_volume

    @staticmethod
    def squeak():
        print("duck is squeaking...")

    @classmethod
    def get_color(cls) -> str:
        return cls.__color

    @property
    def quack_volume(self) -> int:
        return self.__quack_volume

    @quack_volume.setter
    def quack_volume(self, value):
        if value < 0:
            self.__quack_volume = 0
        else:
            self.__quack_volume = value

    def boost_volume(self):
        self.quack_volume *= 2

    @override
    def __str__(self) -> str:
        return f"RubberDuck quack_volume={self.quack_volume} color={RubberDuck.get_color()}"


duck = RubberDuck()
print(duck)   # __str__ output

RubberDuck.squeak()

duck.quack_volume = 10
print("🔊 New volume:", duck.quack_volume)

duck.boost_volume()
print("🚀 Boosted volume:", duck.quack_volume)

print("🎨 Default color:", RubberDuck.get_color())
