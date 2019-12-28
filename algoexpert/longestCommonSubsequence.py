def longestCommonSubsequence(str1, str2):
    # Write your code here.
    n = len(str1)
    m = len(str2)
    dp = [[0 for i in range(m + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    ans = []
    backtrack(dp, ans, str1, str2)
    return ans


def backtrack(dp, ans, str1, str2):
    n = len(dp)
    m = len(dp[0])
    i = n - 1
    j = m - 1
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j - 1] + 1:
            ans.append(str1[i - 1])
            print("appending" , str1[i-1])
            i = i - 1
            j = j - 1
        elif dp[i][j] == dp[i - 1][j]:
            i = i - 1
            print("appending", str1[i - 1])
            ans.append(str1[i - 1])
        else:
            j = j - 1
            print("appending", str2[j - 1])
            ans.append(str2[j - 1])

def abcd(array):
    for i in reversed(range(len(array))):
        print(i)
        print(array[i])
if __name__=="__main__":
    # print(longestCommonSubsequence("ZXVVYZW","XKYKZPW"))
    print(abcd([23,45,67,89]))