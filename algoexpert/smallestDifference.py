def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    n = len(arrayOne)
    m = len(arrayTwo)
    i, j = 0, 0
    diff = float("inf")
    ans_tuple = [-1, -1]
    while (i < n and j < m):
        if arrayOne[i] == arrayTwo[j]:
            return [arrayOne[i], arrayTwo[j]]
        else:
            curr_diff = abs(arrayOne[i] - arrayTwo[j])

            if curr_diff < diff:
                ans_tuple[0] = arrayOne[i]
                ans_tuple[1] = arrayTwo[j]
                diff = curr_diff
            if arrayOne[i] > arrayTwo[j]:
                j += 1
            else:
                i += 1
    return ans_tuple
