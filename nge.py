class Solution:

    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr, n):
        # code here
        stack = []
        res = [-1] * n
        for i in range(n):
            if len(stack) == 0:
                stack.append(i)
            else:
                while len(stack) != 0 and arr[stack[-1]] < arr[i]:
                    res[stack[-1]] = arr[i]
                    stack.pop()
                stack.append(i)

        while len(stack) != 0:
            res[stack.pop()] = -1

        return res

if __name__ =="__main__":
    print(Solution().nextLargerElement([1,3,2,4],4))