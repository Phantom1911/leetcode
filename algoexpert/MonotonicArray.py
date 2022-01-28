def isMonotonic(array):
	if len(array) == 0:
		return True
    initial = array[0]
	i = 0
	while i < len(array) and initial == array[i]:
		i+=1
	if i == len(array):
		return True
	inc = False
	if initial < array[i]:
		inc = True
	if inc:
		for j in range(len(array)-1):
			if array[j+1]<array[j] :
				return False

		return True
	else:
		for j in range(len(array)-1):
			if array[j+1]>array[j]:
				return False
		return True

	return False
