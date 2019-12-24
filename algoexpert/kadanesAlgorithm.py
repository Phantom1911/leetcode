def kadanesAlgorithm(array):
    # Write your code here.
    ans = array[0]
    curr_ans = array[0]
    for i in range(1, len(array)):
        curr_ans += array[i]
        if curr_ans > ans:
            ans = curr_ans
        if curr_ans < 0:
            curr_ans = 0
    return ans
