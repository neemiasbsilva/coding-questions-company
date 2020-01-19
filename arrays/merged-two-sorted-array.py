import numpy as np
import heapq


def main():
    n_test = int(input())

    for i in range(n_test):
        size_arr1, size_arr2 = raw_input().split(' ')
        size_arr1 = int(size_arr1)
        size_arr2 = int(size_arr2)
        print(size_arr1, size_arr2)


if __name__ == "__main__":
    main()