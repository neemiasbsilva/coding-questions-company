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




def main():
	ll = LinkedList()
	ll.head = Node()



if __name__ == '__main__':
	main()