# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"

# unoptimized solution. instead of keeping track of all the elements in the path, we can just keep track of max so far in the path and compare
# current element with max so far

class Solution:
    def goodNodes(self, root: TreeNode):
        goodnodes = []
        self.dfs(root, root, [], goodnodes)
        for n in goodnodes:
            print(n.val)
        return len(goodnodes)

    # the node needs to be max in the path from root to node
    def dfs(self, root, node, path, goodnodes):
        if node is None:
            return
        if self.ismaxinpath(path, node):
            goodnodes.append(node)
        path.append(node)
        self.dfs(root, node.left, path[:], goodnodes)
        self.dfs(root, node.right, path[:], goodnodes)

    def ismaxinpath(self, path, node):
        for i in range(len(path)):
            if path[i].val > node.val:
                return False
        return True

if __name__=="__main__":
    four2 = TreeNode(4, None, None)
    eight = TreeNode(8, four2, None)
    ten = TreeNode(10, None, None)
    four = TreeNode(4, ten, eight)
    root = TreeNode(2, None, four)
    print(Solution().goodNodes(root))

