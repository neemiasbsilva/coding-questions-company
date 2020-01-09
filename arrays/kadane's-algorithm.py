import numpy as np

def kadane(array):
    max_current = max_global = array[0]

    for i in range(1, len(array)):
        max_current = max(array[i], max_current + array[i])

        if max_current > max_global:
            max_global = max_current

    return max_global

def main():
    t = int(input())
    
    for i in range(t):
        
        n = int(raw_input(''))
        array = []
        for i in range(n):
            array.append(int(raw_input()))

        print(kadane(array))


if __name__ == "__main__":
    main()
