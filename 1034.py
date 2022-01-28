class Solution:
    def colorBorder(self, grid, row: int, col: int, color: int) :
        componentColor = grid[row][col]
        seen,borders = set(),[]
        dfs(grid, row, col, seen, componentColor, color,borders)
        for border in borders:
            unhashed = unhash(border)
            grid[int(unhashed[0])][int(unhashed[1])] = color

        return grid

def unhash(s):
    return s.split(":")

def dfs(grid,row,col,seen,componentColor,color,borders):
    dirs = [[0,1],[1,0],[0,-1],[-1,0]]
    if isborder(grid,row,col,componentColor):
        borders.append(hashed(row,col))
    seen.add(hashed(row,col))
    for dire in dirs:
        a,b = row+dire[0],col+dire[1]
        if safe(grid,a,b,componentColor,seen):
            dfs(grid,a,b,seen,componentColor,color,borders)

def isborder(grid,row,col,componentColor):
    m,n = len(grid), len(grid[0])
    dirs = [[0,1],[1,0],[0,-1],[-1,0]]
    for dire in dirs:
        a,b = row+dire[0],col+dire[1]
        if a >= m or b >= n or a<0 or b<0 or grid[a][b] != componentColor:
            return True

    return False

def safe(grid, a, b, componentColor,seen):
    m, n = len(grid), len(grid[0])
    return True if a < m and b < n and a>=0 and b>=0 and grid[a][b] == componentColor and hashed(a,b) not in seen else False


def hashed(row,col):
    return str(row)+":"+str(col)

if __name__=="__main__":
    print(Solution().colorBorder([[1,2,1,2,1,2],[2,2,2,2,1,2],[1,2,2,2,1,2]],1,3,1))