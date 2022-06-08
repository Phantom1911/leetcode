# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        return mergeSort(head)


def mergeSort(node):
    if node.next is None:
        return node
    slow, fast = node, node
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    temp = node
    while temp.next != slow:
        temp = temp.next
    temp.next = None
    part1 = mergeSort(node)
    part2 = mergeSort(slow)

    return merge(part1, part2)


def merge(node1, node2):
    temp1, temp2 = node1, node2
    dummy = ListNode()
    temp = dummy
    while temp1 is not None and temp2 is not None:
        if temp1.val <= temp2.val:
            temp.next = temp1
            temp = temp.next
            temp1 = temp1.next
        else:
            temp.next = temp2
            temp = temp.next
            temp2 = temp2.next
    if temp1 is None:
        temp.next = temp2
    if temp2 is None:
        temp.next = temp1
    return dummy.next












