# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


from collections import deque


def rightSiblingTree(root):
    q = deque()
    q.append((root, None, None))  # (node, parent, isLeftChild)
    while q:
        curr = q.popleft()
        currnode, parent, isLeftChild = curr[0], curr[1], curr[2]
        if currnode is None:
            continue
        q.append((currnode.left, currnode, True))
        q.append((currnode.right, currnode, False))
        if parent is None:
            # currnode.right = None
            continue
        if isLeftChild:
            currnode.right = parent.right
        else:
            if parent.right is not None:
                currnode.right = parent.right.left
            else:
                currnode.right = None

    return root

