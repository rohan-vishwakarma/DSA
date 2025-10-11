class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
# 1 --> 2 --> 3 -- > 4 --> tail points to head
class CircularLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.head.next = newNode
        else:

            pass
    # def __str__(self):
    #     res = ''
    #     temp_node = self.head
    #     while temp_node:

obj = CircularLinkedList()
obj.append(10)
obj.append(20)
print(obj.head.next.data)


            
