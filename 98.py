# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # for each node keep track of the max in left subtree, min in right subtree
        # val > left_subtree(max) and val < right_subtree(min)
        cmin, cmax, isBST = check(root)
        return isBST

def check(node):
    if node is None:
        return -float("inf"), float("inf"), True
    if node.left is None and node.right is None:
        return node.val, node.val, True
    if node.left is not None:
        leftMin, leftMax, isLeftBST = check(node.left)
    else:
        # choose a value of leftMax such that the comparison leftMax < node.val is always true
        # the value of leftMin doesn't matter here
        leftMin, leftMax, isLeftBST = -float("inf"), -float("inf"), True
    if node.right is not None:
        rightMin, rightMax, isRightBST = check(node.right)
    else:
        # choose a value of rightMin such that the comparison rightMin > node.val is always true
        # the value of rightMax doesn't matter here
        rightMin, rightMax, isRightBST = float("inf"), float("inf"), True
    isBST = isLeftBST and isRightBST and leftMax < node.val and rightMin > node.val
    if leftMin != -float("inf"):
        currMin = min(leftMin, node.val)
    else:
        # beware to not include infinities in min and max finding
        currMin = node.val
    if rightMax != float("inf"):
        currMax = max(rightMax, node.val)
    else:
        currMax = node.val

    return currMin, currMax, isBST


# worse solution of actually finding max and min in each subtree
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