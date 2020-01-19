import numpy as np

def main():
    n_test = int(input())

    for i in range(n_test):
        
        n = int(input())
        array = list(map(int, raw_input().split()))
        array = np.asarray(array, dtype=np.uint8)
        missing = 1
        for j in range(n-1):
            if array[j] == missing:
                missing += 1
            else:
                break
        print(missing)
if __name__ == "__main__":
    main()