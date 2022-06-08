from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dis = [[float("inf") for i in range(n)] for i in range(m)]
        q = deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # make the dis of all 1s belonging to this island as 0
                    dfs(i, j, grid, q, visited, dis)
                    break

        # visited set is holding all the 1s which form this island
        # now all 1s that form an island are in the queue
        while q:
            curr = q.popleft()
            i, j = curr[0], curr[1]
            dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for d in dirs:
                a, b = i + d[0], j + d[1]
                if inbounds(a, b, m, n) and dis[a][b] > dis[i][j] + 1:
                    dis[a][b] = dis[i][j] + 1
                    q.append((a, b))

        minDis = float("inf")
        for i in range(m):
            for j in range(n):
                if hashed(i, j) not in visited and grid[i][j] == 1 and dis[i][j] < minDis:
                    minDis = dis[i][j]
        return minDis


def hashed(i, j):
    return str(i) + ':' + str(j)


def inbounds(a, b, m, n):
    if 0 <= a < m and 0 <= b < n:
        return True
    return False


def dfs(i, j, grid, q, visited, dis):
    m, n = len(grid), len(grid[0])
    dis[i][j] = 0
    visited.add(hashed(i, j))
    q.append((i, j))
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for d in dirs:
        a, b = i + d[0], j + d[1]
        if inbounds(a, b, m, n) and grid[a][b] == 1:
            dfs(a, b, grid, q, visited, dis)

if __name__=="__main__":
    print(Solution().shortestBridge([[0,1],[1,0]]))