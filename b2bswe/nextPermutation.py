
class Solution:
    def nextPermutation(self, nums):
        '''
        :type nums: list of int
        :rtype: list of int
        '''
        '''
        think about how this permutation sequence would have got created. I need to create next bigger 
        permutation sequence
        if current is 3495432 - this means all the possibilities with let's say 2 at the most significant
        position have already been explored - since it would have made smaller value permutation
        also to generate the next bigger permutation I would want to change the least significant position 
        as possible - hence we start looking from the right, and we look for the minimum greater element
        to the right of each index. we swap and from the swap position +1 , sort all the elements
        '''
        minGreaterIdx, swappedIdx = -1, -1
        for i in range(len(nums)-2, -1, -1):
            minGreaterIdx = -1
            for j in range(i+1, len(nums), 1):
                if nums[j] > nums[i]:
                    if minGreaterIdx == -1:
                        minGreaterIdx = j
                        swappedIdx = i
                    elif nums[j] < nums[minGreaterIdx]:
                        minGreaterIdx = j
                        swappedIdx = i
            if minGreaterIdx != -1:
                break
        nums[minGreaterIdx], nums[swappedIdx] = nums[swappedIdx], nums[minGreaterIdx]
        partone = nums[:swappedIdx+1]
        partTwo = sorted(nums[swappedIdx+1:])
        return partone+partTwo