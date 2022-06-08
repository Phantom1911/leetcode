class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        amax, bmax = total//cost1 , total//cost2
        count = 0
        for b in range(bmax+1):
            # for this b, find the max a that can be taken
            lo, hi, mid = 0, amax, None
            while lo <= hi:
                mid = (lo+hi)//2
                if mid*cost1 + b*cost2 <=total:
                    # there is scope of increasing mid
                    print(f'{mid} , {b}')
                    lo = mid+1
                else:
                    mid -= 1
                    hi = mid-1
            count += (mid+1)
        return count

if __name__=="__main__":
    print(Solution().waysToBuyPensPencils(20,10,5))