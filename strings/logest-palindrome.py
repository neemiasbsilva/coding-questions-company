
def longest_palindrome(s):

    dp = [[0 for x in range(len(s))] for y in range(len(s))]

    print(dp)

def main():
    n_case = int(input())

    for i in range(n_case):
        s = str(input())

        longest_palindrome(s)

if __name__ == "__main__":
    main()