import numpy as np
import heapq


def main():
    n_test = int(input())

    for i in range(n_test):
        size_arr1, size_arr2 = list(map(int, input().split()))
        print(size_arr1, size_arr2)


if __name__ == "__main__":
    main()