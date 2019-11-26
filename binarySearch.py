def binarySearch(array, target):
    # Write your code here.
    def bs(arr, target, s, e):
        if s > e:
            return -1
        mid = (s + e) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return bs(arr, target, mid + 1, e)
        else:
            return bs(arr, target, s, mid - 1)

    return bs(array, target, 0, len(array) - 1)


pass
