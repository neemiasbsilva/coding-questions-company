
def longest_palindrome(s):

    dp = [[0 for x in range(len(s))] for y in range(len(s))]

    length = 1
    i = 0

    while i < n:
        dp[i][i] = True
        i += 1
    
    start = 0
    i = 0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start = i
            length= 2
        i += 1
    

    k = 3
    while k <= len(s):
        i = 0

        while i < (len(s)-k+1):
            j = i + k - 1

        

def main():
    n_case = int(input())

    for i in range(n_case):
        s = str(input())

        longest_palindrome(s)

if __name__ == "__main__":
    main()