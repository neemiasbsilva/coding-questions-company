import numpy as np

def main():
    n_test = int(input())

    for i in range(n_test):
        
        n = int(input())
        array = list(map(int, raw_input().split()))
        array = np.asarray(array, dtype=np.uint8)
        print(array)

if __name__ == "__main__":
    main()