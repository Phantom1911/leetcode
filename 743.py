import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjlist = {i: set() for i in range(n)}
        k = k - 1
        for edge in times:
            src, dest, wt = edge[0] - 1, edge[1] - 1, edge[2]
            adjlist[src].add((dest, wt))
        seen = set()
        heap = []
        heapq.heappush(heap, (0, k))

        counter = 0
        maxtime = -float("inf")
        while counter < n and heap:
            curr = heapq.heappop(heap)
            currtime, currnode = curr[0], curr[1]
            maxtime = max(maxtime, currtime)
            if currnode in seen:
                # counter+=1      --- don't increment counter here
                # we reached here this means there is a cycle
                # if we increment counter here loop will get evaluated one less time than expected and seen will have less than n elements
                continue
            seen.add(currnode)
            for edge in adjlist[currnode]:
                nbr, wt = edge[0], edge[1]
                nexttime = currtime + wt
                if nbr not in seen:
                    heapq.heappush(heap, (nexttime, nbr))
            counter += 1
        if len(seen) != n:
            return -1
        return maxtime


if __name__=="__main__":
    print(Solution().networkDelayTime([[1,2,1],[2,3,7],[1,3,4],[2,1,2]],3,1))