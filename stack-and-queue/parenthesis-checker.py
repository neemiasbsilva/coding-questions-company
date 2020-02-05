
def parenthesis(s):

    stack = []

    s_temp = list(s)

    stack.append(s_temp[0])

    for i in range(1, len(s_temp)):
        if s_temp[i] == ')' and stack[-1] == '(':
            stack.pop()
        elif s_temp[i] == ']' and stack[-1] == '[':
            stack.pop()
        elif s_temp[i] == '}' and stack[-1] == '{':
            stack.pop()
        else:
            stack.append(s_temp[i])

    if len(stack) == 0:
        print("balanced")
    else:
        print("not balenced")
    
    return 

def main():
    n_case = int(input())

    for i in range(n_case):

        s = str(input())

        parenthesis(s)


if __name__ == "__main__":
    main()

