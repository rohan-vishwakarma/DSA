class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
            newNode.prev = newNode.next = None
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            newNode.next = self.head
            self.tail = newNode
            self.head.prev = newNode
        self.length += 1

    def __str__(self):
        res = ""
        temp = self.head
        while temp is not None:
            res +=str(temp.data)
            if temp.next is not self.head:
                res += ' ⟷ '
                temp = temp.next
            else:
                temp = None
        return res

    def addatposition(self, index, data):
        if index > self.length -1:
            raise IndexError(f"Index {index} out of range")
        pointer = self.head
        newNode = Node(data)
        for i in range(self.length):
            if i == index:
                tPrev = pointer.prev
                tNext = pointer.next
                newNode.prev = tPrev
                tPrev.next = newNode
                newNode.next = pointer
                if pointer is self.head:
                    self.head = newNode
                return True
            pointer = pointer.next
        return

if __name__ == '__main__':
    cdll = CircularDoublyLinkedList()
    cdll.add(12)
    cdll.add(13)
    cdll.add(14)
    cdll.add(15)
    cdll.add(16)
    print("Before => ",cdll)
    print(cdll.addatposition(2,100))
    print("After  => ", cdll)
    print(cdll.head.data)