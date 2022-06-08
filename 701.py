# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
        
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        prev, curr, lastMove = None, root, -1
        while curr is not None:
            if val > curr.val:
                prev = curr
                curr = curr.right
                lastMove = 1
            else:
                prev = curr
                curr = curr.left
                lastMove = 0
        if lastMove == 0:
            prev.left = TreeNode(val)
        else:
            prev.right = TreeNode(val)

        return root