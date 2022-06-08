class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m, n = len(isConnected), len(isConnected[0])
        adjlist = {}
        for i in range(m):
            for j in range(n):
                if isConnected[i][j] == 1:
                    if i not in adjlist:
                        adjlist[i] = []
                    adjlist[i].append(j)
        seen = set()
        ans = 0
        for node in adjlist:
            if node not in seen:
                ans += 1
                dfs(adjlist, node, seen)
        return ans


def dfs(adjlist, node, seen):
    seen.add(node)
    for nbr in adjlist[node]:
        if nbr not in seen:
            dfs(adjlist, nbr, seen)