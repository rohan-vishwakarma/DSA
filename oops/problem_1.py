import math


class Circle:

    def __init__(self, radius):
        self.radius = radius


    def circumference(self):
        return 2*math.pi*int(self.radius)**2
    
    def area(self):
        return math.pi*int(self.radius)**2


def Enter(rad):
    print("Please Enter a Correct Values")
    rad = input("ENTER THE RADIUS :")

    if not rad.isnumeric():
        return Enter(rad)
    obj = Circle(rad)
    print(obj.area())
    print(obj.circumference())



rad = input("ENTER THE RADIUS :")
if rad.isnumeric():
    obj = Circle(rad)
    print(obj.area())
    print(obj.circumference())
else:
    Enter(rad)
    

