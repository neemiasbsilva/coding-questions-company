'''
	Given an array of time intervals (start, end) for classroom lectures 
	(possibly overlapping), find the minimum number of rooms required.
'''
import numpy as np

def main():
	
	arr = [(30, 75), (20, 50), (0, 40), (60, 150)]

	arr = np.array(arr)
	out = 999999999999999999
	
	for x in arr:
		out = min(out, x[1])

	print(out) 



if __name__ == '__main__':
	main()