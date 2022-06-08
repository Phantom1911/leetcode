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


# accepted solution - but still pretty bad runtime

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"
        if k == 0:
            return num
        originalLen = len(num)

        # we want to remove the first occurence of any i where i > i+1 in num and then recursively remove k-1 digits
        for i in range(len(num) - 1):
            if int(num[i]) > int(num[i + 1]):
                num = num[:i] + num[i + 1:]
                num = self.removeKdigits(num, k - 1)
                break

        # simply remove from the end if we were not able to remove required num of elements
        # this is because these elements must be forming an increasing sequence
        # since we already checked if they were forming decreasing sequence - and they were not
        if k - (originalLen - len(num)) != 0:
            toRemove = k - (originalLen - len(num))
            return num[:len(num) - toRemove]

        # to handle case like num = 10200 this double typecasting is required
        return str(int(num))

# monotonic stack based solution -- Accepted

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        removed = 0
        n = len(num)
        if n <= k:
            return "0"
        stack.append(num[0])
        for i in range(1, n):
            if stack:
                while stack and stack[-1] > num[i] and removed < k:
                    removed += 1
                    stack.pop()
                stack.append(num[i])
            else:
                stack.append(num[i])

        ans = ''.join(stack)
        if ans == "":
            return "0"
        ans = str(int(ans))
        if removed < k:
            toRemove = k - removed
            if toRemove >= len(ans):
                return "0"
            return ans[:len(ans) - toRemove]
        return ans

