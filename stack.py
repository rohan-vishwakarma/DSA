class Stack:

	def __init__(self, stackSize):
		self.stackSize = stackSize
		self.length = 0
		self.stack = []

	def isFull(self):
		if len(self.stack) == self.stackSize:
			return True
		else:
			return False

	def push(self, value):

		if self.stackSize == self.length:
			return "STACK IS FULL"
		else:
			stack_list = self.stack
			stack_list.append(value)
			self.length +=1

	def peek(self):
		lastEle = self.stack[-1]
		return lastEle
	

	def __str__(self):
		list = self.stack.reverse()

		if len(self.stack) == 0:
			result = "The Stack Is Empty"
			return result
		else:
			result = [ str(x) for x in self.stack]
			return '\n'.join(result)
		
		

obj = Stack(10)
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
print(obj)