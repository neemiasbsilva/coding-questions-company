import numpy as np


def main():
    n_test = int(input())

    for i in range(n_test):

        arr_strings = list(map(str, raw_input().split('.')))
        arr_strings = np.asarray(arr_strings)
        arr_string_reversed = arr_strings[::-1]
        for j in arr_string_reversed:
            print(j, end='.')
        print('\n')


if __name__ == "__main__":
    main()
