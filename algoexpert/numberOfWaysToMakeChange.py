def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    dp = [0] * (n + 1)
    dp[0] = 1

    # it is important to keep denominations in outer loop and target in inner

    for d in denoms:
        for i in range(1, n + 1):
            if i - d >= 0:
                dp[i] += dp[i - d]
    return dp[n]
