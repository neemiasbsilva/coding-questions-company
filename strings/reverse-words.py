import numpy as np

def main():
    n_test = int(input())

    for i in range(n_test):

        arr_strings = list(map(str, raw_input().split('.')))
        arr_string_reversed = np.flip(arr_strings)
        print(arr_string_reversed)

if __name__ == "__main__":
    main()
