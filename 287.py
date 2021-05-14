# Find the duplicate in an array of N integers ==> [1,3,4,2,2] Output: 2
# https://leetcode.com/problems/find-the-duplicate-number/


class Solution:
    def findDuplicate(self, nums):
        slow,fast = nums[0],nums[0]
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                slow = nums[0]
                break
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

if __name__=="__main__":
    s = Solution()
    print(s.findDuplicate([1,3,4,2,2]))