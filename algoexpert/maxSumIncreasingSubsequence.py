def maxSumIncreasingSubsequence(array):
    # Write your code here.

    n = len(array)
    mss = [0] * n
    # mss represents max subs sum ending at this index
    for i in range(n):
        mss[i] = [array[i], [array[i]]]
    for i in range(1, len(array)):
        for j in range(i):
            if array[i] > array[j]:
                curr_sum = mss[j][0] + array[i]
                if curr_sum > mss[i][0]:
                    mss[i][0] = curr_sum
                    new_arr = mss[j][1][::]
                    new_arr.append(array[i])
                    mss[i][1] = new_arr
    max_idx = 0
    for i in range(len(mss)):
        if mss[i][0] > mss[max_idx][0]:
            max_idx = i
    return mss[max_idx]


pass
