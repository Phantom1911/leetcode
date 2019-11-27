def bubbleSort(array):
    # Write your code here.
	for i in range(len(array)-1):
		for j in range(i+1, len(array)):
			if array[j] < array[i]:
				temp = array[i]
				array[i] = array[j]
				array[j] = temp
	return array
    pass
