# https://practice.geeksforgeeks.org/problems/smallest-number-on-left3403/1#_=_
# similar to Next Greater Element , careful with indices. stack is having indices and not actual numbers
# # Refer : https://www.youtube.com/watch?v=8BDKB2yuGyg

class Solution:
    def leftSmaller(self, n, a):
        # code here
        res = [None] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and a[stack[-1]] > a[i]:
                res[stack.pop()] = a[i]
            stack.append(i)
        while stack:
            res[stack.pop()] = -1

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.leftSmaller(6,[1, 5, 0, 3, 4, 5]))