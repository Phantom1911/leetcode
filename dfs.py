class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
        root = self

        def dfs(node, array):
            if node is None:
                return
            if node.left is None and node.right is None:
                array.append(node.name)
                return
            dfs(node.left, array)
            dfs(node.right, array)

        dfs(root, array)
        return array

    pass


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
        root = self

        def dfs(node, array):
            if node is None:
                return
            if node.left is None and node.right is None:
                array.append(node.name)
                return
            dfs(node.left, array)
            dfs(node.right, array)

        dfs(root, array)
        return array
