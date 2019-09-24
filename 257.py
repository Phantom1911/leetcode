class Solution:
    def binaryTreePathsRec(self, root, current, paths):
        if not root:
            return

        current.append(root.val)

        if not root.left and not root.right:
            # leaf
            paths.append(current[:])
            current.pop()
            return

        self.binaryTreePathsRec(root.left, current, paths)
        self.binaryTreePathsRec(root.right, current, paths)
        current.pop()

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        self.binaryTreePathsRec(root, [], paths)

        return ['->'.join(str(num) for num in path) for path in paths]