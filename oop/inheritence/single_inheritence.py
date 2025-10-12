class Engine:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

class Car(Engine):

    def __init__(self, car_name, engine_name):
        self.__car_name = car_name
        super().__init__(engine_name)

    def getCarName(self):
        return self.__car_name


car = Car("maruti suzuki", "420 horse power")
carname = car.getCarName()
engine  = car.getName()

print(f"car name is {carname} and engine name is {engine}")
