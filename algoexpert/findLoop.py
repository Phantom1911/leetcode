# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value, next):
        self.value = value
        self.next = next


def findLoop(head):
    fast, slow = head.next.next, head.next

    while fast != slow:
        fast = fast.next.next
        slow = slow.next

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

if __name__=="__main__":
    two  = LinkedList(3, None)
    five = LinkedList(6, two)
    four= LinkedList(5, five)
    three = LinkedList(4, four)
    one = LinkedList(2, two)
    two.next = three
    head = LinkedList(1,one)

    print(findLoop(head).value)