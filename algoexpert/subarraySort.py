def subarraySort(array):
    # Write your code here.
    followsSortedProp = [True for i in range(len(array))]
    minFalseElement = -1
    maxTillHere = array[0]
    maxIndexOfFalseElement = -1
    flag = True
    output = [-1, -1]
    for i in range(1, len(array)):
        maxTillHere = max(maxTillHere, array[i])
        if array[i] < maxTillHere:
            followsSortedProp[i] = False
            flag = False
            maxIndexOfFalseElement = i
            if minFalseElement == -1 or array[minFalseElement] > array[i]:
                minFalseElement = i

    if flag:
        return output
    output[1] = maxIndexOfFalseElement
    if array[minFalseElement] < array[0]:
        output[0] = 0
        return output
    minFalseElementValue = array[minFalseElement]
    for i in range(1, len(array)):
        currElem = array[i]
        if array[i - 1] <= array[minFalseElement] < array[i]:
            output[0] = i
            break
    return output



if __name__ == "__main__":
    print(subarraySort([4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 51, 7]))