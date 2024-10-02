#                   +------+         +------+         +------+
#                   |  A   | ------> |  B   | ------> |  C   |
#                   +------+         +------+         +------+
#                      ^                                   |
#                      |___________________________________|
#
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = None
            newNode.prev = None
        else:
            self.tail.next = newNode
            newNode.next = self.head
            newNode.prev = self.tail
            self.tail = newNode

        self.length += 1

    def __str__(self):
        res = ""
        temp = self.head
        brk = False
        for _ in range(self.length):
            res += str(temp.data)
            if temp.next is not self.head:
                res += '->'
            temp = temp.next
        return  res

Cll = CircularLinkedList()
Cll.add(12)
Cll.add(14)
Cll.add(15)
Cll.add(17)
