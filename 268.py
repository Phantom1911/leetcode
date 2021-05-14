class Solution:
    def missingNumber(self, nums):
        num = 0
        for idx in range(len(nums) + 1):
            num ^= idx

        for idx in nums:
            num ^= idx
        return num

if __name__== "__main__":
    print(Solution().missingNumber([3,1,0]))