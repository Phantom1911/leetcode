# https://leetcode.com/problems/binary-tree-preorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        preorder = []
        self.traverse(root, preorder)
        return preorder

    def traverse(self, root, preorder):
        if root is None:
            return
        preorder.append(root.val)
        self.traverse(root.left, preorder)
        self.traverse(root.right, preorder)