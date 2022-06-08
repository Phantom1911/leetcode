from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        maxGold = [-float("inf")]
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    dfs(i, j, grid, set(), maxGold, 0)
        return maxGold[0]


def dfs(a, b, grid, seen, maxGold, currGold):
    if not inbounds(a, b, grid) or hashed(a, b) in seen or grid[a][b] == 0:
        maxGold[0] = max(maxGold[0], currGold)
        return
    currGold += grid[a][b]
    dirs = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    seen.add(hashed(a, b))
    for d in dirs:
        dfs(a + d[0], b + d[1], grid, seen, maxGold, currGold)
    seen.remove(hashed(a,b))


def inbounds(a, b, grid):
    m, n = len(grid), len(grid[0])
    if 0 <= a < m and 0 <= b < n:
        return True
    return False


def hashed(a, b):
    return str(a) + ":" + str(b)

if __name__=="__main__":
    print(Solution().getMaximumGold([[0,0,0,0,0,0,32,0,0,20],
                                     [0,0,2,0,0,0,0,40,0,32],
                                     [13,20,36,0,0,0,20,0,0,0],
                                     [0,31,27,0,19,0,0,25,18,0],
                                     [0,0,0,0,0,0,0,0,0,0],
                                     [0,0,0,0,0,0,0,18,0,6],
                                     [0,0,0,25,0,0,0,0,0,0],
                                     [0,0,0,21,0,30,0,0,0,0],
                                     [19,10,0,0,34,0,2,0,0,27],
                                     [0,0,0,0,0,34,0,0,0,0]]))