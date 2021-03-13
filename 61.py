# https://leetcode.com/problems/rotate-list/

# Refer : https://www.youtube.com/watch?v=VX5Fz9z4-CE

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        # based on 0 indexing , the new head will be at index n - k index
        p = head
        n = 0
        while p.next is not None:
            p = p.next
            n+=1
        n+=1
        k = k % n
        new_head_index = n - k
        p.next = head
        counter = 0
        new_head = head
        while counter != n-k:
            new_head = new_head.next
            counter +=1
        new_tail = head
        while new_tail.next != new_head:
            new_tail = new_tail.next
        new_tail.next = None
        return new_head

    def printList(self, head):
        p = head
        s = ""
        while p is not None:
            s = s + str(p.val) + " -> "
            p = p.next
        print(s)

if __name__=="__main__":
    s = Solution()
    head = ListNode(1, None)
    head.next = ListNode(2, None)
    head.next.next = ListNode(3, None)
    head.next.next.next = ListNode(4, None)
    head.next.next.next.next = ListNode(5, None)

    s.printList(s.rotateRight(head, 2))


