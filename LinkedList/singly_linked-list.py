class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

# 1 --> 2 -- > 3 -->4
class LinkedList:

	def __init__(self):
		self.head = None
		self.next = None
		self.length = 0

	def addElement(self, value):
		newNode = Node(value)
		if self.head is None:
			self.head = newNode
			self.tail = newNode
			self.head.next = None
		else:
			self.tail.next = newNode
			newNode.next = None
			self.tail = newNode
		self.length +=1


	def prepend(self, value):
		new_node = Node(value)
		if self.head is not None:
			temp_node = self.head
			self.head = new_node
			new_node.next = temp_node
		self.length +=1

	def addAtPosition(self, index, value ):

		if index == 0:
			self.prepend(value)
		else:

			new_node = Node(value)
			temp_node = self.head
			for _ in range(index -1):
				temp_node = temp_node.next
			t = temp_node.next
			temp_node.next = new_node
			new_node.next = t
		self.length +=1

	def __str__(self):
		temp_node = self.head
		res = ''
		while temp_node is not None:
			res += str(temp_node.data)
			temp_node =temp_node.next
			if temp_node is not None:
				res += '-->'
		return res

	def __len__(self):
		return self.length

ll = LinkedList()
ll.addElement(12)
ll.addElement(13)
ll.addElement(14)
ll.addElement(15)
ll.addAtPosition(3, 100)
print(ll)

print(len(ll))
