class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


from collections import defaultdict


def maxPathSum(tree):
    '''
    convert tree to graph, then do dfs from each node
    '''


    adjlist, maxsum = {}, [-float("inf")]
    getadjlist(tree, adjlist)
    for n in adjlist:
        seen = set()
        dfs(n, 0, seen, adjlist, maxsum)
    return maxsum[0]


def dfs(node, currsum, seen, adjlist, maxsum):
    currsum += node.value
    maxsum[0] = max(currsum, maxsum[0])
    seen.add(node)
    for child in adjlist[node]:
        if child not in seen:
            dfs(child, currsum, seen, adjlist, maxsum)


def getadjlist(node, adjlist):
    if node is None:
        return
    if node not in adjlist:
        adjlist[node] = []
    if node.left is not None:
        adjlist[node].append(node.left)
        if node.left not in adjlist:
            adjlist[node.left] = []
        adjlist[node.left].append(node)
    if node.right is not None:
        adjlist[node].append(node.right)
        if node.right not in adjlist:
            adjlist[node.right] = []
        adjlist[node.right].append(node)

    getadjlist(node.left, adjlist)
    getadjlist(node.right, adjlist)


if __name__=='__main__':
    tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7])
    print(maxPathSum(tree))



