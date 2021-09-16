# https://leetcode.com/problems/k-diff-pairs-in-an-array/

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # Write your code here
        eleDict = {}
        n = len(nums)
        pair = 0
        # lets calculate the duplicate elements to handle k = 0 in the same loop
        for i in range(n):
            if k == 0:
                if nums[i] not in eleDict:
                    eleDict[nums[i]] = False
                elif eleDict[nums[i]] == False:
                    pair += 1
                    eleDict[nums[i]] = True
            else:
                eleDict[nums[i]] = False

        if k == 0:
            return pair

        for key in eleDict:
            if eleDict[key] == False and key - k in eleDict:
                if eleDict[key - k] == False:
                    pair += 1
            if eleDict[key] == False and key + k in eleDict:
                if eleDict[key + k] == False:
                    pair += 1
            eleDict[key] = True

        return pair
