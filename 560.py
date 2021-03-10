# https://leetcode.com/problems/subarray-sum-equals-k/

# NAIVE SOLUTION :: GIVES TLE
class Solution:
    def subarraySum(self, nums, k):
        n = len(nums)
        cum_sum = [None] * n
        cum_sum[0] = nums[0]
        ans = 0
        if k == nums[0]:
            ans+=1
        for i in range(1, n):
            cum_sum[i] = cum_sum[i-1] + nums[i]
            if cum_sum[i] == k:
                ans += 1
        for i in range(n-1):
            for j in range(i+1, n):
                sub_array_sum = cum_sum[j] - cum_sum[i]
                if sub_array_sum == k:
                    ans +=1
        return ans

if __name__=="__main__":
    s = Solution()
    print(s.subarraySum([1,1,1], 2))