# wrong logic below

# from collections import deque
# from typing import List
#
#
# class Solution:
#     def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
#         m, n = len(dungeon), len(dungeon[0])
#         disMatrix = [[float("inf") for i in range(n)] for i in range(m)]
#         q = deque()
#         q.append([0, 0, 0])
#         while q:
#             curr = q.popleft()
#             i, j,currDis = curr[0], curr[1], curr[2]
#             disMatrix[i][j] = min(currDis - dungeon[i][j], disMatrix[i][j])
#             if inbounds(i + 1, j, m, n):
#                 q.append([i + 1, j, disMatrix[i][j]])
#             if inbounds(i, j + 1, m, n):
#                 q.append([i, j + 1, disMatrix[i][j]])
#         # print(disMatrix)
#         return disMatrix[m - 1][n - 1] + 1
#
#
# def inbounds(i, j, m, n):
#     if 0 <= i < m and 0 <= j < n:
#         return True
#     return False
#
#
# if __name__=="__main__":
#     print(Solution().calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))