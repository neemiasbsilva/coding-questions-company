'''
    Given a string s, recursively remove adjacent duplicate character from the strings.
    The output string should not have any adjacent duplicates.
'''

def removeUtil(s, last_removed):

    if len(s) == 0 or len(s) == 1:
        return s
    
    if s[0] == s[1]:
        last_removed = ord(s[0])
        
        while len(s) > 1 and s[0] == s[1]:
            s = s[1:]
        s = s[1:]

        return removeUtil(s, last_removed)
    
    

def to_string(s):
    return ''.join(s)

def remove(s):
    last_removed = 0
    return to_string(removeUtil(s, last_removed))

def main():
    n_case = int(input())

    for i in range(n_case):
        s = str(input())

        s = list(s)

        remove(s)

if __name__ == "__main__":
    main()