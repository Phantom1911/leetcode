# https://leetcode.com/problems/reverse-linked-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head.next is None:
            return head
        rem_list_reversed = self.reverseList(head.next)

        # get to the end of rem_reversed_list

        p = rem_list_reversed
        while p.next is not None:
            p = p.next
        p.next = head
        return rem_list_reversed


def printList(head):
    p = head
    s = ""
    while p is not None:
        s = s + p.val + " -> "
        p = p.next
    print(s)


if __name__=="__main__":
    s = Solution()
    head = ListNode(1, None)
    head.next = ListNode(2, None)
    head.next.next = ListNode(3, None)
    head.next.next.next = ListNode(4, None)
    head.next.next.next.next = ListNode(5, None)

    printList(s.reverseList(head))



