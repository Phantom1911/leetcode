class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        n = len(binary)
        dp = [0 for i in range(n)]
        dp[0] = 1
        # dp[i] signifies the number of good subsequences in string 0 .. i

        # dp[j] for j < i denotes all the subsequences for string 0 .. j
        # now if we add binnary[i] to all those 'good' subsequnces, do they still remain good?
        # any character added to a good subsequence will result in a good subsequence, unless the good subsequence is '0'  (00 and 01 are both bad subsequences)

        # zeroFound[i] denotes if str 0 .. i contains '0' good subsequence
        zeroFound = [False for i in range(n)]
        self.populateZeroFound(zeroFound, binary)

        for i in range(1, n):
            for j in range(0, i):
                dp[i] += dp[j]
                if (zeroFound[j]):
                    dp[i] -= 1
        print(dp)
        return dp[n - 1]

    def populateZeroFound(self, zeroFound, binary):
        zeroFound[0] = True if binary[0] == 0 else False
        for i in range(1, len(binary)):
            zeroFound[i] = zeroFound[i - 1] or binary[i] == '0'
        return zeroFound

if __name__ == "__main__":
    print(Solution().numberOfUniqueGoodSubsequences("000"))