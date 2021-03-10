# https://practice.geeksforgeeks.org/problems/immediate-smaller-element1142/1

class Solution:

    def immediateSmaller(self, arr, n):
        # code here

        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i] = arr[i + 1]
            else:
                arr[i] = -1

        arr[n - 1] = -1
        return arr

if __name__ == "__main__":
    s = Solution()
    print(s.immediateSmaller([4,2,1,5,3], 5))