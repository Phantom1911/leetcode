# https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge_map = {}
        stack = []
        n = len(nums2)
        for i in range(n):
            while stack and stack[-1] < nums2[i]:
                nge_map[stack.pop()] = nums2[i]

            stack.append(nums2[i])

        # for items left in stack, we didn't find any nge

        while stack:
            nge_map[stack.pop()] = -1

        res = []
        for i in range(len(nums1)):
            res.append(nge_map[nums1[i]])
        return res