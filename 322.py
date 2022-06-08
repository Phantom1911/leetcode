from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float("inf") for i in range(amount+1)] for i in range(len(coins)+1)]
        # when making 0 amount, min coins required are 0
        m, n = len(dp), len(dp[0])
        for i in range(m):
            dp[i][0] = 0
        for i in range(1, m):
            for j in range(1, n):
                currCoin = coins[i-1]
                remAmount = j - currCoin
                if remAmount >= 0:
                    dp[i][j] =  1 + dp[i][remAmount]
                dp[i][j] = min(dp[i][j], dp[i-1][j])
        if dp[m-1][n-1] == float("inf"):
            return -1
        return dp[m-1][n-1]

if __name__=="__main__":
    print(Solution().coinChange([1,2,5],11))