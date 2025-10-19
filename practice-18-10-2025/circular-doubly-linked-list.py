class Node:
    def __init__(self, data):
        self.value = data
        self.is_tail = None
        self.is_head = None
        self.prev  = None
        self.next  = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.prev = new_node
            new_node.next = new_node
            self.head = new_node
            self.head.is_head = 1
            self.tail = new_node
        else:
            old_tail = self.tail
            old_tail.is_tail = None
            self.tail.next = new_node
            new_node.prev = old_tail
            self.tail = new_node
            self.tail.is_tail = 1
        self.length += 1

    def update(self, value, new_value):
        node = self.head
        while node:
            if node.is_head == 1:
                if node.value == value:
                    self.head.value = new_value
                    return True
            else:
                if node.value == value:
                    node.value = new_value
                    return True

            node = node.next
            if node.is_tail == 1:
                if node.value == value:
                    node.value = new_value
                    return True
                break
        return False

    def delete(self, value):
        node = self.head
        while node:
            if node.is_head == 1:
                if node.value == value:
                    next = self.head.next
                    self.head = next
                    self.head.prev = self.tail
                    self.length -=1
                    return True
            else:
                if node.value == value:
                    node.prev.next = node.next
                    node.next.prev = node.prev.next
                    self.length -= 1
                    return True

            node = node.next
        return False

    def __str__(self):
        node = self.head
        dll = ""
        while node:
            dll += str(node.value)
            dll += " <=> "
            node = node.next
            if node.is_tail == 1:
                dll += str(node.value)
                break
        return dll

dll = DoublyLinkedList()
dll.append(12)
dll.append(13)
dll.append(15)
dll.append(17)
dll.append(18)
delete = dll.delete(15)
update = dll.update(18, 20)
print(f"Doubly LinkedList is : {dll}")
print(f"Length : {dll.length}")
print(f"Head is : {dll.head.value}")
print(f"Tail is : {dll.tail.value}")
print(f"Delete Status : {delete}")