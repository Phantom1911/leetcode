# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    def validate(node, mini, maxi):
        if mini <= node.value <= maxi and validate(node.left, mini, node.value) and validate(node.right, node.value, maxi):
            return True
        return False

    return validate(tree, -float("inf"), float("inf"))


pass
