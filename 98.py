# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        def maxInTree(root):
            if root is None:
                return -sys.maxsize
            max_val = root.val
            max_val = max(maxInTree(root.left),maxInTree(root.right),max_val)
            return max_val
        def minInTree(root):
            if root is None:
                return sys.maxsize
            min_val = root.val
            min_val = min(minInTree(root.left),minInTree(root.right),min_val)
            return min_val
        if maxInTree(root.left) < root.val < minInTree(root.right) and self.isValidBST(root.left) and self.isValidBST(root.right):
            return True
        else:
            return False