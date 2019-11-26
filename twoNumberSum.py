def twoNumberSum(array, targetSum):
    # Write your code here.
    ans = []
    s = set()
    for i in range(len(array)):
        if targetSum - array[i] in s:
            ans.append(targetSum - array[i])
            ans.append(array[i])
            print(ans)
            return ans
        else:
            s.add(array[i])

    return ans
