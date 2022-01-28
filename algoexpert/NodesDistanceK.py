# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


from collections import deque


def findNodesDistanceK(tree, target, k):
    parents = {}
    # node is not hashable, hence cannot be key of the map
    # parents map stores value to parent node mapping
    populateParents(tree, None, parents)
    parentOfTargetNode = parents[target]

    targetNode = None
    # this check is necessary - a none parent means that the target node is the root of the tree
    if parentOfTargetNode is None:
        targetNode = tree
    elif parentOfTargetNode.left is not None and parentOfTargetNode.left.value == target:
        targetNode = parentOfTargetNode.left
    elif parentOfTargetNode.right is not None and parentOfTargetNode.right.value == target:
        targetNode = parentOfTargetNode.right
    queue = deque()
    queue.append((targetNode, 0))
    seen = set()
    ans = []
    while len(queue) != 0:
        currPair = queue.popleft()
        currNode, currDis = currPair[0], currPair[1]
        if currDis == k:
            ans.append(currNode.value)
            continue
        seen.add(currNode.value)
        if currNode.left is not None and currNode.left.value not in seen:
            queue.append((currNode.left, currDis + 1))
        if currNode.right is not None and currNode.right.value not in seen:
            queue.append((currNode.right, currDis + 1))
        currParent = parents[currNode.value]
        if currParent is not None and currParent.value not in seen:
            queue.append((currParent, currDis + 1))
    return ans


def populateParents(node, parent, parents):
    if node is None:
        return
    parents[node.value] = parent
    populateParents(node.left, node, parents)
    populateParents(node.right, node, parents)

