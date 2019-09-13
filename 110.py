# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))

        def check_balanced(root):
            if not root:
                return BalancedStatusWithHeight(True, -1)
            if root.left is None and root.right is None:
                return BalancedStatusWithHeight(True, 0)
            left_res = check_balanced(root.left)
            if not left_res.balanced:
                return BalancedStatusWithHeight(False, 0)
            right_res = check_balanced(root.right)
            if not right_res.balanced:
                return BalancedStatusWithHeight(False, 0)
            is_balanced = abs(left_res.height - right_res.height) <= 1
            print(is_balanced)
            height = max(left_res.height, right_res.height) + 1
            return BalancedStatusWithHeight(is_balanced, height)

        return check_balanced(root).balanced
