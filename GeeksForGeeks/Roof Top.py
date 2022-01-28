class Solution:

    # Function to find maximum number of consecutive steps
    # to gain an increase in altitude with each step.
    def maxStep(self, A, N):
        # Your code here
        currlen, maxlen = 0, 0
        for i in range(1, N):
            if A[i] > A[i - 1]:
                currlen += 1
                maxlen = max(maxlen, currlen)
            else:
                currlen = 0
        return maxlen