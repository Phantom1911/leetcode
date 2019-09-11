import heapq


class Solution:
    def nthSuperUglyNumber(self, n: int, p: List[int]) -> int:
        N, m, S = [1], 1, set()
        for _ in range(n):
            while m in S: m = heapq.heappop(N)
            print(m)
            S.add(m)
            for i in p: heapq.heappush(N, i * m)

        return m
