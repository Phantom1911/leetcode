from collections import defaultdict
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # acquire , release method with map
        i,j = 0,0
        chars = defaultdict(int)
        ans = 0
        while j< len(nums):
            chars[nums[j]] += 1
            if len(chars) == k:
                while len(chars) == k:
                    ans += 1
                    chars[nums[i]]-=1
                    if chars[nums[i]] == 0:
                        del chars[nums[i]]
                    i += 1
            j+=1
        return ans

if __name__=="__main__":
    print(Solution().subarraysWithKDistinct([1,2,1,2,3], 2))