# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return the root node in the tree
    def solve(self, A, B):
        return self.impose(A, B)


    def impose(A, B):
        ans = TreeNode(-1)
        if A is None and B is not None:
            return TreeNode(B.val)
        elif A is not None and B is None:
            return TreeNode(A.val)
        elif A is not None and B is not None:
            ans.val = A.val + B.val
            ans.left = A.impose(A.left, B.left)
            ans.right = A.impose(A.right, B.right)
            return ans
        return None
