# https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1

# Refer : https://www.youtube.com/watch?v=8BDKB2yuGyg

class Solution:
    def nextLargerElement(self, arr, n):
        # code here
        nge_map = {}
        stack = []
        for i in range(n):
            while stack and stack[-1] < arr[i]:
                nge_map[stack.pop()] = arr[i]

            stack.append(arr[i])

        # for items left in stack, we didn't find any nge

        while stack:
            nge_map[stack.pop()] = -1
        res = []
        for i in arr:
            res.append(nge_map.get(i))

        return res