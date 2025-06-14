# Given a list of integers and a target integer, return the indices of the two numbers in the
# list that add up to the target. Assume there is exactly one solution.


list = [12,344,5,1,2,3,4,5,6,8,2]

def two_sum(list, target_sum):
    try:
        if len(list) == 0:
            return ValueError("List Cannot Be Empty")
        for i in range(len(list) -1):
            for j in range(i + 1, len(list)-1- 1):
                if list[i] + list[j] == target_sum:
                    result = (list[i],list[j])
                    print(result)

    except Exception as e:
        print(e)
        return e


class Queue:
    def __init__(self, size):
        self.size   = size
        self.length = 0
        self.queue  = []
        self.error  = ""

    def enqueue(self, data):
        if self.length > self.size-1:
            self.error = "Cannot Enqueue Data, As The Queue Not Have Enough Space"
            return self.error
        self.queue.append(data)
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return "Unable to remove element from empty queue"
        element = self.queue[0]
        del self.queue[0]
        return element

    def __str__(self):
        if self.error != "":
            return self.error
        return str(self.queue)

queue = Queue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

queue.dequeue()
queue.dequeue()
queue.dequeue()

