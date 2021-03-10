# https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution:
    def createTargetArray(self, nums, index):
        n = len(nums)
        target = [None] * n
        for i in range(n):
            if index[i] is not None:
                self.shift_to_right_by_one(nums, index[i])
            target[index[i]] = nums[i]
        return target

    def shift_to_right_by_one(self, nums, i):
        n = len(nums)
        for i in range(n - 2, i - 1, -1):
            nums[i + 1] = nums[i]

if __name__=="__main__":
    print(Solution().createTargetArray([0,1,2,3,4], [0,1,2,2,1]))