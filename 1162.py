from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = deque()
        m, n = len(grid), len(grid[0])
        dis = [[float("inf") for i in range(n)] for i in range(m)]
        onePresent = False
        zeroPresent = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dis[i][j] = 0
                    q.append((i, j))
                    onePresent = True
                else:
                    zeroPresent = True
        if not onePresent:
            return -1
        if not zeroPresent:
            return -1

        while q:
            curr = q.popleft()
            i, j = curr[0], curr[1]
            dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for d in dirs:
                a, b = i + d[0], j + d[1]
                if inbounds(a, b, m, n) and dis[a][b] > dis[i][j] + 1:
                    dis[a][b] = dis[i][j] + 1
                    q.append((a, b))
        maxMinDis = -float("inf")
        for i in range(m):
            for j in range(n):
                if dis[i][j] > maxMinDis and grid[i][j] == 0:
                    maxMinDis = dis[i][j]
        return maxMinDis


def inbounds(a, b, m, n):
    if 0 <= a < m and 0 <= b < n:
        return True
    return False