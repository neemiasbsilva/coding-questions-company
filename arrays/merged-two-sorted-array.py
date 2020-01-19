import numpy as np
import heapq


def main():
    n_test = int(input())

    for i in range(n_test):
        size_arr1, size_arr2 = raw_input().split(' ')
        size_arr1 = int(size_arr1)
        size_arr2 = int(size_arr2)
        arr1 = list(map(int, raw_input().split(' ')))
        arr2 = list(map(int, raw_input().split(' ')))

        merged_arr =  np.concatenate((arr1, arr2), axis=1)
        print(np.sort(merged_arr))


if __name__ == "__main__":
    main()