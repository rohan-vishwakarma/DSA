

class Sorting:

    def __init__(self):
        self.array = array

    def SelectionSort(self, array):
        for i in range(0,len(self.array)):

            for j in range(0, len(self.array)):
                if self.array[i] < self.array[j]:
                    temp = self.array[i]
                    self.array[i] = self.array[j]
                    self.array[j] = temp
        return self.array
    
    def Bubblesort(self, array):
        for i in range(0, len(self.array)):
            for j in range(0 ,len(self.array)-1):
                if self.array[j] > self.array[j + 1]:
                    temp = self.array[j+1]
                    self.array[j+1] = self.array[j]
                    self.array[j] = temp
        return self.array
        
    
    def reverse(self, array):
        li = []
        i = -1
        iter = True
        while i < 0:
            li.append(self.array[i])
            if i == -len(self.array):
                break
            i -=1
        return li
    
       

array = [12, 34, 56, 89,2000, 0, 11, 11]
object = Sorting()
print(object.removeDuplicates(array))



