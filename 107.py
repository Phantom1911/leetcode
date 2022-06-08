'''

What if our dict doesn't guarantee any order? We need to maintain maxLevel in that case. Solve below:
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = dict()  # although python3 dicts are ordered, handling for dict which doesn't maintain order is done below by maintaining maxLevel
        if root is None:
            return []
        q = deque()
        q.append((root, 0))
        maxLevel = -1
        while q:
            curr = q.popleft()
            currnode, currlevel = curr[0], curr[1]
            maxLevel = max(maxLevel, currlevel)
            if currlevel not in levels:
                levels[currlevel] = []
            levels[currlevel].append(currnode.val)
            if currnode.left is not None:
                q.append((currnode.left, currlevel + 1))
            if currnode.right is not None:
                q.append((currnode.right, currlevel + 1))
        ans = [[] for i in range(maxLevel + 1)]
        for k in levels.keys():
            ans[maxLevel - k] += levels[k]
        return ans


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional, List


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = dict()  # python3 dicts are ordered
        if root is None:
            return []
        q = deque()
        q.append((root, 1))
        while q:
            curr = q.popleft()
            currnode, currlevel = curr[0], curr[1]
            if currlevel not in levels:
                levels[currlevel] = []
            levels[currlevel].append(currnode.val)
            if currnode.left is not None:
                q.append((currnode.left, currlevel + 1))
            if currnode.right is not None:
                q.append((currnode.right, currlevel + 1))
        ans = []
        for k in reversed(levels.keys()):
            ans.append(levels[k])
        return ans

