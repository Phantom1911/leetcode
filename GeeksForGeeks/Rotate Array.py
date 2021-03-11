#code

def rotateArray(arr , n , d):
    d = d % n
    for i in range(d):
        arr.append(arr[i])
    return arr[d:]

def printArray(arr):
    s = ""
    for i in range(len(arr)):
        s += arr[i] + " "
    s.strip()
    print(s)


#code
if __name__ == "__main__":
    t = int(input())
    while (t>0):
        vals = input().strip().split(" ")
        n, d = int(vals[0]), int(vals[1])
        arr = input().strip().split(" ")
        printArray(rotateArray(arr, n, d))
        t -=1
