def numbersInPi(pi, numbers):
    ans = getmindividers(pi, numbers)
    if ans == float("inf"):
        return -1
    return ans


def getmindividers(pi, numbers):
    if pi in numbers:
        return 0
    if len(pi) == 1 and pi not in numbers:
        return float("inf")
    mindividers = float("inf")
    n = len(numbers)
    # one obvious solve is to place divider at all possible places in the string and check min no of more dividers that need to be added
    for i in range(0, n - 1):
        currdividers = 1 + getmindividers(pi[1:], numbers)
        mindividers = min(currdividers, mindividers)

    return mindividers



if __name__=="__main__":
    print(numbersInPi("3141",["3", "14", "1"]))