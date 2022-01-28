from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefixXorArray = [None for i in range(len(arr))]
        prefixXorArray[0] = arr[0]
        for i in range(1, len(arr)):
            prefixXorArray[i] = prefixXorArray[i - 1] ^ arr[i]
        ans = []
        for i in range(len(queries)):
            query = queries[i]
            l, r = query[0], query[1]
            if l == 0:
                ans.append(prefixXorArray[r])
            else:
                ans.append(prefixXorArray[r] ^ prefixXorArray[l - 1])
        return ans
