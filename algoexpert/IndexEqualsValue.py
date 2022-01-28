def indexEqualsValue(array):
    ans = -1
	s , e = 0, len(array)-1
	while s <= e:
		m = (s+e)//2
		if array[m] == m:
			ans = m  # not returning from here straightaway because we need smallest such index
			e = m-1  # search in the lower part now
		elif array[m] < m :
			s = m+1
		else:
			e = m-1
	return ans
