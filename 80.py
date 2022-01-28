class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        ans = 0
        while i < len(nums):
            curr = nums[i]
            # if i has reached an idx where value is None we should break
            if curr is None:
                break
            count = 0
            while i < len(nums) and nums[i] == curr:
                count += 1
                i += 1
            shiftBy = 0
            if count > 2:
                shiftBy = count - 2
                ans += 2
            else:
                ans += count
            # i!=len(nums) is added because you shouldn't be doing any shifting for ending repeated elements
            if shiftBy > 0 and i != len(nums):
                doshift(nums, shiftBy, i)
                i = i - shiftBy

        return ans


def doshift(arr, shiftBy, idx):
    # mark all the elements in this range with None to handle case like : [0,0,0,0,3]
    for i in range(idx - shiftBy, idx):
        arr[i] = None
    for i in range(idx, len(arr)):
        arr[i - shiftBy] = arr[i]
        arr[i] = None
    return arr
