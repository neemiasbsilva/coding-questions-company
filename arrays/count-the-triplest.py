import numpy as np

def count_the_triplest(array, N):
    # construct the hash
    max_value = array.max()

    answer = 0
    frequence = np.zeros(shape=max_value+1)
    for i in array:
        frequence[i] += 1

    # Case 1: (0, 0, 0)
    answer += frequence[0] * (frequence[0]-1) * (frequence[0]-2) / 6

    # Case 2: (0, x, x)
    for i in range(1, max_value):
        answer += frequence[0] * frequence[i] * (frequence[i]-1) / 2

    # Case 3: (x, x, 2x)
    for i in range(1, (max_value+1) // 2):
        answer += (frequence[i] *
                    (frequence[i]-1) // 2 * frequence[2*i])

    # Case 4: (x, y, x+y)
    for i in range(1, max_value+1):
        for j in range(i+1, max_value-i+1):
            answer += frequence[i] * frequence[j] * frequence[i+j]

    return answer

def main():
    T = input()
    T = int(T)
    for i in range(0, T):
        N = input()
        N = int(N)
        array = np.zeros(shape=(N))
        for i in range(0, N):
            array[i] = int(input())

        answer = count_the_triplest(array, N)

if __name__ == "__main__":
    main()