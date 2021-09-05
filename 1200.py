class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        output = []
        arr = sorted(arr)
        minDiff = float("inf")
        for i in range(len(arr) - 1):
            currDiff = arr[i + 1] - arr[i]
            if minDiff > currDiff:
                minDiff = currDiff

        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == minDiff:
                output.append([arr[i], arr[i + 1]])

        return output