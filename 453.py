class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minimum = min(nums)
        min_index = 0
        n =len(nums)
        for i in range(n):
            if nums[i] == minimum:
                min_index = i
                break
        ans = 0
        for i in range(n):
            ans += (nums[i]-minimum)
        return ans