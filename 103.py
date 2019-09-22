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