# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    ans = []

    def bs(node, currSum):
        if node is None:
            return
        if node.left is None and node.right is None:
            ans.append(currSum + node.value)
            return
        bs(node.left, currSum + node.value)
        bs(node.right, currSum + node.value)

    bs(root, 0)
    return ans
