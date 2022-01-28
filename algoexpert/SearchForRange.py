# Naive solution

def searchForRange(array, target):
    ans = [-1,-1]
	s , e = 0, len(array)-1
	while s <= e:
		m = (s+e)//2
		if array[m] == target:
			if ans[0] == -1 and ans[1] == -1:
				ans[0], ans[1] = m , m
			elif m > ans[1]:
				ans[1] = m
			elif m < ans[0]:
				ans[0] = m
			j = m+1
			while j<len(array) and array[j] == target:
				j+=1
			j-=1
			if j > ans[1]:
				ans[1] = j
			j = m-1
			while j>0 and array[j] == target:
				j-=1
			j+=1
			if j < ans[0]:
				ans[0] = j
			return ans
		elif array[m] < target :
			s = m+1
		else:
			e = m-1
	return ans
