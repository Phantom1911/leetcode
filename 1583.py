# refer : https://www.youtube.com/watch?v=10laHayu2dc
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        d = {i: set() for i in range(n)}
        currPairs = {i: None for i in range(n)}
        # count = 0
        for p in pairs:
            n1, n2 = p[0], p[1]
            currPairs[n1] = n2
            currPairs[n2] = n1
        # print(currPairs)
        for i in range(n):
            preference = preferences[i]  # preference of ith person
            currentlyPairedWith = currPairs[i]
            j = 0
            while preference[j] != currentlyPairedWith:
                d[i].add(preference[j])
                j += 1
        # print(d)
        unhappy = set()
        for key in d:
            for val in d[key]:
                if key in d[val]:
                    unhappy.add(key)  # we can't simply have a count here, because that can result
                    # in the same person being counted multiple times
                    # so we maintain a set of unhappy people
                    '''
                    refer ex:
                    Input: n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]
                    Output: 4
                    '''
        return len(unhappy)
