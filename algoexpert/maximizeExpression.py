def maximizeExpression(array):
    if len(array) < 4:
        return 0
    if len(array) == 4:
        return array[0] - array[1] + array[2] - array[3]
    maxA = [array[i] for i in range(len(array))]
    for i in range(1, len(array)):
        maxA[i] = max(maxA[i - 1], array[i])

    maxAMinusB = [-float("inf") for i in range(len(array))]
    for i in range(1, len(array)):
        # consider that I am choosing B at ith index
        # if B is at ith index, then A can be from 0 to (i-1)th index
        # maxAMinusB[i] denotes max value of A-B where both A and B lie on or before i
        # maxA[i-1]-array[i] => case where B is at ith index
        maxAMinusB[i] = max(maxA[i - 1] - array[i], maxAMinusB[i - 1])

    maxAMinuBPlusC = [-float("inf") for i in range(len(array))]
    for i in range(2, len(array)):
        maxAMinuBPlusC[i] = max(maxAMinusB[i - 1] + array[i], maxAMinuBPlusC[i - 1])

        maxAMinuBPlusCMinusD = [-float("inf") for i in range(len(array))]
    for i in range(3, len(array)):
        maxAMinuBPlusCMinusD[i] = max(maxAMinuBPlusC[i - 1] - array[i], maxAMinuBPlusCMinusD[i - 1])

    return max(maxAMinuBPlusCMinusD)

if __name__=="__main__":
    print(maximizeExpression([3,6,1,-3,2,7]))