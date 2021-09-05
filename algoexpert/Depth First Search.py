class Node:
    def __init__(self, name):
        self.name = name
        self.children = []



def dfs(root):
    dfs_arr = []
    stack = [root]
    while len(stack) != 0 :
        currNode = stack.pop()
        dfs_arr.append(currNode.name)
        for child in currNode.children:
            stack.append(child)
    return dfs_arr


if __name__=="__main__":
    root = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")
    nodeE = Node("E")
    nodeF = Node("F")
    nodeG = Node("G")
    nodeH = Node("H")
    nodeI = Node("I")
    nodeJ = Node("J")
    nodeK = Node("K")
    root.children = [nodeB, nodeC, nodeD]
    nodeB.children = [nodeE, nodeF]
    nodeF.children = [nodeI, nodeJ]
    nodeD.children = [nodeG, nodeH]
    nodeG.children = [nodeK]

    print(dfs(root))
