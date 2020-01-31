
class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None



	def insert(self, data):
		newNode = Node(data)
		newNode.next = self.head
		self.head = newNode


	def show(self):
		current = self.head

		while current:
			print(current.data, end=' ')
			current = current.next


	def rotate(self, k):

		if k == 0:
			return

		current = self.head
		count  = 1
		while current.data != k:
			curent = current.next
			count += 1

	    kthNode = current

	    while current.next is not None:
	    	current = current.next

	    current.next = self.head

	    self.head = kthNode

	    kthNode = None




main():

	n_case = int(input())

	for i in range(n_case):

		length = int(input())

		arr = list(map(int, input().split(' ')))



if __name__ == '__main__':
	main()