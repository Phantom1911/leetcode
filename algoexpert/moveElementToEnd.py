def moveElementToEnd(array, toMove):
    # Write your code here.
	i = len(array)-1
	while(i>=0 and array[i]==toMove):
		i-=1
	j = 0
	while(i>=0 and j<i):
		if array[j] == toMove:
			array[j] = array[i]
			array[i] = toMove
			i-=1
		while array[i]==toMove:
			i-=1
		j+=1
	return array
