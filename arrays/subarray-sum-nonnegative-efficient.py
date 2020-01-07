import numpy as np

def subArraySum(arr, n, s):
    current_sum, start = arr[0], 0

    i = 1

    while i <= n:
        while current_sum > s and start < i - 1:
            current_sum -= arr[start]
            start += 1
        if current_sum == s:
            print("%d %d"% (start+1, i))
            return 1
        if i < n:
            current_sum += arr[i]
        i += 1
    return 0

def main():
    T = int(input())

    for i in range(T):
        N, S = list(map(int, input().split(' ')))
        arr = list(map(int, input().split(' ')))
        arr = np.asarray(arr)

        if subArraySum(arr, N, S) is 0:
            print("-1")
if __name__ == "__main__":
    main()