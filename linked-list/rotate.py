
class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None



main():

	n_case = int(input())

	for i in range(n_case):

		length = int(input())

		arr = list(map(int, input().split(' ')))



if __name__ == '__main__':
	main()