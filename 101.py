# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check_sym(left, right):
            if left is None and right is not None:
                return False
            elif left is not None and right is None:
                return False
            elif left is None and right is None:
                return True
            else:
                if left.val != right.val:
                    return False
                return check_sym(left.left,right.right) and check_sym(left.right,right.left)
        if root is None:
            return True
        else:
            return check_sym(root.left,root.right)