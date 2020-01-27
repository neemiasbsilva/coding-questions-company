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
		newNode.next = self.head
		self.head = newNode


	# show the list
	def show(self):
		current = self.head
		while current:
			print(current.data, end=" ")
			current = current.next

		print("")
def main():
	n_cases = int(input())

	for i in range(n_cases):
		ll = LinkedList()
		length = int(input())
		arr_input = list(map(int, input().split(' ')))

		for elem in arr_input:
			ll.insert(elem)

		ll.show()




if __name__ == '__main__':
	main()