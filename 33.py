# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums, target) :
        pivot = -1
        n = len(nums)
        pivot = self.findPivot(nums,0,n-1)
        if pivot == -1:
            return self.binarySearch(nums, 0, n - 1, target)
        else:
            if nums[pivot] == target:
                return pivot
            elif nums[0] <= target <= nums[pivot] :
                return self.binarySearch(nums, 0, pivot, target)
            return self.binarySearch(nums, pivot + 1, n - 1, target)

    def binarySearch(self, arr, lo, hi, target):

        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    def findPivot(self, arr, lo, hi):
        mid = (lo + hi) // 2
        if arr[mid] < arr[mid - 1]:
            return mid - 1
        elif arr[mid + 1] < arr[mid]:
            return mid
        elif arr[lo] > arr[mid]:
            return self.findPivot(arr, lo, mid)
        elif arr[mid] > arr[hi]:
            return self.findPivot(arr, mid, hi)
        return -1


if __name__=="__main__":
    s = Solution()
    print(s.search([1,3,5], 0))