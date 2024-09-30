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

    def addelememts(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            self.tail.next = None
            self.head.prev = None
        else:
            self.tail.next = newNode
            newNode.next = None
            newNode.prev = self.tail
            self.tail = newNode
            self.tail.next = None

    def __str__(self):
        res = ''
        temp = self.head
        while temp is not None:
            res += str(temp.data)
            if temp.next is not None:
                res += '<-->'
            temp = temp.next
        return res

dll = DoublyLinkedList()
dll.addelememts(12)
dll.addelememts(13)
dll.addelememts(10)





