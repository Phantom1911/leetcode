# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# Great video to understand valley peak approach : https://www.youtube.com/watch?v=K8iHi8AW1ls

class Solution:
    def maxProfit(self, prices):
        profit = 0
        n = len(prices)
        for i in range(1, n):
            # you cannot sell on 1st day
            # compare current element with previous element, the idea is that can you sell on ith day?
            if prices[i-1] < prices[i]:
                profit += prices[i] - prices[i-1]
        return profit

if __name__=="__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))