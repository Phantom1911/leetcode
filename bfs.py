from collections import deque


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
        q = deque()
        q.append(self)
        while any(q):
            curr = q.popleft()
            array.append(curr.val)
            for c in curr.children:
                q.append(c)
        return array
