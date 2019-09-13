# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def max_in_range(nums, low, high):
            ans = -sys.maxsize-1
            for i in range(low,high+1):
                if nums[i]>ans:
                    ans=nums[i]
            return ans
        def max_tree(nums, low, high):
            if low>high:
                return None
            root_value = max_in_range(nums, low, high)
            root = TreeNode(root_value)
            root_index = nums.index(root_value, low, high+1)
            root.left = max_tree(nums, low, root_index-1)
            root.right = max_tree(nums, root_index+1, high)
            return root
        return max_tree(nums, 0, len(nums)-1)