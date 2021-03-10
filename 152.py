# https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums):
        res = max(nums)
        n = len(nums)
        curMin , curMax = 1, 1
        for i in range(n):
            temp = curMax * nums[i]
            # nos to consider:
            # nums[i] can be +ve , -ve, 0
            # case 1 : nums[i] is curMax when [-1, 2]
            # case 2 : curMax * nums[i] when both are positive (both are negative case not applicable, since curMin will always be more negative than curMax)
            # case 3: curMin * nums[i] whne both are negative (both are positive case not applicable, since curMax will alwys be more +ve than curMin)

            curMax = max(nums[i], curMax * nums[i], curMin * nums[i])
            curMin = min(temp, nums[i], curMin*nums[i])
            res = max(res, curMax)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct([2,3,-2,4]))