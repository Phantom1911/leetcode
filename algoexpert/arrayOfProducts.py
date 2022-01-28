def arrayOfProducts(array):
	n = len(array)
	ans = [0 for i in range(n)]
	prod = calcproduct(array)
	numzeros = numberofzeros(array)
    if numzeros >= 1:
		for i in range(n):
			if array[i] == 0:
				if numzeros > 1:
					ans[i] = 0
				else:
					ans[i] = prod
			else:
				ans[i] = 0
	else:
		for i in range(n):
			ans[i] = prod // array[i]
	return ans


def numberofzeros(array):
	count = 0
	for i in range(len(array)):
		if array[i] == 0:
			count+=1
	return count


# this function calculates product ignoring zeros
def calcproduct(array):
	ans = 1
	for i in range(len(array)):
		if array[i] != 0:
			ans *= array[i]
	return ans