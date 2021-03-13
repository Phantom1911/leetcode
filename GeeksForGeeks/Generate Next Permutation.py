# https://practice.geeksforgeeks.org/problems/next-permutation5226/1

# Refer : https://www.geeksforgeeks.org/find-next-greater-number-set-digits/
# A bit complicated algorithm to remember

class Solution:
    def nextPermutation(self, N, arr):
        # code here
        n = len(arr)
        i = n - 2

        while i >= 0 and arr[i] > arr[i + 1]:
            i -= 1
        if i == -1:
            return sorted(arr)
        smallest = i + 1
        j = i + 1
        while j < n:
            if arr[j] < arr[smallest] and arr[j] > arr[i]:
                smallest = j
            j+=1

        # swap arr[i] and arr[smallest]
        arr[i], arr[smallest] = arr[smallest], arr[i]
        res = arr[0:i + 1] + sorted(arr[i + 1:])
        return res

if __name__=="__main__":
    s = Solution()
    print(s.nextPermutation(6,[62,92,96,43,28,37,92,5,3,54,93,83,22]))