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
        print(arr1)
        print(arr2)


if __name__ == "__main__":
    main()