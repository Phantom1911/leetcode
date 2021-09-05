def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    '''
	One way is obviously to list down all the paths from root to leaf
	And check in each of the paths if a subsequence 1-2-3 or 3-2-1 exists
	If either of these subsequences exist, then return True else False

	One way could be to traverse the tree and keep track of the current path.
	If the leaf node is encountered, that means we can't go further down in this path
	At this momennt we should check if our path has any of the subsequences

	Both these approaches can only be applied when you have been given the BST as the input
	But coming to think of it, do we really need a BST to validate the condition?
	the case for n1 - n2 - n3 is when
	'''
    print("hi")

    return (nodeThree < nodeTwo < nodeOne) or \
           (nodeTwo <= nodeThree < nodeOne) or \
           (nodeOne <= nodeThree < nodeTwo) or \
           (nodeOne <= nodeTwo <= nodeThree) or \
           (nodeOne < nodeTwo < nodeThree) or \
           (nodeTwo <= nodeOne < nodeThree) or \
           (nodeThree <= nodeOne < nodeTwo) or \
           (nodeThree <= nodeTwo <= nodeOne)


if __name__=="__main__":
    print(validateThreeNodes(5,8,1))