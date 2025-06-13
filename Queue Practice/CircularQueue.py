from asyncio import QueueFull
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self, max_length):
        self.front = None
        self.rear = None
        self.maxlength = max_length
        self.length = 0

    def enqueue(self, data):
        if self.length == self.maxlength:
            return "Queue Practice is full"
    