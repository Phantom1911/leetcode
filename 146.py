class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.h = {}
        self.capacity = capacity
        self.head = Node('fake head', -1)
        self.tail = Node('fake tail', -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.h:
            self.update(self.h[key])
            return self.h[key].value
        return -1

    def update(self, node):
        self.remove(node)
        self.insertbetween(self.head, self.head.next, node)
        if len(self.h) > self.capacity:
            lastnode = self.tail.prev
            self.remove(lastnode)
            del (self.h[lastnode.key])

    def insertbetween(self, a, b, node):
        a.next = node
        node.next, node.prev = b, a
        b.prev = node

    def remove(self, node):
        p, n = node.prev, node.next
        if p or n:
            p.next = n
            n.prev = p
            node.prev, node.next = None, None

    def put(self, key: int, value: int) -> None:
        if key in self.h:
            self.h[key].value = value
        else:
            self.h[key] = Node(key, value)
        self.update(self.h[key])

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)