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
        self.length += 1

    def __str__(self):
        res = ''
        temp = self.head
        while temp is not None:
            res += str(temp.data)
            if temp.next is not None:
                res += ' <--> '
            temp = temp.next
        return res

    def searchElements(self, value):
        if value is None:
            raise Exception("Value Cannot be Empty")
        if self.length == 0:
            return "DLL is Empty".capitalize()
        temp = self.head
        for _ in range(self.length):
            if temp.data == value:
                return True
            if temp.next is None:
                return False
            temp = temp.next

    def updateElementUsingValue(self, value, newValue):
        if newValue == '' or newValue is None:
            return "New value cannot be null or empty"
        temp = self.head
        for _ in range(self.length):
            if temp.data == value:
                temp.data = newValue
                return "The Value {old} is updated to {new}".format(old = value, new= newValue)
            if temp.next is None:
                return str("Unable to find the value")
            temp = temp.next

dll = DoublyLinkedList()
dll.addelememts(2)
dll.addelememts(5)
dll.addelememts(4)
print("Dll before :", dll)
print(dll.updateElementUsingValue(5, 3))
print("Dll After :",dll)




