# same as : https://www.lintcode.com/problem/645/

"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""


class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        m = {}
        for i in range(n):
            m[i] = set()
            for j in range(n):
                if i == j:
                    continue
                if Celebrity.knows(i, j):
                    m[i].add(j)

        possible = -1
        for key in m:
            if len(m[key]) == 0:
                possible = key
        for key in m:
            if key == possible:
                continue
            if possible not in m[key]:
                return -1
        return possible