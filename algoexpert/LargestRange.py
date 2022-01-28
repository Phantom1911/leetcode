def largestRange(array):
    # Write your code here.
    mini = min(array)
    maxi = max(array)
    numbers = dict()
    for i in range(mini, maxi + 1):
        numbers[i] = False
    for i in range(len(array)):
        numbers[array[i]] = True
    glob_max = 1
    loc_max = 0
    ans = []
    for key in range(mini, maxi + 1):
        while key < maxi + 1 and numbers[key] == True:
            loc_max += 1
            key += 1
        if loc_max > glob_max:
            ans = []
            ans.append(key - loc_max +1)
            ans.append(key-1)
            glob_max = loc_max
            loc_max = 0
    return ans

# the naive solution involves sorting
def largestRangeNaive(array):
    array.sort()
    ans = [array[0], array[0]]
    maxlen = 0
    n = len(array)
    i = 0
    while i < n - 1:
        curr = 0
        if array[i + 1] == array[i] + 1:
            start, end = i, i
            while i < n - 1 and (array[i + 1] == array[i] + 1 or array[i+1] == array[i]):
                i += 1
                curr += 1
            end = start + curr
        else:
            i += 1

        if curr > maxlen:
            ans[0], ans[1] = array[start], array[end]
            maxlen = curr
    return ans


if __name__ == "__main__":
    print(largestRangeNaive([19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]))
