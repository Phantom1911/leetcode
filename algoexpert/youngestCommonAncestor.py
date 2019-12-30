# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    depthOne = height(descendantOne, topAncestor)
    depthTwo = height(descendantTwo, topAncestor)
    if depthOne >= depthTwo:
        return findLCA(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        return findLCA(descendantTwo, descendantOne, depthTwo - depthOne)


def findLCA(lower, higher, diff):
    while diff > 0:
        lower = lower.ancestor
        diff -= 1
    while lower != higher:
        lower = lower.ancestor
        higher = higher.ancestor
    return lower


def height(node, root):
    depth = 0
    while node != root:
        node = node.ancestor
        depth += 1
    return depth

