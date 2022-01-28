from collections import deque


def pathexists(src, dest, adjlist):
    q = deque()
    q.append(src)
    seen = set()
    seen.add(src)
    while q:
        curr = q.pop()
        children = adjlist[curr]
        if dest in children:
            return True
        for child in children:
            if child not in seen:
                q.append(child)
                seen.add(child)

    return False


class Solution:
    def canReach(self, arr, start):
        adjlist = {}
        n = len(arr)
        for i in range(n):
            adjlist[i] = set()
        for i, x in enumerate(arr):
            afterjumpnode = i + x
            if i + x <= n - 1:
                adjlist[i].add(afterjumpnode)
            afterjumpnode = i - x
            if i - x >= 0:
                adjlist[i].add(afterjumpnode)

        for i in range(0, n, 1):
            if i == start:
                continue
            if arr[i] == 0 and not pathexists(start, i, adjlist):
                return False

        return True
if __name__=="__main__":
    print(Solution().canReach([3,0,2,1,2],2))