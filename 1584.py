import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        heap = []
        heapq.heappush(heap, (0, points[0]))
        seen = set()
        mstwt = 0
        while len(seen) != len(points):
            curr = heapq.heappop(heap)
            currx, curry = curr[1][0], curr[1][1]
            if hashed(currx, curry) in seen:
                continue
            mstwt += curr[0]
            seen.add(hashed(currx, curry))
            for point in points:
                if hashed(point[0], point[1]) == hashed(currx, curry):
                    continue
                if hashed(point[0], point[1]) not in seen:
                    heapq.heappush(heap, (dis(curr[1], point), point))
        return mstwt


def hashed(a, b):
    return str(a) + ":" + str(b)


def dis(pa, pb):
    ax, ay, bx, by = pa[0], pa[1], pb[0], pb[1]
    return abs(ax - bx) + abs(ay - by)

if __name__=="__main__":
    print(Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))