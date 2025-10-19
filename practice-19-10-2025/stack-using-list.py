from typing import Union

class StackFullError(Exception):
    """Raised when trying to push to a full stack."""
    pass

class StackEmptyError(Exception):
    """Raised when trying to pop or peek from an empty stack."""
    pass

class Stack:
    def __init__(self, max_length=None):
        self._max_length = max_length
        self.length = 0
        self.data = []

    def push(self, value: int):
        if value is None:
            raise ValueError("Value cannot be null")
        if self._max_length is not None and self.length == self._max_length:
            raise StackFullError("Stack is full, element cannot be added")
        self.data.append(value)
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            raise StackEmptyError("Stack is empty, cannot pop element")
        popped = self.data.pop()
        self.length -= 1
        return popped

    def peek(self):
        if self.length == 0:
            raise StackEmptyError("Stack is empty, cannot peek element")
        return self.data[-1]

    def __str__(self):
        return str(self.data)

# Example usage with exception handling
try:
    stack = Stack(3)
    stack.push(12)
    stack.push(13)
    stack.push(14)
    stack.push(15)  # Raises StackFullError

except StackFullError as e:
    print(f"Error: {e}")

print("Stack:", stack)
print("Peek element:", stack.peek())

