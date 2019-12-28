def getPermutations(array):
    # Write your code here.
    if len(array) == 0:
        return []
    if len(array) == 1:
        copyArr = array[::]
        return [copyArr]
    firstEle = array[0]
    roa = array[1:]
    permsOfroa = getPermutations(roa)
    ans = []
    for perm in ((permsOfroa)):
        for j in range(len(perm) + 1):
            copyArr = perm[::]
            copyArr.insert(j, firstEle)
            ans.append(copyArr)
    return ans
