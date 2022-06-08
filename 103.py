# optimal mainstack and childstack solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        mainStack, childStack = [], []
        mainStack.append(root)
        ltor = True
        ans = []
        while True:
            currlevel = []
            while mainStack:
                curr = mainStack.pop()
                currlevel.append(curr.val)
                if ltor:
                    if curr.left:
                        childStack.append(curr.left)
                    if curr.right:
                        childStack.append(curr.right)
                else:
                    if curr.right:
                        childStack.append(curr.right)
                    if curr.left:
                        childStack.append(curr.left)
            ans.append(currlevel)
            mainStack = childStack
            childStack = []
            ltor = not ltor
            if not mainStack:
                break

        return ans


# below is bad approach

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = deque([(root, 1)])
        levelOrder = {}
        while queue:
            current_node , level = queue.popleft()
            if level not in levelOrder:
                levelOrder[level] = [current_node.val]
            else:
                levelOrder[level].append(current_node.val)
            if current_node.left is not None:
                queue.append((current_node.left, level+1))
            if current_node.right is not None:
                queue.append((current_node.right, level+1))
        ans = []
        for level in levelOrder:
            if level % 2 == 0:
                ans.append(levelOrder[level][::-1])
            else:
                ans.append(levelOrder[level])
        return ans