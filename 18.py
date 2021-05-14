class Solution:
    def fourSum(self, nums, target):
        return self.xSum(4, target, nums)

    def xSum(self, x, target, nums):
        if x > len(nums):
            return []
        if x == len(nums) and sum(nums) == target:
            return [nums]
        if x == 1:
            if target in nums:
                return [[target]]
            else:
                return []
        curr_num = nums[0]
        res = []
        recResWithoutNum = self.xSum(x, target, nums[1:])
        if len(recResWithoutNum) != 0:
            # res.append(recResWithoutNum)
            res += recResWithoutNum
        recResWithNum = self.xSum(x - 1, target - nums[0], nums[1:])
        for rec in recResWithNum:
            res.append([curr_num] + rec)

        return res

if __name__=="__main__":
    print(Solution().fourSum([1,0,-1,0,-2,2], 0))


