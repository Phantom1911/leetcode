def findOdd(arr):
    auxArr = []
    for i in range(len(arr)):
        auxArr.append(decToBinary(arr[i]))
    positionCount = [0 for i in range(8)]   # [0,0, .. 0]
    for i in range(0,8,1):
        currcount = 0
        for arr in auxArr:
            currcount += arr[i]
        positionCount[i] = currcount

# [1,1,2,2,a,b]   => a^b = known ,

def decToBinary(i):
    # returns binary array size 8





if __name__=="__main__":
    print(findOdd([1,1,1,2,2,2,3]))



    # 1 --- [0,0,0,0,0,0]