class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        # arithmetic array => basically AP!
        dp = [0 for i in range(len(nums))]
        # dp[i] here denotes number of APs ending at index i
        dp[0], dp[1] = 0,0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1]-nums[i-2]:
                dp[i] = dp[i-1]+1
        return sum(dp)

