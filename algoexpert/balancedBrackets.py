from collections import deque


def balancedBrackets(string):
    # Write your code here.
    stack = deque()
    for i in range(len(string)):
        if string[i] == "(" or string[i] == "{" or string[i] == "[":
            stack.append(string[i])
        elif string[i] == ")" or string[i] == "}" or string[i] == "]":
            if len(stack) == 0:
                return False
            ele = stack.pop()
            if string[i] == ")" and ele != "(":
                return False
            elif string[i] == "}" and ele != "{":
                return False
            if string[i] == "]" and ele != "[":
                return False
    if len(stack) != 0:
        return False
    return True
