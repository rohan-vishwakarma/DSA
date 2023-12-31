class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enque(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None

        self.length +=1

    def peek(self):
        if self.head is not None:
            return self.head.value
        else:
            return "QUEUE IS EMPTY"

    def deque(self):
        name = self.head.value
        temp = self.head
        nextele = temp.next
        self.head = nextele
        temp = None


        return f"{name} is popped"
        

    def __str__(self):
        temp = self.head
        res =''
        while temp is not None:
            res += str(temp.value)
            temp = temp.next
            if temp is not None:
                res += '--'
        return res
    
obj = Queue()
obj.enque(12)
obj.enque(13)
obj.enque(14)
print(obj)
print(deque.pop())
obj.enque(15)
print(obj)        

        
        


            





