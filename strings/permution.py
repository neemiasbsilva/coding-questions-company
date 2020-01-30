

def permutation(s, l, r):

	# Base case

	if l == r:
		print(s)
	else:

		# Permutation made

		for i in range(l, r):
			s[l], s[r] = s[i], s[l]

			#recursion called
			permutation(l+1, r)

			#backtrack
			s[l], s[r] = s[i], s[l]



def main():
	n_case = int(input())

	for i in range(n_case):
		s = str(input())

		permutation(s, 0, len(s))
		
if __name__ == '__main__':
	main()