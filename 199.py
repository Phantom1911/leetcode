import json
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque, OrderedDict
class Solution:
    def rightSideView(self, root: TreeNode):
        def levelOrder(root):
            q = deque()
            q.append((root,0))
            _dict = OrderedDict()
            while len(q) != 0:
                curr_node = q.popleft()
                if curr_node[1] not in _dict:
                    _dict[curr_node[1]] = [curr_node[0]]
                else:
                    _dict[curr_node[1]].append(curr_node[0])
                if curr_node[0].left is not None:
                    q.append((curr_node[0].left, curr_node[1]+1))
                if curr_node[0].right is not None:
                    q.append((curr_node[0].right, curr_node[1]+1))
            ans = []
            for key in _dict:
                ans.append(_dict[key][-1].val)
            return ans
        return levelOrder(root)

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line);

            ret = Solution().rightSideView(root)
            # for node in ret:
            #     print(node.val)
            print(ret)
            # out = integerListToString(ret);
            # print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()