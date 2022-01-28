def numberOfBinaryTreeTopologies(n):
    memo = {}
    memo[0], memo[1] = 0, 1
    return numOfBinTrees(n, memo)


def numOfBinTrees(n, memo):
    if n <= 0:
        return 0
    if n in memo:
        return memo[n]
    count = 0
    # iterate over number of nodes possible in left subtree, one node is already taken as root
    for i in range(0, n, 1):
        leftTopo = numOfBinTrees(i, memo)
        memo[i] = leftTopo
        rightTopo = numOfBinTrees(n - i - 1, memo)
        memo[n - i - 1] = rightTopo
        if leftTopo == 0 or rightTopo == 0:
            count += (leftTopo + rightTopo)
        else:
            count += leftTopo * rightTopo

    return count


if __name__ == "__main__":
    s = "abc"
    print(s.__hash__())
    # print(numberOfBinaryTreeTopologies(3))