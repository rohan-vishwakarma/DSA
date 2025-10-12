class Engine:
    def __init__(self, name):
        self.__engine_name = name

    def getEngineName(self):
        return self.__engine_name

class Mechanism:
    def __init__(self, mtype):
        self.__type = mtype

    def getMechanismName(self):
        return self.__type


class Car(Engine, Mechanism):
    
    def __init__(self, engine, mechanism):
        Engine.__init__(self, engine)
        Mechanism.__init__(self, mechanism)

    def __str__(self):
        return f"Car Details:\nEngine: {self.getEngineName()}\nMechanism: {self.getMechanismName()}"


n = Car("250 Horse Power", "simple mechanism")

print(n)