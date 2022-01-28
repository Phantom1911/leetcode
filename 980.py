from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        numOfPaths = [0]
        si, sj, fi, fj = -1, -1, -1, -1
        emptyCount = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    si, sj = i, j
                elif grid[i][j] == 2:
                    fi, fj = i, j
                elif grid[i][j] == 0:
                    emptyCount += 1
        currPath = set()
        dfs(si, sj, fi, fj, grid, currPath, numOfPaths, emptyCount)

        return numOfPaths[0]


def dfs(a, b, x, y, grid, currPath, numOfPaths, emptyCount):
    if a == x and b == y:
        # reached the dest
        if len(currPath) == emptyCount - 1:
            numOfPaths[0] += 1
        return
    currPath.add(hashed(a, b))
    dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    for d in dirs:
        i, j = a + d[0], b + d[1]
        if inbounds(i, j, grid) and grid[i][j] != -1 and hashed(i, j) not in currPath:
            dfs(i, j, x, y, grid, currPath, numOfPaths, emptyCount)
    currPath.remove(hashed(a, b))


def inbounds(i, j, grid):
    m, n = len(grid), len(grid[0])
    if 0 <= i < m and 0 <= j < n:
        return True
    return False


def hashed(i, j):
    return str(i) + ":" + str(j)

if __name__=="__main__":
    print(Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))