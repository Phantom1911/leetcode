# https://www.geeksforgeeks.org/count-natural-numbers-whose-permutation-greater-number/
## NAIVE SOLUTION:
# any number which is smallest amongst all its permutations will be increasing (not necessarily strictly increasing)

def printAllIncreasing(n):
    res = []
    for i in range(1, n + 1):
        if isIncreasing(i):
            res.append(i)
    return res


def isIncreasing(num):
    num = str(num)
    n = len(num)
    if n == 1:
        return True
    for i in range(n - 1):
        if int(num[i]) > int(num[i + 1]):
            return False
    return True


# EFFICIENT SOLUTION : uses stacks
# all nos from 1 -9 are increasing so push them on to the stack
def printAllIncreasingEfficient(n):
    stack = []
    if n <= 9:
        return n
    for i in range(1,10):
        stack.append(i)
    res = [1,2,3,4,5,6,7,8,9]
    while stack:
        temp = stack.pop() % 10
        for i in range(temp, 10):
            new_num = temp*10 + i
            if new_num <= n:
                res.append(new_num)
    return res

if __name__ == "__main__":
    # print(printAllIncreasing(15))
    print(printAllIncreasingEfficient(15))