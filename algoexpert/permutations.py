def getPermutations1(array):
    if len(array) == 0:
		return []
	if len(array) == 1:
		return [[array[0]]]
	remPerms = getPermutations(array[1:])
	ans = []
	for per in remPerms:
		for i in range(len(per)+1):
			newPer = insertAtIndex(array[0], i,per)
			ans.append(newPer)
	return ans

def insertAtIndex(ele, i, arr):
	return arr[0:i]+[ele]+arr[i:]



def getPermutations2(array):
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
