class Solution:
    def Maximize(self, a, n):
        # Complete the function
        a = sorted(a)
        ans = 0
        for i in range(len(a)):
            ans += a[i]*i
        return ans % (10**9+7)