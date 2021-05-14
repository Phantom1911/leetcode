class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        nums = set(nums)
        n = len(nums)
        nums = sorted(nums)
        maxLen = 1
        currLen = 1
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                currLen += 1  # continuing the old range
            else:
                currLen = 1  # start of a new range
            if currLen > maxLen:
                maxLen = currLen
        return maxLen
