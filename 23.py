# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq


class Solution:
    def mergeKLists(self, lists):
        root = ListNode(-1)
        temp = root
        heap = []
        i = 0
        while (i < len(lists)):
            if (lists[i] is not None):
                heapq.heappush(heap, [lists[i].val, i])
            i += 1

        while (len(heap) > 0):
            node = heapq.heappop(heap)
            i = node[1]
            root.next = lists[i]
            lists[i] = lists[i].next
            if (lists[i] is not None):
                heapq.heappush(heap, [lists[i].val, i])
            root = root.next
            root.next = None

        return temp.next

if __name__=="__main__":
    print(Solution().mergeKLists())