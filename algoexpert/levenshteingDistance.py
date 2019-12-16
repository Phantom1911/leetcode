def levenshteinDistance(str1, str2):
    # Write your code here.
    n = len(str1)
    m = len(str2)
    dp = [[0 for i in range(m + 1)] for i in range(n + 1)]
    for i in range(m + 1):
        dp[0][i] = i
    for i in range(n + 1):
        dp[i][0] = i
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
    return dp[n][m]
