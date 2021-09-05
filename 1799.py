class Solution:
    def maxScore(self, nums):
        return self.maxScoreHelper(nums, 1)

    def maxScoreHelper(self, nums, currOp):
        if len(nums) == 2:
            return currOp * self.gcd(nums[0], nums[1])

        globMaxScore = -float("inf")

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                tempNums = nums[0:i] + nums[i + 2:j] + nums[j + 1:]
                currScore = currOp * self.gcd(nums[i], nums[j]) + self.maxScoreHelper(tempNums, currOp + 1)
                globMaxScore = max(globMaxScore, currScore)

        return globMaxScore

    def gcd(self, x, y):
        if x == 0 or y == 0:
            return max(x, y)
        smaller = x if x < y else y
        bigger = y if y >= x else x

        return self.gcd(bigger % smaller, smaller)

if __name__=="__main__":
    print(Solution().maxScore([3,4,6,8]))