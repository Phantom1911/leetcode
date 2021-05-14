class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n ==1:
            return nums
        start, mid1, mid2, end = 0, 0, 1, n-1
        for i in range(n):
            if nums[i] == 0 and self.notInCorrectPositionForZero(mid1, i):
                nums[mid1 + 1], nums[i] = nums[i], nums[mid1 + 1]
                mid1 += 1
            elif nums[i] == 1 and self.notInCorrectPositionForOne(mid1, mid2, i):
                nums[mid2 + 1], nums[i] = nums[i], nums[mid2 + 1]
                mid2 += 1
            elif nums[i] == 2 and self.notInCorrectPositionForTwo(mid2, end, i):
                nums[end], nums[i] = nums[i], nums[end]
                end -= 1

        return nums

    def notInCorrectPositionForZero(self, mid1, currIdx):
        if 0 <= currIdx <= mid1:
            return False
        return True

    def notInCorrectPositionForOne(self, mid1, mid2, currIdx):
        if mid1 + 1 <= currIdx <= mid2:
            return False
        return True

    def notInCorrectPositionForTwo(self, mid2, end, currIdx):
        if mid2 + 1 <= currIdx <= end:
            return False
        return True

if __name__=="__main__":
    print(Solution().sortColors([2,0,1]))