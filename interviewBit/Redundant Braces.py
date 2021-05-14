# https://www.interviewbit.com/problems/redundant-braces/#

class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        n = len(A)
        stack = []
        push_chars = ['(','+','-','/','*']
        for i in range(n):
            if A[i] in push_chars:
                stack.append(A[i])
            elif A[i] == ')':
                if stack[-1] == '(':
                    return 1
                while stack and stack[-1] != '(':
                    stack.pop()
                stack.pop()
        return 0