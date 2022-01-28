# x need not be in the array
import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        h = []
        idx = getposn(arr,x)
        dis = 0
        while dis <= k:
            if dis == 0 and inbound(arr,idx):
                heapq.heappush(h, (abs(x-arr[idx]),arr[idx]))
                dis += 1
                continue
            if inbound(arr, idx + dis):
                heapq.heappush(h, (abs(x-arr[idx+dis]),arr[idx+dis]))
            if inbound(arr, idx - dis):
                heapq.heappush(h, (abs(x-arr[idx-dis]),arr[idx-dis]))
            dis+=1

        ans = []
        count = 0
        while count < k:
            ans.append(heapq.heappop(h)[1])
            count += 1
        return sorted(ans)


def inbound(arr, i):
    n = len(arr)
    if i >= 0 and i < n:
        return True
    return False

def getposn(arr,x):
    n = len(arr)
    s,e = 0, n-1
    while s <= e:
        m = (s+e)//2
        if arr[m] == x:
            return m
        elif arr[m] >x:
            e = m-1
        else:
            s=m+1
    return s