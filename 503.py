# https://leetcode.com/problems/next-greater-element-ii/


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