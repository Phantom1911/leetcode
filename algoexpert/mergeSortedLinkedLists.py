# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    # Write your code here.
    temp1 = headOne
    temp2 = headTwo
    temp = LinkedList(float("inf"))
    ans = temp
    while (temp1 != None and temp2 != None):
        if temp1.value <= temp2.value:
            temp.next = temp1
            temp1 = temp1.next
            temp = temp.next
        else:
            temp.next = temp2
            temp2 = temp2.next
            temp = temp.next
    while (temp1 != None):
        temp.next = temp1
        temp1 = temp1.next
        temp = temp.next
    while (temp2 != None):
        temp.next = temp2
        temp2 = temp2.next
        temp = temp.next
    return ans.next