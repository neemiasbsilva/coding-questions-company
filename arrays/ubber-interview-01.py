#############################################################################################
# Given an array of integers, return a new array such that each element at index i of the   #
# new array is the product of all the number in the original array                          #
#############################################################################################
import numpy as np

def product_arr(arr):
    new_arr = np.ones(arr.shape, dtype=np.uint8)
    for i in range(0, arr.shape[0]):
        for j in range(0, arr.shape[0]):
            if j != i:
                new_arr[i] = new_arr[i] * arr[j]
            
    return new_arr

def main():
    arr = [1, 2, 3, 4, 5]
    arr = np.array(arr, dtype=np.uint8)
    print("New array: ", product_arr(arr))

if __name__ == "__main__":
    main()
