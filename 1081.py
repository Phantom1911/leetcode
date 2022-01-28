# the below solution is for smallest substring which contains all distinct characters of string
# need to change this to work for smallest subsequence which contains all distinct characters of string

from collections import defaultdict
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        discount = 0
        diseles = set()
        for i in range(len(s)):
            if s[i] not in diseles:
                discount += 1
                diseles.add(s[i])
        currdistinct = 0
        start = 0
        currcount = defaultdict(lambda: 0)
        minsize, minwindows = len(s), []
        for end in range(len(s)):
            currcount[s[end]] += 1
            if currcount[s[end]] == 1:
                currdistinct += 1
            if currdistinct == discount:
                while currcount[s[start]] > 1:
                    currcount[s[start]] -= 1
                    start += 1
                if end - start + 1 == minsize:
                    minwindows.append(s[start:end + 1])
                elif end - start + 1 < minsize:
                    minwindows = [s[start:end + 1]]
                    minsize = end - start + 1

        return(sorted(minwindows))

if __name__=="__main__":
    print(Solution().smallestSubsequence("cbacdcbc"))