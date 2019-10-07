from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        x = Counter(arr)
        s = set(x.values())
        if len(x) == len(s):
            return True
        return False