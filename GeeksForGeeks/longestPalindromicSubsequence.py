class Solution:

    def longestPalinSubseq(self, S):
        n = len(S)
        dp = [[-float("inf") for i in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-1,-1,-1):
            for j in range(i+1,n,1):
                if S[i] == S[j]:
                    if j == i+1:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j-1],dp[i+1][j],dp[i][j-1])
        return dp[0][n-1]

if __name__=="__main__":
    print(Solution().longestPalinSubseq("dpooefx"))