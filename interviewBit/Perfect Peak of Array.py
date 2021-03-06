# https://www.interviewbit.com/problems/perfect-peak-of-array/

# create two helper arrays
# maxi [i] = max till now, ie max in 0....i , i inclusive
# mini[i] = min in [i ... n-1]

class Solution:
    # @param A : list of integers
    # @return an integer
    def perfectPeak(self, A):
        n = len(A)
        maxi = [None] * n
        maxi[0] = A[0]

        mini = [None] * n
        mini[n - 1] = A[n - 1]
        # create maxi and mini
        for i in range(1, n):
            maxi[i] = max(maxi[i - 1], A[i])

        for i in range(n - 2, -1, -1):
            mini[i] = min(mini[i + 1], A[i])

        # now traverse the array
        # if A[i] > maxi[i-1] and A[i] < mini[i+1] then its the ans
        for i in range(1, n - 1):
            if A[i] > maxi[i - 1] and A[i] < mini[i + 1]:
                return 1

        return 0

