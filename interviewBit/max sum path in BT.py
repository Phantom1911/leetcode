# https://www.interviewbit.com/problems/max-sum-path-in-binary-tree/

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxPathSum(self, A):
        res = [-float("inf")]
        self.maxPath(A, res)
        return res[0]
    def maxPath(self, A, res):
        if A is None:
            return 0
        lmbs = self.maxPath(A.left, res)
        rmbs = self.maxPath(A.right, res)
        current = max(lmbs+A.val, rmbs+A.val, lmbs, rmbs, A.val, lmbs+rmbs+A.val)
        res[0] = max(res[0], current)
        return current

if __name__=="__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    s = Solution()
    print(s.maxPathSum(root))