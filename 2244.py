from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = Counter(tasks)
        ans = 0
        memo = {}
        for key in count:
            ans += getRounds(count[key], memo)
        if ans == float("inf"):
            return -1
        return ans


def getRounds(n, memo):
    if n <= 1:
        return float("inf")
    if n == 3 or n == 2:
        return 1
    if n in memo:
        return memo[n]
    a = getRounds(n - 3, memo)
    b = getRounds(n - 2, memo)
    ans = min(a, b) + 1
    memo[n] = ans
    return ans

if __name__=="__main__":
    print(Solution().minimumRounds([2,2,3,3,2,4,4,4,4,4]))