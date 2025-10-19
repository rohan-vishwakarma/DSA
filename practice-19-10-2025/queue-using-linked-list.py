class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLinkedList:
    def __init__(self, max_length=None):
        self.rear = None
        self.front = None
        self._max_length = max_length
        self._length = 0

    def get_length(self):
        return self._length

    def enqueue(self, value):
        if self._length == self._max_length:
            return "queue reached its maxlength"
        new_node = Node(value)
        if self.rear is None:
            self.rear = self.front =  new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._length += 1

    def dequeue(self):
        if self.get_length() == 0:
            return "queue is empty, dequeue cannot be performed"
        if hasattr(self.front, "next"):
            self.front = self.front.next
        self._length -= 1
        return True


    def __str__(self):
        if self.get_length() == 0:
            return "Queue is empty"
        pointer = self.front
        queue = ""
        while True:
            queue += str(pointer.data)
            if pointer.next is None:
                break
            queue += " <- "
            pointer = pointer.next
        return queue



queue = QueueLinkedList()
queue.enqueue(12)
queue.enqueue(13)
queue.enqueue(14)
queue.enqueue(15)
queue.enqueue(16)
queue.dequeue()
queue.dequeue()


print(f"queue: {queue}")
print(f"length : {queue.get_length()}")

