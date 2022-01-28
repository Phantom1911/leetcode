# https://leetcode.com/problems/powx-n/

'''

This is a nice problem, because this is where you realize that topDown is often a better solution than a bottom up solution.
My bottom up solution timed out whereas top down solution did pretty well. Code below :

'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        nAbs = abs(n)
        # temp = self.helper(x, nAbs)
        powerdict = {}
        powerdict[0] = 1
        powerdict[1] = x
        powerdict[2] = x * x
        temp = self.topDown(powerdict, x, nAbs)
        if n > 0:
            return temp
        else:
            return 1 / temp

    def topDown(self, powerdict, x, n):
        if n in powerdict:
            return powerdict[n]
        temp = self.topDown(powerdict, x, n // 2)
        if n % 2 == 1:
            powerdict[n] = x * temp * temp
        else:
            powerdict[n] = temp * temp
        return powerdict[n]

        # def helper(self, x, n):
    #     # deals with just positive n
    #     # dp = [-1] * (n+1)
    #     # dp[0] = 1
    #     # dp[1] = x
    #     if n == 1:
    #         return x
    #     prev = x
    #     # the bottom up routine actually is bad here since it calculates all the powers of x from 2 to n ..
    #     # .. , which may not be required
    #     for i in range(2, n+1):
    #         if i % 2 == 0:
    #             curr  = prev * prev
    #             # dp[i] = dp[i//2] * dp[i//2]
    #         else:
    #             curr = prev*prev*x
    #             prev = prev*x
    #             # dp[i] = dp[i//2] * dp[i//2] * x
    #     return curr