# https://leetcode.com/problems/search-insert-position/
# Refer : https://www.youtube.com/watch?v=0A40XJH_VvE

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        n = len(nums)
        if target > nums[n-1]:
            return n
        lo,hi=0,n-1
        while lo<=hi:
            mid = (hi+lo)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] > target:
                hi = mid-1
            else:
                lo = mid+1
        return lo