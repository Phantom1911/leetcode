# https://leetcode.com/problems/add-two-numbers/

# LOTS of edge cases.
# [9,9,9,9,9,9,9] + [9,9,9,9]
# [5] + [5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2
        carry = 0
        dummy = ListNode(float("inf"), None)
        p = dummy
        while p1 is not None and p2 is not None:
            res = p1.val + p2.val + carry
            if res >= 10:
                carry = 1
                res = res % 10
            else:
                carry = 0
            resNode = ListNode(res, None)
            p.next = resNode
            p = p.next
            p1, p2 = p1.next, p2.next

        if p1 is None and p2 is not None:
            while p2 is not None:
                res = p2.val + carry
                if res >= 10:
                    carry = 1
                    res = res % 10
                else:
                    carry = 0
                resNode = ListNode(res, None)
                p.next = resNode
                p = p.next
                p2 = p2.next
        else:
            while p1 is not None:
                res = p1.val + carry
                if res >= 10:
                    carry = 1
                    res = res % 10
                else:
                    carry = 0
                resNode = ListNode(res, None)
                p.next = resNode
                p = p.next
                p1 = p1.next
        if carry != 0:
            p.next = ListNode(carry, None)

        return dummy.next
