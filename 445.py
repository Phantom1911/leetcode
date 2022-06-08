# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rev1, rev2 = revLL(l1), revLL(l2)
        temp1, temp2 = rev1, rev2
        dummy = ListNode(-1)
        p = dummy
        carry = 0
        while temp1 is not None and temp2 is not None:
            currSum = temp1.val + temp2.val + carry
            if currSum >= 10:
                carry = 1
            else:
                carry = 0
            temp = ListNode(currSum % 10)
            p.next = temp
            p = temp
            temp1, temp2 = temp1.next, temp2.next

        if temp1 is None:
            while temp2 is not None:
                currSum = temp2.val + carry
                if currSum >= 10:
                    carry = 1
                else:
                    carry = 0
                temp = ListNode(currSum % 10)
                p.next = temp
                p = temp
                temp2 = temp2.next

        if temp2 is None:
            while temp1 is not None:
                currSum = temp1.val + carry
                if currSum >= 10:
                    carry = 1
                else:
                    carry = 0
                temp = ListNode(currSum % 10)
                p.next = temp
                p = temp
                temp1 = temp1.next

        if carry == 1:
            temp = ListNode(1)
            p.next = temp
            p = temp

        return revLL(dummy.next)


def revLL(head):
    if head is None or head.next is None:
        return head
    restRev = revLL(head.next)
    temp = restRev
    while temp is not None and temp.next is not None:
        temp = temp.next
    temp.next = head
    head.next = None
    return restRev