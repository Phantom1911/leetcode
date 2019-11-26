# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        self.head = node

    pass

    def setTail(self, node):
        # Write your code here.
        self.tail = node

    pass

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.

        temp = self.head
        while (temp != node):
            temp = temp.next
        temp2 = temp.prev
        temp.prev = nodeToInsert
        nodeToInsert.next = temp
        nodeToInsert.prev = temp2
        temp2.next = nodeToInsert

    pass

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        temp = self.head
        while (temp != node):
            temp = temp.next
        temp2 = temp.next
        temp.next = nodeToInsert
        nodeToInsert.prev = temp
        nodeToInsert.next = temp2
        temp2.prev = nodeToInsert

    pass

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        i = 0
        temp = self.head
        while i < position - 1:
            temp = temp.next
            i+=1
        temp2 = temp.next
        temp.next = nodeToInsert
        nodeToInsert.prev = temp
        nodeToInsert.next = temp2
        temp2.prev = nodeToInsert

    pass

    def removeNodesWithValue(self, value):
        # Write your code here.
        temp = self.head
        while (temp is not None):
            if temp.val == value:
                previous = temp.prev
                nxt = temp.next
                prev.next = nxt
                nxt.prev = previous
                temp = previous

    pass

    def remove(self, node):
        # Write your code here.
        temp = self.head
        while (temp != node):
            temp = temp.next
        previous = temp.prev
        nxt = temp.next
        previous.next = nxt
        nxt.prev = previous

    pass

    def containsNodeWithValue(self, value):
        # Write your code here.
        temp = self.head
        while (temp is not None):
            if temp.val == value:
                return True
        return False

    pass
