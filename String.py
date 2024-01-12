class String:
    def __init__(self, value):
        self.value = value
        self.length = 0

    def size(self):
        length = 0
        for i in self.value:
            length += 1
        self.length = length
        return length
    
    def reverse(self):

        string = ""
        a =-1
        for i in range(len(self.value)):
            string += str(self.value[a])
            a -=1
        return string
    
    def replace_single(self, letter, replace_with):
        string = ''
        if letter not in self.value:
            return "Element not found"
        for i in range(len(self.value)):           
            if self.value[i] == letter:
                string += str(replace_with)
            else:
                string += str(self.value[i])
        return string
    


    def __str__(self):

        temp = 0
        for i in self.value:
            temp +=1
        self.length = temp

        dict = {
            f' The String is {self.value}':{
                'length' : temp
            }
        }
        return str(dict)
obj = String("Rohan")
print(obj.reverse())
print(obj.replace_single("n", "P"))