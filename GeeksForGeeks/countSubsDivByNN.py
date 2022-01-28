class Solution:
    def countDivisibleSubseq(self, s, N):
        memo = {}
        s = str(s)
        return getcount(s, 0, 0, N, memo) - 1


def getcount(s, idx, rem, k, memo):
    n = len(s)
    if idx == n:
        return 1 if rem == 0 else 0
    if hashed(idx, rem) in memo:
        return memo[hashed(idx, rem)]
    count = 0
    count += getcount(s, idx + 1, rem, k, memo)
    count += getcount(s, idx + 1, (rem * 10 + int(s[idx])) % k, k, memo)

    memo[hashed(idx, rem)] = count
    return count


def hashed(a, b):
    return str(a) + ":" + str(b)

if __name__=="__main__":
    print(Solution().countDivisibleSubseq(330,6))