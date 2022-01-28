class Solution:
    def longestPrefix(self, s: str) -> str:
        lps = getlps(s)
        return s[:lps[-1]]


def getlps(s):
    n = len(s)
    lps = [0 for i in range(n)]
    for i in range(1, n, 1):
        j = lps[i - 1]
        while j > 0 and s[i] != s[j]:
            j = lps[j - 1]
        if s[i] == s[j]:
            j += 1
        lps[i] = j
    return lps






if __name__=="__main__":
    print(Solution().longestPrefix("ababab"))