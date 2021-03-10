def FindMaxSum(a, n):
    '''
    :param a:  given list of values
    :param n: size of a
    :return: Integer
    '''
    # code here
    return max_sum(a)

# NAIVE RECURSIVE SOLUTION : GIVES TLE

def max_sum(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    elif n == 2:
        return max(arr[0], arr[1])
    else:
        return max(arr[0] + max_sum(arr[2:]), max_sum(arr[1:]))

# DP SOLUTION

def max_sum_dp(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    elif n ==  2:
        return max(arr[0], arr[1])
    else:
        dp = [None] * n
        # dp represents max sum if the array we consider is arr[i:]
        dp[n-1] = arr[n-1]
        dp[n-2] = max(arr[n-1], arr[n-2])
        for i in range(n-3, -1, -1):
            dp[i] = max(arr[i]+dp[i+2] , dp[i+1])
        return dp[0]



if __name__=="__main__":
    print(max_sum_dp([5,5,10,100,10,5]))