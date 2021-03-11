# https://leetcode.com/problems/fair-candy-swap/


# let's say A gives a size candy , B gives b size candy
# Sa - a + b = Sb - b + a
class Solution:
    def fairCandySwap(self, A, B):
        Sa = sum(A)
        Sb = sum(B)
        setB = set(B)  # works without a set as well , but the lookup time is higher in that case
        for x in A:
            if x + (Sb - Sa) / 2 in setB:
                return [x, x + (Sb - Sa) / 2]