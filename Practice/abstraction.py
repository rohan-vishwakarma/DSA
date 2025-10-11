from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def drive(self):
        pass

    def stop(self):
        pass

class Honda(Car):
    def drive(self):
        pass
