# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    temp = head
    length = 0
    while temp is not None:
        temp = temp.next
        length += 1
    if k == length:
        head = head.next
        return head
    index = length - k
    temp = head
    counter = 0
    while counter < index:
        temp = temp.next
        counter += 1
    temp.next = temp.next.next
    return head
