import heapq
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # write your code here
        # we would need a max heap for this question
        heap = []
        heapq.heappush(heap, (-1, start))  # (currprob, currnode)
        seen = set()
        # probability = {i : 0 for i in range(n)}
        # probability[start] = 1
        ans = 0
        adjlist = {i: set() for i in range(n)}
        for i in range(len(edges)):
            edge = edges[i]
            n1, n2 = edge[0], edge[1]
            prob = succProb[i]
            adjlist[n1].add((n2, prob))
            adjlist[n2].add((n1, prob))

        while len(seen) != n:
            curr = heapq.heappop(heap)
            currprob, currnode = curr[0], curr[1]
            if curr in seen:
                continue
            if currnode == end:
                ans = -currprob
                break
            seen.add(currnode)
            for edge in adjlist[currnode]:
                nbr, edgeprob = edge[0], edge[1]
                nextprob = edgeprob * -currprob
                if nbr not in seen:
                    heapq.heappush(heap, (-nextprob, nbr))
        return ans

if __name__=="__main__":
    print(Solution().maxProbability(3,[[0,1],[1,2],[0,2]],[0.5,0.5,0.2],0,2))