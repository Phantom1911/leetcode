def maxSubarrayProd(array):
    n = len(array)
    maxeh = [None for i in range(n)]
    mineh = [None for i in range(n)]
    maxeh[0] = array[0]
    mineh[0] = array[0]
    for i in range(1,n):
        maxeh[i] = max(maxeh[i-1]*array[i],mineh[i-1]*array[i],array[i])
        mineh[i] = min(maxeh[i-1]*array[i],mineh[i-1]*array[i],array[i])
    return max(maxeh)

if __name__=="__main__":
    print(maxSubarrayProd([6,-3,-10,0,2]))