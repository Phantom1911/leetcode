#code
# Naive Appraoch::
def rotateArray(arr , n , d):
    d = d % n
    for i in range(d):
        arr.append(arr[i])
    return arr[d:]

# Smart Approach : Always check whether it is clockwise rotation or anticlockwise rotation

# code
def reverseArray(arr, start_idx, end_idx):
    lo, hi = start_idx, end_idx
    while lo < hi:
        arr[lo], arr[hi] = arr[hi], arr[lo]
        lo += 1
        hi -= 1


def rotateArrayEfficient(arr, n, d):
    reverseArray(arr, 0, n - 1)
    reverseArray(arr, n - d, n - 1)
    reverseArray(arr, 0, n - d - 1)
    return arr

def printArray(arr):
    s = ""
    for i in range(len(arr)):
        s += str(arr[i]) + " "
    s.strip()
    print(s)


#code
if __name__ == "__main__":
    t = int(input())
    while (t>0):
        vals = input().strip().split(" ")
        n, d = int(vals[0]), int(vals[1])
        arr = input().strip().split(" ")
        printArray(rotateArrayEfficient(arr, n, d))
        t -=1
