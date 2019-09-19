from collections import Counter

def longestPalindrome(self, s):
    ans = 0
    for v in Counter(s).values():
        ans += v // 2 * 2
        if ans % 2 == 0 and v % 2 == 1:
            ans += 1
    return ans