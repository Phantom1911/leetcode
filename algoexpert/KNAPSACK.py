
def knapsackProblem(items, capacity):
    # 0 --> capacity+1 , 0 --> len(items)
    # dp[i][j] = max value that I can make with cap i and items [0 .. j]
    dp = [[-float("inf") for i in range(len(items))] for i in range(capacity + 1)]
    for i in range(len(items)):
        dp[0][i] = 0
    for i in range(1, capacity + 1):
        dp[i][0] = items[0][0] if items[0][1] <= i else 0
    for i in range(1, capacity + 1):
        for j in range(1, len(items)):
            # I don't pick jth item
            dp[i][j] = dp[i][j - 1]
            # I have picked the jth item
            if i >= items[j][1]:
                dp[i][j] = max(dp[i][j], dp[i - items[j][1]][j - 1] + items[j][0])
    picked = []
    # i,j --> i,j-1 ; i+items[j][1],j-1
    i, j = capacity, len(items) - 1
    m, n = capacity + 1, len(items)
    while inbounds(i, j, m, n):
        a, b = -float("inf"), -float("inf")
        if inbounds(i, j - 1, m, n):
            a = dp[i][j - 1]
        if inbounds(i - items[j][1], j - 1, m, n):
            b = dp[i - items[j][1]][j - 1] + items[j][0]
        if a < b:
            picked.append(j)
            i, j = i - items[j][1], j - 1
        else:
            i, j = i, j - 1

    if dp[i][j] > 0:
        picked.append(0)
    return [dp[capacity][len(items) - 1], (picked)]


def inbounds(a, b, m, n):
    if 0 <= a < m and 0 <= b < n:
        return True
    return False


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


# BELOW SOLUTION IS WRONG
# I tried so hard, and got so far. In the end, it doesn't even matter

# def knapsackProblem(items, capacity):
#     # Write your code here.
#     # return [
#     #   10, // total value
#     #   [1, 2], // item indices
#     # ]
#     # what does dp[i][j] represent here? basically the array to be considered for picking elements is
#     # from i .. n-1 and j is the left capacity to work with
#
#     n = len(items)
#     dp = [[0 for i in range(n)] for j in range(capacity + 1)]
#
#     # dp[0][j] represents the maxValue you can have with capacity 0, which is 0
#     for i in range(n):
#         dp[0][i] = 0
#
#     # fill the last column
#     for i in range(1, capacity + 1):
#         dp[i][n - 1] = items[n - 1][0] if i >= items[n - 1][1] else 0
#     picked_boolean = [False for i in range(n)]
#     for currCap in range(1, capacity + 1):
#         for j in range(n - 2, -1, -1):
#             val1, val2 = 0, 0
#             # if you pick up the jth item
#             if currCap >= items[j][1]:
#                 val1 = dp[currCap - items[j][1]][j + 1] + items[j][0]
#             # if you don't pick up the jth item
#             val2 = dp[currCap][j + 1]
#             if val1 >= val2:
#                 # picked_boolean[j] =True
#                 print("pickinng item " + str(items[j][0]))
#                 dp[currCap][j] = val1
#             else:
#                 dp[currCap][j] = val2
#
#
#     # get the picked items by retracing the path
#     # if I am at dp[i][j] rn, compare it with dp[i][j+1]
#     # if dp[i][j] == dp[i][j+1] , that means jth item was not picked
#
#     picked_items = []
#     # print(picked_boolean)
#     # currVal = dp[capacity][0]
#     # j = capacity
#     # while i < n:
#     #     if currVal != dp[j][i+1]:
#     #         picked_items.append(items[i])
#     #         currVal = dp[][]
#
#     # j = 0
#     # i = capacity
#     # while i > 0 and j < n-1:
#     #     if i - items[j][1] >=0 and dp[i - items[j][1]][j + 1] + items[j][0] >= dp[i][j + 1]:
#     #         picked_items.append(items[j])
#     #         i = i - items[j][1]
#     #     j += 1
#
#     return dp[capacity][0], picked_items


if __name__=="__main__":
    print(knapsackProblem([[1, 2], [4, 3], [5,6], [6, 7]], 10))
