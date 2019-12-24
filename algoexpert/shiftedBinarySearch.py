def shiftedBinarySearch(array, target):
    # Write your code here.
    # first find pivot
    s = 0
    e = len(array) - 1
    pivot = -1
    while (s <= e):
        mid = (s + e) // 2
        if array[mid] > array[mid + 1]:
            pivot = mid
            break
        elif array[mid] <= array[mid + 1]:
            s = mid + 1
    ans = -1
    s = 0
    e = pivot
    while (s <= e):
        m = (s + e) // 2
        if array[m] == target:
            return m
        elif array[m] < target:
            s = m + 1
        else:
            e = m - 1
    s = pivot + 1
    e = len(array) - 1
    while (s <= e):
        m = (s + e) // 2
        if array[m] == target:
            return m
        elif array[m] < target:
            s = m + 1
        else:
            e = m - 1
    return ans
