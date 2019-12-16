def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    if n == 0:
        return 0
    dp = [float("inf")] * (n + 1)
    for denom in denoms:
        if denom <= n:
            dp[denom] = 1
    for i in range(1, n + 1):
        for denom in denoms:
            if i - denom >= 0:
                dp[i] = min(dp[i - denom] + 1, dp[i])
    if dp[n] != float("inf"):
        return dp[n]
    return -1
