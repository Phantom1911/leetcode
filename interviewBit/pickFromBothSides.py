
# THIS IS A WRONG SOLUTION. THE CORRECT SOLVE IS YET TO BE FIGURED OUT.

# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
#         n = len(A)
#         if B > len(A):
#             return None
#         if B == len(A):
#             return self.arr_sum(A)
#         maximum = 0
#         left = 0
#         right = n - 1
#         i = 0
#         while left <= right and i < B:
#             greater = max(A[left], A[right])
#             if greater == A[left]:
#                 left += 1
#             elif greater == A[right]:
#                 right -= 1
#             maximum = greater + maximum
#             i+=1
#
#         return maximum
#
#     def arr_sum(A):
#         s = 0
#         for i in range(0, len(A)):
#             s += A[i]
#         return s
#
# if __name__ == "__main__":
#     s = Solution()
#     print(s.solve([5,-2,3,1,2], 3))
