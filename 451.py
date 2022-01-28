import heapq
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        h = []
        for key in c:
            heapq.heappush(h,(-c[key], key))
        ans = ""
        while h:
            curr = heapq.heappop(h)
            count , ele = -curr[0] , curr[1]
            for i in range(count):
                ans+= ele
        return ans