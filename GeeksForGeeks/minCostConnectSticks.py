
'''
Note: WHY BELOW SOLUTION DOESN'T WORK AND IS WRONG LOGICALLY?

ex : 16,23,32,36
this solution would suggest a joining sequence as follows:

36 -- (32 -- (16 -- 23))   which gives 217 and is wrong

correct sequence is 16 -- 23 => gives new rope of length 39
[39,32,36] are new ropes
now join 32 -- 36 =>
next join 39 and 68
gives cost of 214
'''

from typing import (
    List,
)

# WRONG SOLUTION

# class Solution:
#     """
#     @param sticks: the length of sticks
#     @return: Minimum Cost to Connect Sticks
#     """
#
#     def minimum_cost(self, sticks: List[int], costMap) -> int:
#         # write your code here
#         if len(sticks) == 2:
#             return sticks[0] + sticks[1]
#         if tuple(sticks) in costMap:
#             return costMap[tuple(sticks)]
#         # choose an index one by one to remove
#         minCost = float("inf")
#         totalSum = sum(sticks)
#         for i in range(len(sticks)):
#             currlen = sticks[i]
#             roa = sticks[:i] + sticks[i+1:]
#             restMinCost = self.minimum_cost(roa, costMap)
#             restLen = totalSum - sticks[i]
#             currCost = currlen + restLen + restMinCost
#             minCost = min(currCost, minCost)
#         # print(sticks)
#         # print("mincost " + str(minCost))
#         costMap[tuple(sticks)] = minCost
#         return minCost

if __name__=="__main__":
    costMap = {}
    print(Solution().minimum_cost([23, 16, 36, 32], costMap))
    print(costMap)