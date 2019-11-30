def threeNumberSum(array, targetSum):
    # Write your code here.
    ans = []
    array.sort()
    for i in range(len(array) - 2):
        curr_num = array[i]
        left = i + 1
        right = len(array) - 1

        while left < right:
            if curr_num + array[left] + array[right] == targetSum:
                ans.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif curr_num + array[left] + array[right] > targetSum:
                right -= 1
            else:
                left += 1
    return ans
