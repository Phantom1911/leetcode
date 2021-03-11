# JUST A VARIATION OF KADANE'S ALGORITHM


def maxProductSubarray(nums):
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
    print(maxProductSubarray([2,3,-2,4]))
    print(maxProductSubarray([-2,0,-1]))
