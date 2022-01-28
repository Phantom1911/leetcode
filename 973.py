import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for i in range(k):
            heapq.heappush(h, (-dis(points[i]), points[i]))
        # for minheap to function as maxheap, negate the elements while inserting
        # peek the top element of the heap by using h[0] -- 0th index
        for i in range(k, len(points), 1):
            if abs(h[0][0]) > dis(points[i]):
                heapq.heappushpop(h, (-dis(points[i]), points[i]))
        ans = []
        while h:
            ans.append(heapq.heappop(h)[1])
        return ans


def dis(p):
    return p[0] ** 2 + p[1] ** 2
