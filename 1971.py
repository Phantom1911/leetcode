class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjlist = {i: set() for i in range(n)}
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            adjlist[n1].add(n2)
            adjlist[n2].add(n1)
        flag = [False]
        dfs(adjlist, source, destination, flag, set())
        return flag[0]


def dfs(adjlist, node, dest, flag, seen):
    if node == dest:
        flag[0] = True
        return
    seen.add(node)
    for child in adjlist[node]:
        if child not in seen:
            dfs(adjlist, child, dest, flag, seen)
