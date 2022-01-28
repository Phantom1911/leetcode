# https://leetcode.com/problems/find-all-duplicates-in-an-array/

# TLE SOLUTION :::
# below is a bad solution because it uses extra space

class Solution:
    def findDuplicates(self, nums):
        uniques = []
        ans = []
        n = len(nums)
        for i in range(n):
            if nums[i] in uniques:
                ans.append(nums[i])
            else:
                uniques.append(nums[i])
        return ans

# correct approach is to make use of the fact that numbers of the array are between 1 to n, hence we can use cyclic sort

class Solution2:
    def findDuplicates(self, nums):

            n = len(nums)
            i = 0
            swaps = 0
            while swaps < n:
                if nums[i] - 1 != i:
                    correctidxofthiselement = nums[i] - 1
                    nums[i], nums[correctidxofthiselement] = nums[correctidxofthiselement], nums[i]
                    swaps +=1
                else:
                    i += 1
            ans = []
            print(nums)
            for i in range(len(nums)):
                if nums[i]-1 != i:
                    ans.append(nums[i])

            return ans

if __name__=="__main__":
    print(Solution2().findDuplicates([4,3,2,7,8,2,3,1]))

