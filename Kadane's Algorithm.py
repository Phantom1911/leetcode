# Max Sum Subarray : Solved using Kadane's Algorithm

# Logic of Kadane's Algorithm:
# problem requires us to find the max sum of amongst all the subarrays (having at least 1 element) of the input array
# Brute force would make us find all the subarrays of the array, and then finding their sum, and returning the maximum among them
# thinking about it : all of the subarrays end at some index of input array, right?
# kadane's requires us to have a running track of max_sum_ending_here for each index, which is easy to calculate
# also keep track of max_so_far , to solve in single pass of the array

def maxSumSubarray(arr):
    max_sum_so_far, max_sum_ending_here = arr[0] , arr[0]
    n = len(arr)
    if n == 1:
        return arr[0]
    for i in range(1, n):
        max_sum_ending_here = max(arr[i], max_sum_ending_here+arr[i])
        max_sum_so_far = max(max_sum_so_far, max_sum_ending_here)
    return max_sum_so_far

if __name__ == "__main__":
    print(maxSumSubarray([3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4]))

