maxSum = -float("inf")
def maxPathSum(tree):
    # Write your code here.
    currSum =  0
    getMaxSum(tree,  currSum)
    return maxSum


def getMaxSum(root,  currSum):
    if root is None:
        return
    currSum += root.value
    if root.left is None and root.right is None:
        maxSum = max(maxSum, currSum)
    getMaxSum(root.left,  currSum)
    print("currSum is " + str(currSum))
    print("maxSum is " + str(maxSum))
    getMaxSum(root.right,  currSum)


class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

if __name__ == "__main__":
    one = Tree(1)
    two = Tree(2)
    three = Tree(3)
    four = Tree(4)
    five = Tree(5)
    six = Tree(6)
    seven = Tree(7)
    one.left = two
    one.right = three
    two.left = four
    two.right = five
    three.left = six
    three.right = seven
    print(maxPathSum(one))