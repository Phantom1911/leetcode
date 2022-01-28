class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m, n = m - 1, n - 1
        if m == 0 and n == 0:
            return 1
        return countWays(m, n, {}, m + 1, n + 1)


def countWays(m, n, memo, row, col):
    if (m == 1 and n == 0) or (m == 0 and n == 1):
        return 1
    if not inbounds(m, n, row, col):
        return 0
    if hashed(m, n) in memo:
        return memo[hashed(m, n)]
    res = countWays(m - 1, n, memo, row, col) + countWays(m, n - 1, memo, row, col)
    memo[hashed(m, n)] = res
    # print(f"{hashed(m,n)} , {res}")
    return res


def hashed(a, b):
    return str(a) + ":" + str(b)


def inbounds(a, b, row, col):
    if 0 <= a < row and 0 <= b < col:
        return True
    return False