class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        sums = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sums[hashed(i, j)] = nums[i] + nums[j]

        ans = []
        for i in range(len(nums)):
            for key in sums:
                if sums[key] + nums[i] == 0:
                    if isntMatchingIdx(i, key):
                        unhashedidxs = unhashed(key)
                        val1, val2 = nums[unhashedidxs[0]], nums[unhashedidxs[1]]
                        if sorted([val1, val2, nums[i]]) not in ans:
                            ans.append(sorted([val1, val2, nums[i]]))
        return ans


def hashed(i, j):
    return str(i)+":"+str(j)


def unhashed(key):
    return list(map(int, key.split(":")))


def isntMatchingIdx(i, key):
    return True if i not in unhashed(key) else False


# sort the numbers
# convert this to a 2 pointer solution

# sort the numbers
# convert this to a 2 pointer solution
def hashed(x):
    return str(x[0]) + ":" + str(x[1]) + ":" + str(x[2])


class Solution2:
    def threeSum(self, nums):
        nums = sorted(nums)
        n = len(nums)
        # take each number as target one at a time
        ans = []
        seen = set()
        checkedidxs = set()
        for i in range(len(nums)):
            target = nums[i]
            start, end = i + 1, n - 1  # start is i+1 , to avoid checking for idx combinations we have already checked before
            while start < end:
                if start != i and end != i:
                    if nums[start] + nums[end] + target == 0:
                        x = None
                        if nums[start] <= nums[i] <= nums[end]:
                            x = [nums[start], nums[i], nums[end]]
                        elif nums[i] <= nums[start] <= nums[end]:
                            x = [nums[i], nums[start], nums[end]]
                        else:
                            x = [nums[start], nums[end], nums[i]]
                        if hashed(x) not in seen:
                            ans.append(x)
                            seen.add(hashed(x))
                        start += 1
                        end -= 1
                    elif nums[start] + nums[end] + target > 0:
                        end -= 1
                    elif nums[start] + nums[end] + target < 0:
                        start += 1
                elif i == start:
                    start += 1
                elif i == end:
                    end -= 1
        return ans


if __name__=="__main__":
    print(Solution2().threeSum([-1,0,1,2,-1,-4]))
