"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
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
