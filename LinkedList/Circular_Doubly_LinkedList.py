class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            if self.length == 1:
                temp = self.head
                self.tail = new_node
                self.tail.next = temp
                
        self.length += 1

    def __str__(self):
        temp = self.head
        res = ''
        while temp:
            res += str(temp.value)
            if temp.value == self.tail.value:
                break
            else:
                temp = temp.next
        return res
    
obj = DoublyCircularLinkedList()
obj.append(12)
obj.append(13)
obj.append(14)

print(obj)

