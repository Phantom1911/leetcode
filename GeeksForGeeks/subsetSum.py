class Solution:
    def isSubsetSum(self, N, arr, sum):
        # code here
        # map of subsets ending at different indexes
        # m = {i: set() for i in range(len(arr))}
        # for key in m:
        #     m[key].add(arr[key])

        # for key in range(1, len(arr)):
        #     for i in range(0, key):
        #         lastSums = m[i]
        #         for val in lastSums:
        #             newval = val+arr[key]
        #             m[key].add(newval)
        # # print(m)
        # for key in m:
        #     values = m[key]
        #     if sum in values:
        #         return True
        # return False
        dp = [[False for i in range(sum + 1)] for i in range(len(arr))]
        n = len(arr)
        # 0 sum is always possible with empty set
        for i in range(n):
            dp[i][0] = True
        for i in range(1, sum + 1):
            dp[0][i] = True if arr[0] == i else False
        for i in range(1, n, 1):
            for j in range(1, sum + 1):
                dp[i][j] = dp[i - 1][j]
                if j - arr[i] >= 0:
                    dp[i][j] = dp[i][j] or dp[i-1][j - arr[i]]
        return dp[n - 1][sum]

if __name__=="__main__":
    print(Solution().isSubsetSum(6,[3 ,34 ,4 ,12 ,5 ,2],9))