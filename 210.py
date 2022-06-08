from typing import List

# YET TO FIGURE OUT DFS BASED SOLUTION FOR TOPOLOGICAL SORT THAT TAKES CARE OF THE CYCLES AS WELL

# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         adjlist = {i: set() for i in range(numCourses)}
#         for prereq in prerequisites:
#             src, dest = prereq[0], prereq[1]
#             adjlist[src].add(dest)
#         stack = []
#         seen = set()
#         for key in adjlist:
#             if key not in seen:
#                 dfs(adjlist, key, stack, seen)
#         # print(stack)
#         if len(stack) != numCourses:
#             return []
#         ans = []
#         while stack:
#             ans.append(stack.pop())
#         return ans
#
#
# def dfs(adjlist, node, stack, seen):
#     seen.add(node)
#     flag = True
#     for nbr in adjlist[node]:
#         if nbr not in seen:
#             dfs(adjlist, nbr, stack, seen)
#         else:
#             flag = False
#     if flag:
#         stack.append(node)

if __name__=="__main__":
    print(Solution().findOrder(2, [[1,0]]))