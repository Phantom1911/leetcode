import heapq
'''
used is to handle duplicate elements at different indices
inheap is to make sure we don't push an already pushed element again to the heap
'''

def sortKSortedArray(array, k):
    h = []
    ans = [-1 for i in range(len(array))]
    used = [False for i in range(len(array))]
    inheap = [False for i in range(len(array))]
    for i in range(len(array)):
        for j in range(i - k, i):
            if 0 <= j <= len(array) - 1 and used[j] == False and inheap[j] == False:
                inheap[j] = True
                heapq.heappush(h, (array[j], j))
        for j in range(i, i + k + 1):
            if 0 <= j <= len(array) - 1 and used[j] == False and inheap[j] == False:
                inheap[j] = True
                heapq.heappush(h, (array[j], j))

        curr = heapq.heappop(h)
        currele, curridx = curr[0], curr[1]
        used[curridx] = True
        ans[i] = curr[0]

    return ans


if __name__=="__main__":
    print(sortKSortedArray2([3, 2, 1, 5, 4, 7, 6, 5],3))