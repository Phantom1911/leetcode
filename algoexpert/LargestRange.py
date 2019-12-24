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

if __name__ == "__main__":
    print(largestRange([1,2,3,4]))
