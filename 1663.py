# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ""
        for i in range(n):
            res += 'a'
            k -= 1

        for i in range(n - 1, -1, -1):
            if k >= 25:
                res = res[:i] + 'z' + res[i + 1:]
                k -= 25
            else:
                ascii_char = chr(k + 97)
                res = res[:i] + ascii_char + res[i + 1:]
                k = 0
            if k == 0:
                break
        return res