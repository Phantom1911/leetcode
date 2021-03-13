# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        inorder = []
        self.traverse(root, inorder)
        return inorder

    def traverse(self, root, inorder):
        if root is None:
            return
        self.traverse(root.left, inorder)
        inorder.append(root.val)
        self.traverse(root.right, inorder)