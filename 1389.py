# https://leetcode.com/problems/create-target-array-in-the-given-order/

# the way python's insert(index, element to insert) function works is : it inserts at the given index, shifting all elements to the right

class Solution:
    def createTargetArray(self, nums, index) :
        n = len(nums)
        res = []
        for i in range(n):
            res.insert(index[i], nums[i])

        return res[0:n]


# SOLUTION without using Python's list insert method

class Solution2:
    def createTargetArray(self, nums, index) :
        n = len(nums)
        target = [None] * n
        for i in range(n):
            target = self.insert_at_index(target, index[i], nums[i])

        return target

    def insert_at_index(self, target, index, num):
        if target[index] is None:
            target[index] = num
        else:
            n = len(target)
            j = n-2
            while j != index:
                target[j+1] = target[j]
                j -=1
            target[index] = num
        return target

if __name__=="__main__":
    print(Solution2().createTargetArray([0,1,2,3,4], [0,1,2,2,1]))