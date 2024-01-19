import numpy as np
class Person:


    def __init__(self):
        self.name = np.array('i', [])

    def add(self, list):
        pass
             

    def __str__(self):
        temp =""
        for i in range(len(self.name)):
            temp +=self.name[i]
        return str(temp)
            
    
p = Person()
print(p)



    