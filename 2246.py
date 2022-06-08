from collections import defaultdict
# from functools import cache
from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:

        n = len(s)
        adj = defaultdict(list)

        # build a graph
        for i, p in enumerate(parent):

            if p == -1:
                pass
            else:
                adj[i].append(p)
                adj[p].append(i)


        def dfs(node, prev=None):

            # check different adjacent characters
            if prev is not None and s[node] == s[prev]:
                return 0

            paths = [dfs(nbor, node) for nbor in adj[node] if nbor != prev]
            return 1 + max(paths, default=0)

        return max([dfs(i) for i in range(n)])

if __name__=="__main__":
    print(Solution().longestPath([-1,0,0,1,1,2], "abacbe"))