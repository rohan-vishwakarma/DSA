class StackEmptyException(Exception):
    pass

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.top = 0
        self.before_top = None

class StackLinkedList:

    def __init__(self):
        self.peak = None
        self.bottom = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        if self.bottom is None:
            self.bottom = new_node
            self.peak = new_node
        else:
            self.peak.next = new_node
            self.peak.top = 0
            new_node.before_top = self.peak
            self.peak = new_node
            self.peak.top = 1
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise StackEmptyException("Stack is empty, cannot perform pop operation")
        temp = self.peak.before_top
        self.peak = temp
        if hasattr(self.peak, "top"):
            self.peak.top = 1
        self.length -= 1


    def __str__(self):
        if self.length == 0:
            return "Stack is empty"

        pointer = self.bottom
        stack = ""
        while True:
            stack +=  str(pointer.data)
            if pointer.top == 1:
                break
            stack += " -> "
            pointer = pointer.next
        return  stack

sll = StackLinkedList()
sll.push(12)
sll.push(13)
sll.push(14)
