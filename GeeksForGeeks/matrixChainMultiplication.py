class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        dp = [[float("inf") for i in range(N-1)] for i in range(N-1)]
        m, n = len(dp), len(dp[0])
        for i in range(m):
            for j in range(n):
                if i == j:
                    dp[i][j] = 0
                elif j == i+1:
                    dp[i][j] = arr[i]*arr[i+1]*arr[i+2]
        for i in range(m-1,-1,-1):
            for j in range(i+2,n,1):
                if i == j or j == i+1:
                    continue
                else:
                    for k in range(i,j):
                        leftSide = dp[i][k]
                        rightSide = dp[k+1][j]
                        multiplyLeftAndRightSides = arr[i] * arr[k+1] * arr[j+1]
                        dp[i][j] = min(leftSide+rightSide+multiplyLeftAndRightSides, dp[i][j])
        return dp[0][n-1]

if __name__=="__main__":
    print(Solution().matrixMultiplication(5,[1,2,3,4,5]))