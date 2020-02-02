
def main():
    n_case = int(input())

    for i in n_case:
        s = str(input())

        l = list(s)

        for j in range(len(l)):
            print(l[j], end=' ')

        print('')

if __name__ == "__main__":
    main()