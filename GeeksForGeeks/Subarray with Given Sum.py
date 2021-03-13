# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1
# User function Template for python3

# Problem statement says all array elements are positive: which is a good clue for sliding window problem!
class Solution:

    def subArraySum(self ,arr, n, s):

        # Your code here
        currSum = arr[0]
        left = 0
        for right in range(1 ,n):
            currSum += arr[right]

            while currSum > s and left < right :
                currSum -= arr[left]
                left += 1
            if currSum == s:
                return [left +1, right +1]

        if s in arr:
            return [arr.index(s) +1, arr.index(s) +1]

        return [-1]