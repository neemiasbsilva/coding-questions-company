def next_large_element(arr):
    element = 0
    next = 0
    stack = []

    stack.append(arr[0])

    for i in range(1, len(arr), 1):
        next = arr[i]
        if len(stack) is not 0:
            
            element = stack.pop()

            while element < next:
                # print(str(element)+' -- '+str(next))
                print(str(next), end=' ')
                if len(stack) == 0:
                    break
                element = stack.pop()

            if element > next:
                stack.append(element)
        stack.append(next)

    while len(stack) is not 0:
        element = stack.pop()
        next = -1
        # print(str(element) + " -- " + str(next))
        print(str(next), end=' ')


def main():

    n_case = int(input())

    for i in range(n_case):
        n = int(input())
        arr = list(map(int, input().split(' ')))

        next_large_element(arr)
        print('')

if __name__ == "__main__":
    main()