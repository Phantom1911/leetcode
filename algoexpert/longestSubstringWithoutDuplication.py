def longestSubstringWithoutDuplication(string):
    # Write your code here.
    maxSize = 0
    currSize = 0
    start = 0
    end = 0
    currWindow = set()
    ans = ""
    while end < len(string):
        if string[end] not in currWindow:
            currWindow.add(string[end])
            end += 1
            currSize = end - start
            if currSize > maxSize:
                maxSize = currSize
                ans = string[start:end]
        else:
            currSize = end - start
            if currSize > maxSize:
                maxSize = currSize
                ans = string[start:end]
            j = start
            while (j < len(string) and string[j] != string[end]):
                currWindow.remove(string[j])
                j += 1
            currWindow.remove(string[j])
            start = j + 1

    return ans

# an unsuccessful attempt is below

# def longestSubstringWithoutDuplication2(string):
#     # dp[i] will be the longest substring without duplication ending at index i
#     # ch[i] will be the characters in that longest substring
#     n = len(string)
#     dp = [1 for i in range(n)]
#     ch = [set([string[i]]) for i in range(n)]
#     for i in range(1, n):
#         if string[i] not in ch[i - 1]:
#             dp[i] = dp[i - 1] + 1
#             ch[i].update(ch[i - 1])
#         else:
#
#
#     maxsublen = 0
#     maxsubidx = -1
#     for i in range(n):
#         if dp[i] >= maxsublen:
#             maxsublen = dp[i]
#             maxsubidx = i
#     print(ch[maxsubidx])
#     ans = ""
#     for c in ch[maxsubidx]:
#         ans += c
#     return ans


if __name__=="__main__":
    print(longestSubstringWithoutDuplication2("clementisacap"))
