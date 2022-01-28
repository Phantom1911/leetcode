# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value, next):
        self.value = value
        self.next = next


def zipLinkedList(linkedList):
    fhh = linkedList
    shh = splitll(fhh)
    shhrev = reversell(shh)
    return interweavell(fhh, shhrev)


def interweavell(first, second):
    head = first
    while first is not None and second is not None:
        firstnext, secondnext = first.next, second.next
        first.next = second
        second.next = firstnext
        first = firstnext
        second = secondnext
    return head


def reversell(head):
    if head is None or head.next is None:
        return head
    restrev = reversell(head.next)
    temp = restrev
    while temp.next != None:
        temp = temp.next
    temp.next = head
    head.next = None
    return restrev


def splitll(fhh):
    slow, fast = fhh, fhh
    while slow is not None and fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    if fast is None:  # even length LL
        temp = fhh
        while temp.next != slow:
            temp = temp.next
        temp.next = None
        return slow
    else:
        temp = fhh
        while temp != slow:
            temp = temp.next
        slow = slow.next
        temp.next = None
        return slow

if __name__=="__main__":
    six = LinkedList("6", None)
    five = LinkedList("5", six)
    four = LinkedList("4", five)
    three = LinkedList("3", four)
    two = LinkedList("2", three)
    one = LinkedList("1",two)
    ans = zipLinkedList(one)
    print(ans.value)
