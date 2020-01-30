def string(a):
	return ''.join(a)

def permutation(s, l, r):

	# Base case

	if l == r:
		print(string(s), end=' ')
	else:

		# Permutation made

		for i in range(l, r):
			s[l], s[i] = s[i], s[l]

			#recursion called
			permutation(s, l+1, r)

			#backtrack
			s[l], s[i] = s[i], s[l]



def main():
	n_case = int(input())

	for i in range(n_case):
		s = str(input())
		a = list(s)
		permutation(a, 0, len(s))
		
		print('')
if __name__ == '__main__':
	main()