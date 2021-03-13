# https://leetcode.com/problems/binary-tree-postorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        postorder = []
        self.traverse(root, postorder)
        return postorder

    def traverse(self, root, postorder):
        if root is None:
            return
        self.traverse(root.left, postorder)
        self.traverse(root.right, postorder)
        postorder.append(root.val)