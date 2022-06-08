from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dp = [[float("inf") for i in range(n)] for i in range(n)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                elif dp[i][j] == float("inf"):  # this means i,j has not been visited yet
                    findDis(dp, mat, i, j)
        return dp


def findDis(dp, grid, a, b):
    if dp[a][b] != float("inf"):
        return dp[a][b]
    dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    currDis = float("inf")
    dp[a][b] = -1  # this node is currently being explored
    for d in dirs:
        x, y = a + d[0], b + d[1]
        if inbounds(grid, x, y) and dp[x][y] == float("inf"):
            currDis = min(findDis(dp, grid, x, y) + 1, currDis)
        elif inbounds(grid, x, y):
            if dp[x][y] != float("inf") and dp[x][y] != -1:
                currDis = min(currDis, dp[x][y] + 1)
    dp[a][b] = currDis
    return currDis


def inbounds(grid, x, y):
    m, n = len(grid), len(grid[0])
    if 0 <= x < m and 0 <= y < n:
        return True
    return False


class Solution2:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        minDis = [[None for i in range(n)] for i in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if mat[i][j] == 0:
        #             minDis[i][j] = 0

        for i in range(m):
            for j in range(n):
                visited = set()
                dfs(minDis, mat, visited, i, j)

        minDisTwo = [[None for i in range(n)] for i in range(m)]
        count = 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if minDisTwo[i][j] == None:
                    # this means min dis for i,j has not been calculated yet
                    count += 1
                    visited = set()
                    dfs(minDisTwo, mat, visited, i, j)
        # print(minDisTwo)
        print(count)
        minDisFinal = [[None for i in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                minDisFinal[i][j] = min(minDis[i][j], minDisTwo[i][j])

        return minDisFinal


def hashed(i, j):
    return str(i) + ':' + str(j)


def dfs(minDis, mat, visited, i, j):
    print(hashed(i, j))
    visited.add(hashed(i, j))
    if mat[i][j] == 0:
        minDis[i][j] = 0
        return 0
    # if minDis[i][j] != None:
    #     return minDis[i][j]
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    minForThisCell = float("inf")
    for d in dirs:
        a, b = i + d[0], j + d[1]
        if inbounds(a, b, mat) and hashed(a, b) not in visited:
            minForThisCell = min(dfs(minDis, mat, set(visited), a, b) + 1, minForThisCell)

    if minDis[i][j] != None:
        minDis[i][j] = min(minForThisCell, minDis[i][j])
    else:
        minDis[i][j] = minForThisCell

    return minDis[i][j]


def inbounds(a, b, mat):
    m, n = len(mat), len(mat[0])
    if 0 <= a < m and 0 <= b < n:
        return True
    return False


if __name__=="__main__":
    print(Solution2().updateMatrix([[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]))