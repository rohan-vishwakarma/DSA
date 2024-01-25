from abc import ABC


class Environment(ABC):
    
    def process(self):
        print("this is a process")


obj = Environment()
print(obj.process())
