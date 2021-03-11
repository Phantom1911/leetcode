# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums) :
        nums = sorted(nums)
        positive_begin_index = -1
        for i in range(0, len(nums)):
            if nums[i] == 1 :
                positive_begin_index = i
                break
        if positive_begin_index == -1:
            return 1
        j = 1
        for i in range(positive_begin_index, len(nums)):
            if nums[i] != j:
                return j
            j +=1
        return j

if __name__ == "__main__":
    print(Solution().firstMissingPositive([0,1,2]))