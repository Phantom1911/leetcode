# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first, second = head, head
        counter = 0
        while counter != n:
            second = second.next
            counter += 1
        while second is not None:
            first = first.next
            second = second.next
        p = head
        # two edge cases: single element LL, 2 eles LL and asked to remove second element from the end
        if first == head:
            if head.next is None:
                return None
            else:
                return head.next

        while p != first and p.next != first:
            p = p.next
        p.next = p.next.next

        return head
