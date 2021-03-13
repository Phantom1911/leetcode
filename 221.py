# https://leetcode.com/problems/maximal-square/

# you have look below, diagonal below, and to the right: so fill out the last row and last col first

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = int(matrix[i][j])
        dp = [[None for i in range(cols)] for i in range(rows)]
        maxArea = 0
        # fill the last row
        for i in range(cols):
            dp[rows - 1][i] = matrix[rows - 1][i]
            if dp[rows - 1][i] == 1:
                maxArea = 1
        # fill the last column
        for i in range(rows):
            dp[i][cols - 1] = matrix[i][cols - 1]
            if dp[i][cols - 1] == 1:
                maxArea = 1
        for i in range(rows - 2, -1, -1):
            for j in range(cols - 2, -1, -1):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    min_others = min(dp[i + 1][j], dp[i + 1][j + 1], dp[i][j + 1])
                    if min_others == 0:
                        dp[i][j] = 1
                        if dp[i][j] > maxArea:
                            maxArea = dp[i][j]
                    else:
                        dp[i][j] = min_others + 1
                        if dp[i][j] > maxArea:
                            maxArea = dp[i][j]

        return maxArea * maxArea


if __name__=="__main__":
    s = Solution()
    print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))