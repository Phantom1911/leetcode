def ambiguousMeasurements(measuringCups, low, high):
    memo = {}
    return canMeasureFunc(measuringCups, low, high, memo)


def canMeasureFunc(cups, low, high, memo):
    if hashed(low, high) in memo:
        return memo[hashed(low, high)]
    if low <= 0 and high <= 0:
        return False
    canMeasure = False
    for cup in cups:
        cupLow, cupHigh = cup[0], cup[1]
        if low <= cupLow and cupHigh <= high:
            canMeasure = True
            break
        newLow = low - cupLow
        newHigh = high - cupHigh
        canMeasure = canMeasureFunc(cups, newLow, newHigh, memo)
        if canMeasure:
            break
    memo[hashed(low, high)] = canMeasure
    return canMeasure


def hashed(low, high):
    return str(low) + ":" + str(high)

if __name__=="__main__":
    print(ambiguousMeasurements([
      [1, 3],
    [2, 4],
    [5, 6]
]
, 100,101))