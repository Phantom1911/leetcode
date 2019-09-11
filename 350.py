class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)
        ans = []
        marked = [False for i in range(m+1)]
        for i in range(n):
            curr = nums1[i]
            for j in range(m):
                if nums2[j]==curr and  not marked[j]:
                    ans.append(curr)
                    marked[j] = True
                    break
        return ans