def findClosestValueInBst(tree, target):
    # Write your code here.
    arr = []

    def inorder(node):
        if node is None:
            return
        if node.left is None and node.right is None:
            arr.append(node)
            return
        inorder(node.left)
        arr.append(node)
        inorder(node.right)
        return

    inorder(tree)

    def bs(arr, val, s, e):
        if s > e:
            return -1
        mid = (s + e) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            return bs(arr, val, mid + 1, e)
        else: return bs(arr, val, s, mid-1)

    index = bs(arr, target, 0, len(arr) - 1)
    return arr[index + 1]


