# BF solution below works but gives TLE , even with memo
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        memo = {}
        return self.remove(num, k, memo)

    def remove(self, num, k, memo):
        if len(num) <= k:
            return "0"
        if k == 0:
            return num
        if num + ":" + str(k) in memo:
            return memo[num + ":" + str(k)]
        smallest = int(num)
        for i in range(len(num)):
            smallestafterremovingith = self.remove(num[0:i] + num[i + 1:], k - 1, memo)
            memo[num[0:i] + num[i + 1:] + ":" + str(k - 1)] = smallestafterremovingith
            smallest = min(int(smallestafterremovingith), smallest)

        return str(smallest)

