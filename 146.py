class dequeNode:
    def __init__(self, key=None, value=None, nextNode=None, prevNode=None):
        self.key = key
        self.value = value
        self.nextNode = nextNode
        self.prevNode = prevNode


class mydeque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addAtBeginning(self, eleNode):
        if self.head is None:
            self.head = eleNode
            self.tail = eleNode
        else:
            eleNode.next = self.head
            self.head.prevNode = eleNode
            self.head = eleNode
        self.size += 1

    def removeFromEnd(self):
        # print(self.tail.prevNode.value)
        if self.tail.prevNode is None:
            self.head = None
            self.tail = None
        else:

            self.tail.prevNode.nextNode = None
            self.tail = self.tail.prevNode
            self.tail.prevNode = None

        self.size -= 1

    def removeNode(self, nodePtr):
        if nodePtr == self.tail:
            self.tail = nodePtr.prevNode
        if nodePtr == self.head:
            self.head = nodePtr.nextNode
        if nodePtr.prevNode is not None:
            nodePtr.prevNode.nextNode = nodePtr.nextNode
        if nodePtr.nextNode is not None:
            nodePtr.nextNode.prevNode = nodePtr.prevNode
        nodePtr.nextNode = None
        nodePtr.prevNode = None
        self.size -= 1

    def getEndNode(self):
        return self.tail


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = dict()
        self.nodes = mydeque()

    def get(self, key: int) -> int:
        if key in self.keys:
            if len(self.keys) == 1:
                return self.keys[key].value
            currNode = self.keys[key]
            if currNode == self.nodes.tail:
                self.nodes.tail = self.nodes.tail.prevNode
            self.nodes.removeNode(currNode)
            self.nodes.addAtBeginning(currNode)
            # print(self.nodes.head.key)
            return currNode.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            currNode = self.keys[key]
            self.nodes.removeNode(currNode)
            self.nodes.addAtBeginning(currNode)
            currNode.value = value
        else:
            if self.nodes.size == self.capacity:
                endNode = self.nodes.getEndNode()
                # print(endNode.key)
                del self.keys[endNode.key]
                self.nodes.removeFromEnd()
                # print(self.keys)
            currNode = dequeNode(key, value)
            self.nodes.addAtBeginning(currNode)
            if len(self.keys) == 0:
                self.nodes.tail = currNode
            self.keys[key] = currNode
        # print(self.keys)
        # print(self.nodes.head)

if __name__=="__main__":
    cache = LRUCache(2)
    cache.put(2,1)
    cache.put(2, 2)
    cache.get(2)
    cache.put(1, 1)
    cache.put(4, 1)
    cache.get(2)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


















# class Node:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.prev = None
#         self.next = None
#
#
# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.h = {}
#         self.capacity = capacity
#         self.head = Node('fake head', -1)
#         self.tail = Node('fake tail', -1)
#         self.head.next = self.tail
#         self.tail.prev = self.head
#
#     def get(self, key: int) -> int:
#         if key in self.h:
#             self.update(self.h[key])
#             return self.h[key].value
#         return -1
#
#     def update(self, node):
#         self.remove(node)
#         self.insertbetween(self.head, self.head.next, node)
#         if len(self.h) > self.capacity:
#             lastnode = self.tail.prev
#             self.remove(lastnode)
#             del (self.h[lastnode.key])
#
#     def insertbetween(self, a, b, node):
#         a.next = node
#         node.next, node.prev = b, a
#         b.prev = node
#
#     def remove(self, node):
#         p, n = node.prev, node.next
#         if p or n:
#             p.next = n
#             n.prev = p
#             node.prev, node.next = None, None
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.h:
#             self.h[key].value = value
#         else:
#             self.h[key] = Node(key, value)
#         self.update(self.h[key])

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)