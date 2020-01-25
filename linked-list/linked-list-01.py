'''
	Given a sorted linked list and a value to insert, write a function to insert the value in a sorted way.
	Input: 2 => 5 => 7 => 10 => 15
	Insert the value 9.
	Output: 2 => 5 => 7 => 9 => 10 => 15

'''

# Create a single node to linked list
class Node:
	"""constructor"""
	def __init__(self, data, next=None):
		self.data = data
		self.next = next


#Create a LinkedList Class to join all nodes
class LinkedList:

	def __init__(self):
		self.head = None


	# insertion method
	def insert(self, data):

		newNode = Node(data)

		if self.head:
			current = self.head
			flag = False
			if current.data >= data:
				newNode.next = current
				current = newNode
			else:

				while current.next and current.next.data < newNode.data:
					current = current.next

				newNode.next = current.next
				current.next = newNode



			current = newNode
		else:
			self.head = newNode

	# show the Linked List
	def show(self):
		current = self.head

		while current:
			print current.data
			current = current.next

def main():
	ll = LinkedList()
	
	ll.insert(2)
	ll.insert(5)
	ll.insert(7)
	ll.insert(10)
	ll.insert(15)

	ll.show()


if __name__ == '__main__':
	main()