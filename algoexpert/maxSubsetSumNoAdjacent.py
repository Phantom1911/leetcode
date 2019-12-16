def maxSubsetSumNoAdjacent(array):
    # Write your code here.

    def mss(arr, i):
        if i >= len(arr):
            return 0
        elif i == len(arr) - 1:
            return arr[i]
        else:
            return max(arr[i] + mss(arr, i + 2), mss(arr, i + 1))

    return mss(array, 0)


pass
