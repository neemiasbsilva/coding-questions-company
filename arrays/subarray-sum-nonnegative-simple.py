# Method 1 Simple
# Complexity O(n^2)
import numpy as np

def subArraySum(arr, n, s):

    for i in range(n):
        current_sum = arr[i]
        j = i + 1

        while j <= n:
            if current_sum == s:
                print("%d %d"% (i+1, j))
                return 1
            
            if current_sum > s or j == n:
                break
            
            current_sum += arr[j]
            j += 1
    
    return 0
def main():
    T = int(input())

    for i in range(T):
        N, S = list(map(int,input().split(' ')))
        N = int(N)
        S = int(S)
        # arr = np.zeros(shape=(N), dtype=np.int32)
        arr = list(map(int,input().split(' ')))
        arr = np.asarray(arr)
        if subArraySum(arr, N, S) is 0:
            print("-1")

if __name__ == "__main__":
    main()
