# this whole algo is O(n) and not O(n^2)
# because each element is visited at max twice
# l and r are constantly moving right , l is never reset in the inner loop (which is what happens in n^2 cases)
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0
        currSum = 0
        currLen, minLen = float("inf"), float("inf")
        while r<len(nums):
            currSum += nums[r]
            if currSum >= target:
                while currSum > target and l<=r:
                    currSum -= nums[l]
                    l+=1
                if currSum == target:
                    currLen = r-l+1
                    minLen = min(currLen,minLen)
                elif currSum < target:
                    currLen = r-l+2
                    minLen = min(currLen,minLen)
            r+=1
        if minLen == float("inf"):
            return 0
        return minLen