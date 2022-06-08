from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for i in range(amount+1)] for i in range(len(coins)+1)]
        m, n = len(dp), len(dp[0])
        # if you want to make 0 amount, there is always 1 way
        for i in range(m):
            dp[i][0] = 1
        # if you want to make an amount other than 0 using no coins there are no ways
        # the first row is already 0
        for i in range(1,m):
            for j in range(1,n):
                currCoin = coins[i-1]
                remAmount = j - currCoin
                if remAmount >= 0:
                    dp[i][j] += dp[i][remAmount]
                dp[i][j] += dp[i-1][j]
        return dp[m-1][n-1]

if __name__=="__main__":
    print(Solution().change(5,[1,2,5]))