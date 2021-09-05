'''
as given in the question, array is said to represent BST
when inserting elements from the array left to right
gives the BST

when you start from 0th index of both the arrays,
you have no option but to place 0th index as the root

now that you have the root, all the elements of the array lesser than root value
go to left subtree and all eles greater than root value go to right
This holds true for both the arrays given

for all the eles greater than root and smaller than root, these individual arrays need to be BSTs in themselves

'''



def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) == len(arrayTwo) and len(arrayTwo) == 0:
        return True

    if len(arrayOne) != len(arrayTwo) or arrayOne[0] != arrayTwo[0]:
        return False

    if len(arrayOne) == 1 and len(arrayTwo) == 1 and arrayOne[0] == arrayTwo[0]:
        return True

    greatersOne, greatersTwo = [], []
    smallersOne, smallersTwo = [], []

    rootVal = arrayOne[0]
    for i in range(1, len(arrayOne)):
        if arrayOne[i] >= rootVal:
            greatersOne.append(arrayOne[i])
        if arrayOne[i] < rootVal:
            smallersOne.append(arrayOne[i])
        if arrayTwo[i] < rootVal:
            smallersTwo.append(arrayTwo[i])
        if arrayTwo[i] >= rootVal:
            greatersTwo.append(arrayTwo[i])

    return sameBsts(greatersOne, greatersTwo) and sameBsts(smallersOne, smallersTwo)


