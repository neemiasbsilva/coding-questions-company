import numpy as np


def main():

    n_case = int(input())

    for i in range(n_case):
        n = int(input())
        arr = list(map(int, input().split(' ')))

        result = np.zeros(shape=(n))
        for j in range(len(arr)-1):
            
            print(max(arr[j+1:]))
        
        

if __name__ == "__main__":
    main()