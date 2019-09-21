class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None or root.children is None:
            return 0
        maxd = 0
        for child in root.children:
            maxd = max(maxd, self.maxDepth(child))
        return 1+maxd