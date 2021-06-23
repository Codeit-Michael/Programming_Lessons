
class Node:
	def __init__(self,data=None):
		self.data = data
		self.nxt = None

class linked_list:
	def __init__(self):
		self.head = Node()


	def Append(self, data):
		newNode = Node(data)
		current = self.head
		while current.nxt != None:
			current = current.nxt
		current.nxt = newNode


	def Return(self):
		items = []
		currentNode = self.head

		while currentNode.nxt != None:
			currentNode = currentNode.nxt
			items.append(currentNode.data)
		print(items)

	def Length(self):
		current = self.head
		dataCount = 0

		while current.nxt != None:
			dataCount += 1
			current = current.nxt
		print(dataCount)
		return dataCount

	def Get(self, index):
		if index >= self.Length() or index < 0:
			print('ERROR')
			return None
		currentIdx = 0
		currentNode = self.head
		while True:
			currentNode = currentNode.nxt
			if currentIdx == index:
				return currentNode.data
				print(currentNode.data)
			currentIdx += 1


	def Pop(self, index):
		try:
			currentIdx = 0
			currentNode = self.head

			while True:
				lastNode = currentNode
				currentNode = currentNode.nxt
				if currentIdx == index:
					lastNode.nxt = currentNode.nxt
					return
				currentIdx += 1

		except:
			print('Pop Function', IndexError)
			return


	def Insert(self, index, data):
		if index >= self.Length() or index < 0:
			return self.Append(data)
		currentNode = self.head
		proirNode = self.head
		currentIdx = 0

		while True:
			currentNode = currentNode.nxt
			if currentIdx == index:
				newNode = Node(data)
				priorNode.nxt = newNode
				newNode.nxt = currentNode
				return
			priorNode = currentNode
			currentIdx += 1


	def Set(self, index, data):
		if index >= self.Length() or index < 0:
			print('FUCK YOU')
			return

		currentNode = self.head
		currentIdx = 0

		while True:
			currentNode = currentNode.nxt
			if currentIdx == index:
				currentNode.data = data
				return
			currentIdx += 1

if __name__ == '__main__':
	l1 = linked_list()
	l1.Append(1)
	l1.Append(2)
	l1.Append(3)
	# l1.Return()
	# l1.Length()
	# l1.Get(2)
	# l1.Pop(2)
	# l1.Return()
	# l1.Insert(1, 12)
	# l1.Return()
	# l1.Set(2, 34)
	# l1.Return()

"""
Linked Lists are not really useful in coding but it is the be>
way to teach the kinds of operations in data structures
"""
