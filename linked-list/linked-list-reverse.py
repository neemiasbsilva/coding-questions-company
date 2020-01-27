'''
	Given a linked list of N nodes. The task is to reverse the list
''' 


class Node:
	# constructor
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	# constructor
	def __init__(self):
		self.head = None


	# insertion
	def insert(self, data):
		newNode = Node(data)
		
		if self.head:
			current = self.head
			while current:
				current = current.next

			current = newNode
		else:
			self.head = newNode


	# show the list
	def show(self):
		current = self.head
		while current:
			print(current.data)
			current = current.next

def main():
	n_cases = int(input())

	for i in range(n_cases):
		ll = LinkedList()
		length = int(input())
		arr_input = list(map(int, input().split(' ')))





if __name__ == '__main__':
	main()