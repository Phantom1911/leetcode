# https://leetcode.com/problems/next-greater-element-ii/

# Refer : https://www.youtube.com/watch?v=ARkl69eBzhY&t=366s

# The trick to deal with circular arrays is to duplicate them , and use mod. here, looping i till 2n - 1

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        indices = [-1] * n
        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                indices[stack.pop()] = nums[i % n]
            if i < n:
                stack.append(i)

        return indices