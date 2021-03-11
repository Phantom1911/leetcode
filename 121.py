# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# at any given day i, you can buy , sell or do nothing
# min_buy[i] == min price that you could have bought in from days 0 to i , including i
# max_sell[i+1] == max sell price from i+1 to n-1
# an i which has max difference of min_sell[i] and max_sell[i+1] , would give us the max profit

class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        min_buy = [None] * n
        max_sell = [None] * n
        min_buy[0] = prices[0]
        max_sell[n-1] = prices[n-1]
        for i in range(1, n):
            min_buy[i] = min(min_buy[i-1] , prices[i])
        for i in range(n-2, -1, -1):
            max_sell[i] = max(max_sell[i+1] , prices[i])
        max_profit = 0      # make sure to initiliaze this as 0 , since initializing at -float("inf") fails for case [7,6,5,4,3]
        for i in range(n-1):
            # you can't buy on the last day
            max_profit = max(max_profit, max_sell[i+1] - min_buy[i])
        return max_profit

