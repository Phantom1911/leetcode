from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        evenSum, oddSum = [0 for i in range(len(nums))], [0 for i in range(len(nums))]
        evenSumLeft, oddSumLeft = [0 for i in range(len(nums))], [0 for i in range(len(nums))]
        # when you remove an element, all elements that are to the right of removed element get affected
        n = len(nums)
        # oddsum[i] is sum of all elements at odd indices to the right of i
        oddSum[n-1], evenSum[n-1] = 0,0
        for i in range(len(nums)-2,-1,-1):
            if (i+1)%2==0:
                evenSum[i] = evenSum[i+1]+nums[i+1]
                oddSum[i] = oddSum[i+1]
            else:
                oddSum[i] = oddSum[i+1]+nums[i+1]
                evenSum[i] = evenSum[i+1]
        # oddsumleft is sum of all odd indices to the left of i
        evenSumLeft[0], oddSumLeft[0] = 0,0
        for i in range(1,n):
            if (i-1)%2==0:
                evenSumLeft[i] = evenSumLeft[i-1]+nums[i-1]
                oddSumLeft[i] = oddSumLeft[i-1]
            else:
                oddSumLeft[i] = oddSumLeft[i-1]+nums[i-1]
                evenSumLeft[i] = evenSumLeft[i-1]
        # check by removing elements one by one
        ans = 0
        for i in range(len(nums)):
            if evenSumLeft[i] + oddSum[i] == oddSumLeft[i] + evenSum[i]:
                ans+=1
        return ans