# need to optimize this, giving TLE


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        maximum = -float("inf")
        n = len(A)
        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if is_valid_triplet(A, i, j, k):
                        maximum = max(maximum, A[i] + A[j] + A[k])
        return maximum


def is_valid_triplet(A, i, j, k):
    return A[i] < A[j] < A[k]