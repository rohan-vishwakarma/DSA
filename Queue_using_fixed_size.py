class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:

    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.length = 0
        self.capacity = capacity

    def enque(self, value):

        if self.length == self.capacity:
            return "Queue is full, cannot enque the elements"
        else:
        
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
        if self.head is not None:
            name = self.head.value
            temp = self.head
            nextele = temp.next
            self.head = nextele
            temp = None
            self.length -=1
            return f"{name} is popped"
        else:
            return "No elements to deque, the queue is already empty"


    def __str__(self):
        temp = self.head
        res =''
        while temp is not None:
            res += str(temp.value)
            temp = temp.next
            if temp is not None:
                res += '--'
        
        if res == '':
            res+=str("The Queue is empty")
        return res
    
obj = Queue(1)
obj.enque(12)
print(obj)

    

        
        


            





