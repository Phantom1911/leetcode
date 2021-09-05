class Solution:
    def numIslands(self, grid):
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


if __name__=="__main__":
    print(Solution().numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))