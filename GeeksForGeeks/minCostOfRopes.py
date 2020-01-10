from heapq import heappush, heappop , heapify
def getMinCost(array):
    n = len(array)
    if n == 1:
        return(array[0])

    elif n == 2:
        return(array[0] + array[1])
    cost = 0
    heapify(array)
    while len(array) > 2:
        min1 = heappop(array)
        min2 = heappop(array)
        cost = cost+min1+min2
        heappush(array, min1 + min2)
    x = heappop(array)
    y = heappop(array)
    return cost+x+y

if __name__=="__main__":
    print(getMinCost([4,3,2,6]))