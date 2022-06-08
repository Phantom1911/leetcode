from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        canJump = [[False for i in range(n)] for i in range(m)]
        seen = [[False for i in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and seen[i][j] == False:
                    dfs(i, j, grid, seen, canJump, [False])
        count = 0
        for i in range(m):
            for j in range(n):
                if canJump[i][j] == False and grid[i][j] == 1:
                    count += 1
        return count


def dfs(a, b, grid, seen, canJump, currCanJump):
    m, n = len(grid), len(grid[0])
    if a == 0 or a == m - 1 or b == 0 or b == n - 1:
        canJump[a][b] = True
        currCanJump[0] = True
    seen[a][b] = True
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for d in dirs:
        c, d = a + d[0], b + d[1]
        if inbounds(c, d, grid) and seen[c][d] == False and grid[c][d] == 1:
            dfs(c, d, grid, seen, canJump, currCanJump)
    canJump[a][b] = currCanJump[0]


def inbounds(a, b, grid):
    m, n = len(grid), len(grid[0])
    if 0 <= a < m and 0 <= b < n:
        return True
    return False

if __name__=="__main__":
    print(Solution().numEnclaves([[0,0,1,1,1,0,1,1,1,0,1],
                                  [1,1,1,1,0,1,0,1,1,0,0],
                                  [0,1,0,1,1,0,0,0,0,1,0],
                                  [1,0,1,1,1,1,1,0,0,0,1],
                                  [0,0,1,0,1,1,0,0,1,0,0],
                                  [1,0,0,1,1,1,0,0,0,1,1],
                                  [0,1,0,1,1,0,0,0,1,0,0],
                                  [0,1,1,0,1,0,1,1,1,0,0],
                                  [1,1,0,1,1,1,0,0,0,0,0],
                                  [1,0,1,1,0,0,0,1,0,0,1]]))