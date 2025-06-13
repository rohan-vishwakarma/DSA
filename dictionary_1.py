from celery.bin.control import inspect

from Advance.decorators import hello


class Demo:
    def __init__(self, name):
        self.name = name
        print(f"Object Called of {self.__class__.__name__}")

    def hello(self):
        print("Function is",  hello.__call__)


    def __del__(self):
        print(f"Object {self.name} is destroyed.")

obj = Demo("Rohan")
obj.hello()

