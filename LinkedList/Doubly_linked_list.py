class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            new_node.next = None
        else:
            if self.length == 1:
                self.head.next = new_node
                self.tail = new_node
                new_node.prev = self.head
                new_node.next = None
            else:
                temp = self.tail
                self.tail.next = new_node
                new_node.next = None
                new_node.prev = temp
                self.tail = new_node

        self.length += 1

    def __str__(self):
        temp = self.head
        res =''
        while temp is not None:
            if temp.data == self.head.data:
                res += 'None <- '
                res +=str(temp.data)
                res += '- > '
                temp = temp.next
            else:
                res += '<- '
                res += str(temp.data)
                temp = temp.next
                if temp is not None:
                    res +='->'
                else:
                    res +=' -> None'
        return res

obj = DoublyLinkedList()
obj.append(12)
obj.append(13)
obj.append(14)
print(obj)