# https://leetcode.com/problems/maximum-product-subarray/


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        max_prod_ending_here , max_prod_so_far, min_prod_ending_here = nums[0] , nums[0] , nums[0]
        for i in range(1, n):
            temp = max_prod_ending_here
            max_prod_ending_here = max(max_prod_ending_here * nums[i], nums[i], min_prod_ending_here * nums[i])
            min_prod_ending_here = min(temp * nums[i] , nums[i], min_prod_ending_here*nums[i])
            max_prod_so_far = max(max_prod_so_far, max_prod_ending_here)

        return max_prod_so_far


if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct([2,3,-2,4]))