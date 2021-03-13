# https://practice.geeksforgeeks.org/problems/stickler-theif-1587115621/1

def FindMaxSum(a, n):
    '''
    :param a:  given list of values
    :param n: size of a
    :return: Integer
    '''
    # code here
    if n == 1:
        return a[0]
    dp = [None] * n
    dp[0] = a[0]
    dp[1] = max(a[1], a[0])
    for i in range(2,n):
        dp[i] = max(dp[i-2] + a[i], dp[i-1])
    return dp[n-1]