def numberOfBinaryTreeTopologies(n):
    # Write your code here.
    # let l rep no of nodes in left subtree
    # one node gets used for root
    if n == 0:
        return 1
    dp = [-1 for i in range(n + 1)]
    nT = 0
    for l in range(0, n):
        r = n - l - 1
        if dp[l] == -1:
            dp[l] = numberOfBinaryTreeTopologies(l)
        if dp[r] == -1:
            dp[r] = numberOfBinaryTreeTopologies(r)
        nl = dp[l]
        nr = dp[r]
        nT += nl * nr
    return nT
