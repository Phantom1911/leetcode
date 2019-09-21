class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None or root.left is None and root.right is None:
            return 0
        def traversal(root):
            if root is None:
                return 0
            if root.left is not None and root.left.left is None and root.left.right is None:
                return root.left.val + traversal(root.right)
            return traversal(root.left) + traversal(root.right)
        return traversal(root)