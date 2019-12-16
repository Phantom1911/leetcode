def minNumberOfJumps(array):
    # Write your code here.
    dest = len(array) - 1
    dp = [float("inf") for i in range(len(array))]
    dp[dest] = 0
    for i in range(dest - 1, -1, -1):
        if array[i] <= 0:
            continue
        else:
            max_possible_jump = array[i]
            for curr_jump in range(1, max_possible_jump + 1):
                if i + curr_jump <= dest:
                    dp[i] = min(dp[i], dp[i + curr_jump] + 1)
    if dp[0] != float("inf"):
        return dp[0]
    return -1
