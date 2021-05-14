class Solution:
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        unsorted_start = -1
        unsorted_end = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:  # sorted condition is violated
                unsorted_start = i
                unsorted_end = i + 1
                temp = nums[unsorted_end]
                j = unsorted_end
                while j < n-1 and nums[j+1] == temp:
                    j += 1
                    unsorted_end = j
                break

        # the array is already sorted
        if unsorted_start == -1:
            return 0

        # traverse the array from unsorted_end to find the end of unsorted part
        i = unsorted_end
        while i < len(nums)-1:
            if nums[i] > nums[i+1]:
                unsorted_end = i+1
                i = i+1
                temp = nums[i]
                while i < n-1 and nums[i+1] == temp:
                    i+=1
                    unsorted_end = i
            else:
                i+=1

        return unsorted_end - unsorted_start + 1

if __name__=="__main__":
    print(Solution().findUnsortedSubarray([2,3,3,2,4]))