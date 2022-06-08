# gives TLE
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        possibleStarts = set()
        for i in range(len(cost)):
            if gas[i] >= cost[i]:
                possibleStarts.add(i)
        n = len(cost)
        for s in possibleStarts:
            currTank = 0
            # take the first move
            currTank = gas[s] - cost[s]
            i = (s + 1) % n
            while i != s:
                currTank += gas[i]
                if currTank < cost[i]:
                    break
                else:
                    # make the move
                    currTank -= cost[i]
                i = (i + 1) % n
            if i == s:
                return s
        return -1
