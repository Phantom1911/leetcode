def invertBinaryTree(tree):
    # Write your code here.
    if tree is None:
        return
    if tree.left is None and tree.right is None:
        return tree
    temp = tree.left
    tree.left = tree.right
    tree.right = temp
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


pass
