def knapsackProblem(items, capacity):
    n = len(items)
    m = capacity
    dp = [[0 for i in range(m + 1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
    for i in range(m+1):
        dp[0][i] = 0
    for i in range(1, n+1):
        for j in range(1 , m + 1):
            dp[i][j] = dp[i - 1][j]
            if j - items[i-1][1] >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - items[i-1][1]] + items[i-1][0])
    print( [dp[n][m], getItems(dp, items)])
    # print( [dp[n - 1][m]])


def getItems(dp, items):
    picked_items = []
    n = len(dp)
    m = len(dp[0])
    # print(n)
    # print(m)
    i = n - 1
    j = m - 1
    print(i , j)
    while i >= 0:
        curr_val = dp[i][j]
        # this condn means that curr item was not picked
        if curr_val == dp[i - 1][j]:
            i -= 1
        else:
            picked_items.append(i - 1)

            j -= items[i - 1][1]
            if j == 0:
                break
    return list(reversed(picked_items))

if __name__=="__main__":
    knapsackProblem([[1, 2], [70, 70], [30, 30], [69, 69], [100, 100]], 100)
