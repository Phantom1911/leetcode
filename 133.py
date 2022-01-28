# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    def __repr__(self):
        return f"{self.val}"

from collections import deque

class Solution:
    def cloneGraph(self, node):
        q = deque()
        q.append(node)
        clonemap = {}
        while len(q) != 0:
            curr = q.popleft()
            currclone = Node(curr.val)
            clonemap[curr] = currclone
            for nbr in curr.neighbors:
                if nbr not in clonemap:
                    q.append(nbr)
        q2 = deque()
        q2.append(node)
        seen = set()
        while len(q2) != 0:
            curr = q2.popleft()
            currclone = clonemap[curr]
            if currclone in seen:
                continue
            clonenbrs = []
            for nbr in curr.neighbors:
                clonenbrs.append(clonemap[nbr])
                q2.append(nbr)
            # all neighbors of currclone have been explored so lets add it to seen
            seen.add(currclone)
            currclone.neighbors = clonenbrs

        return clonemap[node]

if __name__=="__main__":
    four = Node(4)
    three = Node(3)
    two = Node(2)
    one = Node(1)

    fournbrs = [one, three]

    threenbrs = [four, two]

    twonbrs = [three, one]

    onenbrs = [two, four]
    one.neighbors = onenbrs
    two.neighbors = twonbrs
    three.neighbors = threenbrs
    four.neighbors = fournbrs

    print(Solution().cloneGraph(one))