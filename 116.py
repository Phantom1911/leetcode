"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# the below is a bad solution since it uses extra space. There is an intelligent recursive way to do this after this solution

from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        curr_level = deque([root])
        next_level = deque([])
        prev = None
        while True:
            curr_node = curr_level.popleft()
            while curr_node:
                if curr_node.left:
                    next_level.append(curr_node.left)
                if curr_node.right:
                    next_level.append(curr_node.right)
                if curr_level:
                    curr_node.next = curr_level.popleft()
                curr_node = curr_node.next
            curr_level = next_level
            next_level = deque([])
            if not curr_level:
                break
        return root

# the intelligent recursive way

def connectNodes(left, right):
    if left is not None or right is not None:
        left.next = right
        connectNodes(left.right, right.left)
    if left is not None:
        connectNodes(left.left, left.right)
    if right is not None:
        connectNodes(right.left, right.right)


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None: return root
        connectNodes(root.left, root.right)
        return root
