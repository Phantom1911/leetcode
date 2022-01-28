from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        dfs(graph, 0, len(graph) - 1, [], ans)
        return ans

def dfs(adjlist, currnode, dest, currpath, ans):
    if currnode == dest:
        # you have to create a copy since arrays are passed as reference (all function calls reference to same object)
        ans.append(currpath[:] + [dest])
    currpath.append(currnode)
    for child in adjlist[currnode]:
        dfs(adjlist, child, dest, currpath, ans)
    # delete what you had appended
    del currpath[-1]