import heapq

# in order to define a heap of custom objects, it is required to put the elements as a tuple -
# the first element of the tuple is the one on which the comparison is to be done.
# TODO : try out inheritance in python classes
class spclStr:
    def __init__(self, s):
        self.name = s

class spclStr2:
    def __init__(self, s,i):
        self.name = s
        self.rank=i

    def __lt__(self, other):
        return self.rank > other.rank

if __name__=="__main__":
    s1 = spclStr("aastik")
    s2 = spclStr("abc")
    s3 = spclStr("def")



    # this actually gives you the default implementation which is the min heap
    l = [(23, s1), (46, s2), (12, s3)]

    heapq.heapify(l)
    while len(l) > 0:
        print(heapq.heappop(l)[1].name)

    print("\n")
    print("max heap time!")

    s4 = spclStr2("ghi",12)
    s5 = spclStr2("jkl",15)
    s6 = spclStr2("mno",18)

    l2 = [s4,s5,s6]
    heapq.heapify(l2)
    while len(l2)>0:
        print(heapq.heappop(l2).name)

