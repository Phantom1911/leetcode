from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        s0, s1, seen = set(), set(), set()
        ans = True
        adjlist = {i: graph[i] for i in range(len(graph))}
        for key in adjlist:
            if key not in seen:
                ans = ans and bfs(key, adjlist, s0, s1, seen)
                if ans == False:
                    return ans
        return ans


def bfs(node, graph, s0, s1, seen):
    q = deque()
    q.append((node, 0))
    while q:
        curr = q.popleft()
        currnode, currset = curr[0], curr[1]
        if (currset == 0 and currnode in s1) or (currset == 1 and currnode in s0):
            return False
        seen.add(currnode)
        if currset == 0:
            s0.add(currnode)
        else:
            s1.add(currnode)
        nextset = 1 if currset == 0 else 0
        for nbr in graph[currnode]:
            if nbr not in seen:
                q.append((nbr, nextset))

    return True

if __name__=="__main__":
    print(Solution().isBipartite([[1,2,3],[0,3,4],[0,3],[0,1,2],[1]]))