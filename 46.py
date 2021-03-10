# https://leetcode.com/problems/permutations/

# THIS IS MY OWN BEAUTIFUL ALGORITHM: CHEERS!

import copy
class Solution:
    def permute(self, nums) :
        return self.getPermutations(nums)

    def getPermutations(self, nums):
        if len(nums) == 1:
            res = []
            res.append([nums[0]])
            return res
        remPerms = self.getPermutations(nums[1:])
        num = nums[0]
        perms = []
        for perm in remPerms:
            for i in range(len(perm) + 1):
                new_perm = copy.deepcopy(perm)
                new_perm.insert(i, num)
                perms.append(new_perm)
        return perms

if __name__ == "__main__":
    s = Solution()
    print(s.getPermutations([1,2,3]))