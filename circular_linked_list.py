class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class CircularLinkedList:

	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def append(self, value):

		new_node  = Node(value)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
			new_node.next = new_node
			self.length +=1
		else:
			if self.length == 1:
				self.head.next = new_node
				new_node.next = self.head
				self.tail = new_node
			else:
				temp = self.tail
				temp.next = new_node
				self.tail = new_node
				new_node.next = self.head

			self.length +=1

	def add(self, index, value):

		if index > self.length-1:
			raise Exception(f"Index out of the range. linked list length is {self.length} ")
		new_node = Node(value)
		temp = self.head
		for _ in range(index - 1):
			temp = temp.next
		inplace = temp.next
		temp.next = new_node
		new_node.next = inplace
		self.length +=1


	def __str__(self):
		temp = self.head
		res = ''
		while temp:
			res += str(temp.data)
			temp = temp.next
			if temp == self.head:
				break
			res += '-->'
		return res

Obj = CircularLinkedList()
Obj.append(12)
Obj.append(14)
Obj.append(15)
Obj.add(2, 13)
print(Obj)

