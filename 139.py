# Word Break

# NON OPTIMAL SOLUTION USING RECURSION , SHOULD BE OPTIMIZED USING DP

class Solution1:
    def wordBreak(self, s, wordDict):
        return canBeBroken(s, wordDict)


def canBeBroken(s, dictionary):
    if s in dictionary:
        return True
    n = len(s)
    for end in range(0, n - 1):
        if s[0:end + 1] in dictionary and canBeBroken(s[end + 1:n], dictionary):
            return True
    return False

# NON OPTIMAL SOLUTION 2 , GIVES TLE

class Solution2:
    def wordBreak(self, s, wordDict):
        if s in wordDict:
            return True
        n = len(s)
        flag = False
        for i in range(n):
            temp_str = s[0:i+1]
            if temp_str in wordDict :
                flag = self.wordBreak(s[i+1:], wordDict)
            if flag == True:
                break
        return flag


# DP SOLUTION

class Solution3:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n
        for i in range(n):
            if dp[i] == False and s[0:i+1] in wordDict:
                dp[i] = True
            if dp[i] == True:
                if i == n-1:
                    return True
                for j in range(i+1, n):
                    if dp[j] == False and s[i+1: j+1] in wordDict:
                        dp[j] = True
                    if j == n-1 and dp[j] == True:
                        return True
        return False

if __name__ == "__main__":
    s2 = Solution2()
    print(s2.wordBreak("abcd", ["a","abc","b","cd"]))