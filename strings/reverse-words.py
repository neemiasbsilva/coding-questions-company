

def main():
    n_test = int(input())

    for i in range(n_test):

        arr_strings = list(map(str, raw_input().split('.')))
        print(arr_strings)

if __name__ == "__main__":
    main()