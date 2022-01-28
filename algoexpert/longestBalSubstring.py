# wrong attempt below.


def longestBalancedSubstring(string):
    stack = []
    maxLen = -1
    for i in range(len(string)):
        if string[i] == '(':
            stack.append(i)
        else:
            # there are 2 cases here
            # it can be a closing bracket matching something
            # or a closing bracket not matching anything
            if len(stack) > 0:
                currLen = i - stack.pop() + 1
                maxLen = max(currLen, maxLen)

    return maxLen
