class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arr_sum = 0
        n = len(nums)
        for i in range(n):
            arr_sum = arr_sum + nums[i]
        if arr_sum % 2 != 0:
            return False
        half_sum = arr_sum // 2

        def isPossibleSum(arr, k, index):
            n = len(arr)
            dp = [[False for i in range(k + 1)] for j in range(n)]
            for i in range(n):
                dp[i][0] = False
            for i in range(1, k + 1):
                if i == arr[0]:
                    dp[0][i] = True
                else:
                    dp[0][i] = False
            for i in range(1, n):
                for j in range(1, k + 1):
                    if j - arr[i] >= 0:
                        dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i]]
                    else:
                        dp[i][j] = dp[i - 1][j]
            return dp[n - 1][k]

            # if index==len(arr):

            # two possibilities : you can take current element or not
            # return isPossibleSum(arr, k-arr[index], index+1) or isPossibleSum(arr,k,index+1)

        return isPossibleSum(nums, half_sum, 0)