class Dog:
    def sound(self):
        return "Dog Barks"

class Cat:
    def sound(self):
        return "Cat Meow"


for i in [Dog(), Cat()]:
    print(i.sound())

