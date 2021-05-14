# Definition for a binary tree node.
# https://leetcode.com/problems/unique-binary-search-trees-ii/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []
        return self.getTrees(1, n)

    def getTrees(self, lowerNodeVal, higherNodeVal):
        ans = []
        if lowerNodeVal > higherNodeVal:
            ans.append(None)
            return ans

        for i in range(lowerNodeVal, higherNodeVal+1):
            leftSubTrees = self.getTrees(lowerNodeVal, i - 1)
            rightSubTrees = self.getTrees(i + 1, higherNodeVal)
            for leftTree in leftSubTrees:
                for rightTree in rightSubTrees:
                    root = TreeNode(i)
                    root.left = leftTree
                    root.right = rightTree
                    ans.append(root)

        return ans

if __name__=="__main__":
    s = Solution()
    print(s.generateTrees(3))