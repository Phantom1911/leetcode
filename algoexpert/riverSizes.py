def riverSizes(matrix):
    ans = []
    # Write your code here.
    n = len(matrix)
    m = len(matrix[0])
    visited = [[False for i in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            currSize = dfs(matrix, i, j, visited)
            if currSize > 0:
                ans.append(currSize)
    return ans


def dfs(matrix, row, col, visited):
    n = len(matrix)
    m = len(matrix[0])
    if row >= n or row < 0 or col >= m or col < 0:
        return 0
    if visited[row][col] == True:
        return 0
    visited[row][col] = True
    if matrix[row][col] != 1:
        return 0

    currSize = dfs(matrix, row - 1, col, visited) + dfs(matrix, row + 1, col, visited) + dfs(matrix, row, col - 1,
                                                                                             visited) + dfs(matrix, row,
                                                                                                            col + 1,
                                                                                                            visited) + 1
    return currSize


pass
