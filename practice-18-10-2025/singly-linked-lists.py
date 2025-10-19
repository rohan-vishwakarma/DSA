from unittest.mock import sentinel


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node
        self._length += 1

    def delete(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None  # List now empty
            self._length -= 1
            return

        prev_node = self.head
        node = self.head.next
        while node is not None:
            if node.data == value:
                prev_node.next = node.next
                if node == self.tail:
                    self.tail = prev_node
                self._length -= 1
                return
            prev_node = node
            node = node.next

    def sort(self):
        if self.head is None or self.head.next is None:
            return  # Already sorted or empty

        for i in range(1, self._length):
            pointer = self.head
            for j in range(self._length - i):
                if pointer.data > pointer.next.data:
                    # Swap data
                    pointer.data, pointer.next.data = pointer.next.data, pointer.data
                pointer = pointer.next

    def __str__(self):
        node = self.head
        lists = ""
        while node is not None:
            lists += str(node.data)
            if node.next is  not None:
                lists += ' => '
            node = node.next
        return lists

ll = LinkedList()
ll.append(200)
ll.append(19)
ll.append(15)
ll.append(17)
ll.append(9)
ll.append(19)

ll.delete(14)



print(f"LinkedList : {ll}")
print(f"head : {ll.head.data}")
print(f"tail : {ll.tail.data}")
print(f"total length : {ll._length}")




