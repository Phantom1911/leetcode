# https://practice.geeksforgeeks.org/problems/edit-distance3702/1


class Solution:
    def editDistance(self, s, t):
        # Code here
        m,n = len(s), len(t)
        dp = [[None for i in range(n+1)] for i in range(m+1)]
        # fill 1st row
        for i in range(n+1):
            dp[0][i] = i
       # fill 1st col
        for i in range(m+1):
           dp[i][0] = i
        for i in range(1, m+1):
           for j in range(1, n+1):
               if s[i-1] == t[j-1]:
                   dp[i][j] = dp[i-1][j-1]
               else:
                   dp[i][j] = 1+ min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])

        return dp[m][n]