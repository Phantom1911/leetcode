def mergeSort(array):
    # Write your code here.
    if len(array) == 1:
        return array
    mid = len(array) // 2
    leftHalf = array[:mid]
    rightHalf = array[mid:]
    return merge(mergeSort(leftHalf), mergeSort(rightHalf))


def merge(array1, array2):
    i, j = 0, 0
    ans = []
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            ans.append(array1[i])
            i += 1
        else:
            ans.append(array2[j])
            j += 1
    while i < len(array1):
        ans.append(array1[i])
        i += 1
    while j < len(array2):
        ans.append(array2[j])
        j += 1
    return ans