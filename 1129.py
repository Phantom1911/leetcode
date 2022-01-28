# Dijkstra solution
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        # adj list is often more helpful than aj matrix
        redGraph = defaultdict(list)
        blueGraph = defaultdict(list)

        for edge in red_edges:
            redGraph[edge[0]].append(edge[1])

        for edge in blue_edges:
            blueGraph[edge[0]].append(edge[1])

        # print(redGraph)
        # 0 -> red
        # 1 -> blue

        q = [[0, 0, 0], [0, 0, 1]]
        ans = [[float("inf"), float("inf")] for i in range(n)]
        ans[0][0] = 0   # shortest dis to 0th node taking red edge
        ans[0][1] = 0   # shortest dis to 0th node taking blue edge

        while q:
            dist, node, color = heappop(q)

            if color:   # color 0 is red , if block is entered is color is 1
                for neighbor in blueGraph[node]:
                    if ans[neighbor][color] < dist + 1:
                        continue
                    ans[neighbor][color] = dist + 1
                    heappush(q, [dist + 1, neighbor, 0])

            else:
                # update all the neighbors of the current node
                for neighbor in redGraph[node]:
                    if ans[neighbor][color] < dist + 1:
                        continue
                    ans[neighbor][color] = dist + 1
                    heappush(q, [dist + 1, neighbor, 1])

        ans2 = []
        for i in range(n):
            curr = min(ans[i])
            if curr == float("inf"):
                ans2.append(-1)
            else:
                ans2.append(curr)

        return ans2

if __name__ == "__main__":
    print(Solution().shortestAlternatingPaths(3, [[0,1]], [[1,2]]))