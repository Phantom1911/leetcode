class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # put nodes and indices in a set
        # if you get to the node which has been visited before, there is a cycle else null
        s = set()
        n = head
        while (n is not None):
            if n not in s:
                s.add(n)
            else: break
            n = n.next
        return n