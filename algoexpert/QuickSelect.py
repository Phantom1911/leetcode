def quickselect(array, k):
    n = len(array)
    # kth smallest element will come at k-1 th idx in the sorted array
    return qshelper(0, n - 1, array, k - 1)


def qshelper(s, e, arr, pos):
    p, l, r = s, s + 1, e
    while l <= r:
        if arr[l] > arr[p] and arr[r] < arr[p]:
            arr[l], arr[r] = arr[r], arr[l]
        if arr[l] <= arr[p]:
            l += 1
        if arr[r] >= arr[p]:
            r -= 1
    arr[r], arr[p] = arr[p], arr[r]
    if r == pos:
        return arr[r]
    elif r < pos:
        return qshelper(r + 1, e, arr, pos)
    else:
        return qshelper(s, r - 1, arr, pos)


if __name__=="__main__":
    print(quickselect([8,5,2,9,7,6,3],3))





