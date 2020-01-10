def longestPalindromicSubstring(string):
    # Write your code here.
    longest_index = [0, 0]
    longest_len = 1
    n = len(string)
    dp = [[False for i in range(n)] for i in range(n)]
    for i in range(n):
        dp[i][i] = True
    for i in range(n-2, -1, -1):
        j = i+1
        if string[i] == string[j]:
            dp[i][j] = True
            longest_index[0] = i
            longest_index[1] = j
            longest_len = 2
    for i in range(n - 3, -1, -1):
        for j in range(i + 2, n):
            if string[i] == string[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = False
            if dp[i][j] is True:
                curr_len = j - i + 1
                if curr_len > longest_len:
                    longest_len = curr_len
                    longest_index[0] = i
                    longest_index[1] = j
    return string[longest_index[0]: longest_index[1] + 1]

if __name__=="__main__":
    print(longestPalindromicSubstring("abcdefghfedcbaa"))