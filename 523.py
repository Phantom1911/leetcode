class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for start in range(0, n-1):
            sum_with_start_fixed = nums[start]
            for end in range(start+1, n):
                sum_with_start_fixed = sum_with_start_fixed + nums[end]
                if k == 0 and sum_with_start_fixed == 0:
                    return True
                elif k!= 0 and sum_with_start_fixed % k == 0:
                    return True
        return False