# a bit optimized solve, here we don't care what was the index of the max in the window , just check if the max was the first element of the previous
# window -- gave TLE in LC
import collections


class Solution1:
    def maxSlidingWindow(self, nums, k):
        if k <= 0 or k > len(nums):
            return None
        if k == 1:
            return nums
        n = len(nums)
        maximum = nums[0]
        for i in range(0, k):
            if nums[i] > maximum:
                maximum = nums[i]
        ans = []
        ans.append(maximum)
        for start in range(1, n - k + 1):
            end = start + k - 1
            # check if the previous max was the first element of previous window
            # if yes, then get the new maximum in new window
            if maximum == nums[start -1]:
                maximum = self.get_max_in_window(nums[start: end+1])
            else:
                maximum = max(maximum, nums[end])
            ans.append(maximum)

        return ans

    def get_max_in_window(self, nums):
        maximum = nums[0]
        for i in range(0, len(nums)):
            if nums[i] > maximum:
                maximum = nums[i]

        return maximum



# unoptimized solve --  gave TLE in LC

class Solution2:
    def maxSlidingWindow(self, nums, k):
        if k <= 0 or k > len(nums):
            return None
        if k == 1:
            return nums
        n = len(nums)
        maximum = nums[0]
        index_of_max = 0
        for i in range(0, k):
            if nums[i] > maximum:
                maximum = nums[i]
                index_of_max = i
        ans = []
        ans.append(maximum)
        for start in range(1, n - k + 1):
            end = start + k - 1
            # check if the previous max still lies inside the new window
            if index_of_max >= start and index_of_max <= end:
                maximum = max(maximum, nums[end])
                ans.append(maximum)
                index_of_max = nums[start:end + 1].index(maximum) + start
            # if previous max doesn't lie inside the new window, calculate max in new window
            else:
                maximum = self.get_max_in_window(nums[start: end + 1])
                index_of_max = nums[start : end+1].index(maximum) + start
                ans.append(maximum)

        return ans

    def get_max_in_window(self, nums):
        maximum = nums[0]
        for i in range(0, len(nums)):
            if nums[i] > maximum:
                maximum = nums[i]

        return maximum

# Approach 3 that I though to optimize further, so that we don't have to spend O(n) to get max in new window when the previous max spills left
# was to track max and second max :: it doesn't work either ::: see why

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         if k <= 0 or k > len(nums):
#             return None
#         if k == 1:
#             return nums
#         n = len(nums)
#         maximum = max(nums[0], nums[1])
#         second_maximum = min(nums[1], nums[0])
#         for i in range(0, k):
#             if nums[i] > maximum:
#                 second_maximum = maximum
#                 maximum = nums[i]
#             elif nums[i] < maximum and nums[i] > second_maximum:
#                 second_maximum = nums[i]
#
#         # now we have got max and second max for the first window
#
#         ans = []
#         ans.append(maximum)
#         for start in range(1, n - k + 1):
#             end = start + k - 1
#             # check if the previous max was the first element of previous window
#             # if yes, then get the new maximum in new window
#             if maximum == nums[start - 1]:
#                 maximum = max(nums[end], second_maximum)

#                 # now in order to get second max in new window , we would need third max, which we dont have :(

# welcome back to sliding window max again after some months. here's deque based solve I got from discuss:

class Solution3:
    def maxSlidingWindow(self, nums, k) :
        res = []
        window = collections.deque()
        for i, num in enumerate(nums):
            while window and num >= nums[window[-1]]:
                window.pop()
            window.append(i)

            if i + 1 >= k:
                res.append(nums[window[0]])

            if i - window[0] + 1 == k:
                window.popleft()

        return res
if __name__=="__main__":
    s1 = Solution3()
    print(s1.maxSlidingWindow(
[7,2,4],
2))