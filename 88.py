class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, currIdx = 0, 0, 0
        while p2 < n:
            if nums1[p1] > nums2[p2]:
                nums1 = self.shiftToRight(nums1, p1)
                nums1[currIdx] = nums2[p2]
                p1+=1
                p2+=1
            else:
                p1+=1
            if nums1[p1] == 0:
                break
            currIdx +=1 # currIdx helps us keep track of where to put the next element in nums1

        print(nums1)

        while p2 < n:
            self.shiftToRight(nums1, currIdx)
            nums1[currIdx] = nums2[p2]
            p2+=1
            currIdx +=1

        return nums1

    def shiftToRight(self, nums, idx):
        n = len(nums)
        for i in range(n-1, idx, -1):
            nums[i] = nums[i-1]
        return nums


if __name__=="__main__":
    print(Solution().merge([4,0,0,0,0,0], 1, [1,2,3,5,6] , 5))