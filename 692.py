import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for w in words:
            freq[w] = 1 if w not in freq else freq[w] + 1
        l = []
        for w in freq:
            l.append(mystr(w, freq[w]))
        heapq.heapify(l)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(l).name)
        return ans


class mystr:
    def __init__(self, s, freq):
        self.name = s
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.name < other.name
        return self.freq > other.freq