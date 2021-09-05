import copy


def powerset(array):
    # Write your code here.
    ans = [[]]
    for ele in array:
        n = len(ans)
        for i in range(n):
            arr = ans[i]
            temp = arr[::]
            temp.append(ele)
            ans.append(temp)
    return ans


class Solution:
    def subsets(self, nums):
        return self.getPowerset(nums)

    def getPowerset(self, nums):
        if len(nums) == 0:
            return [[]]
        startEle = nums[0]
        remPowerset = self.getPowerset(nums[1:])
        currPowerset = list(remPowerset)
        for s in remPowerset:
            if s is not None:
                newS = copy.deepcopy(s)
                newS.insert(0, startEle)
            else:
                newS = [startEle]
            currPowerset.append(newS)
        return currPowerset

if __name__ == "__main__":
    # print(powerset([1, 2, 3]))
    print(Solution().subsets([1,2,3]))



