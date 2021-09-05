class Solution:
    def circularArrayLoop(self, nums):
        n = len(nums)
        if n < 3:
            return False
        # consider each index as starting point
        for i in range(len(nums)):
            if (self.checkCycle(nums, i)):
                return True
            else:
                print("false for start idx " + str(i))
        return False

    def checkCycle(self, nums, start):
        n = len(nums)
        if nums[start] == 0:
            return False
        visited = [False] * n
        visited[start] = True
        currIdx = start
        cycleLen = 1
        if nums[start] > 0:
            isPositiveCycle = True
        else:
            isPositiveCycle = False
        while (True):
            currIdx = (currIdx + nums[currIdx]) % n
            if nums[currIdx] < 0 and isPositiveCycle == True:
                return False
            elif nums[currIdx] > 0 and isPositiveCycle == False:
                return False
            if visited[currIdx] == True:
                break
            else:
                cycleLen += 1
                visited[currIdx] = True

        if cycleLen > 2:
            return True

        return False


if __name__ == "__main__":
    print(Solution().circularArrayLoop([-1,-2,-3,-4,-5]))