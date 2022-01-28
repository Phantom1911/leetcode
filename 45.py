class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        minjumps = [float("inf") for i in range(n)]
        minjumps[n - 1] = 0
        for i in range(n - 2, -1, -1):
            possiblejumps = nums[i]
            for j in range(1, possiblejumps + 1, 1):
                afterjumpidx = i + j
                if afterjumpidx <= n - 1:
                    minjumps[i] = min(minjumps[i], minjumps[i + j] + 1)

        return minjumps[0]