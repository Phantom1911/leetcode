class Solution:
    def uniqueLetterString(self, s: str) -> int:

        hashd = dict()
        i = 0
        sums = 0
        while (i < len(s)):
            if (s[i] not in hashd):  #if this char is not in dict
                hashd[s[i]] = [0, i]   #this is the first time we encounter char, left bound is 0, right is i
            else:  # if we have seen the char before
                num = hashd[s[i]]   # we get the previous bound
                hashd[s[i]] = [num[1] + 1, i]  # we assign the new bound
                sums += (self.calc(i - num[0]) - self.calc(num[1] - num[0]) - self.calc(i - num[1] - 1))
                sums = sums % (10 ** 9 + 7)
                print(num, s[i], sums)
            i += 1

        for i in hashd:
            num = hashd[i]
            sums += (self.calc(len(s) - num[0]) - self.calc(num[1] - num[0]) - self.calc(len(s) - num[1] - 1))
            sums = sums % (10 ** 9 + 7)

        return sums

    def calc(self, n):
        ans = (n * (n + 1)) // 2
        return ans


class Solution2:
    def uniqueLetterString(self, s: str) -> int:
        dp = [[set() for i in range(len(s))] for i in range(len(s))]
        n = len(s)
        count = 0
        for i in range(n):
            dp[i][i].add(s[i])
            count += len(dp[i][i])

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j].update(dp[i][j - 1])
                if s[j] in dp[i][j - 1]:
                    dp[i][j].remove(s[j])
                else:
                    if s[j] not in s[i:j]:
                        dp[i][j].add(s[j])
                count += len(dp[i][j])

        return count


if __name__=="__main__":
    print(Solution2().uniqueLetterString("LEETCODE"))