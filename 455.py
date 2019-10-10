from heapq import _heapify_max, _heappop_max


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(g) == 0 or len(s) == 0: return 0
        _heapify_max(g)
        _heapify_max(s)
        greed, size, count = _heappop_max(g), _heappop_max(s), 0
        while True:
            if size >= greed:
                count += 1
                if len(s) == 0: return count
                size = _heappop_max(s)
            if len(g) == 0: return count
            greed = _heappop_max(g)
