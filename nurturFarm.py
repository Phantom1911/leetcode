# Distributed DB


 # redis KV store
 # nodes
 # consistent hashing
 # replication
 # CAP --- > CP, AP

 # 1. key -- values  ::
 # nodes - which node? hash(hashKey)  - 0 .. n


 # hash space -      s0, s1, s2 ... sn-1
 # hashring
 # key == hash(key) - clockwise

 # in mem DB

class KVStoreInMem:
    def __init__(self):
        self.keys = {}

    def read(self, key):
        if key in self.keys:
            return self.keys[key]
        return None

    def write(self, key, value):
        self.keys[key] = value

kv   -- node1
    -- n2

class KVStore:
    def __init__(self, nodeTimeout):
        self.nodes = []   # collection of nodes

    def adding_a_node(self):
        self.nodes.append(Node())

    def read(self, key):
        node = hash(key)
        return node.read_from_node(key)

    def write(self, key, value):
        node = hash(key)
        node.write_to_node(key,value)

    def pingNode(self):
        for node in self.nodes():
            if not node.checkNode():
                node.state = INACTIVE


def hash(key):
    return Node()

class Node:
    def __init__(self, identifier):
        self.identifier = identifier
        self.keys = {}
        self.state = ACTIVE

    def read_from_node(self, key):
        if key in self.keys:
            return self.keys[key]
        return None

    def write_to_node(self, key, value):
        self.keys[key] = value