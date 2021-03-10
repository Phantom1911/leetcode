# https://leetcode.com/problems/find-all-duplicates-in-an-array/

# TLE SOLUTION :::

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        uniques = []
        ans = []
        n = len(nums)
        for i in range(n):
            if nums[i] in uniques:
                ans.append(nums[i])
            else:
                uniques.append(nums[i])
        return ans

