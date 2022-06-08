from collections import Counter
from math import ceil
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = Counter(answers)
        ans = 0
        for key in c:
            groupSize = key + 1
            if key == 0:
                ans += c[key]
            else:
                val = ceil(c[key] / groupSize) * groupSize
                ans += val

        return ans