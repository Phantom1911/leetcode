from typing import List

# not an efficient solve below

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)   # n = 6
        s, e = 0, n-1   # s = 0, e = 5
        left, right = -1,-1
        while s <= e:
            m = (s+e)//2    # m = 3+5/2 = 4
            if nums[m] == target:  # nums[4] = 8
                left, right = m, m   # l,r =4,4
                if m >=1 and nums[m-1] == target:
                    left = m-1
                    while left>= 0 and nums[left] == target:
                        left -=1
                    left+=1
                if m <= n-2 and nums[m+1] == target:
                    right = m+1
                    while right < n and nums[right] == target:
                        right +=1
                    right -= 1
                return [left,right]
            elif nums[m] < target:   # 7 <8
                s = m+1   # s = 3
            else:
                e = m-1
        return [left,right]

# the next approach is to shrink the start and end when you find the target, but even this doesn't seem to be the most optimal solve:

class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        s, e = 0, n-1
        while s <= e:
            m = (s+e)//2
            if nums[m] == target:
                if nums[s] == nums[e] == target:
                    return [s,e]
                while nums[s] != target:
                    s+=1
                while nums[e] != target:
                    e-=1
            elif nums[m] < target:   # 7 <8
                s = m+1   # s = 3
            else:
                e = m-1
        return [-1,-1]

if __name__=="__main__":
    print(Solution().searchRange([5,7,7,8,8,10],8))