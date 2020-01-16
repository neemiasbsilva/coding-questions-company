# ------------------------------------------------------------------------------------------------
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k #
# ------------------------------------------------------------------------------------------------

def find_k(l, k):

    for i in range(0, len(l)):
        if k - l[i] in l:
            return True
    return False


def main():
    l = [10, 15, 3, 7]
    k = 17

    print(find_k(l, k))



if __name__ == "__main__":
    main()