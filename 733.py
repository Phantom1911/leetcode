class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        dfs(image, sr, sc, image[sr][sc], newColor, set())
        return image
    
def dfs(grid, i, j, oldcolor, newcolor, seen):
    grid[i][j] = newcolor
    seen.add(hashed(i, j))
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for d in dirs:
        a, b = i + d[0], j + d[1]
        if inbounds(grid, a, b) and hashed(a, b) not in seen and grid[a][b] == oldcolor:
            dfs(grid, a, b, oldcolor, newcolor, seen)


def hashed(a, b):
    return str(a) + ":" + str(b)


def inbounds(grid, a, b):
    m, n = len(grid), len(grid[0])
    if 0 <= a < m and 0 <= b < n:
        return True
    return False