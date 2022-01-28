class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, x, y):
            if x>=0 and x<len(grid) and y>=0 and y<len(grid[0]) and grid[x][y] != '0':
                grid[x][y] = '0'
                for i,j in [[-1,0],[0,1],[1,0],[0,-1]]:
                    dfs(grid, x+i, y+j)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i,j)
                    ans +=1
        return ans


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1

        return count


def dfs(grid, i, j):
    m, n = len(grid), len(grid[0])
    moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    for move in moves:
        a, b = i + move[0], j + move[1]
        if inbounds(a, b, m, n) and grid[a][b] == '1':
            grid[a][b] = '0'
            dfs(grid, a, b)


def inbounds(a, b, m, n):
    return True if 0 <= a < m and 0 <= b < n else False